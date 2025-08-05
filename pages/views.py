from django.contrib import messages
from django.shortcuts import render, redirect
from pages.forms import ContactModelForm
from pages.models import StoreModel


def home_view(request):
    return render(request, 'home.html')

def contact_view(request):
    if request.method == "POST":
        form = ContactModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Your contact has been sent to admins ✅"
            )
        else:
            messages.error(request, "Please, correct your data ❌")
            # for field, errors in form.errors.items():
            #     messages.error(request, f"{field}: {'; '.join(errors)}")
        return redirect('pages:contact')
    else:
        context = {
            "stores": StoreModel.objects.filter(picked=True)[:2]
        }
        return render(request, 'pages/contact.html', context)