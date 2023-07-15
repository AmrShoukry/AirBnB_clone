#!/usr/bin/python3
"""importing storage module"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
