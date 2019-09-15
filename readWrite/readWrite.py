import nuke


def create_read_from_write():
    """
    Create a read node from a selected write node
    return: None
    """

    selectedNode = nuke.selectedNode()
    if sel.Class() == "Write":
        read = nuke.createNode("Read")
        read.setXpos(int(selectedNode["xpos"].getValue()))
        read.setYpos(int(selectedNode["ypos"].getValue()+50))
        read["file"].setValue(selectedNode["file"].getValue())
        read["first"].setValue(int(nuke.Root()["first_frame"].getValue()))
        read["last"].setValue(int(nuke.Root()["last_frame"].getValue()))
        read["origfirst"].setValue(int(nuke.Root()["first_frame"].getValue()))
        read["origlast"].setValue(int(nuke.Root()["last_frame"].getValue()))
        read["colorspace"].setValue(int(selectedNode["colorspace"].getValue()))
