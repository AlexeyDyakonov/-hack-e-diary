import random

from datacenter.models import (Chastisement, Commendation, Lesson, Mark,
                               Schoolkid)


def fix_marks(schoolkid_name):
    try:
        child = Schoolkid.objects.get(full_name__contains=schoolkid_name)
        bad_marks = Mark.objects.filter(schoolkid_name=child, points__lte=3).\
            update(points=5)
        bad_marks.save()
    except Schoolkid.DoesNotExist:
        print("Такого имени нет")
    except Schoolkid.MultipleObjectsReturned:
        print("Такого имени нет")


def remove_chastisements(schoolkid_name):
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=schoolkid_name)
        remarks = Chastisement.objects.\
            filter(schoolkid=schoolkid).delete()
        remarks.save()
    except Schoolkid.DoesNotExist:
        print("Такого имени нет")
    except Schoolkid.MultipleObjectsReturned:
        print("Такого имени нет")


def create_commendation(schoolkid_name, lesson, year_of_study, group_letter):

    try:
        lessons = Lesson.objects.filter(
            year_of_study=year_of_study,
            group_letter=group_letter,
            subject__title__contains=lesson).order_by('-subject').first()
        child = Schoolkid.objects.get(full_name__contains=schoolkid_name)
        commendation_list = ['Молодец!',
                             'Отлично!',
                             'Хорошо!',
                             'Гораздо лучше, чем я ожидал!',
                             'Ты меня приятно удивил!',
                             'Ты, как всегда, точен!',
                             'Талантливо!',
                             'Потрясающе!',
                             'Замечательно!',
                             'Ты сегодня прыгнул выше головы!!',
                             'Здорово!',
                             'Я тобой горжусь!',
                             'Ты растешь над собой!']
        commendation_text = random.choice(commendation_list)
        Commendation.objects.create(text=commendation_text,
                                    created=lessons.date,
                                    schoolkid=child,
                                    subject=lessons.subject,
                                    teacher=lessons.teacher)
    except Schoolkid.DoesNotExist:
        print("Такого имени нет")
    except Schoolkid.MultipleObjectsReturned:
        print("Такого имени нет")
