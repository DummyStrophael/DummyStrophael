#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
构建 DummyStrophael 主页所需的全部 SVG 素材（未来科技 / 霓虹赛博风）。

用法：
    python build_assets.py

所有文案、配色、技能标签都集中在这个文件里，改完重新运行即可。
生成结果会写入 ./assets/
"""
from __future__ import annotations

import math
import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
ASSETS = HERE / "assets"
ASSETS.mkdir(exist_ok=True)

# ── 配色 ──────────────────────────────────────────────────────────────────
VOID = "#05060B"
PANEL = "#0A0A12"
EDGE = "#1B2333"
CYAN = "#22D3EE"
MINT = "#7DF9FF"
VIOLET = "#A78BFA"
CRIMSON = "#FF2D55"
TEXT = "#E6EDF3"
MUTED = "#8B97AB"

MONO = "'Cascadia Mono','JetBrains Mono',Consolas,'SF Mono',Menlo,monospace"
SANS = "'Segoe UI',Inter,system-ui,-apple-system,'PingFang SC','Microsoft YaHei',sans-serif"

# ── 可改文案 ──────────────────────────────────────────────────────────────
USER = "DummyStrophael"
ROLE = "creative developer"
TAGLINE = "a good man"
MISSION = "turn caffeine into clean code — ship, learn, repeat"
STACK = [
    ["C", "C++", "Python", "TypeScript", "JavaScript", "Linux"],
    ["Docker", "Git", "Bash", "CMake", "VS Code", "GitHub"],
]
PROJECTS = [
    dict(
        index="01",
        name="TASKS",
        desc=["极客考核 · 任务与笔记", "Assessment tasks, written down."],
        meta="MARKDOWN",
        status="LIVE",
        accent=CYAN,
        file="project-tasks.svg",
    ),
    dict(
        index="02",
        name="NEXT_PROJECT",
        desc=["这个位置留给下一个项目", "Awaiting deployment."],
        meta="QUEUED",
        status="SOON",
        accent=VIOLET,
        file="project-slot.svg",
        slot=True,
    ),
]
BADGES = [
    dict(file="badge-status.svg", label="STATUS", value="ONLINE", accent=CYAN),
    dict(file="badge-email.svg", label="EMAIL", value="2350645758@qq.com", accent=CRIMSON),
    dict(file="badge-github.svg", label="GITHUB", value="DummyStrophael", accent=VIOLET),
]


def head(w: int, h: int, title: str) -> str:
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
        f'viewBox="0 0 {w} {h}" fill="none" role="img" aria-label="{title}">\n'
        f"<title>{title}</title>\n"
    )


def save(name: str, body: str) -> None:
    (ASSETS / name).write_text(body, encoding="utf-8")
    print(f"  [ok] assets/{name} ({len(body)} chars)")


# ══════════════════════════════════════════════════════════════════════════
#  01 · HERO
# ══════════════════════════════════════════════════════════════════════════
def hero() -> None:
    W, H = 1280, 360
    CX, CY = 1082, 178
    rnd = random.Random(2026)

    # ── 轨道刻度
    ticks = []
    for i in range(48):
        a = math.radians(i * 7.5)
        r1, r2 = (86, 96) if i % 6 else (80, 96)
        x1, y1 = r1 * math.cos(a), r1 * math.sin(a)
        x2, y2 = r2 * math.cos(a), r2 * math.sin(a)
        major = i % 6 == 0
        ticks.append(
            f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
            f'stroke="{CYAN}" stroke-opacity="{0.55 if major else 0.2}" '
            f'stroke-width="{1.4 if major else 1}"/>'
        )
    ticks = "".join(ticks)

    # ── 漂浮粒子
    particles = []
    for _ in range(28):
        px = rnd.uniform(16, W - 16)
        py = rnd.uniform(36, H - 6)
        pr = rnd.uniform(0.7, 1.9)
        col = rnd.choice([CYAN, VIOLET, "#FFFFFF", CRIMSON])
        dur = rnd.uniform(9, 20)
        begin = -rnd.uniform(0, dur)
        peak = rnd.uniform(0.18, 0.6)
        particles.append(
            f'<circle cx="{px:.1f}" cy="{py:.1f}" r="{pr:.1f}" fill="{col}">'
            f'<animate attributeName="cy" values="{py:.1f};{py - 120:.1f}" '
            f'dur="{dur:.1f}s" begin="{begin:.1f}s" repeatCount="indefinite"/>'
            f'<animate attributeName="opacity" values="0;{peak:.2f};0" dur="{dur:.1f}s" '
            f'begin="{begin:.1f}s" repeatCount="indefinite"/></circle>'
        )
    particles = "".join(particles)

    orbits = "".join(
        f'<circle cx="0" cy="0" r="{r}" stroke="{c}" stroke-opacity=".35" '
        f'stroke-width="1" stroke-dasharray="{d}"/>'
        for r, c, d in ((96, CYAN, "2 9"), (82, CRIMSON, "26 12"), (64, VIOLET, "3 7"))
    )

    body = f"""<defs>
  <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="#05060B"/>
    <stop offset=".55" stop-color="#0B0714"/>
    <stop offset="1" stop-color="#05060B"/>
  </linearGradient>
  <linearGradient id="titleGrad" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="#FFFFFF"/>
    <stop offset=".32" stop-color="#7DF9FF"/>
    <stop offset=".66" stop-color="#A78BFA"/>
    <stop offset="1" stop-color="#FF2D55"/>
  </linearGradient>
  <linearGradient id="hair" x1="0" y1="0" x2="1280" y2="0" gradientUnits="userSpaceOnUse">
    <stop offset="0" stop-color="{CYAN}" stop-opacity="0"/>
    <stop offset=".45" stop-color="{CYAN}" stop-opacity=".8"/>
    <stop offset=".55" stop-color="{CRIMSON}" stop-opacity=".8"/>
    <stop offset="1" stop-color="{CRIMSON}" stop-opacity="0"/>
  </linearGradient>
  <linearGradient id="sweep" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="{MINT}" stop-opacity="0"/>
    <stop offset=".5" stop-color="{MINT}" stop-opacity=".09"/>
    <stop offset="1" stop-color="{MINT}" stop-opacity="0"/>
  </linearGradient>
  <radialGradient id="glowCrimson" cx="50%" cy="50%" r="50%">
    <stop offset="0" stop-color="{CRIMSON}" stop-opacity=".26"/>
    <stop offset="1" stop-color="{CRIMSON}" stop-opacity="0"/>
  </radialGradient>
  <radialGradient id="glowCyan" cx="50%" cy="50%" r="50%">
    <stop offset="0" stop-color="{CYAN}" stop-opacity=".22"/>
    <stop offset="1" stop-color="{CYAN}" stop-opacity="0"/>
  </radialGradient>
  <radialGradient id="glowViolet" cx="50%" cy="50%" r="50%">
    <stop offset="0" stop-color="{VIOLET}" stop-opacity=".18"/>
    <stop offset="1" stop-color="{VIOLET}" stop-opacity="0"/>
  </radialGradient>
  <radialGradient id="core" cx="50%" cy="45%" r="55%">
    <stop offset="0" stop-color="#FFFFFF"/>
    <stop offset=".35" stop-color="{MINT}"/>
    <stop offset=".75" stop-color="{CYAN}" stop-opacity=".55"/>
    <stop offset="1" stop-color="{VIOLET}" stop-opacity="0"/>
  </radialGradient>
  <radialGradient id="vignette" cx="50%" cy="46%" r="72%">
    <stop offset=".35" stop-color="{VOID}" stop-opacity="0"/>
    <stop offset=".78" stop-color="{VOID}" stop-opacity=".55"/>
    <stop offset="1" stop-color="{VOID}" stop-opacity="1"/>
  </radialGradient>
  <pattern id="grid" width="48" height="48" patternUnits="userSpaceOnUse">
    <path d="M48 0H0V48" stroke="{CYAN}" stroke-opacity=".07" stroke-width="1"/>
  </pattern>
  <pattern id="gridBig" width="192" height="192" patternUnits="userSpaceOnUse">
    <path d="M192 0H0V192" stroke="{VIOLET}" stroke-opacity=".08" stroke-width="1"/>
  </pattern>
  <pattern id="scan" width="4" height="4" patternUnits="userSpaceOnUse">
    <rect width="4" height="1" fill="#FFFFFF" fill-opacity=".02"/>
  </pattern>
  <filter id="glowSoft" x="-25%" y="-80%" width="150%" height="260%">
    <feGaussianBlur stdDeviation="10"/>
  </filter>
  <filter id="glowTight" x="-40%" y="-120%" width="180%" height="340%">
    <feGaussianBlur stdDeviation="4"/>
  </filter>
  <filter id="orbGlow" x="-120%" y="-120%" width="340%" height="340%">
    <feGaussianBlur stdDeviation="14"/>
  </filter>
  <clipPath id="typeClip">
    <rect x="70" y="230" width="0" height="28">
      <animate attributeName="width" values="0;400;400;0;0"
               keyTimes="0;.34;.86;.9;1" dur="12s" repeatCount="indefinite"/>
    </rect>
  </clipPath>
