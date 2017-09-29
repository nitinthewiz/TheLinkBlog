---
layout: null
---
// builds lunr

{% assign count = 0 %}
var links = [{
{% for post in site.posts %}
  "id": {{count}},
  "title": {{post.title | jsonify }},
  "url": {{post.url | jsonify }},
  "external_url": {{post.external-url | jsonify }},
  "date": {{ post.date | date: '%B %-d, %Y' | jsonify }},
  "year": {{ post.year }},
  "month": {{ post.month }},
  "excerpt": {{ post.content | strip_html | truncatewords: 20 | jsonify }}
}{% unless forloop.last %}, { {% endunless %}{% assign count = count | plus: 1 %}{% endfor %}]


var index = lunr(function () {
  this.ref('id')
  this.field('title')
  this.field('url')
  this.field('external_url')
  this.field('date')
  this.field('year')
  this.field('month')
  this.field('excerpt')

  links.forEach(function (doc) {
    this.add(doc)
  }, this)
})

console.log( jQuery.type(index) );

// builds search
$(document).ready(function() {
  $('input#search').on('keyup', function () {
    var resultdiv = $('#results');
    // Get query
    var query = $(this).val();
    // Search for it
    var result = index.search(query);
    // Show results
    resultdiv.empty();
    // Add status
    resultdiv.prepend('<p class="">Found '+result.length+' result(s)</p>');

    // Loop through, match, and add results
    for (var item in result) {
      var searchitem = '<article class="post">'
      searchitem += '<div class="post-confidence">score = '+result[item].score+'</div>';
      searchitem += '<h1><a href="'+links[result[item].ref].external_url+'" onclick="trackOutboundLink(\''+links[result[item].ref].external_url+'\'); return false;">'+links[result[item].ref].title+'</a>&nbsp;<a class="anchor" href="'+links[result[item].ref].url+'"><i class="fa fa-paper-plane" aria-hidden="true"></i></a></h1>';
      searchitem += '<div class="post-date">'+links[result[item].ref].date+'</div>';
      searchitem += '<div class="post-content">'+links[result[item].ref].excerpt+'</div>';
      searchitem += '</article>';

      resultdiv.append(searchitem);
    }

  });
});
