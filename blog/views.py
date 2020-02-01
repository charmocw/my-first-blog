from django.shortcuts import render

# Create your views here.request
def post_list(request):
    return render(request, 'blog/post_list.html', {})