</defs>

<rect width="{W}" height="{H}" fill="url(#bg)"/>
<rect width="{W}" height="{H}" fill="url(#grid)"/>
<rect width="{W}" height="{H}" fill="url(#gridBig)"/>
<ellipse cx="150" cy="30" rx="440" ry="250" fill="url(#glowCrimson)"/>
<ellipse cx="{CX}" cy="{CY}" rx="340" ry="300" fill="url(#glowCyan)"/>
<ellipse cx="640" cy="380" rx="520" ry="180" fill="url(#glowViolet)"/>
<rect width="{W}" height="{H}" fill="url(#vignette)"/>
<rect width="{W}" height="{H}" fill="url(#scan)"/>

<!-- 电路总线 -->
<g opacity=".85">
  <path d="M0 20H214L244 50H392" stroke="{CYAN}" stroke-opacity=".35" stroke-width="1.2"
        stroke-dasharray="3 7">
    <animate attributeName="stroke-dashoffset" values="0;-60" dur="6s" repeatCount="indefinite"/>
  </path>
  <path d="M1280 42H1150L1120 72" stroke="{VIOLET}" stroke-opacity=".3" stroke-width="1.2"
        stroke-dasharray="3 7">
    <animate attributeName="stroke-dashoffset" values="0;60" dur="7s" repeatCount="indefinite"/>
  </path>
  <path d="M0 318H1280" stroke="url(#hair)" stroke-opacity=".55" stroke-width="1"/>
  <g fill="{CYAN}" fill-opacity=".65">
    <rect x="213" y="17" width="6" height="6" transform="rotate(45 216 20)"/>
    <rect x="391" y="47" width="6" height="6" transform="rotate(45 394 50)"/>
  </g>
  <circle r="2.6" fill="{MINT}" filter="url(#glowTight)">
    <animateMotion path="M -20 318 H 1300" dur="9s" repeatCount="indefinite"/>
    <animate attributeName="opacity" values="0;1;1;0" keyTimes="0;.08;.9;1"
             dur="9s" repeatCount="indefinite"/>
  </circle>
