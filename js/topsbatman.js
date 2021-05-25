export function topbatsmanfuction() {
    // To fetch the file from given location
    fetch('python/json/batmanrcb.json')
        .then((response) => {
            return response.json()
        })
        .then((data) => {
            Highcharts.chart('graph', {
                chart: {
                    type: 'column'
                },
                title: {
                    text: 'Top batsman in rcb'
                },

                xAxis: {
                    type: 'category',
                    labels: {
                        rotation: -45,
                        style: {
                            fontSize: '13px',
                            fontFamily: 'Verdana, sans-serif'
                        }
                    }
                },
                yAxis: {
                    min: 0,
                    title: {
                        text: 'Total Runs By Player'
                    }
                },
                legend: {
                    enabled: false
                },
                tooltip: {
                    pointFormat: 'Runs: <b>{point.y:.1f} </b>'
                },
                series: [{

                    data:
                        data
                    ,
                    dataLabels: {
                        enabled: true,
                        rotation: -90,
                        color: '#FFFFFF',
                        align: 'right',
                        format: '{point.y:.1f}', // one decimal
                        y: 10, // 10 pixels down from the top
                        style: {
                            fontSize: '13px',
                            fontFamily: 'Verdana, sans-serif'
                        }
                    }
                }]
            });

        })
        .catch((err) => {
            // When browser fail to load file
            console.log('Your json is not loaded');
        });
};
