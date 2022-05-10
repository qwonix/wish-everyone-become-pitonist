% rebase('layout.tpl', title=title, menu=menu, year=year)

<div class="row justify-content-center container px-4 py-5" id="custom-cards">
    <h2 class="pb-2 border-bottom">Санкт-Петербург</h2>
    <div class="row row-cols-1 row-cols-lg-3 align-items-stretch g-2 ">
        %for fore in weather_forecast:
        <div class="col">
            <div class="card card-cover h-100 overflow-hidden text-white bg-dark rounded-5 shadow-lg"
                 style="background-image: url('{{ fore.image_link }}');
                        background-position: right;
                        background-size: cover;">
                <div class="d-flex flex-column h-100 p-5 pb-3 text-white text-shadow-1">
                    <h2 class="pt-5 mt-5 mb-4 display-2 lh-1 fw-bold">{{ fore.title }}°</h2>
                    <h3 class="pt-4 mt-3 mb-4 display-6 lh-1">{{ fore.description }}</h3>
                    <ul class="d-flex list-unstyled mt-auto">
                        <li class="me-auto">

                        </li>
                        <li class="d-flex align-items-center me-3">

                        </li>
                        <li class="d-flex align-items-center">
                            <span class="badge bg-light">{{ fore.date }}</span>
                        </li>
                    </ul>
                </div>
            </div>
        </div>
        %end
    </div>

    <div class="g-5"></div>
    <div class="g-3"></div>
    <h2 class="pb-2 border-bottom">Оставьте комментарий</h2>

    <div class="row-cols-2 form-group">
        <form action="/comments" method="post">
            <fieldset class="form-group">
                <div>
                    <label class="form-label mt-3">Ваше имя</label>
                    <input class="form-control"
                           pattern="^[А-Яа-яЁё]{3,}$"
                           title="Используйте русский алфавит, минимум 3 символа"
                           placeholder="Имя от 3 символов" name="name" required>

                    <label class="form-label mt-4">Ваш номер телефона</label>
                    <input class="form-control"
                           pattern="^[+]7[ ][0-9]{3}[ ][0-9]{3}-[0-9]{2}-[0-9]{2}$"
                           title="Формат телефона: +7 ххх ххх-хх-хх"
                           placeholder="+7 ххх ххх-хх-хх"
                           name="phone" required>
                </div>

                <label for="exampleTextarea" class="form-label mt-4">Ваш комментарий</label>
                <textarea class="form-control" id="exampleTextarea" rows="5"
                          title="Используйте русский, латинский алфавит и цифры"
                          name="text"
                          placeholder="Текст комментария" required></textarea>
            </fieldset>
            <br>
            <button type="submit" class="btn btn-primary">Отправить</button>
        </form>
    </div>

    <div class="g-4"></div>

    <h2 class="pb-2 border-bottom">Комментарии</h2>

    <div class="row g-2">
        %for comm in comments:
        <div class="card border-primary col-md-7 mb-lg-1">
            <div class="card-header">{{ comm.date }}</div>
            <div class="card-body">
                <h4 class="card-title">{{ comm.name }}</h4>
                <p class="card-text">{{ comm.text }}</p>
            </div>
        </div>
        %end
    </div>
</div>
