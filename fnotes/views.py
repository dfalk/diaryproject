from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from fnotes.models import Entry, EntryTag
from fnotes.forms import EntryForm

def index(request):
    latest_entry_list = Entry.objects.all().order_by('-time')[:25]
    context = {'latest_entry_list':latest_entry_list}
    return render(request, 'fnotes/index.html', context)

def detail(request, entry_id):
    entry = get_object_or_404(Entry, pk=entry_id)
    return render(request, 'fnotes/detail.html', {'entry':entry})

def tag(request, tag_id):
    tag = get_object_or_404(EntryTag, pk=tag_id)
    entry_list = Entry.objects.filter(tags__pk=tag_id)
    return render(request, 'fnotes/list.html', {'tag':tag, 'entry_list':entry_list})

def edit(request, entry_id=None):
    entry = None
    if entry_id:
        entry = get_object_or_404(Entry, pk=entry_id)
    if request.method == 'POST':
        form = EntryForm(request.POST, instance=entry)
        if form.is_valid():
            new_entry = form.save()
            return HttpResponseRedirect(
                reverse("fnotes_detail", args=(new_entry.id,))
            )
    else:
        form = EntryForm(instance=entry)
    return render(request, 'fnotes/edit.html', {'form':form, 'entry':entry})