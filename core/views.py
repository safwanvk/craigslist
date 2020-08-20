from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'core/base.html')


def new_search(request):
    search = request.POST.get('search')
    context = {
        'search': search
    }
    return render(request, 'core/new_search.html', context)
