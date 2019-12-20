import swapper
from django.contrib import admin

from omniport.admin.site import omnipotence

models = [
    'CurrentEducation',
    'PreviousEducation',
    'Achievement',
    'Experience',
    'Position',
    'Project',
    'Interest',
    'Skill',
    'Profile',
    'Book',
    'Paper',
    'Referee',
]

class BaseAdmin(admin.ModelAdmin):
    raw_id_fields = ('student',)

for model in models:
    omnipotence.register(
        swapper.load_model(
            'student_biodata', model
        ), BaseAdmin
    )
