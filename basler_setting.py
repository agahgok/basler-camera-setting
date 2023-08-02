from pypylon import pylon


tl_factory = pylon.TlFactory.GetInstance()
devices = tl_factory.EnumerateDevices()
if len(devices) == 0:
    print("No camera found.")
    exit(1)

camera = pylon.InstantCamera(tl_factory.CreateDevice(devices[0]))


camera.Open()
node_map = camera.GetNodeMap()

# Access the Digital I/O control settings
line_selector = node_map.GetNode("LineSelector")
if not line_selector:
    print("LineSelector node not found.")
    camera.Close()
    exit(1)

line_selector_value = line_selector.GetEntryByName("Line2")
if not line_selector_value:
    print("Line2 option not available for LineSelector.")
    camera.Close()
    exit(1)
line_selector.SetIntValue(line_selector_value.GetValue())

line_source = node_map.GetNode("LineSource")
if not line_source:
    print("LineSource node not found.")
    camera.Close()
    exit(1)

line_source_value = line_source.GetEntryByName("ExposureActive")
if not line_source_value:
    print("ExposureActive option not available for LineSource.")
    camera.Close()
    exit(1)
line_source.SetIntValue(line_source_value.GetValue())



camera.Close()
