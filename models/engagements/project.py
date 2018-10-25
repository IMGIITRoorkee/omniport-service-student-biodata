import swapper
from django.db import models

from common_biodata.models.engagements.project import AbstractProject
from kernel.utils.upload_to import UploadTo
from student_biodata.models.abstract_classes.base_model import BaseModel


class Project(AbstractProject, BaseModel):
    """
    This abstract model holds the information about a project of a student
    """

    image = models.ImageField(
        upload_to=UploadTo('student_biodata', 'projects'),
        blank=True,
        null=True,
    )

    class Meta:
        """
        Meta class for Project
        """

        swappable = swapper.swappable_setting('student_biodata', 'Project')

    def __str__(self):
        """
        Returns the string representation of the model
        :return: the string representation of the model
        """

        student = self.student
        string = super().__str__()
        return f'{student}: {string}'
