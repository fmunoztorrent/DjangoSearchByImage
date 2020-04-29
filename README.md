# Search by Image - Google Cloud Vision API

Django project that accepts an url from a e-commerce website (or other types), makes a webscrap it and stores catalog product listing boxes. Then analizes product images and label each image with Google Vision API.

# Features

  - Webscrap catalog URLs
  - Save images for products and use Cloud Vision API to catalog
  - Visitor can submit images and find products

# Installation
You need docker and docker-compose
In the project root folder:

```sh
$ sudo docker-compose build
$ sudo docker-compose up
```