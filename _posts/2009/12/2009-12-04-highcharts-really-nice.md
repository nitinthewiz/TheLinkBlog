---
title: "Highcharts: Really nice charting API"
date: 2009-12-04 11:36:06 +0000
external-url: http://ajaxian.com/archives/highcharts-really-nice-charting-api
hash: 24e4db909e8df5f47c68284c5ec38436
---

We all want better and better charting libraries. Dojo has some good stuff, Protovis is a good option, and there are many many more (put your favourite below!).

The latest guy in the ring is Highcharts uses either jQuery or MooTools for some common JavaScript tasks. In addition, Internet Explorer needs ExCanvas which emulates the Canvas element.

For some simple code like this:

PLAIN TEXT
JAVASCRIPT:




 


var chart1 = new Highcharts.Chart({


         chart: {


            renderTo: 'chart-container-1',


            defaultSeriesType: 'bar'


         },


         title: {


            text: 'Fruit Consumption'


         },


         xAxis: {


            categories: ['Apples', 'Bananas', 'Oranges]


         },


         yAxis: {


            title: {


               text: 'Fruit eaten'


            }


         },


         series: [{


            name: 'Jane',


            data: [1, 0, 4]


         }, {


            name: 'John',


            data: [5, 7, 3]


         }]


      });

 




You can get nice charts like this:



Be sure to check out the demo gallery.


  

