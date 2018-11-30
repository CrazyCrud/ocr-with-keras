from src.handwritten_text_recognition.document_preprocessing.document_binarization.document_binarization import \
    DocumentBinarization
from src.handwritten_text_recognition.document_preprocessing.document_normalization.document_normalization import \
    DocumentNormalization


class DocumentPreprocessing:
    def __init__(self):
        self.binarization = DocumentBinarization()
        self.normalization = DocumentNormalization()

    def binarize(self):
        self.binarization.binarize()
