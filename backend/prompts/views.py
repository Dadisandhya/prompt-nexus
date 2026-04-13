from django.http import JsonResponse
from .models import Prompt
from .redis_client import increment_view, get_views
import json

# GET all prompts
def get_prompts(request):
    data = list(Prompt.objects.values())
    return JsonResponse(data, safe=False)

# POST create prompt
def create_prompt(request):
    body = json.loads(request.body)

    prompt = Prompt.objects.create(
        title=body['title'],
        content=body['content'],
        complexity=body['complexity']
    )

    return JsonResponse({"id": str(prompt.id)})

# GET single prompt
def get_prompt(request, id):
    prompt = Prompt.objects.get(id=id)

    increment_view(id)
    views = get_views(id)

    return JsonResponse({
        "id": str(prompt.id),
        "title": prompt.title,
        "content": prompt.content,
        "complexity": prompt.complexity,
        "view_count": views
    })