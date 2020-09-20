from django.shortcuts import render

from . import util

import markdown2
import random

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def wikipage(request, title):
    mk2 = util.get_entry(title)
    if mk2:
        contents = markdown2.markdown(mk2)
        return render(request, "encyclopedia/entry.html", {
            "title": title, "content": contents
        })
    else:
        title = "Page Not Found"
        contents = "Sorry, the page you requested for does not exist."
        return render(request, "encyclopedia/error.html", {
            "title": title, "content": contents
        })
    
def results(request):
    query = request.GET.get('query')
    entries = util.list_entries()
    if query in entries:
        contents = markdown2.markdown(util.get_entry(query))
        return render(request, "encyclopedia/entry.html", {
            "title": query, "content": contents
        })
    else:
        matches = []
        for entry in entries:
            if query in entry:
                matches.append(entry)
        return render(request, "encyclopedia/results.html", {
            "query": query, "matches": matches
        })

def create(request):
    return render(request, "encyclopedia/create.html")

def save(request):
    title = request.GET.get('title')
    content = request.GET.get('content')
    entries = util.list_entries()
    if title in entries:
        title = "Page Already Exists!"
        contents = "Sorry, this wiki already exists."
        return render(request, "encyclopedia/error.html", {
            "title": title, "content": contents
        })
    else:
        util.save_entry(title, content)
        contents = markdown2.markdown(util.get_entry(title))
        return render(request, "encyclopedia/entry.html", {
            "title": title, "content": contents
        })

def edit(request):
    title = request.GET.get('title')
    contents = util.get_entry(title)
    return render(request, "encyclopedia/edit.html", {
        "title": title, "content": contents
    })

def update(request):
    title = request.GET.get('title')
    content = request.GET.get('content')
    util.save_entry(title, content)
    contents = markdown2.markdown(util.get_entry(title))
    return render(request, "encyclopedia/entry.html", {
        "title": title, "content": contents
    })

def rand(request):
    entries = util.list_entries()
    lucky = random.choice(entries)
    contents = markdown2.markdown(util.get_entry(lucky))
    return render(request, "encyclopedia/entry.html", {
        "title": lucky, "content": contents
    })