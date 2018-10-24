import swapper
from django.db import models

from common_biodata.models.engagements.position import AbstractPosition
from student_biodata.constants.experience_types import EXPERIENCE_TYPES
from student_biodata.models.abstract_classes.base_model import BaseModel


class Experience(AbstractPosition, BaseModel):
    """
    This model contains information about the experience of a student
    """

    experience_type = models.CharField(
        max_length=3,
        choices=EXPERIENCE_TYPES,
    )

    class Meta:
        """
        Meta class for Experience
        """

        swappable = swapper.swappable_setting('student_biodata', 'Experience')

    def __str__(self):
        """
        Returns the string representation of the model
        :return: the string representation of the model
        """

        student = self.student
        string = super().__str__()
        return f'{student}: {string}'
