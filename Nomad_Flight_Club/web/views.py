from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from . models import FlightDetails
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.forms import DateInput, ModelForm
from users.forms import UserRegisterForm
from django.contrib import messages


def home(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can log in now.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'web/home.html', {'title': 'Home', 'form': form, })


def about(request):
    context = {
        'flights': FlightDetails.objects.all(),
        'title': 'Flights'
    }
    return render(request, 'web/flights_list.html', context=context )


class FlightDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = FlightDetails
    template_name = 'web/flight_detail.html'

    def test_func(self):
        flight = self.get_object()
        return self.request.user == flight.user


class FlightDateInput(DateInput):
    input_type = 'date'


class FlightForm(ModelForm):

    class Meta:
        model = FlightDetails
        fields = ['fly_from' , 'fly_to' , 'from_date' , 'to_date' , 'min_nights' , 'max_nights', 'max_sector_stopovers',
                  'adults', 'stopover_from', 'stopover_to']
        widgets = {
            'from_date': FlightDateInput() ,
            'to_date': FlightDateInput() ,
        }


class FlightCreateView(LoginRequiredMixin, CreateView):
    model = FlightDetails
    template_name = 'web/flight_form.html'
    form_class = FlightForm

    def form_valid(self , form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class FlightUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = FlightDetails
    template_name = 'web/flight_form.html'
    fields = ['fly_from' , 'fly_to' , 'from_date' , 'to_date' , 'min_nights' , 'max_nights' , 'max_sector_stopovers' ,
              'adults' , 'stopover_from' , 'stopover_to']
    widgets = {
        'from_date': FlightDateInput(),
        'to_date': FlightDateInput(),
    }

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        flight = self.get_object()
        return self.request.user == flight.user


class FlightDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = FlightDetails
    template_name = 'web/flight_confirm_delete.html'
    success_url = '/flights-list/'

    def test_func(self):
        flight = self.get_object()
        return self.request.user == flight.user


class FlightListView(LoginRequiredMixin, ListView):
    model = FlightDetails
    template_name = 'web/flights_list.html'
    context_object_name = 'flights'
    ordering = 'fly_from'

