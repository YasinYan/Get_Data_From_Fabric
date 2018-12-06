	var CAresult = ['KijijiCA',0.10,0.59,0.14,0.13,0.19,0.11,0.52,0.35,0.16,0.16]
	var AUresult = ['GumtreeAU',0.08,0.22,0.11,0.10,0.27,0.09,0.13,0.18,0.09,0.09]
	var ARresult = ['AlamaulaAR',0.2,0.34,0.22,0.5,0.08,0.14,0.03,0.09,0.08]
	var MXresult = ['VivanunciosMX',0.4,0.13,0.05,0.75,0.09,0.06,0.05,0.04,0.05]
	var ITresult = ['KijijiIT',0.21,0.11,0.5,0.06,0.05,0.02,0.03,0.06,0.16]
	var ZAresult = ['GumtreeZA',0.09,0.07,0.47,0.08,0.16,0.04,0.06,0.08,0.13,0.09]
	var UKresult = ['GumtreeUK',0.05,0.07,0.07,0.21,0.12,0.15,0.09,0.10,0.20,0.26]
	var AULabel = ['10.0.0', '10.1.1', '10.2.0', '10.3.0', '10.4.0', '10.5.0', '10.6.0', '10.7.0', '10.8.0', '10.9.0']
	var CALabel = ['10.0.0', '10.1.1', '10.2.0', '10.3.0', '10.4.0', '10.5.0', '10.6.0', '10.7.0', '10.8.0', '10.9.0']
	var ZALabel = ['8.1.0', '8.2.0', '8.3.0', '8.4.0', '8.5.0', '8.6.0', '8.8.0', '9.4.0', '10.6.0', '10.7.0']
	var ARLabel = ['5.7.0', '5.8.0', '5.9.0', '6.0.0', '6.1.0', '6.2.0', '6.5.0', '7.1.0', '10.7.0']
	var MXLabel = ['4.7.0', '4.8.0', '4.9.0', '5.0.0', '5.1.0', '5.2.0', '5.5.0', '6.1.0', '10.7.0']
	var ITLabel = ['7.3.0', '7.4.0', '7.5.0', '7.6.0', '7.7.0', '7.9.0', '8.0.0', '8.6.0', '10.7.0']
	var UKLabel = ['8.4.0', '8.5.0', '10.1.0', '10.2.0', '10.3.0', '10.4.0', '10.5.0', '10.6.0', '10.7.0', '10.8.0']
    
    var chartCA = c3.generate({
        bindto: '#chartCA',
        data:{
            columns: [
                CAresult
                ],
             types: {
                KijijiCA:'spline'
            },
        labels:{
        format:{
            KijijiCA: d3.format('')
        }
    }
            },   
        axis: {
            x: {
                type: 'category',
                categories: CALabel
            },
            y: {
                max: 1
            }
        }
    });

    var chartAU = c3.generate({
        bindto: '#chartAU',
        data:{
            columns: [
                AUresult
                ],
            types: {
                GumtreeAU:'spline'
            },
        labels:{
            format:{
            GumtreeAU: d3.format('')
        }
    }
            },  
        axis: {
            x: {
                type: 'category',
                categories: AULabel
            },
            y: {
                max: 1
            }
        }
    });

        var chartUK = c3.generate({
        bindto: '#chartUK',
        data:{
            columns: [
                UKresult
                ],
        types: {
                GumtreeUK:'spline'
            },
        labels:{
            format:{
                GumtreeUK: d3.format('')
            }
        }
            },
        axis: {
            x: {
                type: 'category',
                categories: UKLabel
            },
            y: {
                max: 1
            }
        }
    });

        var chartZA = c3.generate({
        bindto: '#chartZA',
        data:{
            columns: [
                ZAresult
                ],
            types: {
                GumtreeZA:'spline'
            },
        labels:{
        format:{
            GumtreeZA: d3.format('')
        }
        }
            },   
        axis: {
            x: {
                type: 'category',
                categories: ZALabel
            },
            y: {
                max: 1
            }
        }
    });

        var chartAR = c3.generate({
        bindto: '#chartAR',
        data:{
            columns: [
                ARresult
                ],
            types: {
                AlamaulaAR:'spline'
            },
        labels:{
            format:{
                AlamaulaAR: d3.format('')
            }
        }
    },    
        axis: {
            x: {
                type: 'category',
                categories: ARLabel
            },
            y: {
                max: 1
            }
        }
    });

        var chartIT = c3.generate({
        bindto: '#chartIT',
        data:{
            columns: [
                ITresult
                ],
            types: {
                KijijiIT:'spline'
            },
        labels:{
            format:{
                KijijiIT: d3.format('')
            }
        }
    },   
        axis: {
            x: {
                type: 'category',
                categories: ITLabel
            },
            y: {
                max: 1
            }
        }
    });

        var chartMX = c3.generate({
        bindto: '#chartMX',
        data:{
            columns: [
                MXresult
                ],
            types: {
                VivanunciosMX:'spline'
            },
        labels:{
            format:{
                VivanunciosMX: d3.format('')
            }
        }
    },
        axis: {
            x: {
                type: 'category',
                categories: MXLabel
            },
            y: {
                max: 1
            }
        }
    });
