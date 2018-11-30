import os
import sys
from sacred import Experiment

ex_images = Experiment()


@ex_images.config
def default_config():
    batch_size = 32
    epochs = 80
    memory_units = 512
    pool_size = 2

    charset = 67  # a-zA-Z0-9,.- /
    line_width_padded = 535
    line_height_normalized = 64
    max_string_length = 7

    force_new = True


@ex_images.main
def run(batch_size, epochs, memory_units, pool_size, charset, line_width_padded, line_height_normalized,
        max_string_length, force_new):
    from src.handwritten_text_recognition.ocr.train.classifier_controller import Classifier
    from src.handwritten_text_recognition.ocr.train.data_generator import DataGenerator
    from src.handwritten_text_recognition.ocr.train.visualization_callback import VisualizationCallback
    from src.handwritten_text_recognition.config import get_path_to_model_dir_in_assets

    classifier = Classifier()
    image_paths, image_labels = classifier.load_dataset(Classifier.DATASET_TYP['cvl'])
    generator = DataGenerator(downsample_factor=(pool_size ** 2),
                              line_width_padded=line_width_padded,
                              line_height_normalized=line_height_normalized, max_string_length=max_string_length)
    generator.setup_training(image_paths=image_paths, image_labels=image_labels, batch_size=batch_size)

    model = classifier.define_model(charset=charset,
                                    line_height_normalized=line_height_normalized,
                                    memory_units=memory_units, pool_size=pool_size,
                                    line_width_padded=line_width_padded, max_string_length=max_string_length)

    if force_new is False:
        rnn_model = model.get_model()
        rnn_model.load_weights(get_path_to_model_dir_in_assets('cvl-80epochs.h5'))

    test_function = model.get_test_function()
    visualization_callback = VisualizationCallback(test_function, generator.generate_validation())

    classifier.train(generator, epochs, callbacks=[generator, visualization_callback], visualize=True)


if __name__ == '__main__':
    head, tail = os.path.split(os.path.join(os.path.abspath(__file__)))
    PACKAGE_DIR = os.path.join(head, '..{}..{}'.format(os.sep, os.sep))

    sys.path.insert(0, PACKAGE_DIR)

    ex_images.run_commandline()
