import swapper

from common_biodata.models import AbstractBook
from student_biodata.models.abstract_classes.base_model import BaseModel


class Book(AbstractBook, BaseModel):
    """
    This model stores information about a book by a student
    """

    class Meta:
        """
        Meta class for Book
        """

        swappable = swapper.swappable_setting('student_biodata', 'Book')

    def __str__(self):
        """
        Return a string representation of the model
        :return: a string representation of the model
        """

        student = self.student
        string = super().__str__()

        return f'{student} : {string}'
