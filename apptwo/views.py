from django.shortcuts import render

def tnku(request):
    s = "HOPE YOU LIKED IT !"
    return render(request,'apptwo/tnku.html',{'note':s})
