from collections import defaultdict
import rest_framework
from rest_framework.response import Response
from rest_framework import views
from rest_framework.parsers import FileUploadParser
from .models import Deal
import csv
import codecs
from django.db.models import Sum
import copy
from gems_app.serializers import RichSerializer


class FileUploadView(views.APIView):
    parser_classes = [FileUploadParser]
    permission_classes = [rest_framework.permissions.AllowAny]

    def post(self, request, filename, format=None):
        file_obj = request.data['file']
        reader = csv.DictReader(codecs.iterdecode(file_obj, 'utf-8'))
        deals = []
        for row in reader:
            deals.append(
                Deal(customer=row['customer'],
                     item=row['item'],
                     total=row['total'],
                     quantity=row['quantity'],
                     date=row['date'],
                     ))
        Deal.objects.bulk_create(deals)
        return Response(status=204)

    def get(self, request, filename, format=None):
        rich = Deal.objects.all().values('customer').annotate(spent_money=
                                                              Sum('total')).order_by('-spent_money')[:5]
        gems_total = defaultdict(int)
        rich_gems = {}
        for i in rich:  # gems bought by the 5 most spent buyers
            gems_set = set(Deal.objects.filter(customer=i['customer']).values_list('item'))
            rich_gems[i['customer']] = gems_set
            for gem in gems_set:  # count the quantity of gems in gems_total
                gems_total[gem] += 1
        _rich_gems = copy.deepcopy(rich_gems)
        for customer in _rich_gems:  # remove those gems that occur less than twice
            for gem in _rich_gems[customer]:
                if gems_total[gem] <= 1:
                    rich_gems[customer].remove(gem)
        for rich_item in rich:  # add gems to rich
            rich_item['gems'] = rich_gems[rich_item['customer']]
        serializer = RichSerializer(rich, many=True)
        return Response(serializer.data)