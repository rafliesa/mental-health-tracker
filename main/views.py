from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306207480',
        'name': 'Muhammad Rafli Esa Pradana',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)