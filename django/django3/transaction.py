from django.db import transaction

def viewfunc(request):
    # This code executes in autocommit mode (Django's default).
    do_stuff()

    with transaction.atomic():
         # This code executes inside a transaction.
         do_more_stuff()
