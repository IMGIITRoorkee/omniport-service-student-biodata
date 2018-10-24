import swapper
from django.db import models

from kernel.models.root import Model


class AbstractAchievement(Model):
    """
    This model contains information about the achievements of a student
    """

    student = models.OneToOneField(
        to=swapper.get_model_name('kernel', 'Student'),
        on_delete=models.CASCADE,
    )

    achievements = models.TextField()

    class Meta:
        """
        Meta class for AbstractAchievement
        """

        abstract = True

    def __str__(self):
        """
        Returns the string representation of the model
        :return: the string representation of the model
        """

        student = self.student
        achievements = self.achievements
        return f'{student}: {achievements}'


class Achievement(AbstractAchievement):
    """
    This class implements AbstractAchievement
    """

    class Meta:
        """
        Meta class for Achievement
        """

        swappable = swapper.swappable_setting('student_biodata', 'Achievement')
