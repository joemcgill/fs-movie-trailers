"use strict";

// Animate in the movies when the page loads
$(document).ready(function () {  
  $('.movie-card').hide().first().show("fast", function showNext() {
    $(this).next("div").show("fast", showNext);
  });
});
