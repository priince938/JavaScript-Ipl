export function umpirefuction() {
    fetch('http://localhost:8000/python/json/umpire.json')
        .then((response) => {
            return response.json()
        })
        .then((data) => {
            Highcharts.chart('graph', {
                chart: {
                    type: 'column'
                },
                title: {
                    text: 'Umpire Other Than India'
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
                        text: 'Umpire'
                    }
                },
                legend: {
                    enabled: false
                },
                tooltip: {
                    pointFormat: 'Number of Umpire: <b>{point.y:.1f} </b>'
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
            // Do something for an error here
            console.log('Your json is not loaded');
        });
};