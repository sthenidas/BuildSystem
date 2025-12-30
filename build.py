import os

#### Conan Build steps ####
# forcing this makes it overwrite previous profiles, not best practice
os.system("conan profile detect --force")
os.system("conan install . --output-folder=build --build=missing")

#### Meson Build steps #####
os.system("meson setup build --native-file build/conan_meson_native.ini")
os.system("meson compile -C build")

try:
    os.system("rm demo")
except Exception as e:
    print(e)


# Find where Conan installed MoltenVK
def find_moltenvk_icd():
    conan_dir = os.path.expanduser("~/.conan2")

    if not os.path.exists(conan_dir):
        return None

    for root, dirs, files in os.walk(conan_dir):
        if "MoltenVK_icd.json" in files:
            return os.path.join(root, "MoltenVK_icd.json")

    return None


# Usage
icd_path = find_moltenvk_icd()
if icd_path:
    print(f"Found: {icd_path}")
    os.environ["VK_ICD_FILENAMES"] = icd_path
else:
    print("MoltenVK ICD not found")
print(icd_path)


src = "build/demo"
dst = "demo"
os.symlink(src, dst)
