<!DOCTYPE html>
<html>
<head>
  <meta charset='utf-8' />
  <meta name='viewport' content='width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no' />
  <title>Crash Trend Dashboard iOS</title>
  <link href="../static/asset/css/bootstrap.min.css" rel="stylesheet">
  <!-- keen-analysis@1.2.2 -->
  <script src="../static/asset/js/keen-analysis-1.2.2.js" type="text/javascript"></script>

  <!-- keen-dataviz@1.1.3 -->
  <link href="../static/asset/css/keen-dataviz-1.1.3.css" rel="stylesheet" />
  <script src="../static/asset/js/keen-dataviz-1.1.3.js" type="text/javascript"></script>

  <!-- Dashboard -->
  <script src="../static/asset/js/c3.js" type="text/javascript"></script>
  <script src="../static/asset/css/c3.css" type="text/css"></script>
  <link rel="stylesheet" type="text/css" href="../static/asset/css/keen-dashboards.css" />
  <link rel="stylesheet" type="text/css" href="../static/asset/css/connected-devices.css" />
  <link rel="stylesheet" type="text/css" href="../static/asset/css/tooltip-viewport.css" />
  <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script>window.jQuery || document.write('<script src="../static/asset/js/jquery-slim.min.js"><\/script>')</script>
    <script src="../static/asset/js/popper.min.js"></script>
    <script src="../static/asset/js/bootstrap.min.js"></script>
    <script src="../static/asset/js/tooltip-viewport.js"></script>
    <script src="../static/asset/js/selectall.js"></script>
</head>

<body class="keen-dashboard" style="padding-top: 80px;">

</head>
    <header>
      <nav class="navbar navbar-expand-md navbar-dark fixed-top bg-dark">
        <a class="navbar-brand" href="#">Crash Review Dashboard iOS </a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarCollapse" aria-controls="navbarCollapse" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarCollapse">
          <ul class="navbar-nav mr-auto">
            <li class="nav-item">
              <a class="nav-link" href="UpdateiOS"> Update </a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="AndroidDashboard"> Android </a>
            </li>
          </ul> 
        </div>
      </nav>
    </header>

<form action="getiOSData" method="POST">
      <button class="btn btn-outline-success my-2 my-sm-0 form-group" type="Submit" name="action"">Get Release Build Crash Data</button>
<table class="table">
  <thead>
    <tr>
      <th scope="col">#</th>
      <th scope="col">Country</th>
      <th scope="col">Current Release</th>
      <th scope="col">Release in DB</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">1</th>
      <td>
         <input class="form-check-input" type="checkbox" name="inlineRadioOptions1" id="inlineRadio1" value="KijijiCA">
        <img src="../static/asset/fonts/icon_iOS/icon_CA.png" width="30" height="30" class="col-auto">
        Kijiji CA
      </td>
      <td>{{CARelease}}</td>
      <td>{{CANextRelease}}</td>
    </tr>
    <tr>
      <th scope="row">2</th>
      <td>
       <input class="form-check-input " type="checkbox" name="inlineRadioOptions2" id="inlineRadio2" value="GumtreeAU">
        <img src="../static/asset/fonts/icon_iOS/icon_AU.png" width="30" height="30" class="col-auto">
        Gumtree AU
      </td>
      <td>{{AURelease}}</td>
      <td>{{AUNextRelease}}</td>
    </tr>
    <tr>
      <th scope="row">3</th>
      <td>
        <input class="form-check-input " type="checkbox" name="inlineRadioOptions3" id="inlineRadio3" value="GumtreeZA">
        <img src="../static/asset/fonts/icon_iOS/icon_ZA.png" width="30" height="30" class="col-auto">
        Gumtree ZA
      </td>
      <td>{{ZARelease}}</td>
      <td>{{ZANextRelease}}</td>
    </tr>
    <tr>
      <th scope="row">4</th>
      <td>
        <input class="form-check-input " type="checkbox" name="inlineRadioOptions4" id="inlineRadio8" value="GumtreeUK">
        <img src="../static/asset/fonts/icon_iOS/icon_UK.png" width="30" height="30" class="col-auto">
        Gumtree UK
      </td>
      <td>{{UKRelease}}</td>
      <td>{{UKNextRelease}}</td>
    </tr>
    <tr>
      <th scope="row">5</th>
      <td>
        <input class="form-check-input " type="checkbox" name="inlineRadioOptions5" id="inlineRadio4" value="VivanunciosMX">
        <img src="../static/asset/fonts/icon_iOS/icon_MX.png" width="30" height="30" class="col-auto">
        Vivanuncios MX      
      </td>
      <td>{{MXRelease}}</td>
      <td>{{MXNextRelease}}</td>
    </tr>
    <tr>
      <th scope="row">6</th>
      <td>
        <input class="form-check-input " type="checkbox" name="inlineRadioOptions6" id="inlineRadio5" value="KijijiIT">
        <img src="../static/asset/fonts/icon_iOS/icon_IT.png" width="30" height="30" class="col-auto">
        Kijiji IT
      </td>
      <td>{{ITRelease}}</td>
      <td>{{ITNextRelease}}</td>
    </tr>
    <tr>
      <th scope="row">7</th>
      <td>
        <input class="form-check-input " type="checkbox" name="inlineRadioOptions7" id="inlineRadio6" value="AlamaulaAR">
        <img src="../static/asset/fonts/icon_iOS/icon_AR.png" width="30" height="30" class="col-auto">
        Alamaula AR
      </td>
      <td>{{ARRelease}}</td>
      <td>{{ARNextRelease}}</td>
    </tr>
  </tbody>
