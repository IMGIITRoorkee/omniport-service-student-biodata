import swapper

from kernel.admin.site import omnipotence

CurrentEducation = swapper.load_model('student_biodata','CurrentEducation')
PreviousEducation = swapper.load_model('student_biodata','PreviousEducation')
Achievement = swapper.load_model('student_biodata','Achievement')
Experience = swapper.load_model('student_biodata','Experience')
Position = swapper.load_model('student_biodata','Position')
Project = swapper.load_model('student_biodata','Project')
Interest = swapper.load_model('student_biodata','Interest')
Skill = swapper.load_model('student_biodata','Skill')
Profile = swapper.load_model('student_biodata','Profile')
Book = swapper.load_model('student_biodata','Book')
Paper = swapper.load_model('student_biodata','Paper')


omnipotence.register(CurrentEducation)
omnipotence.register(PreviousEducation)
omnipotence.register(Achievement)
omnipotence.register(Experience)
omnipotence.register(Position)
omnipotence.register(Project)
omnipotence.register(Interest)
omnipotence.register(Skill)
omnipotence.register(Profile)
omnipotence.register(Book)
omnipotence.register(Paper)