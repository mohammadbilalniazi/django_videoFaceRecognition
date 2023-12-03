import pickle
import numpy as np
from pathlib import Path
import face_recognition
# from profiles.models import Profile
# from .utils import get_encoded_faces_profile

def classify_face(img):
    #1 way 
    faces_db=handle_face_db()
    #2 way
    # qs=Profile.objects.all()
    # faces_db={}
    # for p in qs:
    #     encoding = None
    #     face_encodings=encode_face(p.photo.path)

    #     if len(face_encodings)>0:
    #         encoding=face_encodings[0]
    #     else:
    #         print("No Face Found in Image")
    #     if encoding is not None:
    #         faces_db[p.user.username]=encoding
    #         data=handle_face_db('INSERT',encoding,p.user.username)

    faces_encoded=list(faces_db.values())
    known_face_names=list(faces_db.keys())
    #load input image
    img=face_recognition.load_image_file(img)
     
    try:
        face_locations=face_recognition.face_locations(img)
        unknown_face_encodings= face_recognition.face_encodings(img,face_locations)
        #identify faces in input image
        faces_names=[]
        # print("faces_encoded ",faces_encoded," known_face_names ",known_face_names," unknown_face_encodings ",unknown_face_encodings)
        for face_encoding in unknown_face_encodings:
            print("face_encoding len new face",len(face_encoding),"face_encoded")
            # print("faces_encoded ",faces_encoded)
            matches = face_recognition.compare_faces(faces_encoded,face_encoding)
            print("face_recognition.compare_face(faces_encoded,face_encoding) ",matches)
            face_distances=face_recognition.face_distance(faces_encoded,face_encoding)
            print("face_distances ",face_distances)
            best_match_index=np.argmin(face_distances)
            print("best_match_index ",best_match_index)
            if matches[best_match_index]:
                name=known_face_names[best_match_index]
            else:
                name="UnKnown"
            
            faces_names.append(name)
        return faces_names[0] # return the name of the first face in the input image
    except: 
        #if no faces are found in the input image or an error occured
        return False
    

def encode_face(img):
    face=face_recognition.load_image_file(img)
    face_encodings=face_recognition.face_encodings(face)
    return face_encodings

def handle_face_db(operation='GET',encoding=[],username=None):
    print("")
    database=Path("database.pickle")
    if not database.is_file():
        with open(database,'wb') as f:
            data={}
            data[username]=encoding
            pickle.dump(data,f)
    
    with open(database,'rb') as f1:
        data=pickle.load(f1)
        if operation=="INSERT":
            with open(database,'wb') as f2:
                data[username]=encoding
                pickle.dump(data,f2)
        return data
