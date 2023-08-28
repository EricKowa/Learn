from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic

from .models import FirstDatabase, SecondDatabase

# Create your views here.

class IndexView(generic.ListView):
    template_name = "app/index.html"
    context_object_name = "latest_entries_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return FirstDatabase.objects.order_by("-entry_created")[:5]

# def index(request):
#     latest_entries_list = FirstDatabase.objects.order_by("-entry_created")[:5]
#     context = {
#         "latest_entries_list" : latest_entries_list,
#     }
#     return render(request, "app/index.html",context)



def undex(request):
    return HttpResponse("Whuuuut theeee???")

class DetailView(generic.DetailView):
    model = FirstDatabase
    template_name = "app/detail.html"
    context_object_name = "entry"

# def detail(request, firstdatabase_id):
    
#     entrilly = get_object_or_404(FirstDatabase, pk=firstdatabase_id)
    
#     return render(request, "app/detail.html", {"entry" : entrilly})


class ResultsView(generic.DetailView):
    model = FirstDatabase
    template_name = "app/results.html"
    context_object_name = "entry"

# def results(request, firstdatabase_id):
#     response = "You're looking at the results to FirstDatabase entry %s."
#     entry = get_object_or_404(FirstDatabase, pk=firstdatabase_id)
#     return render(request, "app/results.html", {"entry": entry})

def numbi(request, firstdatabase_id):
    entry = get_object_or_404(FirstDatabase, pk=firstdatabase_id)
    try:
        pfiffi = entry.seconddatabase_set.get(pk=request.POST["second"])
    except (KeyError, FirstDatabase.DoesNotExist):
        return render(
            request,
            "app/detail.html",
            {
                "entry": entry,
                "error_message": "You didn't select anything from the SecondDatabase."
            },
        )
    else:
        pfiffi.super_number += 1
        pfiffi.save()
        
        return HttpResponseRedirect(reverse("app:results", args=(entry.id,)))

#practiciing the loader and context
def tri(request):
    elsee = "hohoho"
    pulli = "Grrrrr"
    context = {
        "something" : elsee,
        "other" : pulli,
    }
    return render(request, "app/trying.html", context)