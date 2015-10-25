<?php
 require "connection.php";




// escape variables for security
$a = mysql_real_escape_string ($_POST['a']);
$b = mysql_real_escape_string ($_POST['b']);
$c = mysql_real_escape_string ($_POST['c']);

$sql="INSERT INTO test (a,b,c) VALUES ('$a', '$b', '$c')";

mysql_query("INSERT INTO test (a,b,c)
VALUES ('$a', '$b', '$c')");

 ?>





<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Suko</title>

        <link href="asset/jquery.minicolors.css" rel="stylesheet">
        <link href="dashboard/css/bootstrap.min.css" rel="stylesheet">
        <link href="dashboard/css/linecons.css" rel="stylesheet">
        <link href="dashboard/css/custom-fonts.css" rel="stylesheet">
        <link href="dashboard/css/style.css" rel="stylesheet">
        <link href="dashboard/css/Colors/default.css" rel="stylesheet">
        <link href="dashboard/css/dark.css" rel="stylesheet">
        <link href='http://fonts.googleapis.com/css?family=Raleway:400,300,700' rel='stylesheet' type='text/css'>

        <!--[if lt IE 9]>
          <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
          <script src="https://oss.maxcdn.com/libs/respond.dashboard/js/1.4.2/respond.min.js"></script>
        <![endif]-->
    </head>
    <body>


<section id="WORKS" class="body full section-black">
    <div class="background-full" data-background=''>
        <div class='bg-wrapper front-heigh'></div>
        <article class="body left-right">
            <div class="DivParent-background-full text-center around-white front relative">
                <div class="DivWhichNeedToBeVerticallyAligned">
                    <h1 class="text-extra-big font-hard"><span class="text-color" >Suko</span>.Tv </h1>

                    <p class="text-medium-large font-soft text-spacing-small"> </p>
                    <a href="" class="btn-Suko-transparent text-medium-large font-soft play-animations inline"> <span> Sign </span>  <span class="block text-smallest text-left"> Up </span> </a>
                    &nbsp;
                    <a href="" class="bg-color text-box text-medium-large hover-bg-black font-soft play-animations inline"> <span> Log </span>  <span class="block text-smallest text-left"> In </span> </a>
                </div>
                <div class="DivHelper"></div>
            </div>
        </article>
        <div class='control-youtube absolute top'>
            <div id="playerYoutube" class='playerYoutube-bg height-full' data-video_id='8mhaybLTPfk' data-video_quality='default'></div>
        </div>
    </div>
</section>




<section id="footer" class="section-dark front-heigh relative">
    <div class="around-white body small ">
        <p class="text-medium">Copyright © Suko.Tv All Rights Reserved</p>
    </div>
</section>

</section>


<script src="dashboard/js/jquery.min.js"></script>
<script src="dashboard/js/zepto.min.js"></script>
<script src="dashboard/js/SmoothScroll.js"></script>
<script src="dashboard/js/modernizr.custom.js"></script>
<script src="dashboard/js/jquery.localscroll-1.2.7-min.js"></script>
<script src="dashboard/js/jquery.parallax-1.1.3.js"></script>
<script src="dashboard/js/bootstrap.min.js"></script>
<script src="dashboard/js/jquery.nicescroll.min.js"></script>
<script src="dashboard/js/jquery.isotope.min.js"></script>
<script src="dashboard/js/jquery.easing.js"></script>
<script src="dashboard/js/jquery.flexslider-min.js"></script>
<script src="dashboard/js/youtube.js"></script>
<script src="dashboard/js/jquery.fittext.js"></script>


<script src="dashboard/js/owl.carousel.min.js"></script>


<script src="dashboard/js/classie.js"></script>
<script src="dashboard/js/tiltSlider.js"></script>


<script src="dashboard/js/jquery.scrollTo.js"></script>
<script src="dashboard/js/jquery.nav.js"></script>


<script src="dashboard/js/dots.js"></script>


<script src="dashboard/js/jquery.dropdown.js"></script>


<script src="dashboard/js/jpreloader.min.js"></script>


<script src="dashboard/js/jquery.placeholder.js"></script>


<script src="dashboard/js/jquery.countdown.min.js"></script>


<script src="dashboard/js/custom.js"></script>
</body>
</html>
