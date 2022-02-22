import spiceypy

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

    et = spiceypy.str2et(utc)

    state = spiceypy.spkpos('Bennu', et, 'IAU_BENNU', 'LT+S', 'OSIRIS-REx')
    [x, y, z] = state[0]

    print(f"X: {x} km\nY: {y} km\nZ: {z} km")


# CK
# spiceypy.ckobj()