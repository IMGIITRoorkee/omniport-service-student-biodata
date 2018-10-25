import swapper

from kernel.admin.site import omnipotence

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
]

for model in models:
    omnipotence.register(
        swapper.load_model(
            'student_biodata', model
        )
    )