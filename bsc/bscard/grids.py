from django.core.urlresolvers import reverse_lazy
from jqgrid import JqGrid
from models import mision

class BrowserGrid(JqGrid):
    model = mision # could also be a queryset
    url = reverse_lazy('grid_handler')
    caption = 'Mision' # optional
    colmodel_overrides = {
        'id': { 'editable': False, 'width':10 },
    }
