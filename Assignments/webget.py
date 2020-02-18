import os
import urllib


def download(url, to=None):
    """Download a remote file specified by a URL to a 
    local directory.

    :param url: str
        URL pointing to a remote file.

    :param to: str
        Local path, absolute or relative, with a filename 
        to the file storing the contents of the remote file.
    """

    x = urllib.request.urlopen(url)
    print(x.read())

    # TODO: Implement me!
    pass