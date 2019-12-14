from datetime import datetime, date
import os

from django.shortcuts import render
from app.settings import FILES_PATH


def file_list(request, date: date = None):
    template_name = 'index.html'
    files = os.listdir(FILES_PATH)
    print(date.date())
    if date is None:
        context = {
            'files': []
        }
        for file in files:
            file_ctime = datetime.fromtimestamp(os.stat('files/' + file).st_ctime).date()
            file_mtime = datetime.fromtimestamp(os.stat('files/' + file).st_mtime).date()
            context['files'].append({'name': file,
                                     'ctime': file_ctime,
                                     'mtime': file_mtime})

    else:
        context = {
            'files': []
        }
        for file in files:
            file_ctime = datetime.fromtimestamp(os.stat('files/' + file).st_ctime).date()
            file_mtime = datetime.fromtimestamp(os.stat('files/' + file).st_mtime).date()
            if date.date() == file_ctime or date.date() == file_mtime:
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
    return render(request, 'file_content.html', context={'file_name': name, 'file_content': data})
