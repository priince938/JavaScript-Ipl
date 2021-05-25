
export function totalrunsfuction() {
    fetch('http://localhost:8000/python/json/totalruns.json')
        .then((response) => {
            return response.json()
        })
        .then((data) => {
            Highcharts.chart('graph', {
                chart: {
                    type: 'column'
                },
                title: {
                    text: 'Total Runs In IPL '
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
                        text: 'Total runs'
                    }
                },
                legend: {
                    enabled: false
                },
                tooltip: {
                    pointFormat: 'Total runs: <b>{point.y:.1f} </b>'
                },
                series: [{
                    name: 'Population',
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
            console.log('Your csv is not loaded');
        });
};