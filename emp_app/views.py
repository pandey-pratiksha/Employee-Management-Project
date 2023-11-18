from django.shortcuts import render,HttpResponse,redirect
from .models import Employee,Role,Department
from datetime import datetime
from django.db.models import Q

# Create your views her
def index(request):
    return render(request, 'index.html')


def all_emp(request):

        emps=Employee.objects.all()
        context={
            'emps':emps
        }
        print(context,"kkkkkkk")
        return render(request, 'view_all_emp.html',context)

def add_emp(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        salary=int(request.POST['salary'])
        bonus=int(request.POST['bonus'])
        phone=int(request.POST['phone'])
        dept=int(request.POST['dept'])
        role=int(request.POST['role'])
        new_emp=Employee(first_name=first_name,last_name=last_name,salary=salary,bonus=bonus,phone=phone,dep_id=dept,role_id=role,hire_date=datetime.now())
        new_emp.save()
        return HttpResponse('added new employee')
        
    else:
         return render(request,'add_emp.html')

def remove_emp(request,emp_id=0):
    if emp_id:
        try:
            employee_to_be_removed=Employee.objects.get(id=emp_id)
            employee_to_be_removed.delete()
            return HttpResponse("employee removed sussesfully")
        except:
            return HttpResponse("please enter valid id")

    emps=Employee.objects.all()
    context={
        'emps':emps
    }

    return render(request,'remove_emp.html',context)

def filter_emp(request):
    if request.method=='POST':
        name=request.POST['name']
        dept=request.POST['dept']
        role=request.POST['role']
        emps=Employee.objects.all()
        if name:
            emps=emps.filter(Q(first_name__icontains=name) | Q(last_name__icontains=name))
        if dept:
            emps=emps.filter(dep__name__icontains = dept)
        if role:
            emps=emps.filter(role__name__icontains = role)
        context={
            'emps':emps
        }
        return render(request,'view_all_emp.html',context)
    else:

        return render(request,'filter_emp.html')


    
