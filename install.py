import launch
import os

path = os.path.dirname(os.path.realpath(__file__))
req_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), "requirements.txt")



if not launch.is_installed("colorspacious"):
    launch.run_pip("install colorspacious", "colorspacious")

launch.git_clone("https://github.com/WuZongWei6/Pixelization.git", os.path.join(path, "pixelization"), "pixelization", "b7142536da3a9348794bce260c10e465b8bebcb8")

# we remove __init__ because it breaks BLIP - takes over the directory named models which BLIP also uses.
try:
    os.remove(os.path.join(path, "pixelization", "models", "__init__.py"))
except OSError as e:
    pass

with open(req_file) as file:
    for lib in file:
        lib = lib.strip()
        if not launch.is_installed(lib):
            launch.run_pip(f"install {lib}", f"Pixelization dithering requirement: {lib}")