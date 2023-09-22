import bpy

# Get the list of objects in the outliner.
objects = bpy.data.objects

# Select an object in the outliner.
objects.active = objects['Cube']

# Add an object to the outliner.
bpy.ops.outliner.object_add()

# Delete an object from the outliner.
bpy.ops.outliner.object_delete()