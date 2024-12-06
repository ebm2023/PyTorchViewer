- Requirements:

pytorch
viztracer

- Example Usage:

The goal is to be able to view PyTorch Profiler traces in VizViewer with PyTorch source code. 

The file example.py will generate a PyTorch Profiler trace file on an example piece of code. Run python example.py to generate the example trace file torchProfile.json

If we want to see PyTorch source code when we open this trace in VizViewer, run PyTorchViewer.py and provide the unmodified json as a command line argument.

For this example, run this command in terminal: python PyTorchViewer.py torchProfile.json

This will modify the existing json to add source code in a way that VizViewer can interpret, and save it in a new json file called profile_with_code.json

To view trace with VizViewer, run command: vizviewer profile_with_code.json