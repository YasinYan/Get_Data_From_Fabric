
Keen.ready(function(){

    var CAresult = { result:[1.5,0.7,1,1.2,0.5,0.5,0.6,0.5,0.9,1.1]};
    var AUresult = { result:[1.5,0.7,1,1.2,0.5,0.5,0.6,0.5,0.9,1.1]};
    var ARresult = { result:[0.3,0.7,0.1]};
    var MXresult = { result:[1.2,0.4,0.1]};
    var IEresult = { result:[1.4,0.6,0.3]};
    var ITresult = { result:[1,0.4,0.1,0.5,1.2]};
    var ZAresult = { result:[1,0.4,0.1,0.5,1.2]};
    var PLresult = { result:[1,0.4,0.1]};
    var BiweekReleaseLable =['JAN-A', 'JAN-B', 'FEB-A', 'FEB-B', 'MAR-A','MAR-B','APR-A','APR-B','MAY-A','MAY-B'];
    var monthlyReleaseLable =['JAN-A','FEB-A','MAR-A','APR-A','MAY-A'];
    var longestReleaseLable = ['JAN-A','FEB-B','MAR-B'];
    //AU
    var sample_funnel1 = new Keen.Dataviz()
    .el('#chart-06') 
    .colors(['red'])
    .data(AUresult)
    .height(340)
    .type('line')
    .labels(BiweekReleaseLable)
    .title(null)
    .render();
//CA
var sample_funnel2 = new Keen.Dataviz()
    .el('#chart-07') 
    .colors(['green'])
    .data(CAresult)
    .height(340)
    .type('line')
    .labels(BiweekReleaseLable)
    .title(null)
    .notes("JAN-A Notes: caused by ticket GBLANDROID-5839")
    .render();
//ZA
var sample_funnel3 = new Keen.Dataviz()
    .el('#chart-08') 
    .colors(['red'])
    .data(ZAresult)
    .height(340)
    .type('line')
    .labels(monthlyReleaseLable)
    .title(null)
    .render();
//MX
var sample_funnel4 = new Keen.Dataviz()
    .el('#chart-09') 
    .colors(['red'])
    .data(MXresult)
    .height(340)
    .type('line')
    .labels(monthlyReleaseLable)
    .title(null)
    .render();   
//IT
var sample_funnel5 = new Keen.Dataviz()
    .el('#chart-10') 
    .colors(['red'])
    .data(ITresult)
    .height(340)
    .type('line')
    .labels(monthlyReleaseLable)
    .title(null)
    .render();
//AR
var sample_funnel6 = new Keen.Dataviz()
    .el('#chart-11') 
    .colors(['red'])
    .data(ARresult)
    .height(340)
    .type('line')
    .labels(longestReleaseLable)
    .title(null)
    .render();
//IE
var sample_funnel7 = new Keen.Dataviz()
    .el('#chart-12') 
    .colors(['red'])
    .data(IEresult)
    .height(340)
    .type('line')
    .labels(longestReleaseLable)
    .title(null)
    .render();
//PL
var sample_funnel8 = new Keen.Dataviz()
    .el('#chart-13') 
    .colors(['red'])
    .data(PLresult)
    .height(340)
    .type('line')
    .labels(longestReleaseLable)
    .title(null)
    .render();
});
