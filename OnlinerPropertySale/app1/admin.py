from django.contrib import admin

from .models import Admin
from .models import State
from .models import City
from .models import Locality
from .models import SalesRegistration
from .models import UserRegistration
from .models import Transaction
from .models import Suggestions

admin.site.register(Admin)
admin.site.register(State)
admin.site.register(City)
admin.site.register(Locality)
admin.site.register(SalesRegistration)
admin.site.register(UserRegistration)
admin.site.register(Transaction)
admin.site.register(Suggestions)
