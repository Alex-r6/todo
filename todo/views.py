from django.shortcuts import render
from django.tasks import task

from .forms import TaskForm, UpdateTagForm, TagForm
from  .models import *
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import redirect
from django.urls import reverse_lazy


class TaskListView(ListView):
    model = Task
    template_name = "todo/task_list.html"
    context_object_name = "tasks"

    def post(self, request, *args, **kwargs):
        task_id = request.POST.get("task_id")
        task = Task.objects.get(id=task_id)
        task.is_done = not task.is_done
        task.save()
        return redirect('task_list')

    # def update(self, request, *args, **kwargs):
    #     task_id = request.POST.get("task_id")
    #     task = Task.objects.get(id=task_id)
    #     task.content = request.POST.get("content")
    #     task.deadline = request.POST.get("deadline")
    #     task.is_done = request.POST.get("is_done")
    #     task.tags = request.POST.get("tags")
    #     task.save()
    #     return redirect('task_list')
    #
    # def delete(self, request, *args, **kwargs):
    #     task_id = request.POST.get("task_id")
    #     task = Task.objects.get(id=task_id)
    #     task.delete()
    #     return redirect('task_list')


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('task_list')
    template_name_suffix = '_create'

class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('task_list')
    template_name_suffix = '_update'

class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy('task_list')
    template_name_suffix = '_delete'

class TagsListView(ListView):
    queryset = Tag.objects.order_by('name')

class TagCreateView(CreateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy('tag_list')
    template_name_suffix = '_create'

class TagUpdateView(UpdateView):
    model = Tag
    form_class = UpdateTagForm
    success_url = reverse_lazy('tag_list')
    template_name_suffix = '_update'


class TagDeleteView(DeleteView):
    model = Tag
    success_url = reverse_lazy('tag_list')
    template_name_suffix = '_delete'