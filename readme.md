Opening Movie Trailers
======================


## Requirements

This application makes use of the [Rotten Tomatoes API](http://developer.rottentomatoes.com/) and the [Google API](http://code.google.com/apis/console#access). After signing up for account with each, use the following commands to install python clients for each API on your machine using `pip`.

**Rotten Tomatoes API for Python**
```
pip install rottentomatoes
```

**Google API Client**
```
pip install --upgrade google-api-python-client
```

## Getting Started

In order to use this app, you'll need to add a file named `config.py` to to your project folder and include your API keys using the following variables:

```
// Rotten Tomatoes API Key http://developer.rottentomatoes.com/
api_key = "your-key-here"

// Google Apps API Key http://code.google.com/apis/console#access
youtube_key = 'your-key-here'
```

### Running the program

After setting up your config.py file, you can run the program by typing `python project1.py` in your terminal from the project directory.
