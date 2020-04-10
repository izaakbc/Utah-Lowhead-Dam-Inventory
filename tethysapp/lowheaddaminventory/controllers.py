from django.shortcuts import render
from tethys_sdk.permissions import login_required
from tethys_sdk.gizmos import Button
from django.shortcuts import reverse
from tethys_sdk.gizmos import MapView, Button

@login_required()
def home(request):
    """
    Controller for the app home page.
    """

    addlowheaddam_button = Button(
        display_text = 'Add Lowhead Dam',
        name = 'addlowheaddam_button',
        icon='glyphicon glyphicon-plus',
        style='success',
        href=reverse('lowheaddaminventory:addlowheaddam')
    )

    context = {
        'addlowheaddam_button': addlowheaddam_button
    }
    return render(request, 'lowheaddaminventory/home.html', context)




@login_required()
def instructions(request):
    """
    Controller for the Instructions Page
    """

    context = {}
    return render(request, 'lowheaddaminventory/instructions.html', context)

@login_required()
def addlowheaddam(request):
    """
    Controller for the Add Lowhead dam Page
    """

    context = {}
    return render(request, 'lowheaddaminventory/addlowheaddam.html', context)

@login_required()
def existingdams(request):
    """
    Controller for the Existing Lowhead Dam Page
    """

    context = {}
    return render(request, 'lowheaddaminventory/existingdams.html', context)





