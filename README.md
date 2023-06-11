# Помощь ученикам в учебе

Сайт электронного дневника уже запущен и работает. Для подробного ознакомления с сайтом электронного дневника перейдите по [ссылке на репозиторий Github](https://github.com/devmanorg/e-diary). 
Но не все ученики довольны своей успеваемостью, поэтому был создан этот скрипт. 
Он позволяет исправлять плохие оценки(2,3) на отличные(5), также удаляет плохие отзывы об ученике и добавляет положительные рекомендации, что позволяет упросить жизнь учеников в это нелегкое для них время. 


## Запуск

1. Скачайте файл scripts.py из данного репозитория и поместите его в папку, где находится файл manage.py для сайта электронного школьного дневника;

2. Зайдите в Shell. Для этого откройте командную строку и зайдите в директорию, в которой у вас находится файл manage.py и scripts.py. 
Далее напишите в командной строке: `python manage.py shell`. 
В случае успешного выполнения на экране появится надпись `(InteractiveConsole)`. 
Более подробно эта процедура прописана в [документации](https://www.csestack.org/open-python-shell-django/);

3. Необходимо импортировать функции из файла scripts.py. 
Для этого в Shell запишите `import scripts`, а также для более удобного обращения к функциям допишите `from scripts import fix_marks, create_commendation, remove_chastisements`. 
Более подробно эта процедура прописана по [ссылке](https://fooobar.com/questions/37137/call-a-function-from-another-file-in-python)

4. Теперь осталось запустить функции, а остальное скрипт сделает за вас. 
Учтите, что очень важно правильно записать фамилию и имя, иначе скрипт не сработает! 
Следуйте следующему алгоритму:
    * запустите функцию, которая изменяет оценки. Для этого в Shell запишите `fix_marks(schoolkid_name)`, где schoolkid name - ваше имя. 
    
        Пример записи: `fix_marks('Фролов Иван')`. 
          
    * запустите функцию, которая удаляет замечания от учителей. Для этого в Shell запишите `remove_chastisements(schoolkid_name)`, где schoolkid name - ваше имя. 
    
        Пример записи: `remove_chastisements('Фролов Иван')`;
    * запустите функцию, которая добавляет рекомендации от учителей. 
    Для этого в Shell запишите `create_commendation(schoolkid_name, lesson, year_of_study, group_letter)`, 
    где schoolkid name - ваше имя, а lesson - название предмета, по которому вы хотите добавить рекоммендацию, 
    year_of_study - ваш год обучения, group_letter - литера вашего класса. 
        
        Пример записи: `create_commendation('Фролов Иван', 'Математика', 6, 'А')`.
5. Наслаждайтесь отличными оценками и положительными рекомендациями.


    

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
