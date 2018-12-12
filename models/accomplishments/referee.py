import swapper

from django.db import models

from kernel.models.root import Model

from student_biodata.models.abstract_classes.base_model import BaseModel

class AbstractReferee(BaseModel):
    """
    This model contains information about the referee of a student
    """ 

    referee = models.CharField(
        max_length=255,
    )

    designation = models.CharField(
        max_length=127,
    )

    institute = models.CharField(
        max_length=255,
    )

    phone_number = models.CharField(
        max_length=15,
        blank=True
    )

    email = models.EmailField(
        max_length=255,
    )

    class Meta:
        """
        Meta class for AbstractReferee
        """
        abstract = True
        

class Referee(AbstractReferee):
    """
    This class implements Referee
    """

    class Meta:
        """
        Meta class for Referee
        """

        swappable = swapper.swappable_setting('student_biodata', 'Referee')

    def __str__(self):
        """
        Return the string representation of the model
        :return: the string representation of the model
        """
        student_name = self.student.person.full_name
        referee = self.referee
        return f'{student_name} referenced {referee}'
