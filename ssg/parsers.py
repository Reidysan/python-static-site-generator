from copy import copy
from distutils import extension
from importlib.resources import path
from typing import List
from pathlib import Path
import shutil

class Parser:
    extensions: List[str] = []

    def valid_extension(self, extension):
        return extension in self.extensions

    def parse(path, source, dest) -> Path:
        raise NotImplementedError
    
    def read(path):
        with open(path) as file:
            return file.read()
    
    def write(self, path, dest, content, ext=".html"):
        full_path = dest / path.with_suffix(ext).name
        with open(full_path) as file:
            content.write(file)

    def copy(self, path, source, dest):
        shutil.copy2(path, dest / source)

class ResourceParser(Parser):
    extensions = ".jpg", ".png", ".gif", ".css", ".html"
    def parse(path, source, dest):
        copy(path, source, dest)