</g>

<!-- 角标 -->
<g stroke-width="1.4" stroke-linecap="square" opacity=".55">
  <path d="M20 52V20H52" stroke="{CYAN}"/>
  <path d="M1260 52V20H1228" stroke="{VIOLET}"/>
  <path d="M20 308V340H52" stroke="{CRIMSON}"/>
  <path d="M1260 308V340H1228" stroke="{CYAN}"/>
</g>
<text x="1224" y="34" text-anchor="end" font-family="{MONO}" font-size="9"
      letter-spacing="3" fill="#5B6B82" opacity=".8">// NIGHT_CITY_GRID</text>

<!-- 左侧文字 -->
<g>
  <rect x="70" y="46" width="278" height="30" rx="15" fill="{CYAN}" fill-opacity=".05"
        stroke="{CYAN}" stroke-opacity=".45" stroke-width="1"/>
  <circle cx="91" cy="61" r="3.4" fill="{CYAN}">
    <animate attributeName="opacity" values="1;.12;1" dur="2.4s" repeatCount="indefinite"/>
  </circle>
  <text x="105" y="66" font-family="{MONO}" font-size="10.5" letter-spacing="3.4"
        fill="{MINT}">SYSTEM ONLINE</text>
  <text x="243" y="66" font-family="{MONO}" font-size="10.5" letter-spacing="1"
        fill="{CRIMSON}" opacity=".9">v2.0</text>
</g>

<g font-family="{MONO}" font-size="64" font-weight="700" letter-spacing="3">
  <g>
    <animateTransform attributeName="transform" type="translate"
      values="0 0;0 0;-3 0;2 0;0 0" keyTimes="0;.86;.9;.93;1" dur="7.5s" repeatCount="indefinite"/>
    <text x="70" y="172" fill="{CRIMSON}" opacity=".28">DUMMYSTROPHAEL</text>
  </g>
  <g>
    <animateTransform attributeName="transform" type="translate"
      values="0 0;0 0;3 0;-2 0;0 0" keyTimes="0;.86;.9;.93;1" dur="7.5s" repeatCount="indefinite"/>
    <text x="70" y="172" fill="{CYAN}" opacity=".3">DUMMYSTROPHAEL</text>
  </g>
  <text x="70" y="172" fill="url(#titleGrad)" filter="url(#glowSoft)" opacity=".55">
    DUMMYSTROPHAEL
    <animate attributeName="opacity" values=".4;.7;.4" dur="6s" repeatCount="indefinite"/>
  </text>
  <text x="70" y="172" fill="url(#titleGrad)">DUMMYSTROPHAEL</text>
</g>

<text x="72" y="212" font-family="{MONO}" font-size="14" letter-spacing="4.2"
      fill="{TEXT}" opacity=".9">CREATIVE DEVELOPER<tspan fill="#46536A"
      letter-spacing="4.2">  //  </tspan><tspan fill="{VIOLET}"
      letter-spacing="4.2">SYSTEMS · GRAPHICS · WEIRD IDEAS</tspan></text>

<g clip-path="url(#typeClip)">
  <text x="72" y="252" font-family="{MONO}" font-size="14" letter-spacing="1.2"
        fill="{CYAN}">&gt;</text>
  <text x="96" y="252" font-family="{MONO}" font-size="14" letter-spacing="1.2"
        fill="#AFBFD4">building tomorrow, one commit at a time.</text>
</g>
<rect x="96" y="240" width="8" height="15" fill="{CYAN}">
  <animate attributeName="x" values="96;470;470;96;96"
           keyTimes="0;.34;.86;.9;1" dur="12s" repeatCount="indefinite"/>
  <animate attributeName="opacity" values="1;1;0;0;1" keyTimes="0;.5;.55;.95;1"
           dur="1.15s" repeatCount="indefinite"/>
</rect>

<!-- HUD -->
<text x="72" y="336" font-family="{MONO}" font-size="9.5" letter-spacing="2.4"
      fill="#5B6B82">[ SYS ] ONLINE&#160;&#160;&#160;·&#160;&#160;&#160;[ NET ] STABLE&#160;&#160;&#160;·&#160;&#160;&#160;[ AUDIO ] READY</text>
<text x="1224" y="336" text-anchor="end" font-family="{MONO}" font-size="9.5"
      letter-spacing="2.4" fill="#5B6B82">NODE_04 // 2026</text>

