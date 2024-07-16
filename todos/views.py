from django.shortcuts import render

def todo_list(request):
    nome = "Leonardo"
    alunos = ["Aluno um", "Aluno dois", "Aluno tres"]
    return render(request, "todos/todo_list.html", {"nome": nome, "alunos": alunos})