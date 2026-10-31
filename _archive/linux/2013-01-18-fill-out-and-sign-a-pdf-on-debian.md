---
title: "fill out and sign a PDF on debian"
category: linux
---

1. fill out form with xournal and export pdf.  (oowriter didn't read xournal's output even with the libreoffice pdf import extension, but the xournal'd pdf did print, gimp was able to read it, and it was emailable)
2. edit a photo of signature in gimp (nice video [http://youtu.be/efAOsvfi4sU](http://youtu.be/efAOsvfi4sU))
    1. layer/transparency/add alpha channel.  like writing on an overhead slide, the checkerboard represents the background through the slide
    2. use fuzzy select tool from toolbox to select the background from the photo
    3. delete the background, should see checkerboard.  delete within loops for O, Q, etc.
    4. from brushes, select the largest black brush and set mode to overlay.  brush over the signature to darken it  to a uniform black, otherwise it looks grayish like a photo when printed.
    5. open the pdf from gimp and select the page which needs the signature
    6. use the rectangle select tool to select the area where the signature should go.  note the height and/or width of the field.
    7. go to the signature image and image/scale image.  enter either the height or width to scale to, then\`edit/copy visible.
    8. go back to the pdf and right click on the rectangle and paste.
    9. export the page to pdf
3. use pdfshuffler to replace the unsigned page with the signed page in the PDF in order.  may need pdfshuffler orig sign orig (wasn't able to move later pages to earlier ones, but was able to delete pages).
