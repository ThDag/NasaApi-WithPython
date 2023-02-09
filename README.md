# NASA APIs Python Extension

## Making NASA APIs functions available thru simple CLI input with straight simple results.

1. [saving image](##Choosing-to-Save-image-or-not)
2. [setting image saving directory](##Setting-image-saving-directory)

## Usage
write this place wip

## Choosing to Save image or not
Defining any variable the argument `save` takes True or False Default False. 
- True: Saves file to the current working directory if [not set](##Setting-image-saving-directory)
- False: Dosen't save file anywhere just gives string of the image link from NASA   

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
