<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{{ title }} - WeatherApp</title>
    <link href="/static/content/bootstrap.min.css" rel="stylesheet">
</head>
<body>

<div class="col-lg-8 mx-auto p-3 py-md-5">
    <header class="d-flex justify-content-center py-3">
        <ul class="nav nav-pills">
            %for option in menu:
                <li class="nav-item"><a href="{{ option.link }}" class="{{ option.class_name() }}">{{ option.name }}</a></li>
            %end
        </ul>
    </header>

    <main>
        {{!base}}
    </main>
    <footer class="pt-5 my-5 text-muted border-top">
        WeatherApp team &middot; &copy; {{ year }}
    </footer>
</div>

<script src="/static/scripts/bootstrap.bundle.min.js"></script>

</body>
</html>
