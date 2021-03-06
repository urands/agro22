<p align="center">
    <h1 align="center">Приложение</h1>
    </p>
<p>Умная система распознавания пожара, позволяющая анализировать информацию с видеокамер и обнаруживать возгорания в реальном времени. Система позволяет оповещать  пользователей о возгораниях и прогнозировать распространение огня  на основе анализа видеоизображений и погоды.</p>

<h4>Реализованная функциональность</h4>
<ul>
    <li>Обнаружение возгорания по видео и изображению;</li>
    <li>Реализован веб сервис для работы с нейронной сетью;</li>
    <li>Реализовано оповещение через телеграм;</li>
</ul> 
<h4>Особенность проекта в следующем:</h4>
<ul>
 <li>Дообучение модели;</li>
 <li>Обработка и отображение результата в реальном времени;</li>
 <li>Оповещение через телеграм;</li>  
 <li>Отображение текущей ситуации на карте;</li>
 </ul>
<h4>Основной стек технологий:</h4>
<ul>
    <li>Python (Flask, Pytorch, Aiogram)</li>
    <li>C++, CUDA: (Yolov4, Darknet)</li>
	<li>HTML, CSS, JavaScript</li>
	<li>Nginx, Postrgee.</li>
  
 </ul>
<h4>Демо</h4>
<p>Демо сервиса доступно по адресу: http://31.148.136.80/ </p>





СРЕДА ЗАПУСКА
------------
1) развертывание сервиса производится на windows 10;
2) требуется установленный Python 3.9, MS Visual Studio, CMake ;
3) требуется установленная NVidia CUDA SDK Tookit 11.5, CuDNN 8.5;
4) требуется установленный пакет pipenv;


УСТАНОВКА
------------
### Установка пакета name

Выполните 
~~~
git clone https://github.com/Sinclear/default_readme
cd firedetector
pipenv install 
cd ../fireservice
pipenv install 
...
~~~
### Сборка библиотек

Сборка библиотек осуществляется по инструкции

https://github.com/AlexeyAB/darknet/tree/4b35dbbf9a0608a928ea92f58fc83408464f86ce#how-to-compile-on-windows-using-cmake

### Запуск

Два сервиса
1. cd firedetector && pipenv run python app.py 
1. cd fireservice && pipenv run python app.py


РАЗРАБОТЧИКИ

+ Беллавин Юрий fullstack https://t.me/urands 
+ Новикова Лиза фронтэнд https://t.me/livergara 
+ Элина Барна дизайн https://t.me/elyaaabv

