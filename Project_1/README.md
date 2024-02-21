<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://raw.githubusercontent.com/AndreyRysistov/DatasetsForPandas/main/hh%20label.jpg">
    <img src="https://raw.githubusercontent.com/AndreyRysistov/DatasetsForPandas/main/hh%20label.jpg">
  </a>

  <h3 align="center">Проект 1: Анализ резюме из HeadHunter</h3>

  <p align="center">
    Решение части настоящей бизнес-задачи и проба себя в роли аналитика в компании HeadHunter
    <br />
    <a href="https://ru.wikipedia.org/wiki/HeadHunter"><strong>О компании Head Hunter »</strong></a>
    <br />
    <br />
    
</div>


<details>
  <summary>СОДЕРЖАНИЕ</summary>
  <ol>
    <li>
      <a href="#о-проекте">О проекте</a>
      <ul>
        <li><a href="#исследование-структуры-данных">Исследование структуры данных</a></li>
        <li><a href="#преобразование-данных">Преобразование данных</a></li>
        <li><a href="#исследование-зависимостей-в-данных">Исследование зависимостей в данных</a></li>
        <li><a href="#очистка-данных">Очистка данных</a></li>
      </ul>
    </li>
    <li>
      <a href="#Требования-для-запуска-проекта">Требования для запуска проекта</a>
      <ul>
        <li><a href="#prerequisites">Программы и утилиты</a></li>
        <li><a href="#built-with">Используемые в проекте библиотеки</a></li>
      </ul>
    </li>
    <li><a href="#roadmap">Дорожная карта</a></li>
    <li><a href="#contributing">Помочь проекту</a></li>
    <li><a href="#contact">Контакты</a></li>
    <li><a href="#acknowledgments">Благодарности</a></li>
  </ol>
</details>



<!-- О проекте -->
## О проекте

Настало время попробовать свои силы в реальном Data Science-проекте, который станет новым этапом сбора портфолио на GitHub. В нашем распоряжении оказалась база резюме, выгруженная с сайта поиска вакансий hh.ru.
Файл с исходными данными вы можете скачать здесь: https://drive.google.com/file/d/1Kb78mAWYKcYlellTGhIjPI-bCcKbGuTn/view?usp=sharing

Проблематика: часть соискателей не указывает желаемую заработную плату, когда составляет своё резюме.
Компания HeadHunter хочет построить модель, которая бы автоматически определяла примерный уровень заработной платы, подходящей пользователю, исходя из информации, которую он указал о себе. Но прежде чем построить модель, данные необходимо преобразовать, исследовать и очистить.

### Исследование структуры данных</a>

Начинаем со знакомства с данными и исследования их структуры. Нам важно понять, как устроены признаки в данных и какие типы они имеют, чтобы произвести дальнейшие преобразования.

<p align="right">(<a href="#readme-top">Наверх</a>)</p>

### Преобразование данных

Наши данные очень «сырые»: признаки представлены в неудобном для анализа и очистки формате. Это не позволяет нам визуально оценить зависимости в данных. Более того, мы не можем в таком виде заполнить пропущенные значения числовыми константами или найти выбросы. В данном разделе мы старались выполнять обработку с помощью функций-преобразований (lambda-функций), которые принимают аргументом элемент столбца и возвращают его преобразованную версию. Данные функции применяются к признакам с помощью метода apply().

<p align="right">(<a href="#readme-top">Наверх</a>)</p>

### Исследование зависимостей в данных

Теперь у нас есть всё необходимое, чтобы провести первичный анализ зависимостей в наших данных о резюме. Такой анализ часто называют разведывательным анализом (EDA) и он предназначен для выявления связей между признаками, выявления закономерностей, определения распределений признаков, поиска аномалий и других дефектов данных.

<p align="right">(<a href="#readme-top">Наверх</a>)</p>

### Очистка данных

Когда мы проводили визуальный анализ, мы нашли несколько несостыковок в данных: пропуски, гигантские размеры желаемых заработных плат, резюме людей слишком «преклонного» возраста, опыт работы, превышающий возраст. Всё это говорит о том, что данные подлежат очистке.

<p align="right">(<a href="#readme-top">Наверх</a>)</p>



<!-- Требования для запуска проекта -->
## Требования для запуска проекта

Для решения использовался только пройденный материал: переменные, основные структуры данных (списки, словари, множества), циклы, функции, библиотеки numpy, pandas, matplotlib, seaborn, plotly.

### Код и IDE

* [![Jupyter][jupyter.org]][jupyter-url]
* [![Python][python.org]][python-url]

### Ииспользуемые библиотеки python

* [![Pandas][pandas.org]][pd-url]
* [![Numpy][numpy.org]][numpy-url]
* [![Matplotlib][matplotlib.org]][matplotlib-url]
* [![Seaborn][seaborn.org]][seaborn-url]
* [![Plotly][plotly.com]][plotly-url]

<p align="right">(<a href="#readme-top">Наверх</a>)</p>



<!-- Дорожная карта -->
## Дорожная карта

- [x] Выполнить задания в юпитере
- [x] Ответить на задания на учебной платформе
- [ ] Закоммитить финальную версию и отправить на проверку
- [ ] Поддержка других языков
    - [ ] English

<p align="right">(<a href="#readme-top">Наверх</a>)</p>



<!-- Примечание -->
## Примечание

Папка с графиками в формате HTML называется "Graphs_4_Git".

<p align="right">(<a href="#readme-top">Наверх</a>)</p>



<!-- Контакты -->
## Контакты

Ангелина Калинина - [@vesnalinka](https://twitter.com/vesnalinka) - vesnalinka@gmail.com

Project Link: [https://github.com/your_username/repo_name](https://github.com/your_username/repo_name)

<p align="right">(<a href="#readme-top">Наверх</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

Use this space to list resources you find helpful and would like to give credit to. I've included a few of my favorites to kick things off!

* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Malven's Flexbox Cheatsheet](https://flexbox.malven.co/)
* [Malven's Grid Cheatsheet](https://grid.malven.co/)
* [Img Shields](https://shields.io)
* [GitHub Pages](https://pages.github.com)
* [Font Awesome](https://fontawesome.com)
* [React Icons](https://react-icons.github.io/react-icons/search)
* [Awesome Readme](https://github.com/matiassingers/awesome-readme)

<p align="right">(<a href="#readme-top">Наверх</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[jupyter-url]: https://jupyter.org/
[jupyter.org]: https://jupyter.org/assets/logos/rectanglelogo-greytext-orangebody-greymoons.svg
[python-url]: https://www.python.org
[python.org]: https://www.python.org/static/img/python-logo@2x.png
[pd-url]: https://pandas.pydata.org
[pandas.org]: https://pandas.pydata.org/static/img/pandas_white.svg
[numpy-url]: https://numpy.org
[numpy.org]: https://numpy.org/images/logo.svg
[matplotlib-url]: https://matplotlib.org
[matplotlib.org]: https://matplotlib.org/_static/logo_light.svg
[seaborn-url]: https://seaborn.pydata.org
[seaborn.org]: https://seaborn.pydata.org/_static/logo-wide-lightbg.svg
[plotly-url]: https://plotly.com/python/
[plotly.com]: https://plotly.com/all_static/images/graphing_library.svg