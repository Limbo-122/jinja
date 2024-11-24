#style css
@import url('https://fonts.googleapis.com/css2?family=Montserrat&display=swap');

body {
    margin: 0;
    padding: 0;
    font-family: 'Montserrat', sans-serif;
    font-size: 18px;
    line-height: 20px;
    background-color: #fff;
    color: #272727;
}

h1, h2, p {
    margin: 0;
}

ul {
    list-style: none;
    margin: 0;
    padding: 0;
}

.header {
    background-image: url("../img/back.jpg");
    background-size: contain;
    background-repeat: no-repeat;
    background-position: left;
    background-color: #CCE59D;
    padding: 25vh 30px;
    margin-bottom: 60px;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}

.header__text {
    display: flex;
    flex-direction: column;
    gap: 30px;
    width: fit-content;
    text-align: right;
}

main {
    padding: 0 30px 100px;
}

.main__title {
    text-align: center;
    margin-bottom: 100px;
}

.list {
    display: flex;
    justify-content: space-around;
}

.list__item a {
    text-decoration: none;
    display: flex;
    flex-direction: column;
    align-items: center;
    color: inherit;
    gap: 20px;
    padding: 20px;
    border-radius: 24px;
    border: 1px solid #EB8028;
    transition: 0.2s;
}
.list__item_1 a {
    text-decoration: none;
    display: flex;
    flex-direction: column;
    align-items: center;
    color: inherit;
    gap: 20px;
    padding: 20px;
    border-radius: 24px;
    border: 1px solid #0EB07C;
    transition: 0.2s;
}
.item__img {
    object-fit: contain;
    width: 150px;
}

.list__item a:hover {
    box-shadow: 1px 1px 4px 4px #0EB07C;
}

.main__rez {
    display: flex;
    flex-direction: column;
    gap: 20px;
    align-items: center;
}

.rez__img {
    object-fit: contain;
    width: 300px;
}

.main__title--margin {
    margin-bottom: 50px;
}
                                          #lights.html
<!doctype html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta
    name="viewport"
    content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0"
  >
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <link rel="stylesheet" href="../static/css/style.css">
  <title>Расчет энергоэффективности умного дома</title>
</head>
<body>
  <header class="header">
    <div class="header__text">
      <h1>Расчитай энергоэффективность своего дома!</h1>
      <p>Реши проблему излишнего электропотребления самостоятельно!</p>
    </div>
  </header>
  <main>
    {% block content %}
    <h2 class="main__title">Выбери освещение:</h2>
    <ul class="list" id="list">
      <li class="list__item">
        <a href="{{size + '/3' }}">
          <img class="item__img" src="../static/img/light.svg" alt="light">
          <span>2-4 лампочки</span></a>
      </li>
      <!--Задание №2 -->
      <li class="list__item">
        <a href="{{size + '/7' }}"> 
          <img class="item__img" src="../static/img/light.svg" alt="light">
          <span>4-6 лампочек</span></a>
      </li>
      <li class="list__item">
        <a href="{{size + '/10' }}">
          <img class="item__img" src="../static/img/light.svg" alt="light">
          <span>8 и более</span></a>
      </li>
      <li class="list__item_1">
        <a href="{{size + '/3' }}">
          <img class="item__img" src="../static/img/light.svg" alt="light">
          <span>наша экологическая сборка</span></a>
      </li>
    </ul>
    {% endblock %}
  </main>
  <footer>

  </footer>
</body>
</html>
