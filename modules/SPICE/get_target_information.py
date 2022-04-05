import spiceypy
import utilities.time_conversion as time_conversion


# Sample implementation of all kernels

# PCK
def get_target_radii():
    """
    uses PCK kernel and bodvrd function to get the radii of the asteroid
    """

    radii = spiceypy.bodvrd('Bennu', 'RADII', 3)
    print(f"Bennu RADII: {radii}")


# SPK
def get_target_position(utc):
    """
    uses SPK kernel and spkpos function to get the position of spacecraft and asteroid in relation to each other
    """

    et = time_conversion.convert_utc_to_et(utc)

    state = spiceypy.spkpos('Bennu', et, 'IAU_BENNU', 'LT+S', 'OSIRIS-REx')
    [x, y, z] = state[0]

    print(f"X: {x} km\nY: {y} km\nZ: {z} km")


# CK/FK
def get_camera_attitude(utc):
    """
    uses FK and CK kernel
    """

    et = time_conversion.convert_utc_to_et(utc)

    boresight = [ 0.0, 0.0, 1.0 ] # +Z axis is the camera boresight

    """
    Target: Bennu
    Observer Epoch : et
    Reference Frame: ORX_OCAMS_POLYCAM
    Observing Body: OSIRIS-REx
    """
    state = spiceypy.spkpos('Bennu', et, 'ORX_OCAMS_POLYCAM', 'LT+S', 'OSIRIS-REx')
    print(state)

def get_image_vectors():
    pass
    # spiceypy.getfov()