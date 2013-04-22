import subprocess
import gtk.gdk
from tempfile import NamedTemporaryFile


def screenshot_to_gimp():
    ''' Takes a screenshot of the entire screen and opens it in gimp '''
    w = gtk.gdk.get_default_root_window()
    sz = w.get_size()
    pb = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB, False,8,sz[0],sz[1])
    pb = pb.get_from_drawable(w,w.get_colormap(),0,0,0,0,sz[0],sz[1])
    
    f = NamedTemporaryFile(delete=False)
    pb.save_to_callback(f.write, 'png')
    filename = f.name
    f.close()
    subprocess.Popen(['gimp', filename])
    

if __name__ == '__main__':
    screenshot_to_gimp()
    