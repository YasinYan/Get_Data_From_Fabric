	var CAresult = ['KijijiCA',0.12,0.15,0.12,0.06,0.08,0.15,0.07,0.09,0.07,0.09]
	var AUresult = ['GumtreeAU',0.08,0.17,0.09,0.15,0.13,0.67,0.32,0.22,0.51,0.14]
	var ARresult = ['AlamaulaAR',0.06,0.04,0.66,0.08,0.11,0.24,1.02,0.09,0.19]
	var MXresult = ['VivanunciosMX',1.69,0.11,0.8,1.16,0.47,0.07,0.10,0.19,0.09,0.19]
	var ITresult = ['KijijiIT',0.16,0.09,0.16,0.17,0.16,0.11,0.06,0.12,0.06,0.11]
	var ZAresult = ['GumtreeZA',0.21,0.78,0.09,0.07,0.18,0.19,0.13,0.27,0.08,0.11]
	var PLresult = ['GumtreePL',0.08,0.14,0.72,0.11,0.06,0.20,0.57,0.06,0.09]
	var IEresult = ['GumtreeIE',0.06,0.54,0.04,0.03,0.09,0.22,0.04,0.36,0,0.33]
	var AULabel = ['5.8.0', '5.9.0', '5.10.0', '5.11.0', '5.12.0', '5.13.1', '5.14.0', '5.15.0', '5.16.0', '5.21.1']
	var CALabel = ['6.10.0', '6.11.0', '6.12.0', '6.13.0', '6.14.0', '6.15.1', '6.16.0', '6.17.0', '6.18.0', '6.21.1']
	var ZALabel = ['5.6.0', '5.7.0', '5.8.0', '5.9.0', '5.10.0', '5.11.0', '5.13.0', '5.14.0', '5.16.0', '5.21.0']
	var ARLabel = ['5.5.0', '5.6.0', '5.7.0', '5.8.0', '5.9.0', '5.10.0', '5.11.0', '5.14.0', '5.21.0']
	var MXLabel = ['4.8.0', '4.9.0', '4.10.0', '4.11.0', '4.13.0', '4.14.0', '4.16.0', '4.21.0', '4.19.0', '4.21.0']
	var ITLabel = ['6.8.0', '6.9.0', '6.10.0', '6.11.0', '6.13.0', '6.14.0', '6.16.0', '6.21.0', '6.16.0', '6.21.0']
	var PLLabel = ['5.5.0', '5.6.0', '5.7.0', '5.8.0', '5.9.0', '5.10.0', '5.11.0', '5.14.0', '5.21.0']
	var IELabel = ['4.6.0', '4.7.0', '4.8.0', '4.9.0', '4.10.0', '4.11.0', '4.14.0', '4.21.0', '4.11.0', '4.21.0']

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
        bindto: '#chartPL',
        data:{
            columns: [
                PLresult
                ],
            types: {
                GumtreePL:'spline'
            },
        labels:{
        format:{
            GumtreePL: d3.format('')
        }
        }
            },   
        axis: {
            x: {
                type: 'category',
                categories: PLLabel
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
                max: 1.5
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
                max: 2
            }
        }
    });

    var chartIE = c3.generate({
        bindto: '#chartIE',
        data:{
            columns: [
                IEresult
                ],
            types: {
                GumtreeIE:'spline'
            },  
        labels:{
        format:{
            GumtreeIE: d3.format('')
        }
        }
            },
        axis: {
            x: {
                type: 'category',
                categories: IELabel
            },
            y: {
                max: 1
            }
        }
    });
