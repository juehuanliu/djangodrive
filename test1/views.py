from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
# from django.http import HttpResponse
# Create your views here.
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import FileUploadForm
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from .models import CloudFile
from django.conf import settings
from django.contrib.auth.models import User


@login_required
def home(request):
    return render(request, "drive/drive.html")


@login_required
def model_form_upload(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        form.instance.owner = request.user
        form.instance.fileName = request.FILES['file'].name
        if form.is_valid():
            form.save()
            return redirect('test1-home')
    else:
        form = FileUploadForm()
    return render(request, 'drive/document_form.html', {
        'form': form
    })


class FileListView(LoginRequiredMixin, ListView):
    model = CloudFile
    template_name = 'drive/drive.html'
    context_object_name = 'files'
    buckName = settings.AWS_STORAGE_BUCKET_NAME

    def get_queryset(self):
        return CloudFile.objects.filter(owner=self.request.user)

    def get_context_data(self, **kwargs):
        context_data = super(FileListView, self).get_context_data(**kwargs)
        context_data['buckName'] = self.buckName
        return context_data


class FileDetailView(DetailView):
    model = CloudFile
    buckName = settings.AWS_STORAGE_BUCKET_NAME


class FileCreateView(LoginRequiredMixin, CreateView):
    model = CloudFile
    fields = ['description', "file"]

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.fileName = self.request.FILES['file'].name
        return super().form_valid(form)


class FileDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = CloudFile
    success_url = '/'

    def test_func(self):
        cloudFile = self.get_object()
        if self.request.user == cloudFile.owner:
            return True
        return False
