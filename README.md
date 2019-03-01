# osx_desktop_image_changer

## motivation

I couldn't find any tools to set the image on all spaces in 10.13 or 10.14.

## usage

```
# single image on all spaces
./change_desktop_on_all_spaces.py img1

# different images
# - cycles through specified images
./change_desktop_on_all_spaces.py img1 img2 img3 img4 ... img999999
```

## known issues

- doesn't set images for multiple displays yet
- when setting multiple images, if you've reordered the spaces the alternation order can't be guaranteed
  - TODO: need to inspect ~/Library/Preferences/com.apple.spaces.plist and figure out order? 
    - http://ianyh.com/blog/identifying-spaces-in-mac-os-x/

## links

- https://developer.apple.com/library/archive/samplecode/DesktopImage/Introduction/Intro.html#//apple_ref/doc/uid/DTS40008860-Intro-DontLinkElementID_2
