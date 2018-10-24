import swapper
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from common_biodata.models.accomplishments.education import AbstractEducation
from student_biodata.models.abstract_classes.base_model import BaseModel


class PreviousEducation(AbstractEducation, BaseModel):
    """
    This model contains information about the previous education of a student
    """

    cgpa = models.DecimalField(
        verbose_name='CGPA',
        max_digits=5,
        decimal_places=3,
        validators=[
            MinValueValidator(0.000),
            MaxValueValidator(10.000),
        ],
        blank=True,
        null=True,
    )

    percentage = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        validators=[
            MinValueValidator(0.00),
            MaxValueValidator(100.00),
        ],
        blank=True,
        null=True,
    )

    is_percentage = models.BooleanField(
        default=False,
    )

    class Meta:
        """
        Meta class for AbstractPreviousEducation
        """

        verbose_name_plural = 'previous education'
        swappable = swapper.swappable_setting('student_biodata',
                                              'PreviousEducation')

    def __str__(self):
        """
        Return the string representation of the model
        :return: the string representation of the model
        """

        student = self.student
        string = super().__str__()
        return f'{student} : {string}'
