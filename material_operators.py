import bpy

# Create a new material.
bpy.ops.material.new()

# Select the material.
bpy.ops.material.select()

# Assign the material to the active object.
bpy.ops.object.material_slot_add()

# Delete the material.
bpy.ops.material.delete()