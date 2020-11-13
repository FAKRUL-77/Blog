import requests
from django.core.paginator import Paginator
from django.shortcuts import render


# POSTS VIEW ENDPOINT
def posts(request):
    req = requests.get("https://jsonplaceholder.typicode.com/posts")
    objects = req.json()
    paginator = Paginator(objects, 4)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
    }

    return render(request, 'blog-listing.html', {'page_obj': page_obj})


# POST DETAILS VIEW ENDPOINT
def post_details(request):
    return render(request, 'blog-post.html')