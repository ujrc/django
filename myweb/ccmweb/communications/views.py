# Create your views here.
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseForbidden, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic.edit import DeleteView

from accounts.views import account_detail
from accounts.models import Account
from .forms import CommunicationForm
from .models import Communication


@login_required
def comm_detail(request, uuid):
    comm = Communication.objects.get(uuid=uuid)
    if comm.owner != request.user:
        return HttpResponseForbidden()

    return render(request, 'communications/comm_detail.html', {'comm': comm})


@login_required
def comm_cru(request, uuid=None, account=None):
    if uuid:
        comm = get_object_or_404(Communication, uuid=uuid)
        if comm.owner != request.user:
            return HttpResponseForbidden()
    else:
        comm = Communication(owner=request.user)
    if request.POST:
        form = CommunicationForm(request.POST, instance=comm)
        if form.is_valid():
            # make sure the user owns the account
            account = form.cleaned_data['account']
            if account.owner != request.user:
                return HttpResponseForbidden()
            # comm=form.save(commit=False)
            # comm.owner=request.user
            # comm.save()
            form.save()
            # return the user to the account detail view
            if request.is_ajax():
                return render(request, 'communications/comm_item_view.html',
                              {'comm': comm, 'account': account})
            else:
                reverse_url = reverse('accounts.views.account_detail',
                                      args=(account.uuid,))
                return HttpResponseRedirect(reverse_url)
        else:
            # if the form isn't valid, still fetch the account so it can be
            # passed to the template
            account = form.cleaned_data['account']

    else:
        form = CommunicationForm(instance=comm)
    # this is used to fetch the account if it exists as a URL parameter
    if request.GET.get('account'):
        account = Account.objects.get(pk=request.GET.get('account'))
    context_data = {
        'form': form,
        'comm': comm,
        'account': account
    }
    if request.is_ajax():
        template_name = 'communications/comm_item_form.html'
    else:
        template_name = 'communications/comm_cru.html'
    return render(request, template_name, context_data)


class CommMixin(object):
    model = Communication

    def get_context_data(self, **kwargs):
        kwargs.update({'object_name': 'Communication'})
        return kwargs

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CommMixin, self).dispatch(*args, **kwargs)


class CommDelete(CommMixin, DeleteView):
    template_name = 'object_confirm_delete.html'

    def get_object(self, queryset=None):
        obj = super(CommDelete, self).get_object()
        if not obj.owner == self.request.user:
            raise Http404
        account = Account.objects.get(pk=obj.account.id)
        self.account = account
        return obj

    def get_success_url(self):
        return reverse(account_detail, args=(self.account.uuid))
