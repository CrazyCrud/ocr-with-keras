============================
OCR with Keras
============================


This project shows a simple (and unfinished) example of using Keras to recognize text in digitized documents.


Description
===========

No layout segmentation is down in this project...

Training with CVL-Dataset
----

You can download the CVL-Dataset here: https://cvl.tuwien.ac.at/research/cvl-databases/icdar2013-handwritten-digit-and-digit-string-recognition-competition/

Unpack the images in */handwritten_text_recognition/assets/cvl_dataset*

In the project root folder run: 
``python src/handwritten_text_recognition/train.py``

Training with custom dataset
----

Be careful that the images and the corresponding ground truth are located in the same folder.
The ground truth should have the filename of the corresponding image and the *.txt*-extension.

To-Do
----

- [ ] Tests
- [ ] GPU support
- [ ] Post-correction

Note
====

This project has been set up using PyScaffold 3.0. For details and usage
information on PyScaffold see http://pyscaffold.readthedocs.org/.
