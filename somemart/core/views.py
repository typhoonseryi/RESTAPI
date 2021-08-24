import json
from django.http import JsonResponse, Http404
from django.views import View
from jsonschema import validate
from jsonschema.exceptions import ValidationError
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import Item
from somemart.settings import ADD_SCHEMA, SHOW_SCHEMA


@method_decorator(csrf_exempt, name='dispatch')
class AddShowItemsView(View):

    def post(self, request):
        try:
            doc = json.loads(request.body)
            validate(doc, ADD_SCHEMA)
            i = Item.objects.create(title=doc['title'],
                                    description=doc['description'],
                                    params=doc['params'],
                                    )
            i.save()
            return JsonResponse({'id': i.id}, status=201)
        except json.JSONDecodeError:
            return JsonResponse({'errors': 'Invalid JSON'}, status=400)
        except ValidationError as exc:
            return JsonResponse({'errors': exc.message}, status=400)

    def get(self, request):

        try:
            doc = json.loads(request.body)
            validate(doc, SHOW_SCHEMA)
            flt = doc['filter']
            if flt.get('title'):
                titles = [i.title for i in Item.objects.filter(title=flt['title'])]
                return JsonResponse({'titles': titles}, status=200)
            else:
                titles = [i.title for i in Item.objects.filter(params=flt)]
                return JsonResponse({'titles': titles}, status=200)
        except json.JSONDecodeError:
            titles = [i.title for i in Item.objects.all()]
            return JsonResponse({'titles': titles}, status=200)
        except ValidationError as exc:
            return JsonResponse({'errors': exc.message}, status=400)


class GetItemView(View):

    def get(self, request, item_id):
        try:
            i = Item.objects.get(pk=item_id)
        except Item.DoesNotExist:
            raise Http404
        return JsonResponse({'title': i.title,
                             'description': i.description,
                             'params': i.params,
                             }, status=200)
