# spider_squeegee
Stupid Web Tricks with Python, Webdriver, BS4 and more

## What Does What: 

### Tacos.py

*What it do: 

This is a simple python script that uses BS4 and a basic web request to scrape the front page of Yelp.com and return the names and addresses of the restaurants/businesses returned via the query of "Tacos" in "Austin, TX".  

*How it do it:

From a terminal, just run "python tacos.py".  Results are printed to the terminal screen. 

*What it need: 

- Python 2.7
- Beautiful Soup 4
- You need to install Pip and then install these locally before running this script

### Tokyo_Rave_Images.py

*What it do: 

Using Beautiful Soup, Webdriver and your local browser, this thing opens an online archive of rave fliers from Tokyo from the 1990s to the Early 2000s and then downloads each flier into the local /images directory. 

*How it do it: 

- Run python tokyo_rave_images.py from the terminal.
- Images are saved into the /images direcyory (create this directory if it does not exist where this script is run from).
- Images are saved in whatever format they are presented in at the archive in question. 
- This thing takes a while to run - there's over 150 flier images that will be downloaded. 
- Any existing duplicate image files already in the /images directory will be overwritten. 

*What it need: 

- Python 2.7
- The selenium library for python (pip install selenium)
- The latest version of Chrome Driver (see: http://chromedriver.chromium.org/downloads)
- Chrome Driver binary must be present in either /usr/bin, /usr/local/bin or otherwise referenced in your system PATH before running this script. 

### Fun_with_apis.py

What it do: 

Pokes the Yelp.com API  with a stick.

### To Do: 

- Coming Soon!