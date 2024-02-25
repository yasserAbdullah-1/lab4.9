from django.shortcuts import render
from django.http import HttpResponse

def members(request):
    return HttpResponse("this is a site to calculate tax.")
# Create your views here.
def anyNumber(request,number):
    taxRate=1.15
    total=float(number)*taxRate
    return HttpResponse(f"<h1>total price with 15% tax rate={total}</h1>")
def taxRate(request):
    tax_rate = str(0.15)
    return render(request,"members/index.html",{"tax_rate":str(tax_rate)})