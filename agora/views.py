from django.shortcuts import render
def post_list(request):
    return render(request, 'agora/post_list.html', {})