</table>
</form>

   <div class="col">

      <div class="col-sm-8">
        <div class="chart-wrapper">
          <div class="chart-title">
          <img src="../static/asset/fonts/icon_iOS/icon_CA.png" width="30" height="30">
                  Kijiji CA Crash in 10 Release 
          </div>
          <div class="chart-stage">
            <div id="chartCA">
              <script src="../static/asset/js/CrashReview_chart_iOS.js" type="text/javascript"></script></div>
          </div>
          <div class="chart-notes">
          </div>
        </div>
      </div>
      </div>

    <div class="col">

      <div class="col-sm-8">
        <div class="chart-wrapper">
          <div class="chart-title">
          <img src="../static/asset/fonts/icon_iOS/icon_AU.png" width="30" height="30">
                  Gumtree AU Crash in 10 Release 
          </div>
          <div class="chart-stage">
            <div id="chartAU">
               <script src="../static/asset/js/CrashReview_chart_iOS.js" type="text/javascript"></script>
            </div>
          </div>
          <div class="chart-notes">
          </div>
        </div>
      </div>
      </div>

    <div class="col">
      <div class="col-sm-8">
        <div class="chart-wrapper">
          <div class="chart-title">
          <img src="../static/asset/fonts/icon_iOS/icon_UK.png" width="30" height="30">
                  Gumtree UK Crash in 10 Release 
          </div>
          <div class="chart-stage">
            <div id="chartUK">
                <script src="../static/asset/js/CrashReview_chart_iOS.js" type="text/javascript"></script>
            </div>
          </div>
          <div class="chart-notes">
          </div>
        </div>
      </div>
      </div>

      <div class="col">
      <div class="col-sm-8">
        <div class="chart-wrapper">
          <div class="chart-title">
          <img src="../static/asset/fonts/icon_iOS/icon_ZA.png" width="30" height="30">
                  Gumtree ZA Crash in 10 Release 
          </div>
          <div class="chart-stage">
            <div id="chartZA">
              <script src="../static/asset/js/CrashReview_chart_iOS.js" type="text/javascript"></script>
            </div>
          </div>
          <div class="chart-notes">
          </div>
        </div>
      </div>
      </div>

      <div class="col">
      <div class="col-sm-8">
        <div class="chart-wrapper">
          <div class="chart-title">
          <img src="../static/asset/fonts/icon_iOS/icon_AR.png" width="30" height="30">
                  alamaula AR Crash in 10 Release 
          </div>
          <div class="chart-stage">
            <div id="chartAR">
              <script src="../static/asset/js/CrashReview_chart_iOS.js" type="text/javascript"></script>
            </div>
          </div>
          <div class="chart-notes">
          </div>
        </div>
      </div>
      </div>

    <div class="col">
      <div class="col-sm-8">
        <div class="chart-wrapper">
          <div class="chart-title">
          <img src="../static/asset/fonts/icon_iOS/icon_IT.png" width="30" height="30">
                  Kijiji IT Crash in 10 Release 
          </div>
          <div class="chart-stage">
            <div id="chartIT">
              <script src="../static/asset/js/CrashReview_chart_iOS.js" type="text/javascript"></script>
            </div>
          </div>
          <div class="chart-notes">
          </div>
        </div>
      </div>
      </div>

      <div class="col">
      <div class="col-sm-8">
        <div class="chart-wrapper">
          <div class="chart-title">
          <img src="../static/asset/fonts/icon_iOS/icon_MX.png" width="30" height="30">
                  Vivanuncios MX Crash in 10 Release 
          </div>
          <div class="chart-stage">
            <div id="chartMX">
              <script src="../static/asset/js/CrashReview_chart_iOS.js" type="text/javascript"></script>
            </div>
          </div>
          <div class="chart-notes">
          </div>
        </div>
      </div>
      </div>
</body>
</html>