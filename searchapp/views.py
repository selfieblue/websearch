import json
import time
import requests
from django.http import *
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import render
from searchapp.models import linkmodel
from searchapp.models import imagesmodel
from bs4 import BeautifulSoup


def index(request):
   return render_to_response('index.html', context_instance=RequestContext(request))

link_id = ""

def importdata(request):   
    url = "https://selfieblue.wordpress.com"
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text,"html.parser")
    for link in soup.findAll('a',{'class':'feed-item'}):
        ts = time.time()
        link_id = str(int(ts))
        href = link.get('href')
        insert_data = linkmodel(linkid=link_id,linkurl=href)
        insert_data.save()
        feed_images_data(href,link_id)
    response_dict = {}                                          
    response_dict.update({'server_response': 'Imported Data' })
    return HttpResponse(json.dumps(response_dict), content_type='application/json')
    
def feed_images_data(page_url,link_id):
    source_code = requests.get(page_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text,"html.parser")
    for img_name in soup.findAll('img',{'title':'image'}):
        image = str(img_name.get('src'))
        insert_image = imagesmodel(linkid=link_id,imageurl=image)
        insert_image.save()
        
def search(request):
    all_result = "<table style='width:100%'>"
    count = 0
    if count == 0:
        keyword = request.POST['client_response']
        check_num = len(linkmodel.objects.filter(linkurl__contains=keyword))
        if check_num <= 0:
            all_result = "<tr align='center'><td>Sorry,not found this keyword on my database ! :(</td></tr>"
        else:
            for e in linkmodel.objects.filter(linkurl__contains=keyword):
                count +=1
                all_result += "<tr><td><a href='"+e.linkurl+"' target='_blank'><b>Result #"+str(count)+"</b></a></td></tr>"
                all_result += "<tr><td>"
                for i in imagesmodel.objects.filter(linkid__contains=e.linkid):
                    all_result += "<a href='"+i.imageurl+"' target='_blank'><img src='"+i.imageurl+"' style='width:50px;height:50px;'/></a>"
                    
                all_result += "</td></tr>"
            
    all_result += "</table>"    
    
    return HttpResponse(all_result, content_type='text/html')
