// Load the Visualization API and the corechart package.
      google.charts.load('current', {'packages':['corechart', 'bar']});

      // Set a callback to run when the Google Visualization API is loaded.
      google.charts.setOnLoadCallback(drawChart);

      // Callback that creates and populates a data table,
      // instantiates the pie chart, passes in the data and
      // draws it.
      function drawChart() {

        // Create the data table.
        var data = google.visualization.arrayToDataTable([
          ['Team', 'Sports League'],
          ['San Francisco Giants',  10],
          ['Golden State Warriors', 5],
          ['San Jose Sharks', 4], 
          ['Los Angeles Dodgers', 1]
        ]);

        // Set chart options
        var options = {
          title: 'Most popular sports teams',
          chartArea: {width: '50%'},
          hAxis: {
            title: 'Total Votes',
            minValue: 0
          },
          vAxis: {
            title: 'Teams'
          }
        };

        // Instantiate and draw our chart, passing in some options.
        var chart = new google.visualization.BarChart(document.getElementById('chart_div'));
        chart.draw(data, options);
      }