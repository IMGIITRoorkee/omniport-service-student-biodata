import swapper
from django.db import models

from common_biodata.models import AbstractPaper
from formula_one.utils.upload_to import UploadTo
from student_biodata.models.abstract_classes.base_model import BaseModel


class Paper(AbstractPaper, BaseModel):
    """
    This model stores information about a paper by a student
    """

    paper = models.FileField(
        upload_to=UploadTo('student_biodata', 'papers'),
        blank=True,
        null=True,
    )

    class Meta:
        """
        Meta class for Paper
        """

        swappable = swapper.swappable_setting('student_biodata', 'Paper')

    def __str__(self):
        """
        Return a string representation of the model
        :return: a string representation of the model
        """

        student = self.student
        string = super().__str__()

        return f'{student} : {string}'
