from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)


def main(request):
    logger.info('Index page accessed')
    res = """
        <h1>Добро пожаловать на мой первый Django-сайт!</h1>
        <p>Привет! Я - Александр!</p>
        """
    logging.info('Пользователь посетил главную страницу')
    return HttpResponse(res)


def about(request):
    res = """
        <h1>Обо мне</h1>
        <p>Привет! Меня зовут Алексанр и я начинающий Python-разработчик.</p>
        """
    logging.info('Пользователь посетил страницу "О себе"')
    return HttpResponse(res)
