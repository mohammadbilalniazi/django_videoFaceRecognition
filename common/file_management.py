
# Create your models here.
def delete_file(obj,file_field,message=None):
    ok=False
    message=""
    if hasattr(obj,file_field):
        file_to_be_deleted=getattr(obj,file_field)
        import os
        import pathlib
        from django.conf import settings
        complete_path_file=pathlib.PurePath(settings.MEDIA_ROOT,pathlib.Path(file_to_be_deleted.name))
        if os.path.exists(complete_path_file):
            os.remove(complete_path_file)
            ok=True
            message="file deleted"
        else:
            ok=False
            message="file not exists in storage"
    else:
        ok=False
        message="object has no file"
    return (ok,message)
