import bpy

# Create a new node.
bpy.ops.node.new('ShaderNodeMath')

# Select the node.
bpy.ops.node.select()

# Connect the node to another node.
bpy.ops.node.link_append()

# Delete the node.
bpy.ops.node.delete()
