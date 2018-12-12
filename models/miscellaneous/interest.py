import swapper
from django.db import models

from common_biodata.models import AbstractInterest
from student_biodata.models.abstract_classes.base_model import BaseModel


class Interest(AbstractInterest, BaseModel):
    """
    This model contains the interests of the student
    """

    class Meta:
        """
        Meta class for Interest
        """

        swappable = swapper.swappable_setting('student_biodata', 'Interest')

    def __str__(self):
        """
        Return the string representation of the model
        :return: the string representation of the model
        """

        student = self.student
        string = super().__str__()
        return f'{student}: {string}'
