from django.shortcuts import render

# Create your views here.
def inherit_parent(request):
    return render(request,'parent.html')

def inherit_child(request):
    return render(request,'child.html')