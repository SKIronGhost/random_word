from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

attempt = 0


def index(request):
    global attempt
    attempt = 0
    word = ''
    context = {
        "word": word,
        "attempt": attempt
    }
    return render(request, "ram_wrd.html", context)


def generate_word(request):
    global attempt
    attempt += 1
    word = get_random_string(14)
    context = {
        "word": word,
        "attempt": attempt
    }
    return render(request, 'ram_wrd.html', context)

