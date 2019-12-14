from collections import Counter

from django.shortcuts import render_to_response

# Для отладки механизма ab-тестирования используйте эти счетчики
# в качестве хранилища количества показов и количества переходов.
# но помните, что в реальных проектах так не стоит делать
# так как при перезапуске приложения они обнулятся
counter_show = Counter()
counter_click = Counter()


def index(request):
    # Реализуйте логику подсчета количества переходов с лендига по GET параметру from-landing
    land = request.GET.get('from-landing')
    if land == 'original':
        counter_click['original'] += 1
    elif land == 'test':
        counter_click['test'] += 1
    print('click: ', counter_click)
    return render_to_response('index.html')


def landing(request):
    # Реализуйте дополнительное отображение по шаблону app/landing_alternate.html
    # в зависимости от GET параметра ab-test-arg
    # который может принимать значения original и test
    # Так же реализуйте логику подсчета количества показов
    land = request.GET.get('ab-test-arg')
    print(land)
    if land == 'original':
        counter_show['original'] += 1
        res = render_to_response('landing.html')
    elif land == 'test':
        counter_show['test'] += 1
        res = render_to_response('landing_alternate.html')
    print('show:', counter_show)
    return res


def stats(request):
    # Реализуйте логику подсчета отношения количества переходов к количеству показов страницы
    # Чтобы отличить с какой версии лендинга был переход
    # проверяйте GET параметр marker который может принимать значения test и original
    # Для вывода результат передайте в следующем формате:
    if counter_show['original'] != 0:
        result_original = counter_click['original'] / counter_show['original']
    else:
        result_original = 0
    if counter_show['test'] != 0:
        result_test = counter_click['test'] / counter_show['test']
    else:
        result_test = 0
    return render_to_response('stats.html', context={
        'test_conversion': result_test,
        'original_conversion': result_original,
    })
