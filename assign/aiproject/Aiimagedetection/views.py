from django.shortcuts import render,redirect,HttpResponse
from .forms import *
import xml.etree.ElementTree as ET
from PIL import ImageFont,Image,ImageDraw
from .serializers import *
from rest_framework.renderers import JSONRenderer
import csv
# Create your views here.
def home(request):
    form=ElementsForm()
    if request.method=='POST':
        form=ElementsForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            data=Elements.objects.all()
            for i in data:
                imgp=i.imgf
                xmlp=i.xmlf
            imgp='media/'+str(imgp)
            xmlp='media/'+str(xmlp)
            mytree=ET.parse(xmlp)
            myroot=mytree.getroot()
            pn=myroot[1].text
            image=Image.open(imgp)
            draw=ImageDraw.Draw(image)
            ft=ImageFont.truetype('arial.ttf',30)
            for i in myroot.findall('object'):
                tn=i.find('name').text
                a=int(i.find('bndbox')[0].text)
                b=int(i.find('bndbox')[1].text)
                c=int(i.find('bndbox')[2].text)
                d=int(i.find('bndbox')[3].text)
                idata=Details.objects.create(picname=pn,objectname=tn,xmin=a,ymin=b,xmax=c,ymax=d)
                idata.save()
                draw.text(xy=(a,b-30),text=tn,fill='red',font=ft)
                draw.rectangle((a,b,c,d),outline='red',width=3)
                image.save(imgp)

            return redirect('/')
    
    return render (request,'index.html',{'form':form})

def fileresponse(request):
   
    for i in Elements.objects.all():
        d1=i
    serilizedata=Serialdata(d1)
    jd=JSONRenderer().render(serilizedata.data)
    return HttpResponse(jd,content_type='application/json')

def report(request): 
    sd=request.POST.get('Sdate')
    ed=request.POST.get('Edate')
    response=HttpResponse(content_type="text/csv")
    d2=Details.objects.filter(timestamp__gte=sd).filter(timestamp__lte=ed)
    writer=csv.writer(response)
    writer.writerow(['picture name','object name','xmin','ymin','xmax','ymax','timestamp'])
    for d in d2.values_list('picname','objectname','xmin','ymin','xmax','ymax','timestamp'):
        writer.writerow(d)
    response['Content-Disposition']='attachment; filename ="reportextract.csv"'
    return response