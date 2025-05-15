from django.shortcuts import render

def todo_list(request):
    return render(request, "lista/todo_list.html")