import swapper
from django.db import models

from formula_one.models.base import Model
from student_biodata.models.abstract_classes.base_model import BaseModel


class AbstractSkill(BaseModel):
    """
    This abstract model holds the information about the Skills of a
    student
    """

    computer_languages = models.TextField(
        blank=True,
    )

    software_packages = models.TextField(
        blank=True,
    )

    additional_courses = models.TextField(
        blank=True,
    )

    minor_courses = models.TextField(
        blank=True,
    )

    languages = models.TextField(
        blank=True,
    )

    class Meta:
        """
        Meta class for AbstractSkill
        """

        abstract = True

    def __str__(self):
        """
        Returns the string representation of the model
        :return: the string representation of the model
        """

        student = self.student
        return f'{student}'


class Skill(AbstractSkill):
    """
    This class implements AbstractSkill
    """

    class Meta:
        """
        Meta class for Skill
        """

        swappable = swapper.swappable_setting('student_biodata', 'Skill')
