# ASTRA3D Desktop — Product & Engineering Plan

**Publisher:** ANISH ENTERPRISES  
**Product:** ASTRA3D Desktop  
**Base:** Blender upstream source  
**License:** GPL-3.0 derivative; preserve all upstream file-level notices and compatible licenses.

## Status

This fork contains the upstream Blender source. The initial ASTRA3D identity layer and a small application-template extension are being added. This is not yet a renamed binary, a completed visual redesign, or a production release.

## Product principles

1. Preserve Blender's proven native data model, file format, editor architecture, Python API, and rendering backends.
2. Make ASTRA3D identity additive and reviewable. Avoid mass search-and-replace across upstream source.
3. Keep upstream copyright, SPDX, third-party and trademark notices intact.
4. Ship product-specific behavior through isolated application templates, Python extensions, and narrowly scoped patches before changing core UI code.
5. Build and test on supported operating systems before claiming compatibility.

## Brand system

- Primary surfaces: deep graphite and charcoal.
- Accent: restrained warm orange for primary actions and selected states.
- Typography: preserve readable upstream UI typography; do not bundle unlicensed fonts.
- Product name: ASTRA3D Desktop.
- Publisher line: ANISH ENTERPRISES.
- Do not reuse Blender Foundation logos or imply official endorsement.

## Initial customization delivered in this branch

### ASTRA3D application template

Path: `scripts/startup/bl_app_templates_system/ASTRA3D/`

The template registers a focused ASTRA3D panel in the 3D Viewport sidebar. It provides:
- Save project.
- Pack external resources into the .blend file.
- Add a camera.
- Add common mesh primitives.
- Render the active frame.
- Display current scene, render engine, output resolution and frame.

The panel uses Blender's public Python API and does not alter core editor behavior or project data automatically.

## Roadmap

### Phase 1 — Foundation
- [x] Preserve the upstream fork and its history.
- [x] Add ASTRA3D product README and roadmap.
- [x] Add isolated ASTRA3D application template and quick-tools panel.
- [ ] Add automated Python syntax/import smoke test for the template using a built Blender executable.
- [ ] Build the unmodified upstream baseline on Windows, Linux and macOS.

### Phase 2 — Visual identity
- [ ] Design original ASTRA3D logo and icon assets.
- [ ] Create an ASTRA3D theme preset using supported theme APIs.
- [ ] Create branded splash and About artwork without Blender Foundation marks.
- [ ] Add installer, application metadata, file associations and product versioning.

### Phase 3 — Product workflows
- [ ] Project launcher and recent-project management.
- [ ] Guided workspace presets for modeling, sculpting, animation, VFX and rendering.
- [ ] Asset-library onboarding and reusable project templates.
- [ ] Non-destructive project packaging and dependency checks.

### Phase 4 — Enterprise and collaboration
- [ ] Optional account-backed asset sync and team collaboration service.
- [ ] Role-based project access and audit history in a separately maintained service.
- [ ] Organization policy controls and managed deployment.
- [ ] Offline-first behavior; cloud features must never be required for core editing.

### Phase 5 — Release engineering
- [ ] Reproducible build pipeline for supported platforms.
- [ ] License and third-party notices audit.
- [ ] Regression suite for startup, file load/save, rendering and extensions.
- [ ] Signed installers, update channel and release notes.

## Build and development

Follow the official Blender build handbook: https://developer.blender.org/docs/handbook/building_blender/

After cloning, initialize/update required dependencies using the upstream instructions (commonly `make update` on supported environments). The source repository alone is not a built application. Validate each Python customization against the exact Blender revision before packaging.

## Upstream maintenance

- Keep `upstream` pointing to https://github.com/blender/blender.git in local clones.
- Track the upstream default branch and record the base commit for every ASTRA3D patch series.
- Never force-push shared product branches without explicit coordination.
- Prefer small commits and upstream-compatible changes.
