import os
import tempfile

filename = tempfile.mkdtemp(".doc")
open (filename, "w").write("hellllllllllllllllllllllllllo!")

os.startfile(filename, "print")