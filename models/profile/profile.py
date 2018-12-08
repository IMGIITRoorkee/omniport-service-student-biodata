import swapper
from django.db import models

from kernel.utils.upload_to import UploadTo

from common_biodata.models.profile.profile import AbstractProfile


class Profile(AbstractProfile):
    """
    This model contains informatation about the home page of the student
    """
    student = models.OneToOneField(
        to=swapper.get_model_name('kernel', 'Student'),
        on_delete=models.CASCADE,
    )

    custom_website = models.BooleanField(
        default=False,
    )

    resume = models.FileField(
        blank=True,
        null=True,
        upload_to=UploadTo('student_biodata', 'resume')
    )
    class Meta:
        """
        Meta class for AbstractProfile
        """

        swappable = swapper.swappable_setting('student_biodata', 'Profile')

    def __str__(self):
        """
        Return the string representation of the model
        :return: the string representation of the model
        """

        student = self.student
        string = super().__str__()
        return f'{student} : {string}'
