def time_convertor(seconds, time_format=0):
    """
    SEMANTICS : instead of converting the seconds in minutes outside, one can do it here.

    Args:
        seconds: runtime
        time_format:  0 is in seconds (no change), 1 is in min, 2 is in hour.

    Returns:
        converted time.

    """
    seconds_int = round(seconds)
    seconds_frac = seconds - seconds_int
    if time_format == 0:
        return seconds_int, seconds_frac
    else:
        m, s = divmod(seconds_int, 60)
        if time_format == 1:
            return s, m, seconds_frac
        else:
            h, m = divmod(m, 60)
            return s, m, h, seconds_frac


def time_text(s, m, h, seconds_frac=0):
    """
    SEMANTICS :

    Args:
        s:
        m:
        h:
        seconds_frac:

    Returns:

    """
    if s == 0:
        ts = ""
    elif s == 1:
        ts = f"{s + seconds_frac:d} second "
    else:
        ts = f"{s:d} seconds "

    if m == 0:
        tm = ""
    elif m == 1:
        tm = f"{m:d} minute "
    else:
        tm = f"{m:d} minutes "

    if h == 0:
        th = ""
    elif h == 1:
        th = f"{h:d} hour "
    else:
        th = f"{h:d} hours "

    if h == s and s == m and m == 0:
        ts = " {} second ".format(seconds_frac)
    return ts, tm, th


def time_computational(A, B, title="no title"):
    """ function that I put at the end of certain functions to know how long they runned.

    Args:
        A: beg simul's time.
        B: end simul's time.
        title: function or bookmark to recognize where from the time.

    Returns:

    """
    seconds = B - A
    beg = " Program : " + title + ", took roughly :"
    print(100 * '~')
    s, m, h, seconds_frac = time_convertor(seconds, time_format=2)
    ts, tm, th = time_text(s, m, h, seconds_frac)
    print(''.join([beg, th, tm, ts, 'to run.']))
    return