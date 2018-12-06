	var CAresult = ['KijijiCA',0.18,0.11,0.17,0.19,0.18,0.27,0.04]
	var AUresult = ['GumtreeAU',0.15,0.22,0.07,0.11,0.23,0.47,0.03,0.04]
	var ARresult = ['AlamaulaAR',0.20,0.34,0.22,0.50,0.08,0.14,0.03]
	var MXresult = ['VivanunciosMX',0.40,0.13,0.05,0.75,0.09,0.06,0.05]
	var ITresult = ['KijijiIT',0.21,0.11,0.50,0.06,0.05,0.02,0.03]
	var ZAresult = ['GumtreeZA',0.09,0.07,0.47,0.08,0.16,0.04,0.06]
	var PLresult = ['GumtreeUK',0.15,0.07,0.04,0.09,0.10,0.08,0.03]
    var IEresult = 
	var AULabel = ['8.9.0', '9.0.0', '9.1.0', '9.2.0', '9.3.0', '9.4.0', '9.5.0', '9.6.0']
	var CALabel = ['8.9.0', '9.0.0', '9.1.0', '9.2.0', '9.3.0', '9.4.0', '9.5.0']
	var ZALabel = ['8.1.0', '8.2.0', '8.3.0', '8.4.0', '8.5.0', '8.6.0', '8.8.0']
	var ARLabel = ['5.7.0', '5.8.0', '5.9.0', '6.0.0', '6.1.0', '6.2.0', '6.5.0']
	var MXLabel = ['4.7.0', '4.8.0', '4.9.0', '5.0.0', '5.1.0', '5.2.0', '5.5.0']
	var ITLabel = ['7.3.0', '7.4.0', '7.5.0', '7.6.0', '7.7.0', '7.9.0', '8.0.0']
	var PLLabel = ['7.4.0', '7.5.0', '7.6.0', '7.7.0', '7.8.1', '7.9.0', '8.0.0']
    var IELable = 

    var chartCA = c3.generate({
        bindto: '#chartCA',
        data:{
            columns: [
                CAresult
                ],
        labels:{
        format:{
            KijijiCA: d3.format('')
        }
        }
            },
        type: 'spline',    
        axis: {
            x: {
                type: 'category',
                categories: CALabel
            },
            y: {
                max: 2
            }
        }
    });

    var chartAU = c3.generate({
        bindto: '#chartAU',
        data:{
            columns: [
                AUresult
                ],
        labels:{
        format:{
            GumtreeAU: d3.format('')
        }
        }
            },
        type: 'spline',    
        axis: {
            x: {
                type: 'category',
                categories: AULabel
            },
            y: {
                max: 2
            }
        }
    });

        var chartUK = c3.generate({
        bindto: '#chartPL',
        data:{
            columns: [
                PLresult
                ],
        labels:{
        format:{
            GumtreePL: d3.format('')
        }
        }
            },
        type: 'spline',    
        axis: {
            x: {
                type: 'category',
                categories: PLLabel
            },
            y: {
                max: 2
            }
        }
    });

        var chartZA = c3.generate({
        bindto: '#chartZA',
        data:{
            columns: [
                ZAresult
                ],
        labels:{
        format:{
            GumtreeZA: d3.format('')
        }
        }
            },
        type: 'spline',    
        axis: {
            x: {
                type: 'category',
                categories: ZALabel
            },
            y: {
                max: 2
            }
        }
    });

        var chartAR = c3.generate({
        bindto: '#chartAR',
        data:{
            columns: [
                ARresult
                ],
        labels:{
        format:{
            AlamaulaAR: d3.format('')
        }
        }
            },
        type: 'spline',    
        axis: {
            x: {
                type: 'category',
                categories: ARLabel
            },
            y: {
                max: 2
            }
        }
    });

        var chartIT = c3.generate({
        bindto: '#chartIT',
        data:{
            columns: [
                ITresult
                ],
        labels:{
        format:{
            KijijiIT: d3.format('')
        }
        }
            },
        type: 'spline',    
        axis: {
            x: {
                type: 'category',
                categories: ITLabel
            },
            y: {
                max: 2
            }
        }
    });

        var chartMX = c3.generate({
        bindto: '#chartMX',
        data:{
            columns: [
                MXresult
                ],
        labels:{
        format:{
            VivanunciosMX: d3.format('')
        }
        }
            },
        type: 'spline',    
        axis: {
            x: {
                type: 'category',
                categories: MXLabel
            },
            y: {
                max: 2
            }
        }
    });

    var chartIE = c3.generate({
        bindto: '#chartIE',
        data:{
            columns: [
                MXresult
                ],
        labels:{
        format:{
            GumtreeIE: d3.format('')
        }
        }
            },
        type: 'spline',    
        axis: {
            x: {
                type: 'category',
                categories: IELabel
            },
            y: {
                max: 2
            }
        }
    });
