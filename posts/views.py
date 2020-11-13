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
def post_details(request, post_id):

    post_link = "https://jsonplaceholder.typicode.com/posts/" + str(post_id)
    post_comment_link = post_link + '/comments'

    post_request = requests.get(post_link)
    comment_request = requests.get(post_comment_link)

    post_object = post_request.json()
    post_comments_object = comment_request.json()

    context = {
        'post_obj': post_object,
        'comments_obj': post_comments_object,
    }

    return render(request, 'blog-post.html', context)