import datetime
import os

from django.shortcuts import render
from app.settings import FILES_PATH


def file_list(request, year=None, month=None, day=None):
    template_name = 'index.html'
    files = os.listdir(FILES_PATH)
    if year == None and month == None and day == None:
        context = {
            'files': []
        }
        for file in files:
            file_ctime = datetime.datetime.fromtimestamp(os.stat('files/' + file).st_ctime).date()
            file_mtime = datetime.datetime.fromtimestamp(os.stat('files/' + file).st_mtime).date()
            context['files'].append({'name': file,
                                     'ctime': file_ctime,
                                     'mtime': file_mtime})

    else:
        context = {
            'files': []
        }
        for file in files:
            request_date = datetime.datetime(year=year, month=month, day=day).date()
            file_ctime = datetime.datetime.fromtimestamp(os.stat('files/' + file).st_ctime).date()
            file_mtime = datetime.datetime.fromtimestamp(os.stat('files/' + file).st_mtime).date()
            if request_date == file_ctime or request_date == file_mtime:
                context['files'].append({'name': file,
                                         'ctime': file_ctime,
                                         'mtime': file_mtime})
    return render(request, template_name, context)


def file_content(request, name):
    # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
    if name in os.listdir(FILES_PATH):
        file = os.path.join(FILES_PATH, name)
        with open(file, 'r') as f:
            data = f.read()

    return render(
        request,
        'file_content.html',
        context={'file_name': name, 'file_content': data}
    )
