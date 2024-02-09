from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from .models import *
from .forms import *
# Create your views here.
def index(req):
    items = Tovar.objects.all()
    items2 = Izbran.objects.all()
    data={'tovari':items, 'izbrannie':items2}
    return render(req,'index.html',data)

def buy(req,id):
    item = Tovar.objects.get(id=id)
    item.vkorzine=True
    item.save()
    user = req.user
    print(id, user)
    print(req.session.session_key)
    if user.username:
        if Korzina.objects.filter(tovar_id=id, user_id=user.id):
            getTovar = Korzina.objects.get(tovar_id=id)
            getTovar.count+=1
            getTovar.summa = getTovar.calcSumma()
            getTovar.save()
        else:
            Korzina.objects.create(count=1, tovar=item, summa=item.price, user=user)
    else:
        #newuser = User.objects.create_user(username='Tempuser')
        # if Korzina.objects.filter(tovar_id=id, user_id__isnull=True):
        #     getTovar = Korzina.objects.get(tovar_id=id)
        #     getTovar.count+=1
        #     getTovar.summa = getTovar.calcSumma()
        #     getTovar.save()
        # else:
        Korzina.objects.create(count=1, tovar=item, summa=item.price)
    return redirect('home')

def toKorz(req):
    items = Korzina.objects.filter(user_id=req.user.id)
    myform = Myforms()
    itog=0
    for i in items:
        itog+=i.calcSumma()
    # if req.POST:
    #     myform = Myforms(req.POST)
    #     print('post')
    #     print(req.POST)
    #     if myform.is_valid():
    #         print('valid')
    #         print(myform.cleaned_data['name'])
            # korzinaZakaz(req)
            # print(myform)
    data = {'items':items,'itog':itog,'myform':myform}
    return render(req,'korzina.html',data)

def delete(req,id):
    item = Korzina.objects.get(id=id)
    item.delete()
    return redirect('toKorz')

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import requests
@method_decorator(csrf_exempt)
def korzinaZakaz(req):
    print('1')
    if req.POST:
        print('2')
        adres = req.POST.get('k1')
        name = req.POST.get('k2')
        tel = req.POST.get('k3')
        # print(adres)
        items = Korzina.objects.filter(user_id=req.user.id)
        samzakaz=''
        for one in items:
            samzakaz+= one.tovar.opis+' '+str(one.count)+' '+str(one.summa)+'\n'
        itog = 0
        for i in items:
            itog += i.summa
        Zakaznew.objects.create(adres=adres, name=name, tel=tel, total=itog,
                                samzakaz=samzakaz)
        items.delete()
        ####################################################################
        TOKEN = "5472379675:AAHU7pHJLYY3qOvKHWuF913hDoru1-6Vkis"
        chat_id = "1186459178"
        message = samzakaz + adres +' '+ name +' '+ tel
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
        print(requests.get(url).json())  # Эта строка отсылает сообщение
        #######################################################################
        return JsonResponse({'mes':'data success','link':'../'})
    return redirect('home')
#https://api.telegram.org/botTOKEN/getUpdates

def korzinaCount(req, num, id):
    tovar = Korzina.objects.get(id=id)
    print(num, id)
    tovar.count+=int(num)
    # if tovar.count<0:
    #     tovar.count=0
        #tovar.delete()
    tovar.save()
    if tovar.count<0:
        tovar.count=0
        tovar.delete()
    return redirect('toKorz')

@method_decorator(csrf_exempt)
def toizbran(req):
    print('123')
    if req.POST:
        k1=req.POST.get('k1')
        k2=req.POST.get('k2')
        print(k1,k2)
        # item = Tovar.objects.get(id=k1)
        if Izbran.objects.filter(tovar_id=k1):
            item = Izbran.objects.get(tovar_id=k1)
            item.delete()
        else:
            Izbran.objects.create(tovar_id=k1)

        return JsonResponse({'mes': 'data success', 'link': ''})
    return redirect('home')