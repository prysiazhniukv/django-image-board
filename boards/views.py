from django.shortcuts import render, get_object_or_404, redirect
from .forms import ThreadForm
from .models import Board

# Create your views here.


def book_details(request, slug):
    board = get_object_or_404(Board, slug=slug)
    threads = board.thread_set.order_by("-created_at")
    return render(
        request,
        "board_details.html",
        {
            "board": board,
            "threads": threads,
        },
    )


def thread_create(request, slug):
    board = get_object_or_404(Board, slug=slug)

    form = ThreadForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        thread = form.save(commit=False)
        thread.board = board
        thread.save()
        return redirect("boards:board_details", slug=board.slug)

    return render(
        request,
        "thread_form.html",
        {
            "board": board,
            "form": form,
        },
    )