<!-- 右侧核心 -->
<g transform="translate({CX} {CY})">
  <circle r="112" fill="url(#glowCyan)" opacity=".55"/>
  <circle r="52" fill="url(#glowViolet)" opacity=".9"/>
  <g>
    <animateTransform attributeName="transform" type="rotate" from="0" to="360"
                      dur="26s" repeatCount="indefinite"/>
    {orbits}
  </g>
  <g>
    <animateTransform attributeName="transform" type="rotate" from="360" to="0"
                      dur="18s" repeatCount="indefinite"/>
    {ticks}
  </g>
  <circle r="27" fill="{CYAN}" opacity=".35" filter="url(#orbGlow)"/>
  <circle r="24" fill="url(#core)">
    <animate attributeName="r" values="23;26;23" dur="4s" repeatCount="indefinite"/>
  </circle>
  <circle r="30" stroke="{MINT}" stroke-width="1.2" fill="none">
    <animate attributeName="r" values="30;58" dur="3.4s" repeatCount="indefinite"/>
    <animate attributeName="stroke-opacity" values=".55;0" dur="3.4s" repeatCount="indefinite"/>
  </circle>
  <path d="M0 -9L9 0L0 9L-9 0Z" fill="#FFFFFF" opacity=".95"/>
  <circle cx="0" cy="-96" r="3" fill="{MINT}">
    <animate attributeName="opacity" values="1;.2;1" dur="3s" repeatCount="indefinite"/>
  </circle>
  <circle cx="0" cy="82" r="2.4" fill="{CRIMSON}"/>
</g>

{particles}

<!-- 扫描线 -->
<rect x="0" y="-140" width="{W}" height="140" fill="url(#sweep)" opacity=".8">
  <animate attributeName="y" values="-140;360" dur="7s" repeatCount="indefinite"/>
</rect>
"""

    save("hero.svg", head(W, H, "DummyStrophael - futuristic developer banner") + body + "</svg>\n")


# ══════════════════════════════════════════════════════════════════════════
#  02 · TERMINAL
# ══════════════════════════════════════════════════════════════════════════
def terminal() -> None:
    W, H = 1000, 300
    CYCLE = 14.0
    lines = [
        ("prompt", "whoami", 0.5),
        ("out", f'{USER} · {ROLE} · "{TAGLINE}"', 1.1),
        ("prompt", "cat mission.txt", 1.9),
        ("out", f"> {MISSION}", 2.5),
        ("prompt", "git log -1 --oneline", 3.3),
        ("out", "a1b2c3d feat: redesign the future", 3.9),
        ("caret", "", 4.6),
    ]

    rows = []
    y = 84
    for kind, text, at in lines:
        appear = min(at / CYCLE, 0.9)
        kt = f"0;{appear:.3f};{appear + 0.015:.3f};.94;.97;1"
        vals = "0;0;1;1;0;0"
        if kind == "prompt":
            inner = (
                f'<text x="36" y="{y}" font-family="{MONO}" font-size="15" fill="{CRIMSON}">$</text>'
                f'<text x="54" y="{y}" font-family="{MONO}" font-size="15" '
                f'letter-spacing=".4" fill="{MINT}">{text}</text>'
            )
        elif kind == "out":
            inner = (
                f'<text x="36" y="{y}" font-family="{MONO}" font-size="15" '
                f'letter-spacing=".3" fill="#93A3B8">{text}</text>'
            )
        else:
            inner = (
                f'<text x="36" y="{y}" font-family="{MONO}" font-size="15" fill="{CRIMSON}">$</text>'
                f'<rect x="58" y="{y - 12}" width="9" height="15" fill="{MINT}">'
                f'<animate attributeName="opacity" values="1;1;0;0;1" keyTimes="0;.5;.55;.95;1" '
                f'dur="1.1s" repeatCount="indefinite"/></rect>'
            )
        rows.append(
            f'<g opacity="0">{inner}'
            f'<animate attributeName="opacity" values="{vals}" keyTimes="{kt}" '
            f'dur="{CYCLE}s" repeatCount="indefinite"/></g>'
        )
        y += 30
    rows = "".join(rows)

    # 右侧均衡器
    eq = []
    x = 742
    rnd = random.Random(7)
    for i in range(13):
        h1 = rnd.randint(12, 62)
        h2 = rnd.randint(12, 62)
        h3 = rnd.randint(8, 48)
        dur = round(rnd.uniform(1.4, 2.6), 2)
        eq.append(
            f'<rect x="{x}" y="{186 - h1}" width="7" height="{h1}" rx="2" fill="{CYAN}" '
            f'fill-opacity="{0.9 - i * 0.03:.2f}">'
            f'<animate attributeName="height" values="{h1};{h2};{h3};{h1}" dur="{dur}s" '
            f'repeatCount="indefinite"/>'
            f'<animate attributeName="y" values="{186 - h1};{186 - h2};{186 - h3};{186 - h1}" '
            f'dur="{dur}s" repeatCount="indefinite"/></rect>'
        )
        x += 13
    eq = "".join(eq)

    body = f"""<defs>
  <linearGradient id="win" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#0C0D17"/>
    <stop offset="1" stop-color="#06060D"/>
  </linearGradient>
  <linearGradient id="topline" x1="0" y1="0" x2="1000" y2="0" gradientUnits="userSpaceOnUse">
    <stop offset="0" stop-color="{CYAN}" stop-opacity=".7"/>
    <stop offset=".5" stop-color="{VIOLET}" stop-opacity=".5"/>
    <stop offset="1" stop-color="{CRIMSON}" stop-opacity=".6"/>
  </linearGradient>
  <filter id="tglow" x="-60%" y="-300%" width="220%" height="700%">
    <feGaussianBlur stdDeviation="6"/>
  </filter>
