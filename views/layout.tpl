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
            <!-- <li class="nav-item"><a href="/" class="nav-link active" aria-current="page">Home</a></li> -->
            <li class="nav-item"><a href="/" class="nav-link">Home</a></li>
            <li class="nav-item"><a href="/about" class="nav-link">About</a></li>
            <li class="nav-item"><a href="/contact" class="nav-link">Contact</a></li>
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
