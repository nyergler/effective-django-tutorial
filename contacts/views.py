from django.views.generic import ListView

from contacts.models import Contact


class ListContactView(ListView):

    model = Contact
    template_name = 'contact_list.html'
