import swapper
from django.contrib.contenttypes import fields as contenttypes_fields

from django.db import models

from kernel.models.root import Model


class AbstractReference(Model):
    """
    This model contains information about the reference of a student
    """

    student = models.ForeignKey(
        to=swapper.get_model_name('kernel', 'Student'),
        on_delete=models.CASCADE,
    )
    
    referee = models.CharField(
        max_length=255,
    )

    designation = models.CharField(
        max_length=3,
    )

    institute = models.CharField(
        max_length=255,
    )

    body = models.TextField(
        blank=True,
        help_text="This field contains body of the reference letter (OPTIONAL)"
    )

    contact_information = contenttypes_fields.GenericRelation(
        to='kernel.ContactInformation',
        related_query_name='reference',
        content_type_field='entity_content_type',
        object_id_field='entity_object_id',
    )

    class Meta:
        """
        Meta class for AbstractReference
        """
        abstract = True
        

class Reference(AbstractReference):
    """
    This class implements Reference
    """

    class Meta:
        """
        Meta class for Reference
        """

        swappable = swapper.swappable_setting('student_biodata', 'Reference')

    def __str__(self):
        """
        Return the string representation of the model
        :return: the string representation of the model
        """
        student_name = self.student.person.full_name
        referee = self.referee
        return f'{student_name} referenced {referee}'