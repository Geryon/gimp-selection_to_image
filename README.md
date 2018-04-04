GIMP selection_to_image.py

This is a GIMP plugin, tested with GIMP 2.8.  It adds the ability to select a region in an image and with minimal input, save it directly to a file.

I wrote this for a specific task, to scan in thousands of family photos.  I set this up for personal use and because of this there's a number of hard coded items and assumptions made.  Regardless, I wanted to toss this up here since finding newer GIMP examples seemed hard to come by. 

I have this set up so that it stores all the files on my Desktop, sorted by year and it prepends the year to the filename, along with a front/back designation based on the side of the picture scanned.  This is also designed to work from scanning with XSANE as it scans to a single layered flat image.  I assume the image is flat and force pulling from layer 0 becaues of this.  If the designation directory doesn't exist, it gets created and the first file in there will be assigned the id '0000', thus creating '<year>-0000-<front/back>.<file_type>'.  The script will auto-increment the file ID count.

Beyond using it as a code sample, it can easily be added to GIMP by copying it into your GIMP plug-ins directory, generally in '~/.gimp-2.8/plug-ins'.  I would also recommend changing the 'dir_path' variable as this will only work if ran as root or your user name is 'nick'.  I am also aware that I could have had these as UI options, but I wanted to minimize what information I needed to provide each time I ran this.

I also feel the code can better handle the file formats, as they don't work quite well.  I have it, by default, writing PNG and RAW.  RAW on my system creates a '.data' file, but I have other GIMP installs that lack this by default; so it can be disabled.  If you select multiple file formats it will create multiple files.
