from django.http import HttpResponseRedirect


def main_index(request):
    return HttpResponseRedirect('/vote/')