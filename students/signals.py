# _*_ coding: utf-8 _*_
import logging
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import Student, Group, Exam, Teacher, Resoult


# Students logging
@receiver(post_save, sender=Student)
def log_student_updated_added_event(sender, **kwargs):
    '''Writes information about newly added or updated student log file'''

    logger = logging.getLogger(__name__)

    student = kwargs['instance']
    if kwargs['created']:
        logger.info("Student added: %s %s (ID: %d)", student.first_name, student.last_name, student.id)
    else:
        logger.info("Student updated: %s %s (ID: %d)", student.first_name, student.last_name, student.id)


@receiver(post_delete, sender=Student)
def log_student_deleted_event(sender, **kwargs):
    '''Writes information about newly deleted student log file'''
    logger = logging.getLogger(__name__)

    student = kwargs['instance']
    logger.info("Student deleted: %s %s (ID: %d)", student.first_name, student.last_name, student.id)


# Groups logging
@receiver(post_save, sender=Group)
def log_group_updated_added_event(sender, **kwargs):
    '''Writes information about newly added or updated group log file'''

    logger = logging.getLogger(__name__)

    group = kwargs['instance']
    if kwargs['created']:
        logger.info("Group added: %s (ID: %d)", group.title, group.id)
    else:
        logger.info("Group updated: %s (ID: %d)", group.title, group.id)
    # print sender



@receiver(post_delete, sender=Group)
def log_group_deleted_event(sender, **kwargs):
    '''Writes information about newly deleted group log file'''

    logger = logging.getLogger(__name__)
    group = kwargs['instance']
    logger.info("Group deleted: %s (ID: %d)", group.title, group.id)



# Exams logging
@receiver(post_save, sender=Exam)
def log_exam_updated_added_event(sender, **kwargs):
    '''Writes information about newly added or updated group log file'''

    logger = logging.getLogger(__name__)

    exam = kwargs['instance']
    if kwargs['created']:
        logger.info("Exam added: %s %s (ID: %d)", exam.title, exam.date, exam.id)
    else:
        logger.info("Group updated: %s %s (ID: %d)", exam.title, exam.date, exam.id)
    # print sender



@receiver(post_delete, sender=Exam)
def log_exam_deleted_event(sender, **kwargs):
    '''Writes information about newly deleted group log file'''

    logger = logging.getLogger(__name__)
    exam = kwargs['instance']
    logger.info("Group deleted: %s %s (ID: %d)", exam.title, exam.date, exam.id)


# Resoult logging
@receiver(post_save, sender=Resoult)
def log_resoult_updated_added_event(sender, **kwargs):
    '''Writes information about newly added or updated group log file'''

    logger = logging.getLogger(__name__)

    resoult = kwargs['instance']
    if kwargs['created']:
        logger.info("Exam_resoult added: %s %s (ID: %d)", resoult.title, resoult.exam, resoult.id)
    else:
        logger.info("Exam_resoult updated: %s %s (ID: %d)", resoult.title, resoult.exam, resoult.id)
    # print sender



@receiver(post_delete, sender=Resoult)
def log_resoult_deleted_event(sender, **kwargs):
    '''Writes information about newly deleted group log file'''

    logger = logging.getLogger(__name__)
    resoult = kwargs['instance']
    logger.info("Exam_resoult deleted: %s %s (ID: %d)", resoult.title, resoult.exam, resoult.id)


# Teacher logging
@receiver(post_save, sender=Teacher)
def log_teacher_updated_added_event(sender, **kwargs):
    '''Writes information about newly added or updated student log file'''

    logger = logging.getLogger(__name__)

    teacher = kwargs['instance']
    if kwargs['created']:
        logger.info("Teacher added: %s %s (ID: %d)", teacher.first_name, teacher.last_name, teacher.id)
    else:
        logger.info("Teacher updated: %s %s (ID: %d)", teacher.first_name, teacher.last_name, teacher.id)


@receiver(post_delete, sender=Student)
def log_student_deleted_event(sender, **kwargs):
    '''Writes information about newly deleted student log file'''
    logger = logging.getLogger(__name__)

    teacher = kwargs['instance']
    logger.info("Teacher updated: %s %s (ID: %d)", teacher.first_name, teacher.last_name, teacher.id)