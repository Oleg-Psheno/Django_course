from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'mainapp/index.html')


def products(request):
    context = {
        'products': [{"name": "Худи черного цвета с монограммами adidas Originals", "description": 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.', "price": '6 090,00', },
                     {"name": "Синяя куртка The North Face", "description": 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и '
                                                               'теплый пуховый наполнитель.', "price": '23 725,00', },
                     {"name": "Коричневый спортивный oversized-топ ASOS DESIGN", "description": 'Материал с плюшевой текстурой. '
                                                                                               'Удобный и мягкий.', "price": '3 '
                                                                                                                             '390,00', },
                     {"name": "Черный рюкзак Nike Heritage",
                      "description": 'Плотная ткань. Легкий материал.', "price": '2 340,00', },
                     {"name": "Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex",
                      "description": 'Гладкий кожаный верх. Натуральный материал.', "price": '13 590,00', },
                     {"name": "Темно-синие широкие строгие брюки ASOS DESIGN",
                      "description": 'Легкая эластичная ткань сирсакер Фактурная ткань.', "price": '2 890,00', },],
        'title':'products',


    }

    return render(request, 'mainapp/products.html', context)