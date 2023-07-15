#!/usr/bin/python3
"""importing storage module"""
from models.engine import file_storage

storage = file_storage.FileStorage()
storage.reload()
