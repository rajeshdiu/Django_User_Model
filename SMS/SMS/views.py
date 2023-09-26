from django.shortcuts import render

def home(request):
    send_mail(
    "Test Mail",
    "Hello World",
    "lecturer2.wadp.nsda@dipti.com.bd",
    ["rajeshcpi1212@gmail.com"],
    fail_silently=False,
    )
    return render(request,"index.html")
