import swapper
from django.db import models
from student_biodata.models.abstract_classes.base_model import BaseModel


class AbstractAchievement(BaseModel):
    """
    This model contains information about the achievements of a student
    """

    student = models.ForeignKey(
        to=swapper.get_model_name('kernel', 'Student'),
        on_delete=models.CASCADE,
    )

    achievement = models.TextField()

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
        achievement = self.achievement
        return f'{student}: {achievement}'


class Achievement(AbstractAchievement):
    """
    This class implements AbstractAchievement
    """

    class Meta:
        """
        Meta class for Achievement
        """

        swappable = swapper.swappable_setting('student_biodata', 'Achievement')
