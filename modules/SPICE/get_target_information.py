import spiceypy

# PCK
def get_target_radii():
    radii = spiceypy.bodvrd('Bennu', 'RADII', 3)
    print(f"Bennu RADII: {radii}")


# SPK
def get_target_position(utc):
    # utctim = input('Input UTC Time: ')
    # print('Converting UTC Time: {:s}'.format(utctim))
    et = spiceypy.str2et(utc)
    # print('ET seconds past J2000: {:16.3f}'.format(et))

    state = spiceypy.spkpos('Bennu', et, 'J2000', 'LT+S', 'OSIRIS-REx')
    [x, y, z] = state[0]

    print(f"X: {x} km\nY: {y} km\nZ: {z} km")
