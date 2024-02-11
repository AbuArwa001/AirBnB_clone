#!/usr/bin/python3
"""
Module that imports  cmd module:
    console Starting point
"""

from .engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
