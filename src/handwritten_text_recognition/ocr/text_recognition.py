import numpy as np
from src.handwritten_text_recognition.config import get_path_to_model_dir_in_assets
from src.handwritten_text_recognition.ocr.model_container import ModelContainer
from src.handwritten_text_recognition.ocr.train.data_generator import DataGenerator
import src.handwritten_text_recognition.ocr.text_preprocessing as text_preprocessing


class TextRecognition(object):
    class __TextRecognition:
        def __init__(self, model_name='cvl-80epochs_prediction.h5'):
            self.model_data = {
                "line_width_padded": 535,
                "line_height_normalized": 64
            }

            self.model_container = ModelContainer()
            self.data_generator = DataGenerator()

            self._load_model(model_name)

        def _load_model(self, model_name):
            self.model_container.load_model(get_path_to_model_dir_in_assets(model_name))

        def recognize_text(self, image_array):
            image_array = text_preprocessing.process_image(image_array, self.model_data['line_height_normalized'])
            image_array = text_preprocessing.pad_sequence(image_array, self.model_data['line_height_normalized'],
                                                          self.model_data['line_width_padded'])

            batch_images = np.ones(
                [1, self.model_data['line_width_padded'], self.model_data['line_height_normalized'], 1])
            batch_images[0, 0:self.model_data['line_width_padded'], :, 0] = image_array

            if self.model_container.model is not None:
                self.model_container.predict(batch_images, self.data_generator)
            else:
                print("No model was chosen")

    instance = None

    def __new__(cls, *args, **kwargs):
        if not TextRecognition.instance:
            TextRecognition.instance = TextRecognition.__TextRecognition()
        return TextRecognition.instance

    def __getattr__(self, name):
        return getattr(self.instance, name)

    def __setattr__(self, name):
        return setattr(self.instance, name)
