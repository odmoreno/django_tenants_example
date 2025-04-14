from django.shortcuts import render, redirect

from django.http import HttpResponse

from .models import Employee


def index(request):
    employees = Employee.objects.all()
    return render(request, "client_index.html", {"employees": employees})
    # return HttpResponse(f"<h1/>{request.tenant}</h1>")


def create_employee(request):
    print("create employee")
    print(request.POST)
    if request.POST:
        name = request.POST.get("name")
        print(name)
        employee = Employee(name=name)
        employee.save()
        return redirect("client_index")
    # employee = Employee(name=name)
    # employee.save()
    # return HttpResponse(f"<h1>{request.tenant} employee created!</h1>")
