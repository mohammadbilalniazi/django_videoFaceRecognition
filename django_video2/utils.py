# from profiles.models import Profile
from .face import encode_face,handle_face_db

    

def get_encoded_faces_table(qs,field=None,row_id="all",store_in_pickle=True):
    # qs="{}.objects.all()".format(table)
    # qs=eval(qs)
    # qs=Profile.objects.all()
    face_data={}

    for p in qs:
        encoding = None
        face_encodings=encode_face(p.photo.path)

        if len(face_encodings)>0:
            encoding=face_encodings[0]
        else:
            print("No Face Found in Image")
        if encoding is not None:
            face_data[p.user.username]=encoding
            if store_in_pickle:
                data=handle_face_db('INSERT',encoding,p.user.username)
    return face_data # return dictionary of encoded faces
    
