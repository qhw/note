# -*- coding: utf-8 -*- 

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from things.models.models import Note
import datetime, time
import json
import os, re, string
from our import settings

#显示首页
def note_show(request):
    return render_to_response('note.html')

#获取笔记标题列表
def note_subjects(request):
    notes = Note.objects.filter(flag=0).order_by("-modifytime")
    
    results = {}
    i = 0
    for note in notes:
        results[i] = [note.id, note.title]
        i += 1
    return HttpResponse(json.dumps(results))

#获取指定笔记id的内容
def note_get(request):
    note_id = request.POST["id"]
    note = Note.objects.get(id=int(note_id))
    results = {"id" : note.id, "subject" : note.title, "content" : note.content}
    return HttpResponse(json.dumps(results))

#创建一个新的笔记
def note_create(request):
    note_subject = request.POST["subject"]
    note_content = request.POST["content"]
    note_createtime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    note = Note(title=note_subject, content = note_content, 
                createtime=note_createtime, modifytime=note_createtime, flag=0)
    note.save()
    return HttpResponse(note.id)

#更新笔记
def note_update(request):
    note_id = request.POST["id"]
    note_subject = request.POST["subject"]
    note_content = request.POST["content"]
    note_modifytime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    note = Note.objects.filter(id=int(note_id))
    note.update(title=note_subject, content=note_content, modifytime=note_modifytime)
    return HttpResponse("success")

#删除笔记
def note_delete(request):
    note_id = request.POST["id"]
    Note.objects.get(id = int(note_id)).delete();
    return HttpResponse("success")
    
    
       
    