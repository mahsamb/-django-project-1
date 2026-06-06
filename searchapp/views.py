from django.core.paginator import Paginator, EmptyPage
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render

from searchapp.utils.utils import get_online_anonymous_count
from .models import (
    SiteVisit,
    bagmodel_english_json,
    pantsmodel_english_json,
    shoesmodel_english_json,
    tshirtmodel_english_json,
)

CATEGORY_MAP = {
    'تیشرت': ('tshirt', tshirtmodel_english_json),
    'شلوار': ('pants', pantsmodel_english_json),
    'کیف': ('bag', bagmodel_english_json),
    'کفش': ('shoes', shoesmodel_english_json),
}

MODEL_MAP = {
    'tshirt': tshirtmodel_english_json,
    'pants': pantsmodel_english_json,
    'bag': bagmodel_english_json,
    'shoes': shoesmodel_english_json,
}

ITEMS_PER_PAGE = 9


def to_persian_number(number):
    en_to_fa = str.maketrans("0123456789", "۰۱۲۳۴۵۶۷۸۹")
    return str(number).translate(en_to_fa)


def get_site_stats():
    visit_obj = SiteVisit.objects.first()
    total = visit_obj.total_visits if visit_obj else 0
    return to_persian_number(total), to_persian_number(get_online_anonymous_count())


def queryset_to_results(queryset, category_key):
    return [
        (product.id, product.title_fa, product.description, category_key)
        for product in queryset
    ]


def get_products(query_text='', category_label='تیشرت', limit=200):
    category_key, Model = CATEGORY_MAP.get(category_label, CATEGORY_MAP['تیشرت'])
    queryset = Model.objects.all().order_by('id')
    if query_text:
        queryset = queryset.filter(
            Q(title_fa__icontains=query_text)
            | Q(description__icontains=query_text)
            | Q(attributes__icontains=query_text)
        )
    return queryset_to_results(queryset[:limit], category_key)


def base_context():
    total_visits, online_count = get_site_stats()
    return {
        'total_visits': total_visits,
        'online_count': online_count,
    }


def search(request, feature="", desc="", all_feat=""):
    context = base_context()

    if request.method == 'POST':
        query = request.POST.get('query', '').strip()
        category = request.POST.get('category', 'تیشرت')
        results = get_products(query, category)
        paginator = Paginator(results, ITEMS_PER_PAGE)
        page_obj = paginator.get_page(1)
        request.session['combined_list'] = results
        request.session['query'] = query
        request.session['category'] = category
        context.update({
            'images_cohere_rank': list(page_obj),
            'query': query,
            'selected_category': category,
            'page_obj': page_obj,
        })
        return render(request, 'search.html', context)

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        page_number = request.GET.get('page', 1)
        combined_list = request.session.get('combined_list', [])
        if not combined_list:
            return JsonResponse({'products': []})
        paginator = Paginator(combined_list, ITEMS_PER_PAGE)
        try:
            page_obj = paginator.page(page_number)
        except EmptyPage:
            return JsonResponse({'products': []})
        products_list = [
            {'file_name': item[3], 'image_url': item[0], 'text': item[1]}
            for item in page_obj
        ]
        return JsonResponse({'products': products_list})

    results = get_products('', 'تیشرت')
    paginator = Paginator(results, ITEMS_PER_PAGE)
    page_obj = paginator.get_page(request.GET.get('page', 1))
    context.update({
        'images_cohere_rank': list(page_obj),
        'page_obj': page_obj,
        'selected_category': 'تیشرت',
    })
    return render(request, 'search.html', context)


def product_details(request, pk, file_name):
    ModelClass = MODEL_MAP.get(file_name)
    if not ModelClass:
        return JsonResponse({'error': 'Invalid category'}, status=400)
    product = ModelClass.objects.get(pk=pk)
    return JsonResponse({
        'title_fa': product.title_fa,
        'attributes': product.attributes,
        'image_link': product.image_link,
    })


def about_us(request):
    return render(request, 'aboutUs.html', base_context())


def contact_us(request):
    return render(request, 'contactUs.html', base_context())
