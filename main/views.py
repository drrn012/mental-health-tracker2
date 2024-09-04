from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306123456',
        'name': 'Derensh Pandian',
        'class': 'PBP KKI'
    }

    return render(request, "main.html", context)