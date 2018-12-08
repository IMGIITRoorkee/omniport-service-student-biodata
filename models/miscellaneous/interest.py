import swapper
from django.db import models

from common_biodata.models import AbstractInterest


class Interest(AbstractInterest):
    """
    This model contains the interests of the student
    """

    student = models.ForeignKey(
        to=swapper.get_model_name('kernel', 'Student'),
        on_delete=models.CASCADE,
    )

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
