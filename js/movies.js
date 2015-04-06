"use strict";

// namespace everything
var Movies = Movies || {};

Movies.Movie = Backbone.Model.extend({
  defaults: {
    'poster_image_url': 'https://placehold.it/300x400',
    'storyline': 'A short description of the movie.',
    'trailer_youtube_url': '',
    'title': 'Movie Title'
  }
});

Movies.MoviesCollection = Backbone.Collection.extend({
  model: Movies.Movie
});

Movies.MovieList = Backbone.View.extend({
  el: $('.movies-wrap'),

  initialize: function( movieList ) {
    this.collection = new Movies.MoviesCollection( movieList );
    this.render();
  },

  render: function() {
    this.collection.each( function( movie ){
      this.renderMovie( movie );
    }, this );
  },

  renderMovie: function( movie ) {
    // set up a movie card from a model
    var movieCard = new Movies.MovieCard({
      model: movie
    });
    // append the subview to our view
    this.$el.append( movieCard.render().el );
  }
});

// Set up views
Movies.MovieCard = Backbone.View.extend({
  tagName: 'div',
  className: 'movie-card',
  template: _.template( $( '#tmpl-movie' ).html() ),

  events: {
    'click': 'openDetails'
  },

  render: function() {
    this.$el.html( this.template(this.model.attributes) );
    return this;
  },

  openDetails: function() {
    var movieDetails = new Movies.MovieDetails({
      model: this.model
    });

    movieDetails.render();
  }
});

Movies.MovieDetails = Backbone.View.extend({
  el: $('#theater'),
  tagName: 'div',
  className: 'container trailer-video-container',
  template: _.template( $( '#tmpl-movie-details' ).html() ),

  events: {
    'click .btn-close': 'closeTheater'
  },


  render: function() {
    this.$el.append( this.template(this.model.attributes) ).show();
  },

  'closeTheater': function() {
    this.$el.hide().html('');
  }
})
