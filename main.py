import face_recognition
import os
import shutil

def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"): # add more extensions if needed
            img_path = os.path.join(folder, filename)
            images.append(img_path)
    return images

def recognize_faces(reference_image_path, folder_path, output_folder, tolerance=0.5):

    reference_image = face_recognition.load_image_file(reference_image_path)
    reference_encoding = face_recognition.face_encodings(reference_image)[0]

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    images = load_images_from_folder(folder_path)

    for image_path in images:
        unknown_image = face_recognition.load_image_file(image_path)
        unknown_encodings = face_recognition.face_encodings(unknown_image)

        if unknown_encodings:
            results = face_recognition.compare_faces(unknown_encodings, reference_encoding, tolerance=tolerance)

            if True in results:
                shutil.copy(image_path, output_folder)
                print(f"Match found: {image_path}")
            else:
                print(f"No match: {image_path}")
        else:
            print(f"No faces found in {image_path}")

# Folder Names
reference_image_path = "./test.jpg"
folder_path = "./input"
output_folder = "./output"

recognize_faces(reference_image_path, folder_path, output_folder)
