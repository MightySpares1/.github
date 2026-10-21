W,H=1200,300
steps=[("1","Search","Part name, number or category"),("2","Fit check","Select make · model · year"),("3","Order","Secure checkout"),("4","Delivered","Shipped to your door across AU")]
cx=[180,460,740,1020]
def icon(i):
    if i==0: return '<circle cx="-4" cy="-4" r="13" fill="none" stroke="#0B1426" stroke-width="5"/><line x1="6" y1="6" x2="16" y2="16" stroke="#0B1426" stroke-width="6" stroke-linecap="round"/>'
    if i==1: return '<path d="M-15 0 L-4 11 L16 -11" stroke="#0B1426" stroke-width="6" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'
    if i==2: return '<path d="M-18 -12 h6 l6 20 h18 l5 -14 h-26" stroke="#0B1426" stroke-width="4.5" fill="none" stroke-linejoin="round" stroke-linecap="round"/><circle cx="-4" cy="14" r="3.5" fill="#0B1426"/><circle cx="12" cy="14" r="3.5" fill="#0B1426"/>'
    return '<rect x="-18" y="-14" width="36" height="28" rx="3" fill="none" stroke="#0B1426" stroke-width="4.5"/><path d="M-18 -4 h36 M-4 -14 v10" stroke="#0B1426" stroke-width="4.5"/>'
T=8  # loop seconds
nodes=[]
for i,(n,t,s) in enumerate(steps):
    d=i*1.6
    nodes.append(f'''<g transform="translate({cx[i]} 140)">
  <circle r="44" fill="#16243F" stroke="#26375C" stroke-width="2"/>
  <circle class="ring" style="animation-delay:{d}s" r="44" fill="none" stroke="#FFC233" stroke-width="4"/>
  <g class="node" style="animation-delay:{d}s"><circle r="34" fill="url(#brand)"/>{icon(i)}</g>
  <text y="80" text-anchor="middle" class="t">{t}</text>
  <text y="102" text-anchor="middle" class="s">{s}</text>
  <text x="-38" y="-36" class="n">{n}</text>
</g>''')
svg=f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="How it works: search, fit check, order, delivered">
<defs><linearGradient id="brand" x1="0" x2="1"><stop offset="0" stop-color="#FF7A1A"/><stop offset="1" stop-color="#FFC233"/></linearGradient><linearGradient id="line" gradientUnits="userSpaceOnUse" x1="180" y1="0" x2="1020" y2="0"><stop offset="0" stop-color="#FF7A1A"/><stop offset="1" stop-color="#FFC233"/></linearGradient></defs>
<style>
 text{{font-family:'Segoe UI',Helvetica,Arial,sans-serif}}
 .t{{font-size:20px;font-weight:800;fill:#F9FAFB}} .s{{font-size:13.5px;fill:#9CA3AF}} .n{{font-size:13px;font-weight:800;fill:#FFC233}}
 .track{{stroke-dasharray:6 10;animation:dash 1s linear infinite}}
 .prog{{stroke-dasharray:840;stroke-dashoffset:840;animation:prog {T}s linear infinite}}
 .node{{animation:node {T}s ease-out infinite;transform-box:fill-box;transform-origin:center}}
 .ring{{opacity:0;animation:ring {T}s ease-out infinite;transform-box:fill-box;transform-origin:center}}
 .van{{animation:van {T}s linear infinite}}
 @keyframes dash{{to{{stroke-dashoffset:-16}}}}
 @keyframes prog{{0%{{stroke-dashoffset:840}}60%{{stroke-dashoffset:0}}90%{{stroke-dashoffset:0;opacity:1}}100%{{stroke-dashoffset:0;opacity:0}}}}
 @keyframes node{{0%{{transform:scale(.55);opacity:.35}}6%{{transform:scale(1.12);opacity:1}}10%,88%{{transform:scale(1);opacity:1}}100%{{transform:scale(.55);opacity:.35}}}}
 @keyframes ring{{0%{{opacity:0;transform:scale(1)}}4%{{opacity:1}}18%{{opacity:0;transform:scale(1.5)}}100%{{opacity:0}}}}
 @keyframes van{{0%{{transform:translateX(0)}}60%{{transform:translateX(840px)}}100%{{transform:translateX(840px)}}}}
 @media (prefers-reduced-motion:reduce){{*{{animation:none!important}} .prog{{stroke-dashoffset:0}}}}
</style>
<rect width="{W}" height="{H}" rx="20" fill="#0B1426"/>
<text x="{W/2}" y="46" text-anchor="middle" font-size="26" font-weight="800" fill="url(#brand)">How it works</text>
<line class="track" x1="180" y1="140" x2="1020" y2="140" stroke="#26375C" stroke-width="4"/>
<line class="prog" x1="180" y1="140" x2="1020" y2="140" stroke="url(#line)" stroke-width="5" stroke-linecap="round"/>
{''.join(nodes)}
<g class="van"><g transform="translate(180 76)">
  <rect x="-22" y="-12" width="30" height="20" rx="3" fill="#FFC233"/><path d="M8 -6 h9 l7 8 v6 h-16z" fill="#FF7A1A"/>
  <circle cx="-12" cy="10" r="4.5" fill="#E5E7EB"/><circle cx="14" cy="10" r="4.5" fill="#E5E7EB"/>
</g></g>
</svg>'''
open('../profile/assets/how-it-works.svg','w').write(svg)

# footer wave
F=f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="120" viewBox="0 0 1200 120" role="img" aria-label="Mighty Spares">
<defs><linearGradient id="brand" x1="0" x2="1"><stop offset="0" stop-color="#FF7A1A"/><stop offset="1" stop-color="#FFC233"/></linearGradient></defs>
<style>
 .w1{{animation:w 9s linear infinite}} .w2{{animation:w 6s linear infinite reverse}}
 @keyframes w{{to{{transform:translateX(-600px)}}}}
 @media (prefers-reduced-motion:reduce){{*{{animation:none!important}}}}
</style>
<g class="w1" opacity=".35"><path fill="url(#brand)" d="M0 60 Q150 20 300 60 T600 60 T900 60 T1200 60 T1500 60 T1800 60 V120 H0Z"/></g>
<g class="w2"><path fill="#0B1426" d="M0 80 Q150 45 300 80 T600 80 T900 80 T1200 80 T1500 80 T1800 80 V120 H0Z"/></g>
<text x="600" y="110" text-anchor="middle" font-family="'Segoe UI',Arial,sans-serif" font-size="14" font-weight="700" fill="#FFC233" letter-spacing="3">DRIVE ON · MIGHTY SPARES</text>
</svg>'''
open('../profile/assets/footer.svg','w').write(F)
