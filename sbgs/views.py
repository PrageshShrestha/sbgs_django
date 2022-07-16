from django.shortcuts import render

from django.conf import settings
import os 
# from .models import Visitors
# from hitcount.views import HitCountDetailView

English = {
    'home':'Home',
    
    'title':'SBGS',
    'home':'Home',
    'Location':'Location',
    'Befe':'Benefits and Features',
    'Cont':'Contact us',
    'language':'Language',
    'title':'SBGS',
    'Found':'Founded by',
    'found_name':'Panchalal Shrestha',
    'topic_sentence':'Find Your Gents Clothing at Swet Bhairav General Stores . Find Recent Trends In Less ',
    'highlight':'Cause Its Professional',
    'More_pics':'More Pics(Drag to see )',
    'Features':'Features',
    'fe1':'Wide Variety of Cothes . Close in Customer Support',
    'fe2':'hug with big hall Better customer experiance with better price',

    'Feature1':'Boys and Gents Outfits ',
    'f1':'at one place',
    'Feature2':'Shop like Daraz',
    'f2':'But there is a touch lol',
    
    'Feature3': 'find recent trends ',
    'f3':'at our shop ',
    
    'Feature4':'Styling your personality ',
    'f4':'with low cost ',
    'Feature5':'Our Journey Begins when ',
    'f5':'Customers go alive ',
    'contacts':'Contact us at:',
    'number1':9844053689,
    'number2':9801606601,
    'profile':'Our Profile',
    'comments':'Comments',
    'submit':'Submit',
    'like':'like',
    'reply':'reply' , 
    'direction':'Durga mandir ko pachhim patti',
    'hello':'Approximately 300m From Main Road',
    'exact_city':'Lalbandi-7,Sarlahi',
    'find':'Find us',
    'creator':'Author:Pragesh Shrestha ',
    'welcome':'Welcome to Swet Bhairab General Stores'
    

    
}
Nepali = {
    'welcome':'स्वेत भैरब जनरल स्टोर्समा स्वागत छ ।',
    'title':'SBGS',
    'home':'होम',
    'Location':'अहिले को स्थान',
    'Befe':'सुविधा ',
    'Cont':'सम्पर्क',
    'language':'भाषा',
    
    'Found':'पसले',
    'found_name':'पंचलाल श्रेष्ठ ',
    'topic_sentence':'केटा र पुरुष का लागि कपडा खरिद गर्न सम्झिने पर्ने  , स्वेत भैरव गेनेरल स्टोर्स ।  पाउनुहोस् कपडाहरु सजिलो र छिटो ',
    'highlight':'हजुर झैँ फेसन  तेही',
    'More_pics':'अन्य फोटोहरु  ',
    'Features':'विशेषताहरू',
    'Feature1':'केटा र gents लुगा/कपडा हरु ',
    'f1':'एकै स्थान मा ',
    'Feature2':'online को मज्जा offline मा ',
    'f2':'पारदर्शिता ',
    
    'Feature3': 'समयाकलिन ट्रेन्डहरु ',
    'f3':'सहजै पौनासकिने ',
    
    'Feature4':'राम्रो लागौनुहोस  ',
    'f4':' सस्तो मा ',
    'Feature5':'Quality नै अहिले को style हो ',
    
    'contacts':'हाम्रा सम्पर्कहरु:',
    'number1':'९८०१६०६६०१',
    'number2':'९८४४०५३६८९',
    'profile':'प्रोफाइल',
    'comments':'',
    'submit':'',
    'like':'',
    'reply':'' ,   
    'direction':'दुर्गा मन्दिर को पचिम पट्टि ',
    'hello':'मैन road भन्दा ३०० मीटर (hat बजार )',
    'exact_city':'लालबन्दी -७ ,सर्लाही ',
    'find':'हाम्रो ठेगाना',
    'creator':'लेखक:प्रगेश श्रेष्ठ ',
    
}

# mainpage
# location
# benefits and features
# contact us 
# language
# ______________
# title = homepage
# Founded by:Panchalal shrestha
# findyour gents clothing at Swet Bhairav General stores. Find recent treends in less price Cause quality is king
# More pics
# Features
# Wide Variety of Cothes . Close in Customer Support hug with big hall Better 
# customer experiance with better price 
# Boys and Gents Outfits 
# at one place
# Get oxiticin with Us 
# find recent trends at our shop 
# Styling your personality 
# with low cost 
# Our Journey Begins when 
# Customers go alive 
# ____________________________
# Contacts 
# 9845022298
# 9801606601
# our Profile 
# Panchalal Shrestha 
# ___________________________
# Comments 
# name:
# submit like reply







    # path = settings.MEDIA_ROOT
    # img_list = os.listdir(path + 'static/media/pictures')
    # context = {"images": img_list}
    # return render (request, '(path to django template)', context)    
def second_english(request):
     return render(request , 'english.html' , {'English':English })   
def hello(request):
    
   
    #if Button:
       # playsound('static/beep.mp3')
   
    # x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    # if x_forwarded_for:
    #     ip = x_forwarded_for.split(',')[0]
    # else:
    #     ip = request.META.get('REMOTE_ADDR')
    
    # device_type = ""
    # browser_type = ""
    # browser_version = ""
    # os_type = ""
    # os_version = ""
    # if request.user_agent.is_mobile:
    #     device_type = "Mobile"
    # if request.user_agent.is_tablet:
    #     device_type = "Tablet"
    # if request.user_agent.is_pc:
    #     device_type = "PC"
    
    # browser_type = request.user_agent.browser.family
    # browser_version = request.user_agent.browser.version_string
    # os_type = request.user_agent.os.family
    # os_version = request.user_agent.os.version_string
    # Visitors.Browser_type = browser_type
    # Visitors.Ip = ip
    # Visitors.Browser_version = browser_version
    # Visitors.OS_type = os_type
    # Visitors.os_version = os_version
    return render(request , 'homepage.html',{'English':Nepali})
       

      
        
  
       
# Create your views here.
 
# Create your views here.
