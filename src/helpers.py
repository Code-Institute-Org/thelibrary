import os
import uuid


def get_unique_filename(instance, filename):
    """
    Take a filename and make it unique.
    Returns new file path into images folder
    with file name attached.
    Source: 
    https://stackoverflow.com/questions/2673647/enforce-unique-upload-file-names-using-django/2677474#2677474
    """
    name = filename.split('.')[0]
    ext = filename.split('.')[-1]
    filename = f"{name}-{uuid.uuid4()}.{ext}"
    return os.path.join(f"images/", filename)