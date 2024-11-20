from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Student, JSS1, JSS2, JSS3, SS1, SS2, SS3, Science, Commercial, Art

@receiver(post_save, sender=Student)
def create_student_records(sender, instance, created, **kwargs):
    if created:
        if instance.student_class == "JSS1":
            JSS1.objects.create(student=instance)
        elif instance.student_class == "JSS2":
            JSS2.objects.create(student=instance)
        elif instance.student_class == "JSS3":
            JSS3.objects.create(student=instance)
        elif instance.student_class == "SS1":
            SS1.objects.create(student=instance)
        elif instance.student_class == "SS2":
            SS2.objects.create(student=instance)
        elif instance.student_class == "SS3":
            SS3.objects.create(student=instance)

        if instance.student_class in ["SS1", "SS2", "SS3"]:
            if instance.department == "Science":
                Science.objects.create(student=instance)
            elif instance.department == "Commercial":
                Commercial.objects.create(student=instance)
            elif instance.department == "Art":
                Art.objects.create(student=instance)
