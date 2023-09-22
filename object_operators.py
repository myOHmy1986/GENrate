import bpy

# Create a new object.
bpy.ops.object.primitive_cube_add()

# Select the object.
bpy.ops.object.select_all(action='SELECT')

# Move the object.
bpy.ops.object.translate(value=(1.0, 0.0, 0.0))

# Delete the object.
bpy.ops.object.delete()
