<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{{ title }} - WeatherApp</title>
    <link href="/static/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="/static/css/bootstrap-icons.min.css">
</head>
<body>

<div class="col-lg-8 mx-auto p-3 py-md-5">
    <header class="d-flex justify-content-center py-3">
        <ul class="nav nav-pills">
            %for option in menu:
            <li class="nav-item">
                <a href="{{ option.link }}" class="{{ option.class_name() }}">{{ option.name }}</a>
            </li>
            %end
        </ul>
    </header>

    <main>
        {{!base}}
    </main>
    <footer class="pt-5 my-5 text-muted border-top">
        WeatherApp Team &middot; &copy; {{ year }}<br>
        <i class="bi-github" role="img"></i>
        <a  style="margin: 2px; text-decoration: none " href="https://github.com/qwonix/wish-everyone-become-pitonist">Source code</a>
    </footer>
</div>

<script src="/static/js/bootstrap.bundle.min.js"></script>

</body>
</html>
