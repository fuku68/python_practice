from django.db import transaction

@transaction.non_atomic_requests
def my_view(request):
    do_stuff()
