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
The ground truth should be named according to the corresponding image and should have the *.txt*-extension.

```python
python src/handwritten_text_recognition/train.py with folder_containing_training_samples
```

Predict unseen text
----

You can use the following function to predict text:
The module 'src/handwritten_text_recognition/ocr/text_recognition.py' contains a function called 'recognize_text' which takes a line image and predicts the text.


To-Do
----

- [ ] Tests
- [ ] GPU support
- [ ] Post-correction

Note
====

This project has been set up using PyScaffold 3.0. For details and usage
information on PyScaffold see http://pyscaffold.readthedocs.org/.