</defs>
<rect width="{W}" height="{H}" fill="{PANEL}" rx="16"/>
<rect x=".5" y=".5" width="{W - 1}" height="{H - 1}" rx="15.5" stroke="{EDGE}"/>
<rect x=".5" y=".5" width="{W - 1}" height="35" rx="15.5" fill="#0E101C"/>
<rect x=".5" y="20" width="{W - 1}" height="16" fill="#0E101C"/>
<path d="M.5 21.5H999.5" stroke="{EDGE}"/>
<path d="M.5 2H999.5" stroke="url(#topline)" stroke-width="2"/>
<circle cx="26" cy="18" r="5" fill="{CRIMSON}" fill-opacity=".85"/>
<circle cx="44" cy="18" r="5" fill="{VIOLET}" fill-opacity=".55"/>
<circle cx="62" cy="18" r="5" fill="{CYAN}" fill-opacity=".55"/>
<text x="86" y="22" font-family="{MONO}" font-size="11" letter-spacing="1.6"
      fill="#6F7F96">dummy@future: ~</text>
<text x="964" y="22" text-anchor="end" font-family="{MONO}" font-size="10"
      letter-spacing="2" fill="#46536A">zsh — 96×28</text>
<path d="M724 56V262" stroke="{EDGE}" stroke-dasharray="2 6"/>
<text x="742" y="84" font-family="{MONO}" font-size="9.5" letter-spacing="2.6"
      fill="#5B6B82">LIVE TELEMETRY</text>
{eq}
<text x="742" y="216" font-family="{MONO}" font-size="10" letter-spacing="2"
      fill="#5B6B82">SIGNAL</text>
<text x="804" y="216" font-family="{MONO}" font-size="10" letter-spacing="1"
      fill="{CYAN}">▮▮▮▮▯</text>
<text x="742" y="244" font-family="{MONO}" font-size="10" letter-spacing="2"
      fill="#5B6B82">UPTIME</text>
<text x="804" y="244" font-family="{MONO}" font-size="10" letter-spacing="1"
      fill="{VIOLET}">99.9%</text>
{rows}
</svg>
"""
    save("terminal.svg", head(W, H, "Terminal - whoami") + body)


# ══════════════════════════════════════════════════════════════════════════
#  03 · MUSIC CARD
# ══════════════════════════════════════════════════════════════════════════
CJK = "'Segoe UI','PingFang SC','Microsoft YaHei','Noto Sans CJK SC',sans-serif"
TRACK = "天外来物"
ARTIST = "薛之谦"
ALBUM = "ALBUM · 天外来物 · 2020"


def music_card() -> None:
    W, H = 1000, 220
    rnd = random.Random(17)
    eq = []
    x = 760
    for i in range(8):
        h1 = rnd.randint(14, 46)
        h2 = rnd.randint(14, 52)
        h3 = rnd.randint(10, 34)
        dur = round(rnd.uniform(0.9, 1.6), 2)
        eq.append(
            f'<rect x="{x}" y="{150 - h1}" width="7" height="{h1}" rx="2" fill="{MINT}" '
            f'fill-opacity="{0.85 - i * 0.055:.2f}">'
            f'<animate attributeName="height" values="{h1};{h2};{h3};{h1}" '
            f'dur="{dur}s" repeatCount="indefinite"/>'
            f'<animate attributeName="y" values="{150 - h1};{150 - h2};{150 - h3};'
            f'{150 - h1}" dur="{dur}s" repeatCount="indefinite"/></rect>'
        )
        x += 13
    eq = "".join(eq)

    body = f"""<defs>
  <linearGradient id="mbg" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="#0B0C15"/>
    <stop offset="1" stop-color="#07070E"/>
  </linearGradient>
  <radialGradient id="mglow" cx="50%" cy="50%" r="50%">
    <stop offset="0" stop-color="{VIOLET}" stop-opacity=".22"/>
    <stop offset="1" stop-color="{VIOLET}" stop-opacity="0"/>
  </radialGradient>
  <radialGradient id="discBg" cx="50%" cy="50%" r="50%">
    <stop offset="0" stop-color="#1C2842"/>
    <stop offset=".72" stop-color="#0C111C"/>
    <stop offset="1" stop-color="#070A11"/>
  </radialGradient>
  <linearGradient id="mlabel" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="{VIOLET}"/>
    <stop offset="1" stop-color="{CYAN}"/>
  </linearGradient>
  <linearGradient id="mname" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="#FFFFFF"/>
    <stop offset="1" stop-color="{MINT}"/>
  </linearGradient>
  <linearGradient id="mprog" x1="204" y1="0" x2="724" y2="0" gradientUnits="userSpaceOnUse">
    <stop offset="0" stop-color="{VIOLET}"/>
    <stop offset=".55" stop-color="{CYAN}"/>
    <stop offset="1" stop-color="{MINT}"/>
  </linearGradient>
  <linearGradient id="medge" x1="14" y1="0" x2="966" y2="0" gradientUnits="userSpaceOnUse">
    <stop offset="0" stop-color="{CYAN}" stop-opacity="0"/>
    <stop offset=".3" stop-color="{CYAN}" stop-opacity=".75"/>
    <stop offset=".7" stop-color="{VIOLET}" stop-opacity=".6"/>
    <stop offset="1" stop-color="{CRIMSON}" stop-opacity="0"/>
  </linearGradient>
  <pattern id="mgrid" width="26" height="26" patternUnits="userSpaceOnUse">
    <path d="M26 0H0V26" stroke="#FFFFFF" stroke-opacity=".018"/>
  </pattern>
  <clipPath id="mclip">
    <path d="M0 14Q0 0 14 0H966L1000 34V206Q1000 220 986 220H14Q0 220 0 206Z"/>
  </clipPath>
