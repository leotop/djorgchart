# Leotop system
from orgchart.models import OrgChartModel

# Django kernel.
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import Http404
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django import forms


def home(request):
    # counter = OrgChartModel.objects.select_related().count()
    result = OrgChartModel.objects.select_related()
    counter = len(result)
    return render(
        request, 'orgchart/home.html',
        {
            'data': result,
            'counter': counter
        }
    )


class ChartForm(forms.Form):
    title = forms.CharField(max_length=250, label='Название', required=True)
    content = forms.CharField(label='Сообщение', widget=forms.Textarea)


def chart_edit(request, id):
    try:
        if request.method == 'POST':  # If the form has been submitted...
            form = ChartForm(request.POST)  # A form bound to the POST data
            json_result = OrgChartModel.objects.get(id=id)
            if form.is_valid():
                title = form.cleaned_data['title']
                content = form.cleaned_data['content']
                b = OrgChartModel(id=id, Title=title, Content=content)
                b.save()
                json_result = OrgChartModel.objects.get(id=id)
                return render(request, 'orgchart/index.html', {'data': json_result, 'form': ChartForm})
        else:
            json_result = OrgChartModel.objects.get(id=id)
            form = ChartForm()

    except OrgChartModel.DoesNotExist:
        raise Http404

    # b = OrgChartModel(id="1", Title="NEW", Content="data")
    # b.save()
    return render(request, 'orgchart/index.html', {'data': json_result, 'form': ChartForm})

init_chart = '''[{"id":1,"name":"Главная","parent":0},
{"id":2,"name":"Услуги","parent":1},
{"id":3,"name":"Портфолио","parent":1},
{"id":4,"name":"Клиенты","parent":1},
{"id":5,"name":"Прайс-лист","parent":1},
{"id":6,"name":"Контакты","parent":1},
{"id":7,"name":"Услуга 1","parent":2},
{"id":8,"name":"Услуга 2","parent":2},
{"id":9,"name":"Услуга 3","parent":2},
{"id":10,"name":"Проекты 1","parent":3},
{"id":11,"name":"Проекты 2","parent":3},
{"id":12,"name":"Калькулятор","parent":5},
{"id":13,"name":"Excel","parent":5},
{"id":14,"name":"Схема проезда","parent":6}]'''

init_chart = '''[{"id":1,"name":"Главная","parent":0}]'''


def chart_new(request):
    b = OrgChartModel(Title="Новая структурная схема", Content=init_chart)
    b.save()
    last_id = OrgChartModel.objects.order_by('id').last()
    return HttpResponseRedirect(reverse('chart_edit', kwargs={'id': last_id.id}))


def chart_delete(request, id):
    OrgChartModel.objects.filter(id=id).delete()
    return HttpResponseRedirect(reverse('chart_home'))