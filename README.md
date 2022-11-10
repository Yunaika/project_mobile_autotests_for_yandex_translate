
# Пример организации мобильного автотестирования для приложения Яндекс Переводчик
> Яндекс Переводчик — это сервис автоматического перевода слов и выражений, текстов с фотографий и картинок, 
> сайтов и мобильных приложений.

## :open_book: Содержание:
- [Описание проекта](#heavy_check_mark-описание)
- [Кратко](#heavy_check_mark-кратко)
- [Технологии и инструменты](#gear-технологии-и-инструменты)
- [Что проверяем](#heavy_check_mark-реализованные-ui-проверки)
- Запуск тестов:
  - [Jenkins](#-запуск-тестов-из-jenkins)
  - [Локально](#computer-локальный-запуск)
- Отчеты:
  - [Allure](#bar_chart-отчеты-о-прохождении-тестов-доступны-в-allure)
  - [BrowserStack](#)
  - [Telegram](#-telegram)
  - [Email](#email-email)
- [Allure TestOps](#briefcase-проект-интегрирован-с-allure-testops)
- [Видео прогона теста](#movie_camera-пример-видео-тестового-прогона)


## :heavy_check_mark: Описание
В проекте представлен пример автоматизации UI-тестирования мобильного приложения с использованием Python + Pytest + Selene + Appium + Allure.
<p>При написании тестов применялись инструменты объектно-ориентированной парадигмы, а также использовался шаблон 
проектирования PageObjects.
<p>Реализован локальный запуск тестов через Android Studio, а также удаленный в BrowserStack.</p>
<p>Подключена система отчетности Allure Reports с вложениями (логи, скриншоты, видео, etc). Реализовано автоматическое
подтягивание allure.title из названия функций и их параметров, используя декораторы @step.

<p>По факту прохождения теста отправляется уведомление с результатами в Telegram и на электронную почту.
<p>Реализован запуск тестов как с использованием Android Studio, так и Browserstack.
<p>Осуществлена интеграция с Allure TestOps.

## :heavy_check_mark: Кратко
- [x] `Page Object` с шагами `Fluent of Invocations`
- [x] `Application Manager`
- [x] Self-documenting code
- [x] Кастомный локальный запуск с использованием `Android Studio` или `Browserstack`
- [x] Удаленный запуск с использованием `Jenkins` и `Browserstack`
- [x] `Allure Reports` с вложениями (логи, скриншоты, видео)
- [x] Интеграция с `Allure TestOps`
- [x] Отправка результатов тестирования по `email` и в `Telegram`

## :gear: Технологии и инструменты:

<div align="center">
  <img src="https://github.com/Yunaika/yunaika/blob/main/img/logos/python.webp" title="Python" alt="Python" width="40" height="40"/>&nbsp;
  <img src="https://github.com/Yunaika/yunaika/blob/main/img/logos/pytest.png" title="Pytest" alt="Pytest" width="45" height="45"/>&nbsp; 
  <img src="https://github.com/Yunaika/yunaika/blob/main/img/logos/selenium-original.svg" title="Selenium" alt="Selenium" width="40" height="40"/>&nbsp;  
  <img src="https://github.com/Yunaika/yunaika/blob/main/img/logos/selene.png" title="Selene" alt="Selene" width="50" height="50"/>&nbsp;
  <img src="https://github.com/Yunaika/yunaika/blob/main/img/logos/appium.png" title="Appium" alt="Selenoid" width="40" height="40"/>&nbsp;  
  <img src="https://github.com/Yunaika/yunaika/blob/main/img/logos/pycharm.png" title="PyCharm" alt="PyCharm" width="40" height="40"/>&nbsp;    
  <img src="https://github.com/Yunaika/yunaika/blob/main/img/logos/jenkins.png" title="Jenkins" alt="Jenkins" width="40" height="40"/>&nbsp;
  <img src="https://github.com/Yunaika/yunaika/blob/main/img/logos/android-studio.png" title="AndroidStudio" alt="Jenkins" width="40" height="40"/>&nbsp;
  <img src="https://github.com/Yunaika/yunaika/blob/main/img/logos/browserstack.png" title="BrowserStack" alt="Jenkins" width="40" height="40"/>&nbsp;
  <img src="https://github.com/Yunaika/yunaika/blob/main/img/logos/Allure.svg" title="Allure Report" alt="Allure Report" width="40" height="40"/>&nbsp;
  <img src="https://fs.getcourse.ru/fileservice/file/download/a/159627/sc/333/h/32108dd5b6c9c9c3cf4220fe6b2cc7fc.svg" title="Allure TestOps" alt="Allure TestOps" width="40" height="40"/>&nbsp;
  <img src="https://github.com/Yunaika/yunaika/blob/main/img/logos/telegram.png" title="Telegram" alt="Telegram" width="40" height="40"/>&nbsp;
</div>

## :heavy_check_mark: Реализованные UI-проверки

> - перевод текста с английского на русский;
> - переключение языков перевода по кнопке;
> - кнопка Translate site видна при вводе адреса сайта;
> - очистка заполненного поля ввода по клику на иконку крестика;
> - открытие текста перевода в полноэкранном поп-апе.

## <img width="4%" title="Jenkins" src="https://github.com/Yunaika/yunaika/blob/main/img/logos/jenkins.png"> Запуск тестов из [Jenkins](https://jenkins.autotests.cloud/job/juliamur_python_autotests_yatranslate_diplom/)

Для запуска тестов из Jenkins:
1. Нажмите кнопку "Собрать сейчас".
<p><img src="media/screenshots/jenkins1.jpg" alt="Jenkins"/></p>

## :computer: Локальный запуск 

Для локального запуска:
1. Склонируйте репозиторий
2. Установите Poetry `poetry install`
3. Откройте проект в PyCharm, установите интерпретатор
4. Запустите BrowserStack
   - Получите ваш username, access key и загрузите apk из папки resources для получения app id
6. Установите Android Studio и Appium
   - Запустите Appim Server
   - Запустите в Android Studio эмуляцию устройства
   - Введите в командной строке `adb devices` для проверки, что устройство доступно
7. Создайте `env` файлы по образцам в папке проекта:
    - `config.browserstack.env` с вашими данными
    - `config.local.env`
9. Запустите тесты в PyCharm или в командной строке: 
```bash
pytest . --alluredir allure-results/
```
10. Проверьте статус запуска в BrowserStack

### :heavy_plus_sign: Параметры сборки

> В файле `config.py` измените значение `EnvContext`:
> - `local` — локальный запуск в запущенном устройстве Android Studio
> - `browserstack` — запуск тестов в BrowserStack

## :bar_chart: Отчеты о прохождении тестов доступны в Allure

### <img width="3%" title="Allure" src="https://github.com/Yunaika/yunaika/blob/main/img/logos/Allure.svg"> Allure

> При локальном запуске введите в командной строке:
```bash
allure serve .\allure-results
```

#### Примеры отображения тестов

<p><img src="media/screenshots/allure_reports_1.jpg" alt="Allure"/></p>

<p><img src="media/screenshots/allure_reports_2.jpg" alt="Allure"/></p>

### <img width="2.5%" title="BrowserStack" src="https://github.com/Yunaika/yunaika/blob/main/img/logos/browserstack.png"> BrowserStack

<img src="media/screenshots/browserstack.jpg" alt="BrowserStack"/>

### <img width="2.5%" title="Telegram" src="https://github.com/Yunaika/yunaika/blob/main/img/logos/telegram.png"> Telegram

Настроена отправка отчета в Telegram

<img src="media/screenshots/telegram.jpg" alt="Telegram"/>

### Email

Настроена отправка отчета на электронную почту

<img src="media/screenshots/email.jpg" alt="Email"/>

## :briefcase: Проект интегрирован с Allure TestOps 

#### Автоматически собраны тест-кейсы

<img src="media/screenshots/allure_testops1.jpg" alt="Allure TestOps"/>

## :movie_camera: Пример видео тестового прогона

В отчетах Allure для каждого UI-теста прикреплен не только скриншот, но и видео прохождения теста

<p align="center">
  <img title="Video" src="media/screencasts/test_open_fullscreen_translated_text.gif">
</p>

