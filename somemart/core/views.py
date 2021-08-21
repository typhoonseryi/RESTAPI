import json
from django.http import HttpResponse, JsonResponse, Http404
from django.views import View
from jsonschema import validate
from jsonschema.exceptions import ValidationError
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import Item

ADD_SCHEMA = {
    "type": "object",
    "properties": {
        "title": {
            "type": "string",
            "minLength": 1,
            "maxLength": 64
        },
        "description": {
            "type": "string",
            "minLength": 1,
            "maxLength": 1024
        },
    },
    "required": ["title", "description", "params"],
}


@method_decorator(csrf_exempt, name='dispatch')
class AddItemView(View):

    def post(self, request):
        try:
            document = json.loads(request.body)
            validate(document, ADD_SCHEMA)
            i = Item.objects.create(title=document['title'],
                                    description=document['description'],
                                    params=document['params'],
                                    )
            i.save()
            return JsonResponse({'id': i.id}, status=201)
        except json.JSONDecodeError:
            return JsonResponse({'errors': 'Invalid JSON'}, status=400)
        except ValidationError as exc:
            return JsonResponse({'errors': exc.message}, status=400)

    def get(self, request):

        flt = request.GET.get('filter')
        if flt:
            key, value = flt.split('=')
            if key == 'title':
                titles = [i.title for i in Item.objects.filter(title=value)]
                return JsonResponse({'titles': titles}, status=201)
            else:
                titles = [i.title for i in Item.objects.filter(params__contains={key: value})]
                return JsonResponse({'titles': titles}, status=201)
        else:
            titles = [i.title for i in Item.objects.all()]
            return JsonResponse({'titles': titles}, status=201)


class GetItemView(View):

    def get(self, request, item_id):
        try:
            i = Item.objects.get(pk=item_id)
        except Item.DoesNotExist:
            raise Http404
        return JsonResponse({'title': i.title, 'description': i.description, 'params': i.params}, status=201)