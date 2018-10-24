from django.db import models

import swapper

from common_biodata.models.profile.profile import AbstractProfile
from student_biodata.models.abstract_classes.base_model import BaseModel


class Profile(AbstractProfile, BaseModel):
    """
    This model constains informatation about the home page of the student
    """

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
