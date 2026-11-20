# SPDX-FileCopyrightText: 2026 ANISH ENTERPRISES
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""ASTRA3D Desktop application-template customization.

This template adds a compact project quick-tools panel to the 3D Viewport.
It intentionally relies only on Blender's public Python API and leaves the
underlying scene untouched until the user activates an operator.
"""

import bpy


class ASTRA3D_PT_project_tools(bpy.types.Panel):
    """Quick actions for an ASTRA3D project."""

    bl_label = "ASTRA3D Project"
    bl_idname = "ASTRA3D_PT_project_tools"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "ASTRA3D"

    def draw(self, context):
        layout = self.layout
        scene = context.scene

        project = layout.box()
        project.label(text="Project", icon="FILE_BLEND")
        project.operator("wm.save_as_mainfile", text="Save Project", icon="FILE_TICK")
        project.operator("file.pack_all", text="Pack External Resources", icon="PACKAGE")

        creation = layout.box()
        creation.label(text="Create", icon="OUTLINER_OB_MESH")
        row = creation.row(align=True)
        row.operator("mesh.primitive_cube_add", text="Cube")
        row.operator("mesh.primitive_uv_sphere_add", text="Sphere")
        creation.operator("object.camera_add", text="Add Camera", icon="CAMERA_DATA")

        output = layout.box()
        output.label(text="Render", icon="RENDER_STILL")
        output.label(text=f"Engine: {scene.render.engine}")
        output.label(
            text=f"Resolution: {scene.render.resolution_x} × "
            f"{scene.render.resolution_y}"
        )
        output.label(
            text=f"Frame: {scene.frame_current} / {scene.frame_end}"
        )
        output.operator("render.render", text="Render Frame", icon="RENDER_STILL")


classes = (
    ASTRA3D_PT_project_tools,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
