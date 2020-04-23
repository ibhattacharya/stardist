from __future__ import absolute_import, print_function

from .model2d import Config2D, StarDist2D, StarDistData2D
from .model3d import Config3D, StarDist3D, StarDistData3D
from .pretrained import register_model, register_aliases

from csbdeep.utils import backend_channels_last
import keras.backend as K
if not backend_channels_last():
    raise NotImplementedError(
        "Keras is configured to use the '%s' image data format, which is currently not supported. "
        "Please change it to use 'channels_last' instead: "
        "https://keras.io/getting-started/faq/#where-is-the-keras-configuration-file-stored" % K.image_data_format()
    )
del backend_channels_last, K

# register pre-trained models (TODO: replace with updatable solution)
register_model(StarDist2D,   '2D_dsb2018', 'https://cloud.mpi-cbg.de/index.php/s/1k5Zcy7PpFWRb0Q/download?path=/paper&files=2D_dsb2018.zip', '6287bf283f85c058ec3e7094b41039b5')
register_model(StarDist2D,   '2D_demo',    'https://cloud.mpi-cbg.de/index.php/s/1k5Zcy7PpFWRb0Q/download?path=/examples&files=2D_demo.zip', '31f70402f58c50dd231ec31b4375ea2c')
register_model(StarDist3D,   '3D_demo',    'https://cloud.mpi-cbg.de/index.php/s/1k5Zcy7PpFWRb0Q/download?path=/examples&files=3D_demo.zip', 'f481c16c1ee9f28a8dcfa1e7aae3dc83')
# register aliases (if any)
register_aliases(StarDist2D, '2D_dsb2018', 'DSB 2018 (from StarDist 2D paper)')
