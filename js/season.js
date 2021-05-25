export function season() {
    // Fetch the file from given location
    fetch('http://localhost:8000/python/json/season.json')
        .then(response => response.json()
        )
        .then((data) => {
            let category_list = data[0]
            let season_list = data[1]
            Highcharts.chart('graph', {
                chart: {
                    type: 'bar'
                },
                title: {
                    text: 'Stacked bar chart of Season Matches'
                },
                xAxis: {
                    categories: category_list
                },
                yAxis: {
                    min: 0,
                    title: {
                        text: 'Total Matches from 2008-2017'
                    }
                },
                legend: {
                    reversed: true
                },
                plotOptions: {
                    series: {
                        stacking: 'normal'
                    }
                },
                series: season_list
            });


        })
        .catch((err) => {
            // When browser fail to load json
            console.log('Your json is not loaded');
        })
}