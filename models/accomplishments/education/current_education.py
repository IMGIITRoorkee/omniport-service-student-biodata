import swapper
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from student_biodata.models.abstract_classes.base_model import BaseModel


class AbstractCurrentEducation(BaseModel):
    """
    This model contains information about the current education of a student
    """

    semester = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(10)
        ]
    )

    cgpa = models.DecimalField(
        verbose_name='CGPA',
        max_digits=5,
        decimal_places=3,
        validators=[
            MinValueValidator(0.000),
            MaxValueValidator(10.000),
        ],
    )

    sgpa = models.DecimalField(
        verbose_name='SGPA',
        max_digits=5,
        decimal_places=3,
        validators=[
            MinValueValidator(0.000),
            MaxValueValidator(10.000),
        ],
    )

    class Meta:
        """
        Meta class for AbstractCurrentEducation
        """

        abstract = True
        unique_together = ('student', 'semester')

    def __str__(self):
        """
        Returns the string representation of the model
        :return: the string representation of the model
        """

        student = self.student
        semester = self.semester
        return f'{student}: {semester}'


class CurrentEducation(AbstractCurrentEducation):
    """
    This class implements AbstractCurrentEducation
    """

    class Meta:
        """
        Meta class for CurrentEducation
        """

        verbose_name_plural = 'current education'
        swappable = swapper.swappable_setting('student_biodata',
                                              'CurrentEducation')
