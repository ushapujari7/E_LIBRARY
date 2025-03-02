from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import UserRegistrationForm
from .models import UserProfile


def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            # Create UserProfile
            role = form.cleaned_data['role']
            UserProfile.objects.create(user=user, role=role)

            return redirect('login')  # Redirect to login after registration
        else:
            form = UserRegistrationForm()
        return render(request, 'register.html', {'form': form})

