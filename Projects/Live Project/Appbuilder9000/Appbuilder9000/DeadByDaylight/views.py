from django.shortcuts import render, redirect, get_object_or_404
from .models import Killer, Survivor, SurvivorPerk, KillerPerk
from .forms import KillerForm, SurvivorForm, SurvivorPerkForm, KillerPerkForm


# Create your views here.
def deadByDaylight_home(request):
    return render(request, 'DeadByDaylight/deadByDaylight_home.html')

def deadByDaylight_killers(request):
    killer = Killer.Killers.all()
    killerPerk = KillerPerk.KillerPerks.all()
    content = {'killer': killer, 'killerPerk': killerPerk}
    return render(request, 'DeadByDaylight/deadByDaylight_killers.html', content)

def create_killer(request):
    form = KillerForm(data=request.POST or None)
    perkform = KillerPerkForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            perkform.save()
            return redirect('deadByDaylight_killers')
    content = {'form': form, 'perkform': perkform}
    return render(request, 'DeadByDaylight/deadByDaylight_createK.html', content)

def deadByDaylight_survivors(request):
    surv = Survivor.Survivors.all()
    surv2 = SurvivorPerk.SurvivorPerks.all()
    content = {'survivor': surv, 'survivorPerk': surv2}
    return render(request, 'DeadByDaylight/deadByDaylight_survivors.html', content)

def create_survivor(request):
    form = SurvivorForm(data=request.POST or None)
    perkform = SurvivorPerkForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            perkform.save()
            return redirect('deadByDaylight_survivors')
    content = {'form': form, 'perkform': perkform}
    return render(request, 'DeadByDaylight/deadByDaylight_createS.html', content)

def survivorDetails(request, pk):
    surv = get_object_or_404(Survivor, pk=pk)
    perk = get_object_or_404(SurvivorPerk, pk=pk)
    content = {'survivor': surv, 'survivorPerk': perk}
    return render(request, 'DeadByDaylight/deadByDaylight_survivor_details.html', content)

def killerDetails(request, pk):
    killer = get_object_or_404(Killer, pk=pk)
    perk = get_object_or_404(KillerPerk, pk=pk)
    content = {'killer': killer, 'killerPerk': perk}
    return render(request, 'DeadByDaylight/deadByDaylight_killer_details.html', content)

def deadByDaylight_edit(request, pk):
    survivor = get_object_or_404(Survivor, pk=pk)
    perk = get_object_or_404(SurvivorPerk, pk=pk)
    survform = SurvivorForm(data=request.POST or None, instance=survivor)
    perkform = SurvivorPerkForm(data=request.POST or None, instance=perk)
    if request.method == 'POST':
        if survform.is_valid():
            survform.save()
            perkform.save()
            return redirect('../survdetails')
    content = {'survform': survform, 'perkform': perkform, 'survivor': survivor}
    return render(request, 'DeadByDaylight/deadByDaylight_edit.html', content)

def deadByDaylight_kedit(request, pk):
    killer = get_object_or_404(Killer, pk=pk)
    perk = get_object_or_404(KillerPerk, pk=pk)
    killerform = KillerForm(data=request.POST or None, instance=killer)
    perkform = KillerPerkForm(data=request.POST or None, instance=perk)
    if request.method == 'POST':
        if killerform.is_valid():
            killerform.save()
            perkform.save()
            return redirect('../killerdetails')
    content = {'killerform': killerform, 'perkform': perkform, 'killer': killer}
    return render(request, 'DeadByDaylight/deadByDaylight_kedit.html', content)


def deadByDaylight_delete(request):
    if request.method == 'POST':
        survivor = request.POST.get('survivor_id')
        Survivor.Survivors.filter(id=survivor).delete()
        SurvivorPerk.SurvivorPerks.filter(id=survivor).delete()
        return redirect('../survivor')

def deadByDaylight_kdelete(request):
    if request.method == 'POST':
        killer = request.POST.get('killer_id')
        Killer.Killers.filter(id=killer).delete()
        KillerPerk.KillerPerks.filter(id=killer).delete()
        return redirect('../killers')

def deadByDaylight_secret(request):
    return render(request, 'DeadByDaylight/deadByDaylight_secret.html')