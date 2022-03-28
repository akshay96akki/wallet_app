from django.db.models import Sum
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .models import Wallet


class CustomLoginView(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('walletlist')


class RegisterPage(FormView):
    template_name = 'register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('walletlist')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('walletlist')
        return super(RegisterPage, self).get(*args, **kwargs)


class Walletlist(LoginRequiredMixin, ListView):
    model = Wallet
    template_name = 'wallet_list.html'
    context_object_name = 'entries'


def balance(request):
    balance = Wallet.objects.aggregate(TOTAL = Sum('amount'))['TOTAL']
    return render(request, 'balance.html', {'balance': balance})


class CreateEntry(LoginRequiredMixin, CreateView):
    model = Wallet
    template_name = 'wallet_form.html'
    fields = ['amount']
    success_url = reverse_lazy('walletlist')

    def form_valid(self, form):                         #restricts from showing user in form
        form.instance.user = self.request.user
        return super(CreateEntry, self).form_valid(form)


class EntryUpdate(LoginRequiredMixin, UpdateView):
    model = Wallet
    template_name = 'wallet_form.html'
    fields = ['amount']
    success_url = reverse_lazy('walletlist')


class DeleteEntry(LoginRequiredMixin, DeleteView):
    model = Wallet
    template_name = 'wallet_delete_confirmation_form.html'
    fields = '__all__'
    context_object_name = 'entries'
    success_url = reverse_lazy('walletlist')