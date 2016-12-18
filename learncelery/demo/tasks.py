from __future__ import absolute_import, unicode_literals
from bs4 import BeautifulSoup
import requests

from celery import task

from .models import Link


@task
def add(x, y):
    return x + y


@task
def mul(x, y):
    return x * y


@task
def xsum(numbers):
    return sum(numbers)


@task
def get_link_name(id, url):
    link = Link.objects.get(id=id)
    title = url + ' - WEBPAGE'

    try:
        # Get page.
        result = requests.get(url=url)
        soup = BeautifulSoup(result.content, 'html.parser')

        # Get title and set it as link's name.
        title = soup.html.head.title.text

    except Exception as e:
        pass

    # Set link title and save link.
    link.name = title
    link.save()
