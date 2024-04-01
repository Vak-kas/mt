from django.shortcuts import render, HttpResponse, redirect
from .forms import CardForm
from .models import Card
import random
from django.http import JsonResponse



# Create your views here.

def index(request):
    return HttpResponse("안녕하세요 로그인에 오신것을 환영합니다.")


# gold/views.py

from django.shortcuts import render

def main_view(request):
    # 이미지 파일의 정적 경로를 context에 추가합니다.
    context = {
        'card_image_url': 'image.PNG'
    }
    return render(request, 'gold/card.html', context)



# gold/views.py


def makeCard(request):
    if request.method == 'POST':
        form = CardForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data.get('quantity')
            num = form.cleaned_data.get('num')
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')

            for _ in range(quantity):
                Card.objects.create(num=num, title=title, content=content)
            return redirect('gold/make_card.html')  # 'some-view'는 성공시 리디렉트 될 URL 이름입니다.

    else:
        form = CardForm()

    return render(request, 'gold/make_card.html', {'form': form})


def draw_card(request):
    cards = list(Card.objects.all())
    if cards:
        card = random.choice(cards)
        return JsonResponse({
            'title': card.title,
            'content': card.content
        })
    else:
        return JsonResponse({'error': 'No cards available'}, status=500)
