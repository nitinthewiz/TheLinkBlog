---
layout: null
---
// builds lunr

var links = [{
{% for post in site.posts %}
  "title": {{post.title | jsonify }},
  "url": {{post.url | jsonify }},
  "external_url": {{post.external-url | jsonify }},
  "date": {{ post.date | date: '%B %-d, %Y' | jsonify }},
  "excerpt": {{ post.content | strip_html | truncatewords: 20 | jsonify }}
}{% unless forloop.last %}, { {% endunless %}{% endfor %}]


var index = lunr(function () {
  this.ref('title')
  this.field('url')
  this.field('external_url')
  this.field('date')
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
      // var searchitem = '<div class="result"><div class="result-body"><a href="'+result[item].url+'" class="post-title">'+result[item].title+'</a><div class="post-date small">'+result[item].date+'</div><p>'+result[item].excerpt+'</p></div>';
      var searchitem = '<div class="result">'+result[item].ref+' ('+result[item].score+')</div>';
      resultdiv.append(searchitem);
    }

  });
});
