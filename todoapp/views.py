from django.shortcuts import render,redirect
from .models import TodoModel
# Create your views here.
def homepage(request):
	mytodo = TodoModel.objects.all()
	context = { "mytodos" : mytodo }
	return render(request,'homepage/homepage.html', context)

def addtask(request):
	#we need to write a code to add input data to database
	mytask = request.POST['task']
	if mytask != "":
		TodoModel(task = mytask).save()
	
	return redirect(request.META['HTTP_REFERER'])

def deletetask(request,taskpk):
	#write code to delete data from data base
	TodoModel.objects.filter(id = taskpk).delete()
	return redirect(request.META['HTTP_REFERER'])

def edittaskview(request,taskpk):
	#write code to update task(data in database)
	context = {"todopk": taskpk}
	return render(request,"homepage/edittask.html",context)
	

def edittask(request,taskpk):
	userenteredtask = request.POST['task']
	todo = TodoModel.objects.filter(id = taskpk)[0]
	todo.task = userenteredtask
	if todo.task != "":
		todo.save()
	
	return redirect('homepage')