
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('account.urls')),
    path('students/',include('students.urls')),
    path('note/',include('note.urls')),
    path('grades/',include('grades.urls')),
    path('parent/',include('parents.urls')),
    path('teachers/',include('teachers.urls')),
    path('manager/',include('managers.urls')),
   
 ]

##############################################################################
#        to upload photos into img folder or another folder that you chose                                                                    #
#                                                                            #
##############################################################################
if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
     
     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)