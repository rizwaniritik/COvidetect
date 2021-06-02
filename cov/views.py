from django.shortcuts import render,HttpResponse,redirect
import pickle
import numpy as np
import json
# Create your views here.

with open('./static/codetector.pickle','rb')as f:
    model=pickle.load(f)
f.close()
def home(request):
    if request.method=="POST": 
      
        
        fever=(request.POST.get('fever'))
        age=(request.POST.get('age'))
       
        runnynose=request.POST.get('Runnynose')
        bodypain=request.POST.get('BodyPain')
        diffbreath=request.POST.get('diffbreath')
       
        inf=[fever,bodypain,age,runnynose,diffbreath]
        r=round((model.predict_proba([inf])[0][1]*100),2)
        print(r)
        
       
        
        return render(request,"home.html",context={'probability':r ,'fever' :fever,'age':age ,'runnynose':runnynose ,'diffbreath' : diffbreath ,'bodypain':bodypain})
  

    return render(request,"home.html")





