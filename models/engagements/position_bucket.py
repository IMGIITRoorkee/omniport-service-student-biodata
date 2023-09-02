import swapper

from django.db import models

from formula_one.models.base import Model


class PositionBucket(Model):
    """
    This model contains information about a different position buckets for a position held by a student
    """

    position = models.ForeignKey(
        to=swapper.get_model_name('student_biodata', 'Position'),
        on_delete=models.CASCADE,
        related_name='position_buckets'
    )

    title = models.CharField(
        max_length=127
    )

    description = models.TextField(
        blank=True
    )

    priority = models.IntegerField(
        default=0,
    )

    visibility = models.BooleanField(
        default=True,
    )

    class Meta:
        """
        Meta class for PositionBucket
        """

        swappable = swapper.swappable_setting('student_biodata', 'PositionBucket')

    def __str__(self):
        """
        Returns the string representation of the model
        :return: the string representation of the model
        """

        student = self.position.student
        title = self.title
        position = self.position.position
        organization = self.position.organisation
        return f'{student}: {title} in {position} at {organization}'
    