</defs>
<g clip-path="url(#mclip)">
  <rect width="1000" height="220" fill="url(#mbg)"/>
  <rect width="1000" height="220" fill="url(#mgrid)"/>
  <ellipse cx="112" cy="110" rx="200" ry="150" fill="url(#mglow)"/>
</g>
<path d="M0 14Q0 0 14 0H966L1000 34V206Q1000 220 986 220H14Q0 220 0 206Z" stroke="{EDGE}"/>
<path d="M966 0L1000 34" stroke="{CYAN}" stroke-opacity=".6" stroke-width="1.2"/>

<g transform="translate(112 110)">
  <circle r="80" stroke="{CYAN}" stroke-opacity=".22" stroke-width="1" stroke-dasharray="2 9">
    <animateTransform attributeName="transform" type="rotate" from="0" to="360"
                      dur="34s" repeatCount="indefinite"/>
  </circle>
  <circle r="64" fill="url(#discBg)" stroke="#243049"/>
  <g>
    <animateTransform attributeName="transform" type="rotate" from="0" to="360"
                      dur="9s" repeatCount="indefinite"/>
    <circle r="52" stroke="#FFFFFF" stroke-opacity=".05"/>
    <circle r="44" stroke="#FFFFFF" stroke-opacity=".06"/>
    <circle r="36" stroke="#FFFFFF" stroke-opacity=".07"/>
    <path d="M0 -58A58 58 0 0 1 41 -41" stroke="{CYAN}" stroke-opacity=".55" stroke-width="2"
          stroke-linecap="round"/>
  </g>
  <circle r="17" fill="url(#mlabel)"/>
  <path d="M-3.5 -6.5L7 0L-3.5 6.5Z" fill="#06070C"/>
</g>

<text x="204" y="62" font-family="{MONO}" font-size="10.5" letter-spacing="5"
      fill="{CYAN}">NOW PLAYING</text>
<text x="204" y="106" font-family="{CJK}" font-size="30" font-weight="600"
      fill="url(#mname)">{TRACK}</text>
<text x="204" y="134" font-family="{CJK}" font-size="14" letter-spacing=".5"
      fill="{MUTED}">{ARTIST}</text>
<text x="204" y="160" font-family="{MONO}" font-size="9" letter-spacing="2.6"
      fill="#5B6B82">{ALBUM}</text>

<rect x="204" y="186" width="520" height="4" rx="2" fill="#161E2C"/>
<rect x="204" y="186" width="338" height="4" rx="2" fill="url(#mprog)"/>
<circle cx="542" cy="188" r="4" fill="#FFFFFF">
  <animate attributeName="opacity" values="1;.35;1" dur="2.2s" repeatCount="indefinite"/>
</circle>

<text x="966" y="46" text-anchor="end" font-family="{MONO}" font-size="9.5"
      letter-spacing="2.6" fill="{CYAN}">OPEN PLAYLIST ↗</text>
<text x="760" y="92" font-family="{MONO}" font-size="9" letter-spacing="3"
      fill="#5B6B82">SIGNAL</text>
{eq}
<text x="760" y="178" font-family="{MONO}" font-size="9" letter-spacing="2.4"
      fill="#5B6B82">1125 LIKED · 19 SHOWN</text>
</svg>
"""
    save("music-card.svg", head(W, H, f"Now playing - {TRACK}") + body)


# ══════════════════════════════════════════════════════════════════════════
#  04 · ARSENAL
# ══════════════════════════════════════════════════════════════════════════
def arsenal() -> None:
    W = 1000
    CH = 38
    GAP = 14
    ROW_GAP = 16
    PAD = 24
    FONT = 13
    CW = 8.3  # 13px 等宽字体的近似字符宽度
    colors = [CYAN, VIOLET, CRIMSON]

    rows = []
    for ri, labels in enumerate(STACK):
        widths = [len(t) * CW + 46 for t in labels]
        total = sum(widths) + GAP * (len(labels) - 1)
        x = (W - total) / 2
        y = PAD + ri * (CH + ROW_GAP)
        color = colors[ri % len(colors)]
        chips = []
        for label, w in zip(labels, widths):
            chips.append(
                f"<g>"
                f'<rect x="{x:.1f}" y="{y}" width="{w:.1f}" height="{CH}" rx="8" '
                f'fill="{color}" fill-opacity=".055" stroke="{color}" stroke-opacity=".38"/>'
                f'<rect x="{x + 14:.1f}" y="{y + CH / 2 - 3:.1f}" width="6" height="6" '
                f'transform="rotate(45 {x + 17:.1f} {y + CH / 2:.1f})" fill="{color}"/>'
                f'<text x="{x + 30:.1f}" y="{y + CH / 2 + 4.5:.1f}" font-family="{MONO}" '
                f'font-size="{FONT}" letter-spacing=".5" fill="#CBD8E8">{label}</text>'
                f"</g>"
            )
            x += w + GAP
        rows.append("".join(chips))

    H = PAD * 2 + len(STACK) * CH + (len(STACK) - 1) * ROW_GAP
    body = f"""<defs>
  <linearGradient id="aglow" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="{CYAN}" stop-opacity=".35"/>
    <stop offset=".5" stop-color="{VIOLET}" stop-opacity=".28"/>
    <stop offset="1" stop-color="{CRIMSON}" stop-opacity=".3"/>
  </linearGradient>
