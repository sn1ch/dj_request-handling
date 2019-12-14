from django.urls import register_converter

from app.converters import DateConverter

register_converter(DateConverter, 'date')