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

</div>
