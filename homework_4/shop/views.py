from typing import Any
from django.shortcuts import get_object_or_404, HttpResponse
from django.views.generic import TemplateView
from shop.models import Customer, Product, Order
from django.http import HttpRequest
from shop.forms import ProductForm
from django.core.files.storage import FileSystemStorage


class TemplateProducts(TemplateView):
    template_name = 'shop/products.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.order_by('name')
        return context


class TemplateInfoAboutProduct(TemplateView):
    template_name = 'shop/product_info.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        product = get_object_or_404(Product, pk=context['product_id'])
        form = ProductForm(instance=product)
        context['product'] = product
        context['form'] = form
        return context

    def post(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        context = self.get_context_data(**kwargs)
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            product = get_object_or_404(Product, pk=context['product_id'])
            product.name = form.cleaned_data['name']
            product.price = form.cleaned_data['price']
            product.description = form.cleaned_data['description']
            if image:
                fs = FileSystemStorage()
                fs.save(f'{product.id}_{image.name}', image)
                product.image = f'{product.id}_{image.name}'
            product.save()
            context['message'] = f'{product.name} updated'
            # return self.render_to_response(context)
        return self.get(request=request, **context)
