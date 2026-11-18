#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate playlist/index.html (NIGHT CITY style cover wall).

用法：
    python build_playlist.py

改歌单就改下面的 TRACKS 列表（曲名, 歌手），封面图放在 assets/covers/01.jpg …
19 首之外要加歌，记得同时把封面按序号放进 assets/covers/。
README 里的 ARCHIVE 表格是手写的，加歌时也一起改。
"""

from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "playlist" / "index.html"

TRACKS = [
    ("最佳歌手 (Live)", "薛之谦 · 许嵩"),
    ("媚人", "薛之谦"),
    ("崇拜", "薛之谦"),
    ("我好像在哪见过你", "薛之谦"),
    ("一半", "薛之谦"),
    ("爱好 (2024 音乐缘计划现场)", "薛之谦"),
    ("念", "薛之谦"),
    ("关于你", "薛之谦"),
    ("配合", "薛之谦"),
    ("火星人来过", "薛之谦"),
    ("Royalty", "Egzod · Maestro Chives"),
    ("锤子 (feat. 范丞丞)", "KnowKnow · 范丞丞"),
    ("AI", "薛之谦"),
    ("无数", "薛之谦"),
    ("无名之海", "石岩"),
    ("陪你去流浪", "薛之谦"),
    ("Die For You", "Grabbitz"),
    ("Teeth", "5 Seconds of Summer"),
    ("丑八怪 (Live)", "薛之谦"),
]

KUGOU = "https://www.kugou.com/yy/html/search.html#searchType=song&searchKeyWord="


def card(i: int, title: str, artist: str) -> str:
    keyword = quote(f"{title.split(' (')[0]} {artist.split(' · ')[0]}", safe="")
    return f"""      <a class="track" href="{KUGOU}{keyword}" target="_blank" rel="noopener">
        <span class="cover"><img src="../assets/covers/{i:02d}.jpg" alt="{title}" loading="lazy"><i>{i:02d}</i></span>
        <span class="name">{title}</span>
        <span class="artist">{artist}</span>
      </a>"""


cards = "\n".join(card(i, t, a) for i, (t, a) in enumerate(TRACKS, start=1))

HTML = f"""<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>我喜欢 · AUDIO ARCHIVE</title>
<style>
  :root{{
    --void:#05060B; --panel:#0A0A12; --edge:#1B2333;
    --cyan:#22D3EE; --mint:#7DF9FF; --violet:#A78BFA; --crimson:#FF2D55;
    --ink:#E6EDF3; --muted:#8B97AB;
    --mono:"Cascadia Mono",Consolas,"SF Mono",Menlo,monospace;
    --sans:"Segoe UI","PingFang SC","Microsoft YaHei",system-ui,sans-serif;
  }}
  *{{box-sizing:border-box}}
  html,body{{margin:0;background:var(--void);color:var(--ink);font-family:var(--sans)}}
  body{{
    min-height:100vh;padding:34px 32px 80px;position:relative;overflow-x:hidden;
    background:
      radial-gradient(900px 520px at 6% -8%, #FF2D5526, transparent 70%),
      radial-gradient(900px 520px at 96% 104%, #22D3EE24, transparent 70%),
      var(--void);
  }}
  body::before{{
    content:"";position:fixed;inset:0;pointer-events:none;z-index:0;
    background-image:
      linear-gradient(#22D3EE12 1px,transparent 1px),
      linear-gradient(90deg,#22D3EE12 1px,transparent 1px);
    background-size:52px 52px;
    mask-image:radial-gradient(circle at 50% 30%,#000 10%,transparent 78%);
    -webkit-mask-image:radial-gradient(circle at 50% 30%,#000 10%,transparent 78%);
  }}
  body::after{{
    content:"";position:fixed;inset:0;pointer-events:none;z-index:0;opacity:.35;
    background:repeating-linear-gradient(180deg,#ffffff05 0 1px,transparent 1px 4px);
  }}
  .wrap{{position:relative;z-index:1;max-width:1080px;margin:0 auto}}

  .top{{
    display:flex;align-items:center;justify-content:space-between;gap:16px;
    padding-bottom:16px;border-bottom:1px solid var(--edge);
    font:11px/1 var(--mono);letter-spacing:3px;color:#5B6B82;
  }}
  .top a{{color:var(--cyan);text-decoration:none}}
  .top a:hover{{text-decoration:underline}}
  .top b{{color:var(--mint);font-weight:400}}

  .deck{{display:flex;align-items:center;gap:30px;margin:52px 0 44px}}
  .disc{{
    width:116px;height:116px;flex:0 0 auto;border-radius:50%;position:relative;
    background:
      repeating-radial-gradient(circle at 50% 50%,#ffffff09 0 1px,transparent 1px 4px),
      radial-gradient(circle at 50% 46%,#22304E 0%,#0C111C 62%,#06090F 100%);
    border:1px solid #243049;box-shadow:0 0 42px -12px #22D3EE66,inset 0 0 0 1px #ffffff12;
    animation:spin 12s linear infinite;
  }}
  .disc::before{{
    content:"";position:absolute;inset:13px;border-radius:50%;
    border-top:1px solid #22D3EE99;border-right:1px solid transparent;
    transform:rotate(-35deg);
  }}
  .disc::after{{
    content:"";position:absolute;inset:0;margin:auto;width:34px;height:34px;border-radius:50%;
    background:linear-gradient(135deg,var(--violet),var(--cyan));
  }}
  .disc span{{
    position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);
    width:0;height:0;border-left:9px solid #06070C;border-top:6px solid transparent;
    border-bottom:6px solid transparent;z-index:2;margin-left:2px;
  }}
  @keyframes spin{{to{{transform:rotate(360deg)}}}}

  .eyebrow{{font:600 10px/1 var(--mono);letter-spacing:6px;color:var(--cyan)}}
  h1{{
    font-size:56px;line-height:1.05;margin:16px 0 10px;letter-spacing:1px;font-weight:700;
    background:linear-gradient(92deg,#FFFFFF 0%,var(--mint) 38%,var(--violet) 68%,var(--crimson) 100%);
    -webkit-background-clip:text;background-clip:text;color:transparent;
  }}
  .meta{{font:12px/1.6 var(--mono);letter-spacing:1.4px;color:var(--muted)}}
  .meta b{{color:var(--ink);font-weight:600}}

  .grid{{
    display:grid;gap:30px 20px;grid-template-columns:repeat(5,minmax(0,1fr));
    margin-top:10px;
  }}
  @media (max-width:1040px){{ .grid{{grid-template-columns:repeat(4,minmax(0,1fr))}} }}
  @media (max-width:780px){{ .grid{{grid-template-columns:repeat(3,minmax(0,1fr))}} }}
  @media (max-width:540px){{ .grid{{grid-template-columns:repeat(2,minmax(0,1fr))}} .deck{{flex-direction:column;align-items:flex-start}} h1{{font-size:42px}} }}

  .track{{display:block;text-decoration:none;color:inherit}}
  .cover{{
    position:relative;display:block;aspect-ratio:1/1;border-radius:6px;overflow:hidden;
    border:1px solid var(--edge);background:#0E1420;
    transition:transform .25s ease,border-color .25s ease,box-shadow .25s ease;
  }}
  .cover img{{width:100%;height:100%;object-fit:cover;display:block;filter:saturate(.92);
              transition:transform .35s ease,filter .35s ease}}
  .cover i{{
    position:absolute;top:8px;left:8px;padding:3px 6px;border-radius:3px;
    font:10px/1 var(--mono);letter-spacing:1.4px;color:var(--mint);
    background:#05060BD9;border:1px solid #22D3EE55;font-style:normal;
  }}
  .track:hover .cover{{
    transform:translateY(-4px);border-color:#22D3EE88;
    box-shadow:0 0 0 1px #22D3EE44,0 22px 44px -22px #22D3EE99;
  }}
  .track:hover .cover img{{transform:scale(1.045);filter:saturate(1.1)}}
  .name{{
    display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden;
    margin-top:11px;font-size:13.5px;line-height:1.45;font-weight:600;letter-spacing:.2px;
  }}
  .artist{{display:block;margin-top:4px;font:11px/1.5 var(--mono);color:#6F7F96;
           white-space:nowrap;overflow:hidden;text-overflow:ellipsis}}
  .track:hover .name{{color:var(--mint)}}

  .foot{{
    margin-top:56px;padding-top:20px;border-top:1px solid var(--edge);
    display:flex;flex-wrap:wrap;align-items:center;gap:14px 22px;
    font:11px/1.7 var(--mono);letter-spacing:1.6px;color:#5B6B82;
  }}
  .foot a{{color:var(--cyan);text-decoration:none;border-bottom:1px solid #22D3EE44;padding-bottom:1px}}
  .foot a:hover{{border-color:var(--cyan)}}
  .foot .dot{{color:var(--edge)}}
  .bar{{display:flex;gap:4px;margin-left:auto}}
  .bar i{{display:block;width:4px;height:14px;border-radius:2px;background:linear-gradient(180deg,var(--cyan),#22D3EE22);
         transform-origin:bottom;animation:eq 1.2s ease-in-out infinite alternate}}
  .bar i:nth-child(2){{animation-delay:-.3s}} .bar i:nth-child(3){{animation-delay:-.6s}}
  .bar i:nth-child(4){{animation-delay:-.15s}} .bar i:nth-child(5){{animation-delay:-.45s}}
  @keyframes eq{{from{{transform:scaleY(.3)}}to{{transform:scaleY(1)}}}}
</style>
</head>
<body>
<div class="wrap">

  <div class="top">
    <span><a href="https://github.com/DummyStrophael">← DUMMYSTROPHAEL</a></span>
    <span>AUDIO ARCHIVE <b>//</b> KUGOU</span>
    <span><b>19</b> SHOWN / <b>1125</b> LIKED</span>
  </div>

  <div class="deck">
    <div class="disc"><span></span></div>
    <div>
      <div class="eyebrow">PLAYLIST · NO.01</div>
      <h1>我喜欢</h1>
      <div class="meta">1125 首收藏 · 按播放次数取前 <b>19</b> 首 · 封面为官方专辑图</div>
    </div>
  </div>

  <div class="grid">
{cards}
  </div>

  <div class="foot">
    <span>点任意一首 → 去酷狗搜索这首歌</span>
    <span class="dot">·</span>
    <a href="{KUGOU}{quote('薛之谦', safe='')}" target="_blank" rel="noopener">完整歌单 ↗</a>
    <span class="dot">·</span>
    <a href="https://github.com/DummyStrophael">返回主页</a>
    <div class="bar"><i></i><i></i><i></i><i></i><i></i></div>
  </div>

</div>
</body>
</html>
"""

OUT.parent.mkdir(exist_ok=True)
OUT.write_text(HTML, encoding="utf-8")
print(f"wrote {OUT} ({len(HTML)} chars, {len(TRACKS)} tracks)")
