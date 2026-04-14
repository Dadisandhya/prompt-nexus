from django.http import JsonResponse
from .models import Prompt
from .redis_client import increment_view, get_views
import json


def home(request):
    return JsonResponse({"message": "Prompt Nexus API is running 🚀"})


# GET all prompts
def get_prompts(request):
    try:
        data = list(Prompt.objects.values())
        return JsonResponse(data, safe=False)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


# POST create prompt
def create_prompt(request):
    if request.method != "POST":
        return JsonResponse({"error": "Only POST method allowed"}, status=405)

    try:
        body = json.loads(request.body)

        title = body.get('title')
        content = body.get('content')
        complexity = body.get('complexity')

        # validation
        if not title or not content or not complexity:
            return JsonResponse({"error": "Missing fields"}, status=400)

        prompt = Prompt.objects.create(
            title=title,
            content=content,
            complexity=complexity
        )

        return JsonResponse({"id": str(prompt.id)})

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


# GET single prompt
def get_prompt(request, id):
    try:
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

    except Prompt.DoesNotExist:
        return JsonResponse({"error": "Prompt not found"}, status=404)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
