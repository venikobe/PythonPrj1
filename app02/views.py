from django.shortcuts import render
from .forms import TaskForm
from .models import TaskModel
from django.db.models import Count, Avg, Min, Max, StdDev, Sum

def mainPage(request):
    template = '2base.html'
    return render(request, template)

def taskForm(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            overwork = form.cleaned_data["overworkInput"]
            day = form.cleaned_data["dayInput"]
            newtask = TaskModel(overworkInput = overwork, dayInput = day)
            newtask.save()
            objList = TaskModel.objects.all().order_by('-id')
            return taskAnswer(request)
    else:
        form = TaskForm()
    template = '2task.html'
    context = {'form': form}
    return render(request, template, context)


def taskAnswer(request):
    objList = TaskModel.objects.all().order_by('-id')
    updateObj = TaskModel.objects.filter(id=objList[0].id)
    taskStr = f'Сколько записей о переработках в {objList[0].dayInput}?'
    updateObj.update(taskQuestion = taskStr)

    asplit = objList[0].overworkInput.split("| ")
    c = 0
    for i in range(len(asplit)):
        ass = asplit[i].split(", ")
        if objList[0].dayInput == ass[1]:
            c+=int(ass[2])
    updateObj.update(result = c)

    template = '2answer.html'
    context ={'model':{'question': objList[0].taskQuestion,
                        'input': objList[0].overworkInput,
                        'day': objList[0].dayInput,
                        'result': objList[0].result,
                        'currentime': objList[0].currenttime}}
    return render(request, template, context)

def alldata(request):
    namesList = []
    for name in TaskModel._meta.get_fields():
        namesList.append(name.verbose_name)
    context = {'info': TaskModel.objects.all(),
               'names': namesList}
    template = '2alldata.html'
    return render(request, template, context)

def notAllData(request):

    objList = TaskModel.objects.all().filter(result__gt=0).order_by('-id')
    stats = [objList.aggregate(Count("result")),
             objList.aggregate(Avg("result")),
             objList.aggregate(Min("result")),
             objList.aggregate(Max("result")),
             objList.aggregate(StdDev("result")),
             objList.aggregate(Sum("result"))]
    print(stats)

    namesList = []
    for name in TaskModel._meta.get_fields():
        namesList.append(name.verbose_name)

    template = "2notalldata.html"
    context = {'stats': stats,
               'names': namesList,
               'info': objList}
    return render(request, template, context)
