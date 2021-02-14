from django.shortcuts import render
from .models import TodoList
from .forms import TodoForm

from django.views import View
from django.views import generic

class Todo_board(generic.TemplateView):
    def get(self, request, *args, **kwargs):
        template_name = 'todo_board/todo_board_list.html'
        todo_list = TodoList.objects.all()

        return render(request, template_name, {"todo_list" : todo_list})


def check_post(request):
    template_name = 'todo_board/todo_board_success.html'
    
    if request.method == "POST" :
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=True)
            # todo.todo_save()
            message = "일정을 추가하였습니다"
            return render(request, template_name, {"message": message})
    else:
        template_name = "todo_board/todo_board_insert.html"
        form = TodoForm
        return render(request, template_name, {"form":form})


# def check_post(request):
#     template_name = 'todo_board/todo_board_success.html'
#     if request.method == "POST":
#         if str(request.path).split("/board/")[1].split("/")[0] == "insert":
#             form = TodoForm(request.POST)
#             if form.is_valid():
#                 message = "일정을 추가하였습니다."
#                 if len(request.POST.get('title')) < 2:
#                     message = "제목은 2글자 이상으로 입력해주세요!"
#                 else:
#                     todo = form.save(commit=False)
#                     todo.todo_save()
#                 return render(request, template_name, {"message": message})

#     else:
#         template_name = 'todo_board/todo_board_insert.html'
#         form = TodoForm
#         return render(request, template_name, {"form" : form})