% rebase('layout.tpl', title=title, menu=menu, year=year)

<!-- Форма для добавления новинки -->
<div class="row">
    <div class="col-md-4">
        <h5 class="card-title">Добавить новинку</h5>
        <form action="/novelties" method="post" onsubmit="return validate_all();">
            <fieldset class="form-group">
                <label for="exampleInputEmail1" class="form-label mt-4">Email</label>
                <input class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp"
                       placeholder="your-email@domain.com" name="email" required>

                <label for="exampleInputNickname1" class="form-label mt-4">Никнейм</label>
                <input class="form-control" id="exampleInputNickname1" name="nickname" required>

                <label for="exampleInputTitle1" class="form-label mt-4">Заголовок</label>
                <input class="form-control" id="exampleInputTitle1" name="title" required>

                <label for="exampleTextarea" class="form-label mt-4">Ваш текст</label>
                <textarea class="form-control" id="exampleTextarea" rows="2" name="description" required></textarea>
            </fieldset>
            <br>
            <button type="submit" class="btn btn-primary">Опубликовать</button>
        </form>
    </div>
</div>

<br>
<hr>
<br>

<div class="row g-3">
    %for noveltie in actual_novelties:
    <!-- Карточка для отображения новинки -->
    <div class="col-md-12">
        <div class="card">
            <div class="card-body">
                <h5 class="card-title">{{ noveltie.title }}</h5>
                <p>
                    <b>Автор:</b> {{ noveltie.nickname }},
                    <b>Email: </b> {{ noveltie.email }},
                    <b>Опубликовано: </b> {{ noveltie.date }}
                </p>
                <p class="card-text">
                %for s in noveltie.description.splitlines():
                    <p>{{ s }}</p>
                %end
                </p>
            </div>
        </div>
    </div>
    %end
</div>
