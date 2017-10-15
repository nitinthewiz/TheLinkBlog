---
title: "Highcharts: Really nice charting API"
date: 2009-12-04 05:36:06 -0600
external-url: http://ajaxian.com/archives/highcharts-really-nice-charting-api
hash: 24e4db909e8df5f47c68284c5ec38436
year: 2009
month: 12
scheme: http
host: ajaxian.com
path: /archives/highcharts-really-nice-charting-api

---

We all want better and better charting libraries. Dojo has some good stuff, Protovis is a good option, and there are many many more (put your favourite below!).

The latest guy in the ring is Highcharts uses either jQuery or MooTools for some common JavaScript tasks. In addition, Internet Explorer needs ExCanvas which emulates the Canvas element.

For some simple code like this:

PLAIN TEXT
JAVASCRIPT:




 


var chart1 = new Highcharts.Chart(&#123;


         chart: &#123;


            renderTo: 'chart-container-1',


            defaultSeriesType: 'bar'


         &#125;,


         title: &#123;


            text: 'Fruit Consumption'


         &#125;,


         xAxis: &#123;


            categories: ['Apples', 'Bananas', 'Oranges]


         &#125;,


         yAxis: &#123;


            title: &#123;


               text: 'Fruit eaten'


            &#125;


         &#125;,


         series: [&#123;


            name: 'Jane',


            data: [1, 0, 4]


         &#125;, &#123;


            name: 'John',


            data: [5, 7, 3]


         &#125;]


      &#125;);

 




You can get nice charts like this:



Be sure to check out the demo gallery.


  

