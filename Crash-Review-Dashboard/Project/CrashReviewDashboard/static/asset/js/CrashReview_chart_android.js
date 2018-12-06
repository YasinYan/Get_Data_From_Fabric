	var CAresult = ['KijijiCA',0.09,0.06,0.10,0.1,0.17,0.20,0.06,0.05,0.26,0.06]
	var AUresult = ['GumtreeAU',0.3,0.08,0.12,0.13,0.20,0.19,0.11,0.10,0.46,0.09]
	var ARresult = ['AlamaulaAR',0.04,0.66,0.08,0.11,0.24,1.02,0.69,0.24,1.02,0.08]
	var MXresult = ['VivanunciosMX',0.07,0.24,0.24,0.21,0.11,0.24,0.20,0.90,0.09,0.12]
	var ITresult = ['KijijiIT',0.09,0.16,0.17,0.16,0.11,0.09,0.14,0.04,1.48,0.12]
	var ZAresult = ['GumtreeZA',0.18,0.16,0.11,0.09,0.15,0.13,0.89,0.09,0.33,0.10]
	var PLresult = ['GumtreePL',0.14,0.72,0.11,0.06,0.20,0.57,0.06,0.05,0.19,0.10]
	var IEresult = ['GumtreeIE',0.06,0.54,0.04,0.03,0.09,0.22,0.09,0.38,0.83,0]
	var AULabel = ['5.22.0', '5.23.0', '5.24.0', '5.25.1', '5.26.0', '5.27.0', '5.28.1', '5.30.0', '5.31.0', '5.32.0']
	var CALabel = ['6.22.0', '6.23.0', '6.24.0', '6.25.1', '6.26.0', '6.27.0', '6.28.1', '6.30.0', '6.31.0', '6.32.0']
	var ZALabel = ['5.19.0', '5.20.0', '5.21.0', '5.22.0', '5.24.0', '5.26.0', '5.28.0', '5.30.0', '5.31.0', '5.32.0']
	var ARLabel = ['5.6.0', '5.7.0', '5.8.0', '5.9.0', '5.10.0', '5.11.0', '5.14.0', '5.21.0', '5.28.0', '5.30.0']
	var MXLabel = ['4.16.0', '4.18.0', '4.19.0', '4.21.0', '4.22.0', '4.24.0', '4.26.0', '4.28.0', '4.30.0', '4.32.0']
	var ITLabel = ['6.9.0', '6.10.0', '6.11.0', '6.13.0', '6.14.0', '6.16.0', '6.21.0', '6.22.0', '6.28.0', '6.30.0']
	var PLLabel = ['5.6.0', '5.7.0', '5.8.0', '5.9.0', '5.10.0', '5.11.0', '5.14.0', '5.21.0', '5.28.0', '5.30.0']
	var IELabel = ['4.6.0', '4.7.0', '4.8.0', '4.9.0', '4.10.0', '4.11.0', '4.14.0', '4.21.0', '4.28.0', '4.30.0']

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
        type: 'spline',    
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
