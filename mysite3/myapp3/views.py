from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact
from .forms import CreateContactForm, EditContactForm

def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'myapp3/contactlist.html', {'contacts': contacts})

def create_contact(request):
     if request.method == 'POST':
        form = CreateContactForm(request.POST)
        if form.is_valid():
            formdata = form.cleaned_data
            Contact.objects.create(
                name = formdata['name'],
                address = formdata['address'],
                profession = formdata['profession'],
                tel_number = formdata['tel_number'],
                email = formdata['email'],
            )
            return redirect('contact_list')
     else:
        form = CreateContactForm()

     return render(request, 'myapp3/createcontact.html', {'form': form})
	

def edit_contact(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)

    if request.method == 'POST':
        form = EditContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()  # This will update the existing contact with the new data
            return redirect('contact_list')
    else:
        form = EditContactForm(instance=contact)

    return render(request, 'myapp3/editcontact.html', {'form': form})

def delete_contact(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)
    contact.delete()
    return redirect('contact_list')


