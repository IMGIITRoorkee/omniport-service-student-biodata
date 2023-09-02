import swapper

from omniport.admin.site import omnipotence

models = [
    'CurrentEducation',
    'PreviousEducation',
    'Achievement',
    'Experience',
    'Position',
    'PositionBucket',
    'Project',
    'Interest',
    'Skill',
    'Profile',
    'Book',
    'Paper',
    'Referee',
]

for model in models:
    omnipotence.register(
        swapper.load_model(
            'student_biodata', model
        )
    )
