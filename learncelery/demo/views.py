from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse

from .forms import LinkForm
from .tasks import add, get_link_name


def index(request):
    sum = add.delay(2, 3)
    return HttpResponse('Task Scheduled...sum is {}'.format(sum))


def create_link(request):
    form = LinkForm(request.POST or None)

    if form.is_valid():
        link = form.save()
        get_link_name.delay(id=link.id, url=link.destination)
        return redirect(reverse('index'))

    return render(request, 'demo/create_link.html', {'form': form})
