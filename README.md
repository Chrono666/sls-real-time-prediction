# Real time classification of SLS (lightweight version)

The purpose of this project is to create a quick and lightweight script to classify images of an SLS process.
For this purpose a vgg16 model was trained and saved.

The contained script starts a scheduler which calls three functinos every 35 sec:
* load latest modified image from folder.
* use vgg16 model to predict if it contains curling or not.
* still missing is the conversion of the raw images to the rgb jpeg format.

## Set up
* set up a virtual environment with anaconda and the contained yaml file
* start script in context of environment either in the terminal or through pycharm