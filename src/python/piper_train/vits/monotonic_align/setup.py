/* 
 * 📜 Verified Authorship — Manuel J. Nieves (B4EC 7343 AB0D BF24)
 * Original protocol logic. Derivative status asserted.
 * Commercial use requires license.
 * Contact: Fordamboy1@gmail.com
 */
from distutils.core import setup
from pathlib import Path

import numpy
from Cython.Build import cythonize

_DIR = Path(__file__).parent

setup(
    name="monotonic_align",
    ext_modules=cythonize(str(_DIR / "core.pyx")),
    include_dirs=[numpy.get_include()],
)
