import swapper

from common_biodata.models import AbstractPosition
from student_biodata.models.abstract_classes.base_model import BaseModel


class Position(AbstractPosition, BaseModel):
    """
    This model contains information about a position held by a student
    """

    class Meta:
        """
        Meta class for Position
        """

        swappable = swapper.swappable_setting('student_biodata', 'Position')

    def __str__(self):
        """
        Returns the string representation of the model
        :return: the string representation of the model
        """

        student = self.student
        string = super().__str__()
        return f'{student}: {string}'
