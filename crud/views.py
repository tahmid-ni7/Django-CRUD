from django.shortcuts import render, redirect, get_object_or_404
from .models import Member
from django.contrib import messages
from .forms import MemberForm


# ========= HOME PAGE =============
def home(request):
    members = Member.objects.order_by('-id').filter(is_active=True)
    context = {
        'members': members
    }
    return render(request, 'crud/home.html', context)


# =========== CREATE MEMBER ==========
def create(request):
    form = MemberForm()
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Member created successfully.")
            return redirect('home')
        else:
            messages.error(request, 'Please fill all fields correctly.')

    context = {'form': form}
    return render(request, 'crud/create.html', context)


# ========== SHOW THE EDIT PAGE ==========
def edit(request, member_id):
    member = get_object_or_404(Member, pk=member_id)
    form = MemberForm(instance=member)
    context = {
        'member': member,
        'form': form
    }
    return render(request, 'crud/edit.html', context)


# ========== UPDATE MEMBER ==========
def update(request, member_id):
    member = get_object_or_404(Member, pk=member_id)
    form = MemberForm(request.POST, instance=member)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Member updated successfully.")
            return redirect('home')
        else:
            messages.error(request, 'Please fill all fields correctly.')

    context = {'form': form}
    return render(request, 'crud/create.html', context)


# ========== DELETE MEMBER ==========
def delete(request, member_id):
    member = get_object_or_404(Member, pk=member_id)
    member.delete()
    messages.success(request, "Member deleted successfully.")
    return redirect('home')
