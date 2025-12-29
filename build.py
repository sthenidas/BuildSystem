

import os

#### Conan Build steps ####

os.system("conan install . --output-folder=build --build=missing")

#### Meson Build steps #####

os.chdir("build")
os.system("meson setup --native-file conan_meson_native.ini .. meson-src")
os.system("meson compile -C meson-src")

os.chdir("..")
src = "build/meson-src/demo"
dst = "demo"
os.symlink(src,dst)

