# -*- coding: utf-8 -*- 

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import datetime, time
import json
import os, re, string
from our import settings

#上传文件
@csrf_exempt
def ke_upload_view(request):
    ext_allowed = {}
    ext_allowed["image"] = ['gif', 'jpg', 'jpeg', 'png']
    ext_allowed["flash"] = ["swf", "flv"]
    ext_allowed["media"] = ["swf", "flv", "mp3", "wav", "wma", "wmv", "mid", "avi", "mpg", "asf", "rm", "rmvb"]
    ext_allowed["file"] = ["doc", "docx", "xls", "xlsx", "ppt", "htm", "html", "txt", "zip", "rar", "gz" , "bz2"]
    
    max_size = 1000000
    today = datetime.datetime.today()
    dir_name = request.GET["dir"]
    save_dir = '/attached/' + dir_name + '/%d/%d/%d/' % (today.year, today.month, today.day)
    save_path = settings.TEMPLATE_DIRS[0] + save_dir
    save_url = settings.MEDIA_URL  + save_dir

    if request.method == 'POST':
        file_content = request.FILES['imgFile']

        if not file_content.name:
            return HttpResponse(json.dumps(
                { 'error': 1, 'message': u'请选择要上传的文件' }
            ))
            
        ext = file_content.name.split('.').pop()
        
        if ext not in ext_allowed[dir_name]:
            return HttpResponse(json.dumps(
                { 'error': 1, 'message': u'请上传后缀为%s的文件' %  ext_allowed[dir_name]}
            ))

        if file_content.size > max_size:
            return HttpResponse(json.dumps(
                { 'error': 1, 'message': u'上传的文件大小不能超过10MB'}
            ))

        if not os.path.isdir(save_path):
            os.makedirs(save_path)

        new_file = '%s.%s' % (int(time.time()), ext)

        destination = open(save_path+new_file, 'wb+')
        for chunk in file_content.chunks():
            destination.write(chunk)
        destination.close()

        return HttpResponse(json.dumps(
                { 'error': 0, 'url': save_url+new_file}
        ))
        
#从服务器上选择文件  
def file_manager_json(request):
  root_path = settings.TEMPLATE_DIRS[0] + "/attached/"
  root_url = settings.MEDIA_URL + "/attached/"
  file_types = ["gif", "jpg", "jpeg", "png", "bmp"]
  dir_types = ['image', 'flash', 'media', 'file']
  
  dir_name = request.GET["dir"]
   
  
  if dir_name:
    if dir_name not in dir_types:
      print("Invalid Directory name.")
      return
    root_path = root_path + dir_name + "/"
    root_url = root_url + dir_name + "/"
    if not os.path.isdir(root_path) or not os.path.exists(root_path):
      os.makedirs(root_path)
  
 
  path = request.GET["path"]
  if not path:
    path = ""
  current_path = root_path + path
  current_url = root_url + path
  current_dir_path = path
  moveup_dir_path = ""
  
  if path:
    m = re.search(r'(.*?)[^\/]+\/$', current_dir_path)
    moveup_dir_path = m.group(1)

  order = request.GET["order"]
  if order:
    order = string.lower(order)
  else:
    order = "name"
       
  if ".." in current_path:
    print "Access is not allowed."
    return

  if re.search(r'(\/$)', current_path).group(0) != '/':
    print "Parameter is not valid."
    return
  
  if not os.path.isdir(current_path) or not os.path.exists(current_path):
    print "'Directory does not exist."
    return
   
  file_list = []
  if os.listdir(current_path):
    for file_name in os.listdir(current_path):
      dicts = {}
      file_path = current_path + file_name
      if os.path.isdir(file_path):
        dicts["is_dir"] = True
        dicts["has_file"] = len(os.listdir(file_path)) > 0
        dicts["filesize"] = 0
        dicts["is_photo"] = False
        dicts["filetype"] = ""
      else:
        dicts["is_dir"] = False
        dicts["has_file"] = False
        dicts["filesize"] = os.path.getsize(file_path)

        extensions = string.split(file_name, ".")
        length = len(extensions) - 1
        if string.lower(extensions[length]) in file_types:
          dicts["is_photo"] = True
        else:
          dicts["is_photo"] = False
        dicts["filetype"] = string.lower(extensions[length])
      dicts["filename"] = file_name
      dicts["datetime"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
      file_list.append(dicts)
    
    results = {}
    results["moveup_dir_path"] = moveup_dir_path
    results["current_dir_path"] = current_dir_path
    results["current_url"] = current_url
    results["total_count"] = len(file_list)
    results["file_list"] = file_list

    return HttpResponse(json.dumps(results))
                
               
       
    
    
       
    