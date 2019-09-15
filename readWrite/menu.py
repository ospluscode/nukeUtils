import nuke
import readWrite

# add the command to the menu; also a hot key
nuke.menu("Nuke").addCommand("utilities/create read from write", "readWrite.create_read_from_write()", "alt+l")
