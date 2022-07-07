from django.shortcuts import render


# Create your views here.
def get_booktable_list(request):
    return render(request, "booktable/booktable_list.html")
