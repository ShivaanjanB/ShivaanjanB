"""Generate assets/header.svg: an animated profile banner.

Slow wireframe waves drift in the background (CSS, paused for reduced motion) and a
monospace line types out three phrases in turn (SMIL, which GitHub's image proxy keeps).
Run: python assets/make_header.py
"""
import math
from pathlib import Path

W, H = 1000, 220
PHRASES = [
    "data pipelines that are tested and monitored",
    "LLM systems checked before anyone trusts them",
    "finance data, London, open to graduate roles",
]
FONT_SIZE = 21
CHAR_W = 12.6           # textLength forces each glyph to this width, so the reveal is exact
X0, Y_TYPE = 92, 168
TYPE_S, ERASE_S = 0.045, 0.012   # seconds per character
HOLD_S, GAP_S = 2.4, 0.35


def wave_path(amplitude, period, baseline, phase=0.0):
    """A sine wave twice the banner's width, so shifting it by W loops seamlessly."""
    pts = [
        f"{x},{baseline + amplitude * math.sin(2 * math.pi * x / period + phase):.1f}"
        for x in range(0, 2 * W + 1, 10)
    ]
    return "M" + " L".join(pts)


# Build the typing timeline: (time, phrase index, characters shown).
events, t = [], 0.0
for i, phrase in enumerate(PHRASES):
    n = len(phrase)
    for k in range(1, n + 1):
        events.append((t + k * TYPE_S, i, k))
    t += n * TYPE_S + HOLD_S
    for k in range(n - 1, -1, -1):
        events.append((t + (n - k) * ERASE_S, i, k))
    t += n * ERASE_S + GAP_S
CYCLE = t


def discrete_animate(attr, series):
    """series: [(time, value)] starting at time 0; values hold until the next time."""
    key_times = ";".join(f"{s / CYCLE:.5f}" for s, _ in series)
    values = ";".join(f"{v:.1f}" for _, v in series)
    return (
        f'<animate attributeName="{attr}" dur="{CYCLE:.2f}s" repeatCount="indefinite" '
        f'calcMode="discrete" keyTimes="{key_times}" values="{values}"/>'
    )


clips, texts = [], []
cursor_series = [(0.0, X0)]
for i, phrase in enumerate(PHRASES):
    series = [(0.0, 0.0)] + [(s, k * CHAR_W) for s, j, k in events if j == i]
    cursor_series += [(s, X0 + k * CHAR_W) for s, j, k in events if j == i]
    clips.append(
        f'<clipPath id="c{i}"><rect x="{X0}" y="{Y_TYPE - 26}" width="0" height="36">'
        f"{discrete_animate('width', series)}</rect></clipPath>"
    )
    texts.append(
        f'<text x="{X0}" y="{Y_TYPE}" clip-path="url(#c{i})" class="mono" '
        f'textLength="{len(phrase) * CHAR_W:.1f}" lengthAdjust="spacingAndGlyphs">{phrase}</text>'
    )
cursor_series.sort()

waves = [
    # amplitude, period, baseline, phase, seconds per loop, opacity
    (14, 250, 70, 0.0, 26, 0.18),
    (20, 500, 118, 1.3, 38, 0.14),
    (10, 200, 160, 2.1, 22, 0.12),
    (26, 1000, 196, 0.6, 48, 0.16),
]
wave_svg = "".join(
    f'<g class="drift" style="animation-duration:{dur}s"><path d="{wave_path(a, p, b, ph)}" '
    f'stroke-opacity="{op}"/></g>'
    for a, p, b, ph, dur, op in waves
)

svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="Rishi (Shivaanjan) Bhattacharjee, Graduate Data and AI Engineer in London">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#0B1220"/>
      <stop offset="1" stop-color="#14304F"/>
    </linearGradient>
    <clipPath id="frame"><rect width="{W}" height="{H}" rx="16"/></clipPath>
    {''.join(clips)}
  </defs>
  <style>
    .drift {{ animation: drift linear infinite; }}
    .drift path {{ fill: none; stroke: #7CC4F0; stroke-width: 1.4; }}
    @keyframes drift {{ from {{ transform: translateX(0); }} to {{ transform: translateX(-{W}px); }} }}
    .eyebrow {{ font: 600 14px 'Segoe UI', 'Helvetica Neue', Arial, sans-serif; letter-spacing: 3px; fill: #5FD3B8; }}
    .name {{ font: 700 42px 'Segoe UI', 'Helvetica Neue', Arial, sans-serif; fill: #F5F7FA; }}
    .mono {{ font: {FONT_SIZE}px Consolas, 'Courier New', monospace; fill: #D7E3F0; }}
    .prompt {{ font: 700 {FONT_SIZE}px Consolas, 'Courier New', monospace; fill: #5FD3B8; }}
    .cursor {{ fill: #5FD3B8; animation: blink 1s steps(1) infinite; }}
    @keyframes blink {{ 50% {{ opacity: 0; }} }}
    @media (prefers-reduced-motion: reduce) {{ .drift, .cursor {{ animation: none; }} }}
  </style>
  <g clip-path="url(#frame)">
    <rect width="{W}" height="{H}" fill="url(#bg)"/>
    {wave_svg}
    <text x="60" y="58" class="eyebrow">GRADUATE DATA &amp; AI ENGINEER · LONDON</text>
    <text x="60" y="112" class="name">Rishi (Shivaanjan) Bhattacharjee</text>
    <text x="60" y="{Y_TYPE}" class="prompt">&gt;</text>
    {''.join(texts)}
    <rect class="cursor" x="{X0}" y="{Y_TYPE - 19}" width="11" height="24">{discrete_animate('x', cursor_series)}</rect>
  </g>
</svg>
"""

out = Path(__file__).with_name("header.svg")
out.write_text(svg, encoding="utf-8")
print(f"wrote {out} ({len(svg) // 1024} KB, cycle {CYCLE:.1f}s)")
