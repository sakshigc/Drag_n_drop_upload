from django.conf import settings
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render,get_object_or_404
from django.shortcuts import redirect
from django.utils import timezone

from django.core.files.storage import FileSystemStorage

from django.template.loader import get_template
from django.http import HttpResponse, HttpResponseNotFound
from django.views.generic import View

def model_form_upload(request):

	if request.method == 'POST' and request.FILES['myfile']:
		# form = UploadFileForm(request.POST, request.FILES)
		myfile = request.FILES['myfile']
		fs = FileSystemStorage()
		filename = fs.save(myfile.name, myfile)
		uploaded_file_url = fs.url(filename)
		return redirect('/sucess')
	return render(request,"upload.html")

def sucess(request):
	return HttpResponseNotFound('<h1> Check Base dir/ Media</h1>')