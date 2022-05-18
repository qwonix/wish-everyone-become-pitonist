% rebase('layout.tpl', title=title, menu=menu, year=year)

<div class="col-md-4 form-group justify-content-center">
    <h2>Задайте вопрос</h2>
    <form action="/form" method="post">
        <fieldset class="form-group">
            <label class="form-label mt-4">Ваш email</label>
            <input class="form-control" aria-describedby="emailHelp"
                   placeholder="Введите email" name="email" required>

            <label for="exampleTextarea" class="form-label mt-4">Ваш вопрос</label>
            <textarea class="form-control" id="exampleTextarea" rows="2" name="question"
                      placeholder="Введите ваш вопрос" required></textarea>
        </fieldset>
        <br>
        <button type="submit" class="btn btn-primary">Отправить</button>
    </form>
</div>