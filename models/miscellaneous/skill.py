import swapper
from django.db import models

from kernel.models.root import Model


class AbstractSkill(Model):
    """
    This abstract model holds the information about the Skills of a
    student
    """

    student = models.OneToOneField(
        to=swapper.get_model_name('kernel', 'Student'),
        on_delete=models.CASCADE,
    )

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

        swappable = swapper.swappable_setting('biodata', 'Skill')
