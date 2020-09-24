from django.shortcuts import render

def calc(request):
    c=0
    if request.method == 'POST':
        a = request.POST['num1']
        b = request.POST['num2']
        op = request.POST['op']
        if op not in ['+','-','*','/','%']:
            c = 'SELECT AN OPERAND'
            return render(request,'appone/calc.html',{'error':c})
        else:
            c=result(a,b,op)
    return render(request,'appone/calc.html',{'result':c})

def result(a,b,op):
    return eval(a+op+b)