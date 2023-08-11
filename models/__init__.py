#!/usr/bin/python3
"""
    Module models/__init__.py
    Initialize the FileStorage instance
"""

from .engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