</defs>
{"".join(rows)}
</svg>
"""
    save("arsenal.svg", head(W, H, "Tech arsenal") + body)


# ══════════════════════════════════════════════════════════════════════════
#  04 · PROJECT CARDS
# ══════════════════════════════════════════════════════════════════════════
def project_cards() -> None:
    W, H = 440, 236
    for p in PROJECTS:
        accent = p["accent"]
        slot = p.get("slot", False)
        stroke = (
            f'stroke="{accent}" stroke-opacity=".55" stroke-dasharray="6 5"'
            if slot
            else f'stroke="{EDGE}"'
        )
        if slot:
            inner = f"""
<g>
  <rect x="24" y="176" width="240" height="4" rx="2" fill="{accent}" fill-opacity=".12"/>
  <rect x="24" y="176" width="20" height="4" rx="2" fill="{accent}">
    <animate attributeName="width" values="20;214;20" dur="3.6s" repeatCount="indefinite"/>
  </rect>
  <text x="416" y="205" text-anchor="end" font-family="{MONO}" font-size="16"
        fill="{accent}" opacity=".7">↗</text>
</g>"""
        else:
            inner = f"""
<g>
  <path d="M24 176H416" stroke="{EDGE}"/>
  <circle cx="30" cy="200" r="3.2" fill="{accent}"/>
  <text x="42" y="204" font-family="{MONO}" font-size="10" letter-spacing="1.8"
        fill="#6F7F96">{p['meta']}</text>
  <text x="416" y="205" text-anchor="end" font-family="{MONO}" font-size="16"
        fill="{accent}">↗</text>
</g>"""

        desc = "".join(
            f'<text x="24" y="{132 + i * 20}" font-family="{SANS}" font-size="11.5" '
            f'letter-spacing=".2" fill="#7E8DA3">{line}</text>'
            for i, line in enumerate(p["desc"])
        )

        body = f"""<defs>
  <linearGradient id="cbg" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="#0B0C15"/>
    <stop offset="1" stop-color="#06060C"/>
  </linearGradient>
  <linearGradient id="cname" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="#FFFFFF"/>
    <stop offset="1" stop-color="{accent}"/>
  </linearGradient>
  <radialGradient id="cglow" cx="50%" cy="50%" r="50%">
    <stop offset="0" stop-color="{accent}" stop-opacity=".3"/>
    <stop offset="1" stop-color="{accent}" stop-opacity="0"/>
  </radialGradient>
  <pattern id="cgrid" width="22" height="22" patternUnits="userSpaceOnUse">
    <path d="M22 0H0V22" stroke="#FFFFFF" stroke-opacity=".022"/>
  </pattern>
</defs>
<path d="M0 14Q0 0 14 0H406L440 34V222Q440 236 426 236H14Q0 236 0 222Z" fill="url(#cbg)" {stroke}/>
<path d="M0 14Q0 0 14 0H406L440 34V222Q440 236 426 236H14Q0 236 0 222Z" fill="url(#cgrid)"/>
<ellipse cx="400" cy="20" rx="170" ry="90" fill="url(#cglow)"/>
<path d="M406 0L440 34" stroke="{accent}" stroke-opacity=".7" stroke-width="1.4"/>
<path d="M0 0H56" stroke="{accent}" stroke-width="2" opacity=".85"/>
<text x="24" y="42" font-family="{MONO}" font-size="10" letter-spacing="2.4"
      fill="#5B6B82">[ {p['index']} ]</text>
<rect x="374" y="26" width="46" height="18" rx="9" fill="{accent}" fill-opacity=".1"
      stroke="{accent}" stroke-opacity=".55"/>
<text x="397" y="38.5" text-anchor="middle" font-family="{MONO}" font-size="8.5"
      letter-spacing="1" fill="{accent}">{p['status']}</text>
<text x="24" y="96" font-family="{MONO}" font-size="27" font-weight="700"
      letter-spacing="1.5" fill="url(#cname)">{p['name']}</text>
{desc}
{inner}
</svg>
"""
        save(p["file"], head(W, H, f"{p['name']} project card") + body)


# ══════════════════════════════════════════════════════════════════════════
#  05 · DIVIDER / FOOTER
# ══════════════════════════════════════════════════════════════════════════
#  05 · BADGES
# ══════════════════════════════════════════════════════════════════════════
def badges() -> None:
    H = 32
    for b in BADGES:
        label, value, accent = b["label"], b["value"], b["accent"]
        lw = len(label) * 6.6
        vw = len(value) * 7.0
        label_x = 30
        value_x = label_x + lw + 12
        W = round(value_x + vw + 16)
        body = f"""<defs>
  <linearGradient id="bglow" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="{accent}" stop-opacity=".18"/>
    <stop offset="1" stop-color="{accent}" stop-opacity="0"/>
  </linearGradient>
</defs>
<rect x=".5" y=".5" width="{W - 1}" height="{H - 1}" rx="4" fill="{PANEL}"
      stroke="{accent}" stroke-opacity=".45"/>
<rect x=".5" y=".5" width="{min(64, W - 1)}" height="{H - 1}" rx="4" fill="url(#bglow)"/>
<rect x=".5" y=".5" width="3" height="{H - 1}" fill="{accent}"/>
<rect x="16" y="{H / 2 - 2.5}" width="5" height="5" transform="rotate(45 18.5 {H / 2})"
      fill="{accent}"/>
