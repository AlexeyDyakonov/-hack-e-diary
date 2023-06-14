import random

from datacenter.models import (Chastisement, Commendation, Lesson, Mark,
                               Schoolkid)


COMMENDATIONS = ['Молодец!',
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


def get_schoolkid(schoolkid_name):
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=schoolkid_name)
        return schoolkid
    except Schoolkid.DoesNotExist:
        print("Такого имени нет")
    except Schoolkid.MultipleObjectsReturned:
        print("Найдено несколько совпадений")
        

def fix_marks(schoolkid_name):
    schoolkid = get_schoolkid(schoolkid_name)
    Mark.objects.filter(schoolkid=schoolkid, points__lte=3).update(points=5)


def remove_chastisements(schoolkid_name):
    schoolkid = get_schoolkid(schoolkid_name)
    Chastisement.objects.filter(schoolkid=schoolkid).delete()


def create_commendation(schoolkid_name, lesson, year_of_study, group_letter):
    try:
        schoolkid = get_schoolkid(schoolkid_name)
        lesson = Lesson.objects.filter(
            year_of_study=year_of_study,
            group_letter=group_letter,
            subject__title__contains=lesson).order_by('-date').first()
        commendation_text = random.choice(COMMENDATIONS)
        Commendation.objects.create(text=commendation_text,
                                    created=lessons.date,
                                    schoolkid=schoolkid,
                                    subject=lessons.subject,
                                    teacher=lessons.teacher)
    except AttributeError:
        print("Неверно введен предмет или год обучения или литер класса")
        
