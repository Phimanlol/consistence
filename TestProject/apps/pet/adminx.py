# -*- coding: UTF-8 -*-
import xadmin
from .models import Pet

class PetAdmin(object):
    list_display = ['name', 'age', 'user', 'type',
                    'adopted', 'size', 'add_time', 'photo'
                    ]
    search_field = ['age', 'adopted', 'size']
    list_editable = ['adopted', 'size', 'photo']
    list_filter = ['name', 'age', 'user', 'type',
                   'adopted', 'size', 'add_time'
                   ]


xadmin.site.register(Pet, PetAdmin)