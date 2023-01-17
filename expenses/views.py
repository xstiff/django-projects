from django.views.generic.list import ListView
from .forms import ExpenseSearchForm, SortbyForm
from .models import Expense, Category
from .reports import summary_per_category


class ExpenseListView(ListView):
    model = Expense
    paginate_by = 6

    def get_context_data(self, *, object_list=None, **kwargs):
        queryset = object_list if object_list is not None else self.object_list

        form = ExpenseSearchForm(self.request.GET)
        sortbyform = SortbyForm(self.request.GET)
        if sortbyform.is_valid():
            sort_order = sortbyform.cleaned_data.get('dropdown', '')
        if form.is_valid():
            name = form.cleaned_data.get('name', '').strip()
            date = form.cleaned_data.get('date', '')
            
            if name:
                queryset = queryset.filter(name__icontains=name)
            if date:
                queryset = queryset.filter(date__icontains=date)
            if sort_order:
                queryset = queryset.order_by(sort_order)

        return super().get_context_data(
            form=[form,sortbyform],
            object_list=queryset,
            summary_per_category=summary_per_category(queryset),
            **kwargs)

class CategoryListView(ListView):
    model = Category
    paginate_by = 5

