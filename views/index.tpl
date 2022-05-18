% rebase('layout.tpl', title=title, menu=menu, year=year)

<!-- Заголовок сайта -->
<div class="px-4 py-5 my-5 text-center">
    <h1 class="display-5 fw-bold">Погода</h1>
    <div class="col-lg-6 mx-auto">
        <p class="lead mb-4">В такую дивную погоду — в холодный дождь и грязный снег — становится вкуснее кофе, теплее
            кот и мягче плед.</p>
    </div>
</div>

<!-- Колонки с текстом -->
<div class="row">
    <div class="col-md-4">
        <h2>Кажется, дождь начинается</h2>
        <p>
            Bottle — это мощный, основанный на паттернах способ создания динамических веб-сайтов,
            который обеспечивает чистое разделение проблем
            и дает вам полный контроль над разметкой для приятной и гибкой разработки.
        </p>
    </div>
    <div class="col-md-4">
        <h2>Больше библиотек</h2>
        <p>Bootstrap — это открытый и бесплатный HTML, CSS и JS фреймворк,
            который используется веб-разработчиками
            для быстрой вёрстки адаптивных дизайнов сайтов и веб-приложений language.
        </p>
    </div>
    <div class="col-md-4">
        <h2>Байкал – не только озеро</h2>
        <p>Российский процессор семейства Baikal, созданный российской бесфабричной компанией
            Baikal Electronics с использованием двух 32-битных процессорных ядер
            P5600 архитектуры MIPS32 Release 5 от компании Imagination Technologies
        </p>
    </div>
    <div class="col-md-4">
        <h2>Ask a Question</h2>
        <form action="/home" method="post">
            <fieldset class="form-group">
                <label for="exampleInputEmail1" class="form-label mt-4">Your email</label>
                <input class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp"
                       placeholder="Enter email" name="email">

                <label for="exampleTextarea" class="form-label mt-4">Your question</label>
                <textarea class="form-control" id="exampleTextarea" rows="2" name="question"></textarea>
            </fieldset>
            <br>
            <button type="submit" class="btn btn-primary">Submit</button>
        </form>
    </div>
</div>
