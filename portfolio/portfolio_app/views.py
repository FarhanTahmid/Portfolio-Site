from django.shortcuts import render

def homepage(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        message=request.POST['message']
        data={
            'name':name,
            'email':email,
            'message':message
        }
        print(data)
    return render(request,'index-2.html')
