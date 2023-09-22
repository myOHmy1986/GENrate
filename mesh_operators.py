import bpy

# Create a new mesh.
bpy.ops.mesh.primitive_cube_add()

# Select the mesh.
bpy.ops.object.select_all(action='SELECT')

# Subdivide the mesh.
bpy.ops.mesh.subdivide()

# Delete the mesh.
bpy.ops.object.delete()
