#!/usr/bin/env python
##
##  pyvnc2swf - image.py
##
##  $Id: image.py,v 1.2 2008/11/15 12:05:08 euske Exp $
##
##  Copyright (C) 2005 by Yusuke Shinyama (yusuke at cs . nyu . edu)
##  All Rights Reserved.
##
##  This is free software; you can redistribute it and/or modify
##  it under the terms of the GNU General Public License as published by
##  the Free Software Foundation; either version 2 of the License, or
##  (at your option) any later version.
##
##  This software is distributed in the hope that it will be useful,
##  but WITHOUT ANY WARRANTY; without even the implied warranty of
##  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##  GNU General Public License for more details.
##
##  You should have received a copy of the GNU General Public License
##  along with this software; if not, write to the Free Software
##  Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307,
##  USA.
##

import sys
from .util import lowerbound, upperbound, stderr
try:
    import pygame
    print('Using pygame', pygame.ver)
    pygame.init()
    try:
        pygame.mixer.quit()
    except NotImplementedError:
        pass

except ImportError:
    stderr('Pygame is required.')
    sys.exit(1)

#  format: 1: solid,
#          2: raw (uncompressed)
#          3: DefineBitLossless
#          4: SCREENVIDEOPACKET
IMG_SOLID = 1
IMG_RAW = 2
IMG_LOSSLESS = 3
IMG_VIDEOPACKET = 4


def bgr2rgb(data):
    return b''.join(
        [b'%d' % (data[i + 2] + data[i + 1] + data[i]) for i in range(0, len(data), 3)])

def imgsize(img):
    return img.get_size()

def create_image(w, h):
    return pygame.Surface((w, h), 0, 32)

def create_image_from_string_rgb(w, h, data):
    return pygame.image.fromstring(data, (w, h), 'RGB')

def create_image_from_string_rgbx(w, h, data):
    return pygame.image.fromstring(data, (w, h), 'RGBX')

def create_image_from_string_xrgb(w, h, data):
    return pygame.image.fromstring(data[1:] + 'x', (w, h), 'RGBX')

def create_image_from_string_argb(w, h, data):
    bdata = b''.join([
        b'%d' % (data[i + 1] + data[i + 2] + data[i + 3] + data[i])
        for i in range(0, len(data), 4)
    ])
    return pygame.image.fromstring(bdata, (w, h), 'RGBA')

def create_image_from_string_rgb_flipped(w, h, data):
    return pygame.image.fromstring(data, (w, h), 'RGB', 1)

def crop_image(img, dimension):
    assert len(dimension) == 4
    (x, y, w, h) = dimension
    (wm, hm) = img.get_size()
    return img.subsurface((x, y, upperbound(wm - x, w), upperbound(hm - y, h)))

def paste_image(dest, src, position):
    assert len(position) == 2
    return dest.blit(src, position)

def save_image(img, fname):
    if not fname.endswith('.bmp'):
        stderr(
            'Warning: this format not supported by pygame, raw rgb is used instead.'
        )
    return pygame.image.save(img, fname)

def convert_image_to_string_rgb_flipped(img):
    return pygame.image.tostring(img, 'RGB', 1)

def convert_image_to_string_rgb(img):
    return pygame.image.tostring(img, 'RGB')

def convert_image_to_string_xrgb(img):
    return pygame.image.tostring(img, 'ARGB')

def solid_fill(dest, rect, color):
    return dest.fill(color, rect)

def scale_image(img, scaling):
    # this might cause segmentation faults sometimes :(
    # In that case, use the following instead:
    #   (w,h) = img.get_size()
    #   return pygame.transform.scale(img, (int(w*scaling), int(h*scaling)))
    return pygame.transform.rotozoom(img, 0, scaling)
