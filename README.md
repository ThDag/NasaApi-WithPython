# NASA APIs Python Extension

## Making NASA APIs functions available thru simple python classes and objects with straight simple results.

1. [usage](##Usage)
2. [setting image saving directory](##Setting-image-saving-directory)

## Usage
### Main Setting
Main settings apply to every functions these are...
- api_key  \
  Takes Nasa Api key, default is DEMO_KEY, only takes string

- save  \
  Chooses to Save Images or not, only takes True or False, if True will download images to img_dir if False will return urls

- img_dir  \
  Chooses where to save downlaoded images, only takes string, [How to use](##Setting-image-saving-directory)

- img_name  \
  Chooses name of the image name if image is singular, only takes string

### Astronomy Picture Of the Day
wip

## Setting image saving directory 
Default saving directory is current working directory (.) While Chossing saving directory start from current working directory
and from there 


example:
```Python
image_saver = main(api_key='DEMO_KEY', save=True, img_dir='../dir1/dir2')
# in this case it saves the file to the dir2 inside dir1 one which is inside current working directories parent directory
```

### Note
Image Name cant be changed (for now)


## Credit
Just me -> https://github.com/ThDag \
Also NASA -> https://api.nasa.gov

Create Issue for any idea or problem or request.
