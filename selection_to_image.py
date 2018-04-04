#!/usr/bin/env python

# GIMP Python plug-in template.

import glob
import re
import os
from gimpfu import *


def fetch_next_image_id(dir_path, year):
    filenames = glob.glob("%s/%s*" % (dir_path, year))
    counts = []
    for name in filenames:
        m = re.findall('(\d{4})', name)
        counts.append(int(m[2]))
    max_count = 0 if len(counts) == 0 else max(counts) + 1
    return "%04d" % max_count


def determine_file_formats(png=0, raw=0, jpeg=0:
    formats = []
    if png:
        formats.append('png')
    if raw:
        formats.append('tiff')
    if jpeg:
        formats.append('jpg')

    return formats


def selection_to_image(timg, tdrawable, year, pic_side, raw, png, jpeg):
    pic_side = "back" if pic_side else "front"
    dir_path = "/home/nick/Desktop/Family Pictures/" + year

    # Determine next image increment
    img_count = fetch_next_image_id(dir_path, year)

    filebase = "%s/%s-%s-%s" % (dir_path, year, img_count, pic_side)
    gimp.progress_init("Creating files with base name %s." % filebase)

    # Create the directory if it's missing
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    # Fetch our selected area
    pdb.gimp_image_get_selection(timg)

    # Fetch the selected image boundries
    selected, x1, y1, x2, y2 = pdb.gimp_selection_bounds(timg)

    # Toss an error up if nothing was selected
    if not selected:
        pdb.gimp_message("A selection must be made first.")
        return

    # Put the selected area in the copy buffer
    pdb.gimp_image_select_rectangle(timg, 2, x1, y1, abs(x1-x2), abs(y1-y2))
    copied = pdb.gimp_edit_copy(timg.layers[0])

    if not copied:
        pdb.gimp_message("Empty area selected.")
        return

    # Create a new image
    new_img = pdb.gimp_edit_paste_as_new()
    new_drw = pdb.gimp_image_active_drawable(new_img)

    # Save in requested formats
    for file_format in determine_file_formats(png, raw, jpeg):
        filen = "%s-%s-%s.%s" % (year, img_count, pic_side, file_format)
        pdb.gimp_file_save(new_img, new_drw,
                           filebase + '.' + file_format,
                           filen)

    pdb.gimp_image_delete(new_img)
    pdb.gimp_progress_end()
    pdb.gimp_displays_flush()

    return


register(
    "python_fu_selection_to_image",
    "Create Image from Selection",
    "Create and save a new image from a selection",
    "Nicholas DeClario",
    "Nicholas DeClario",
    "2018",
    "<Image>/File/Create/Selection to Image (Py)...",
    "RGB*, GRAY*",
    [
        (PF_STRING, "year", "Year", "1985"),
        (PF_OPTION, "pic_side", "Picture Side", 0, ["Front", "Back"]),
        (PF_TOGGLE, "raw", "RAW", 1),
        (PF_TOGGLE, "png", "PNG", 1),
        (PF_TOGGLE, "jpeg", "JEPG", 0),
    ],
    [],
    selection_to_image)

main()
