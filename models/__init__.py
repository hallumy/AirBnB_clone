"""Creates a unique file instance
for the application
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
