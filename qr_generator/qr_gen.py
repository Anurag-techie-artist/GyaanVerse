import hashlib
import os
import qrcode

def generator(course_id, user_id):
    # Hash user ID
    user_id_data = str(user_id)
    user_hash_dig = hashlib.sha256(user_id_data.encode()).hexdigest()

    # Hash course ID
    course_id_data = str(course_id)
    course_hash_dig = hashlib.sha256(course_id_data.encode()).hexdigest()

    # Generate QR Code
    qr = qrcode.QRCode(version=4, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=3)
    qr_data = f"/attendance/selfattendance/{user_hash_dig}/{course_hash_dig}"
    qr.add_data(qr_data)
    qr.make(fit=True)
    img = qr.make_image()

    # Define save directory
    save_dir = "static/qr_codes"
    os.makedirs(save_dir, exist_ok=True)  # ✅ Create directory if it doesn't exist

    # Define save location
    save_location = os.path.join(save_dir, f"{user_id}_{course_id}_qrcode.png")
    img.save(save_location)  # ✅ Save QR Code

    return os.path.relpath(save_location, "static")  # ✅ Return relative path for use in Flask
