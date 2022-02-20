import spiceypy

# LSK - The leapseconds kernel is used in conversions between ephemeris time (ET/TDB) and Coordinated Universal Time (UTC)
# SCLK - The spacecraft clock kernel is used in conversions between spacecraft clock time (SCLK) and ephemeris time (ET/TDB).

# ET -> UTC
def convert_et_to_utc(et):
    """
    Convert an input time from ephemeris seconds past J2000
    to Calendar, Day-of-Year, or Julian Date format, UTC.

    https://naif.jpl.nasa.gov/pub/naif/toolkit_docs/C/cspice/et2utc_c.html

    :param et: Input epoch, given in ephemeris seconds past J2000.
    :return: Output time string in UTC
    """

    return spiceypy.et2utc(et)

# UTC -> ET
def convert_utc_to_et(utc_epoch):
    """
    Convert a string representing an epoch to a double precision
    value representing the number of TDB seconds past the J2000
    epoch corresponding to the input epoch.

    https://naif.jpl.nasa.gov/pub/naif/toolkit_docs/C/cspice/str2et_c.html

    :param time: A string representing an epoch.
    :return: The equivalent value in seconds past J2000, TDB.
    """

    return spiceypy.str2et(utc_epoch)

# SCLK -> ET
def convert_sclk_to_et(sclk, spacecraft_code):
    """
    Convert a spacecraft clock string to ephemeris seconds past J2000 (ET).

    https://naif.jpl.nasa.gov/pub/naif/toolkit_docs/C/cspice/scs2e_c.html

    :param sclk: An SCLK string.
    :param spacecraft_code: NAIF integer code for a spacecraft.
    :return: Ephemeris time, seconds past J2000.
    """

    return spiceypy.scs2e(spacecraft_code, sclk)

# ET -> SCLK
def convert_et_to_sclk(et, spacecraft_clock_code):
    """
    Convert an epoch specified as ephemeris seconds past J2000 (ET) to a
    character string representation of a spacecraft clock value (SCLK).

    https://naif.jpl.nasa.gov/pub/naif/toolkit_docs/C/cspice/sce2s_c.html

    :param spacecraft_clock_code: NAIF spacecraft clock ID code.
    :param et: Ephemeris time, specified as seconds past J2000.
    :return: An SCLK string.
    """
    
    return spiceypy.sce2s(spacecraft_clock_code, et)