from django.contrib import admin

from topics.models import Lecture, Topic

class LectureAdmin(admin.ModelAdmin):
    pass

class TopicAdmin(admin.ModelAdmin):
    pass

admin.site.register(Lecture, LectureAdmin)
admin.site.register(Topic, TopicAdmin)