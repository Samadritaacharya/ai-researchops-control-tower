# Interactive web design system

This web layer uses an original portfolio design language: dark editorial surfaces, restrained glass, oversized product typography, evidence-dense cards, and motion that explains system state.

## Reference translation
- Taste Skill v2: audit-first redesign, deliberate hierarchy, avoid generic template UI.
- awesome-design-md: record visual constraints explicitly and favor developer-tool precision over decorative chrome.
- React Three Fiber: declarative system map.
- ShaderGradient v2: low-density animated ambient field with capped pixel density.
- liquid-glass-js: visual reference only; CSS backdrop-filter is used because the upstream roadmap still includes React wrappers, accessibility, and performance/mobile work.
- liquid-logo: shader concept reference only; the center orb uses original GLSL displacement, moving bands, and Fresnel edges.

## Rules
1. Motion communicates state and honors reduced-motion preferences.
2. WebGL has a readable fallback.
3. No remote font, model key, database, analytics service, or paid API is required.
4. Synthetic data and deterministic behavior stay explicit.
5. The original Python application remains intact beside the web layer.

Deploy `frontend/` as the Vercel Root Directory. No environment variables are required.
