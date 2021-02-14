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

class Todo_board_detail(generic.DetailView):
    model = TodoList
    template_name = "todo_board/todo_board_detail.html"
    context_object_name = 'todo_list'

# update와 관련된 기능을 제공해줌. save 기능과 form 데이터를 받아오는 기능이 필요
class Todo_board_update(generic.UpdateView):
    model = TodoList
    fields = ('title', 'content', 'end_date')
    template_name = 'todo_board/todo_board_update.html'
    success_url = '/board/'

    # 만약 form이 유효하다면 form_valid 함수를 실행해서 폼을 저장
    def form_valid(self, form):
        form.save()
        return render(self.request, 'todo_board/todo_board_success.html', {"message": "일정을 업데이트 했습니다"})

    def get(self, request, *args, **kwargs):
        #오브젝트를 받아와서 폼 클래스를 받아온 후 이것을 return
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        context = self.get_context_data(object = self.object, form=form)
        return self.render_to_response(context)

class Todo_board_delete(generic.DeleteView):
    model = TodoList
    success_url = '/board/'
    context_object_name = 'todo_list'
    
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