<text x="{label_x}" y="{H / 2 + 3.4}" font-family="{MONO}" font-size="9.5"
      letter-spacing="2.2" fill="{accent}">{label}</text>
<text x="{value_x}" y="{H / 2 + 4}" font-family="{MONO}" font-size="11.5"
      letter-spacing=".3" fill="#DCE6F2">{value}</text>
</svg>
"""
        save(b["file"], head(W, H, f"{label}: {value}") + body)


# ══════════════════════════════════════════════════════════════════════════
#  06 · DIVIDER / FOOTER
# ══════════════════════════════════════════════════════════════════════════
def divider() -> None:
    W, H = 1280, 46
    body = f"""<defs>
  <linearGradient id="dl" x1="0" y1="0" x2="640" y2="0" gradientUnits="userSpaceOnUse">
    <stop offset="0%" stop-color="{CYAN}" stop-opacity="0"/>
    <stop offset="62%" stop-color="{CYAN}" stop-opacity=".75"/>
    <stop offset="92%" stop-color="{CYAN}" stop-opacity=".95"/>
    <stop offset="100%" stop-color="{CYAN}" stop-opacity="0"/>
  </linearGradient>
  <linearGradient id="dr" x1="640" y1="0" x2="1280" y2="0" gradientUnits="userSpaceOnUse">
    <stop offset="0%" stop-color="{CRIMSON}" stop-opacity="0"/>
    <stop offset="8%" stop-color="{CRIMSON}" stop-opacity=".95"/>
    <stop offset="38%" stop-color="{CRIMSON}" stop-opacity=".75"/>
    <stop offset="100%" stop-color="{CRIMSON}" stop-opacity="0"/>
  </linearGradient>
</defs>
<path d="M40 23H590" stroke="url(#dl)" stroke-width="1.2"/>
<path d="M690 23H1240" stroke="url(#dr)" stroke-width="1.2"/>
<g transform="translate(640 23)">
  <g>
    <animateTransform attributeName="transform" type="rotate" from="0" to="360"
                      dur="22s" repeatCount="indefinite"/>
    <rect x="-7" y="-7" width="14" height="14" stroke="{CYAN}" stroke-opacity=".9"
          stroke-width="1.2"/>
  </g>
  <rect x="-3" y="-3" width="6" height="6" fill="{CRIMSON}"/>
  <circle r="15" stroke="{VIOLET}" stroke-opacity=".3"/>
</g>
"""
    save("divider.svg", head(W, H, "divider") + body + "</svg>\n")


def footer() -> None:
    W, H = 1280, 160
    rnd = random.Random(3)
    bars = []
    n = 34
    bw, gap = 4, 5
    total = n * bw + (n - 1) * gap
    x0 = (W - total) / 2
    for i in range(n):
        base = 6 + 10 * math.sin(i / 2.2) ** 2
        h1 = round(base + rnd.uniform(2, 14), 1)
        h2 = round(base + rnd.uniform(2, 22), 1)
        h3 = round(base + rnd.uniform(2, 9), 1)
        dur = round(rnd.uniform(1.8, 3.2), 2)
        x = x0 + i * (bw + gap)
        col = CYAN if i < n / 2 else CRIMSON
        bars.append(
            f'<rect x="{x:.1f}" y="{120 - h1:.1f}" width="{bw}" height="{h1}" rx="1.5" '
            f'fill="{col}" fill-opacity=".55">'
            f'<animate attributeName="height" values="{h1};{h2};{h3};{h1}" dur="{dur}s" '
            f'repeatCount="indefinite"/>'
            f'<animate attributeName="y" values="{120 - h1:.1f};{120 - h2:.1f};'
            f'{120 - h3:.1f};{120 - h1:.1f}" dur="{dur}s" repeatCount="indefinite"/></rect>'
        )
    body = f"""<defs>
  <linearGradient id="fl" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="{CYAN}" stop-opacity="0"/>
    <stop offset=".3" stop-color="{CYAN}" stop-opacity=".5"/>
    <stop offset=".7" stop-color="{VIOLET}" stop-opacity=".45"/>
    <stop offset="1" stop-color="{CRIMSON}" stop-opacity="0"/>
  </linearGradient>
  <linearGradient id="ft" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="#FFFFFF" stop-opacity=".95"/>
    <stop offset=".55" stop-color="{MINT}" stop-opacity=".9"/>
    <stop offset="1" stop-color="{VIOLET}" stop-opacity=".95"/>
  </linearGradient>
</defs>
<rect x="120" y="10" width="1040" height="1" fill="url(#fl)"/>
<text x="640" y="34" text-anchor="middle" font-family="{MONO}" font-size="10.5"
      letter-spacing="4" fill="#6B7C93">© 2026 {USER.upper()} — ALL SYSTEMS NOMINAL</text>
<text x="640" y="76" text-anchor="middle" font-family="{MONO}" font-size="19"
      font-weight="700" letter-spacing="6" fill="url(#ft)">STAY HUNGRY. STAY CURIOUS.</text>
{"".join(bars)}
<text x="640" y="150" text-anchor="middle" font-family="{MONO}" font-size="10"
      letter-spacing="3" fill="#55657C">BUILT WITH CAFFEINE · POWERED BY CURIOSITY</text>
"""
    save("footer.svg", head(W, H, "footer") + body + "</svg>\n")


if __name__ == "__main__":
    print("building assets ...")
    hero()
    terminal()
    music_card()
    arsenal()
    project_cards()
    badges()
    divider()
    footer()
    print("done.")
