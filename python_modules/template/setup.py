from distutils.core import setup, Extension
from Cython.Build import cythonize
import numpy

setup(
        name="EXAMPLE",
        include_dirs=[numpy.get_include()],
        ext_modules=cythonize(Extension('EXAMPLE', sources=["EXAMPLE.pyx"], export_symbols=[
                'pluginStartup',
                'pluginisready',
                'getParamNum',
                'getParamConfig',
                'pluginFunction',
                'eventFunction',
                'spikeFunction',
                'setIntParam',
                'setFloatParam',
                'getIntParam',
                'getFloatParam'
        ]))
)
