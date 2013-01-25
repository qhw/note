# -*- coding: utf-8 -*- 

from django.http import HttpResponse
from django.shortcuts import render_to_response
from things.models.models import Note
import json

#统计笔记数量
def note_total_number(request):
    return HttpResponse(get_note_total_number())

#返回一页数据，指定开始位置和结束位置
def note_page(request):
    start = request.POST["start_num"]
    end = request.POST["end_num"]
    
    max_elem = end
    total_numbers = get_note_total_number()
    if int(max_elem) > total_numbers:
      max_elem = total_numbers
  
    results = {}
    i = 0
    notes = Note.objects.all().order_by("-modifytime")[start:max_elem]
    for note in notes:
      results[i] = [note.id, note.title, note.content]
      i += 1
    return HttpResponse(json.dumps(results))

#返回笔记数量
def get_note_total_number():
    return Note.objects.all().count()
  
def pagination(request):
    return render_to_response("pagination.html")
       
    
    
       
    