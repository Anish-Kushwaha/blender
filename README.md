# ASTRA3D Desktop

**ASTRA3D Desktop by ANISH ENTERPRISES** is an independent desktop 3D creation product built as a derivative of the Blender project.

The goal is to develop a professional, extensible 3D production environment while preserving the mature upstream foundations for modeling, sculpting, geometry nodes, rigging, animation, simulation, rendering, compositing, motion tracking, and video editing.

> **Project status:** Early customization stage. This repository currently contains the upstream Blender source plus the initial ASTRA3D product identity and application-template layer. It is not yet a separately built or released ASTRA3D application.

## Product direction

- **Product:** ASTRA3D Desktop
- **Publisher:** ANISH ENTERPRISES
- **Interface direction:** graphite / charcoal surfaces with a restrained orange accent
- **Primary platform:** desktop (Windows, Linux, macOS, subject to upstream support)
- **Project format:** retain Blender's native `.blend` format for compatibility
- **Upstream:** [blender/blender](https://github.com/blender/blender)
- **Upstream documentation:** [Blender build handbook](https://developer.blender.org/docs/handbook/building_blender/)

## Product ecosystem

ASTRA3D is a **browser-first, cross-device** 3D creation platform. The browser Studio runs directly on phones, tablets, laptops and desktop browsers; this Blender-derived repository is the optional workstation companion for advanced desktop production. The browser Studio is maintained separately at [Anish-Kushwaha/ASTRA3D](https://github.com/Anish-Kushwaha/ASTRA3D). Browser projects will use a versioned ASTRA3D scene document and glTF 2.0 / GLB interchange where supported. Native `.blend` files remain desktop-native; the browser does not currently open them directly.

## What's included now

- Full upstream Blender source and history, maintained as a fork.
- An ASTRA3D application template at `scripts/startup/bl_app_templates_system/ASTRA3D`.
- An ASTRA3D quick-tools panel in the 3D Viewport sidebar for common project actions.
- Product and engineering roadmap in [`docs/ASTRA3D_DESKTOP.md`](docs/ASTRA3D_DESKTOP.md).

## Build

ASTRA3D Desktop uses Blender's upstream build system and dependency workflow. Start with the official [build instructions](https://developer.blender.org/docs/handbook/building_blender/). Do not treat a GitHub source checkout as a compiled application.

Typical dependency update step after cloning the repository and its submodules:

```bash
make update
```

Then follow the platform-specific build instructions in the handbook. Builds have not yet been validated for ASTRA3D branding changes.

## Upstream and licensing

ASTRA3D Desktop is a derivative work of Blender. Blender as a whole is distributed under the GNU General Public License, version 3; individual files may carry different but compatible licenses. Preserve upstream copyright notices, SPDX identifiers, third-party notices, and license files when modifying or redistributing the source.

- [Blender license information](https://www.blender.org/about/license/)
- [GNU GPL version 3](https://www.gnu.org/licenses/gpl-3.0.html)
- See `COPYING` and `doc/license/` in this repository.

ASTRA3D and ANISH ENTERPRISES are product identifiers of their respective owner. Blender is a project of the Blender Foundation; ASTRA3D is not an official Blender Foundation product and is not endorsed by the Foundation.

## Repository relationship

This desktop product is intentionally separate from the MIT-licensed ASTRA3D web platform: [Anish-Kushwaha/ASTRA3D](https://github.com/Anish-Kushwaha/ASTRA3D).

The Blender upstream remote should remain available as `upstream` in local Git checkouts. Keep product-specific changes in focused commits so they can be reviewed and rebased against upstream.
