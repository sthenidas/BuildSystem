

import os

#### Conan Build steps ####

os.system("conan install . --output-folder=build --build=missing")

#### Meson Build steps #####

os.system("meson setup build --native-file build/conan_meson_native.ini")
os.system("meson compile -C build")

src = "build/demo"
dst = "demo"
os.symlink(src,dst)

