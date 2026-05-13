import random
from django.shortcuts import render
from .models import Taom, Buyurtma


def menyu_view(request):
    taomlar = Taom.objects.all()

    # 1. Omadli taom (tasodifiy bittasini tanlash)
    omadli_taom = random.choice(taomlar) if taomlar.exists() else None

    # 2. Jonli buyurtmalar (eng oxirgi 5 ta buyurtma holati)
    jonli_buyurtmalar = Buyurtma.objects.all().order_by('-vaqti')[:5]

    # 3. Chegirmali va Trenddagilar (oldingi kodimiz)
    chegirmadagilar = Taom.objects.filter(chegirma_foizi__gt=0)

    context = {
        'taomlar': taomlar,
        'omadli_taom': omadli_taom,
        'jonli_buyurtmalar': jonli_buyurtmalar,
        'chegirmadagilar': chegirmadagilar,
    }
    return render(request, 'index.html', context)
