import json, sys
S = 'ferramentas/mapa-mental/saida/'
dados = json.load(open(S + 'mapa-dados.json', encoding='utf-8'))
slim = []
for j in dados:
    slim.append({
        # B11: o título do nó é o nome padrão; o nome no site vai no detalhe
        'id': j['id'], 'c': j['codigo'], 'n': j['nome_padrao'] if j['nome_padrao'] != '[CONFIRMAR]' else j['nome_no_site'] + ' (nome padrão [CONFIRMAR])', 'ns': j['nome_no_site'], 'l': j['linha'], 't': j['tipo'], 'a': j['area']['codigo'], 'an': j['area']['nome'],
        'r': j['recorte'], 'o': j['onda'], 'loc': j['local'], 'mod': j['modalidade_normalizada'], 'tu': j['turma'], 'ch': j['carga_horaria'],
        'i': j['inicio'], 'fd': j['fonte_da_data'], 'd': j['dias_ate_inicio'], 'p': j['preco_texto_site'], 'st': j['status_catalogo'],
        'm': j['status_midia']['campanha'], 'g': (j['gut'] or {}).get('total'), 'gm': (j['gut'] or {}).get('motivo'),
        'k': [{'e': e['entrega'], 'q': e['quantidade_minima'], 'rq': e['regra_quantidade'], 'rp': ', '.join(e['responsavel']), 's': e['status'], 'qa': e['qa'], 'f': e['arquivo']} for e in j['kit']['entregas']],
        'ka': [{'e': e['entrega'], 'q': e['quantidade'], 'rp': ', '.join(e['responsavel']), 's': e['status'], 'f': e['arquivo']} for e in j['kit']['acrescimos']],
        # B14: arquivos das camadas; "devolvido" aparece como rascunho a revisar
        'cam': [[k, a['caminho'], a['estado']] for k in ('geral', 'linha', 'area') for a in j['arquivos_por_camada'][k]],
        'kt': j['kit']['template'], 'can': [[c['canal'], c['estado']] for c in j['canais']],
        'pe': [{'ref': p['ref_plano'], 'd': p['descricao'], 'b': p['bloqueia']} for p in j['pendencias']],
        'ap': [{'ref': a['ref'], 'o': a['o_que']} for a in j['aprovacoes']],
        'bl': j['resumo']['bloqueado'], 'fi': j['fontes']['ficha'], 'mt': j['metas'],
    })
DATA = json.dumps(slim, ensure_ascii=False, separators=(',', ':'))
AREAS = {}
for j in dados:
    if j['area']['codigo'].startswith('A'): AREAS[j['area']['codigo']] = j['area']['nome']

CSS = r"""
:root{
  /* Layout: barra de filtros fixa no topo, resumo, árvore Linha > Área > Item com detalhe em gaveta */
  --bg:#f3f5f4; --surface:#ffffff; --ink:#18232b; --muted:#56656e; --line:#d6dedb;
  --accent:#23715f; --accent-soft:#dcebe6;
  --o1:#c4492f; --o2:#23715f; --o3:#4d55a8; --hist:#8a949a;
  --block:#b3261e; --block-soft:#fbe4e1; --ok:#2e7d32; --wait:#9a6a00;
  --f-display:"Avenir Next","Segoe UI Semibold","Helvetica Neue",system-ui,sans-serif;
  --f-body:"Segoe UI","Helvetica Neue",Roboto,system-ui,sans-serif;
  --f-data:ui-monospace,"SF Mono","Cascadia Mono","Roboto Mono",Menlo,monospace;
}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){
  --bg:#0f1619; --surface:#172126; --ink:#e3ebe8; --muted:#9aa9a4; --line:#2b3a3f;
  --accent:#5cc2a6; --accent-soft:#1d3a33; --o1:#f0826b; --o2:#5cc2a6; --o3:#9aa2f0; --hist:#7d888e;
  --block:#ff8a80; --block-soft:#3a1f1d; --ok:#81c784; --wait:#e0b84d; color-scheme:dark}}
:root[data-theme="dark"]{
  --bg:#0f1619; --surface:#172126; --ink:#e3ebe8; --muted:#9aa9a4; --line:#2b3a3f;
  --accent:#5cc2a6; --accent-soft:#1d3a33; --o1:#f0826b; --o2:#5cc2a6; --o3:#9aa2f0; --hist:#7d888e;
  --block:#ff8a80; --block-soft:#3a1f1d; --ok:#81c784; --wait:#e0b84d; color-scheme:dark}
*{box-sizing:border-box}
body{background:var(--bg);color:var(--ink);font:15px/1.5 var(--f-body);margin:0}
body::before{content:"";position:fixed;inset:0 0 auto;height:env(safe-area-inset-top,0px);z-index:10;background:var(--surface)}
.wrap{padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));max-width:1180px;margin:0 auto}
header.top{background:var(--surface);border-bottom:1px solid var(--line)}
header.top .wrap{padding-block:22px 18px;display:grid;gap:6px}
.eyebrow{font:600 12px/1 var(--f-data);letter-spacing:.08em;text-transform:uppercase;color:var(--accent)}
h1{font:700 clamp(24px,3.4vw,34px)/1.15 var(--f-display);margin:0;text-wrap:balance;letter-spacing:-.01em}
.lede{color:var(--muted);max-width:70ch;margin:0}
.bar{position:sticky;top:env(safe-area-inset-top,0px);z-index:5;background:var(--surface);border-bottom:1px solid var(--line)}
.bar .wrap{padding-block:10px;display:flex;flex-wrap:wrap;gap:8px;align-items:center}
.bar input,.bar select{font:inherit;font-size:14px;color:var(--ink);background:var(--bg);border:1px solid var(--line);border-radius:8px;padding:7px 10px;min-width:0}
.bar input[type=search]{flex:1 1 220px}
.bar label.chk{display:flex;gap:6px;align-items:center;font-size:14px;color:var(--ink)}
:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
main .wrap{padding-block:20px 48px;display:grid;gap:22px}
.summary{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:10px}
.tile{background:var(--surface);border:1px solid var(--line);border-radius:10px;padding:12px 14px;display:grid;gap:2px}
.tile b{font:700 24px/1.1 var(--f-display);font-variant-numeric:tabular-nums}
.tile span{color:var(--muted);font-size:13px}
.legend{display:flex;flex-wrap:wrap;gap:14px;font-size:13px;color:var(--muted)}
.dot{display:inline-block;width:10px;height:10px;border-radius:50%;margin-right:6px;vertical-align:-1px}
details.l1{background:var(--surface);border:1px solid var(--line);border-radius:12px}
details.l1>summary{list-style:none;cursor:pointer;padding:14px 16px;display:flex;gap:10px;align-items:baseline;flex-wrap:wrap}
details.l1>summary h2{font:700 20px/1.2 var(--f-display);margin:0}
summary::-webkit-details-marker{display:none}
summary .meta{color:var(--muted);font-size:13px;font-variant-numeric:tabular-nums}
.chev{display:inline-block;transition:transform .15s;color:var(--muted)}
details[open]>summary .chev{transform:rotate(90deg)}
@media (prefers-reduced-motion:reduce){.chev{transition:none}}
.l1 .body{padding:0 16px 14px;display:grid;gap:8px}
details.l2{border-top:1px solid var(--line)}
details.l2>summary{list-style:none;cursor:pointer;padding:10px 0;display:flex;gap:10px;align-items:baseline;flex-wrap:wrap}
details.l2>summary h3{font:600 16px/1.3 var(--f-display);margin:0}
.items{display:grid;gap:6px;padding:0 0 10px}
.item{border:1px solid var(--line);border-left:4px solid var(--hist);border-radius:8px;background:var(--bg)}
.item.o1{border-left-color:var(--o1)} .item.o2{border-left-color:var(--o2)} .item.o3{border-left-color:var(--o3)}
.item>summary{list-style:none;cursor:pointer;padding:9px 12px;display:grid;grid-template-columns:auto 1fr auto;gap:4px 10px;align-items:baseline}
.item .code{font:600 12px/1 var(--f-data);color:var(--muted);font-variant-numeric:tabular-nums}
.item .nm{font-weight:600;min-width:0}
.item .tags{display:flex;gap:6px;flex-wrap:wrap;justify-content:flex-end}
.tag{font:600 11px/1 var(--f-data);letter-spacing:.03em;padding:4px 7px;border-radius:999px;background:var(--accent-soft);color:var(--ink);white-space:nowrap}
.tag.block{background:var(--block-soft);color:var(--block)}
.tag.hist{background:transparent;border:1px solid var(--line);color:var(--muted)}
.det{padding:4px 12px 14px;display:grid;gap:12px;min-width:0}
.kv{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:6px 18px;font-size:14px}
.kv div{min-width:0} .kv dt{color:var(--muted);font-size:12px;text-transform:uppercase;letter-spacing:.05em} .kv dd{margin:0;overflow-wrap:anywhere}
.tbl{overflow-x:auto} table{border-collapse:collapse;width:100%;font-size:13px}
th,td{text-align:left;padding:6px 8px;border-bottom:1px solid var(--line);vertical-align:top}
th{color:var(--muted);font-weight:600;font-size:12px;text-transform:uppercase;letter-spacing:.04em}
td.f{font-family:var(--f-data);font-size:12px;color:var(--muted);overflow-wrap:anywhere}
.s-aguardando_aprovacao{color:var(--wait);font-weight:600} .s-devolvido,.s-revisar_por_mudanca{color:var(--block);font-weight:600}
.s-a_fazer,.s-inventario_pendente{color:var(--muted);font-weight:600} .s-aprovado{color:var(--ok);font-weight:600}
h4{margin:0;font:600 13px/1 var(--f-data);text-transform:uppercase;letter-spacing:.06em;color:var(--muted)}
ul.pend{margin:0;padding-left:18px;display:grid;gap:4px;font-size:14px}
ul.pend li.b{color:var(--block)}
.chips{display:flex;flex-wrap:wrap;gap:6px}
.chip{font-size:12px;padding:3px 8px;border-radius:6px;border:1px solid var(--line)} .chip.ativo{border-color:var(--accent);color:var(--accent);font-weight:600}
.chip.teste{border-style:dashed} .chip.fora{color:var(--muted)}
.empty{color:var(--muted);padding:12px 0}
footer .wrap{padding-block:0 32px;color:var(--muted);font-size:13px;display:grid;gap:6px}
@media (max-width:560px){.item>summary{grid-template-columns:1fr}.item .tags{justify-content:flex-start}.bar{position:static}.bar select{flex:1 1 45%}}
"""

JS = r"""
const D=__DATA__, AREAS=__AREAS__;
const LIN={pos:'Pós-graduação',livres:'Cursos Livres',eventos:'Eventos',graduacao:'Graduação'};
const REC={planejar:'no recorte',historico:'histórico',pendencia:'pendência'};
const MID={ativa:'mídia ativa',pausada:'mídia pausada',sem_campanha:'sem campanha',nao_consta:'mídia não consta'};
const QM={'1_por_docente_autorizado':'1 por docente autorizado','1_por_palestrante_autorizado':'1 por palestrante autorizado'};
const CAM={aprovado:'aprovado',pendente_de_aprovacao:'aguarda aprovação',devolvido:'rascunho a revisar'};
const ST={aguardando_aprovacao:'aprovado pelo qa, aguarda aprovação humana',a_fazer:'a fazer',inventario_pendente:'inventário pendente',devolvido:'devolvido para correção',revisar_por_mudanca:'revisar por mudança',nao_aplicavel:'não se aplica',aprovado:'aprovado'};
const $=s=>document.querySelector(s);
const esc=s=>String(s??'').replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const fmt=iso=>iso?iso.split('-').reverse().join('/'):'-';
function fill(sel,vals,label){const el=$(sel);el.innerHTML=`<option value="">${label}</option>`+vals.map(([v,t])=>`<option value="${esc(v)}">${esc(t)}</option>`).join('');}
fill('#f-linha',Object.entries(LIN),'Todas as linhas');
fill('#f-onda',[['1','Onda 1'],['2','Onda 2'],['3','Onda 3'],['x','Fora do recorte']],'Todas as ondas');
fill('#f-area',Object.keys(AREAS).sort((a,b)=>+a.slice(1)-+b.slice(1)).map(a=>[a,a+' '+AREAS[a]]),'Todas as áreas');
fill('#f-status',[['aberto','aberto'],['aberto (contínuo)','aberto (contínuo)'],['verificar','verificar'],['sem venda','sem venda'],['encerrado','encerrado'],['sem página','sem página']],'Todo status do catálogo');
fill('#f-midia',Object.entries(MID),'Toda situação de mídia');
function pass(x){
  const q=$('#f-q').value.trim().toLowerCase(), l=$('#f-linha').value, o=$('#f-onda').value, a=$('#f-area').value, s=$('#f-status').value, m=$('#f-midia').value, b=$('#f-block').checked;
  if(q && !(x.n.toLowerCase().includes(q)||x.ns.toLowerCase().includes(q)||x.c.includes(q)||x.loc.toLowerCase().includes(q))) return false;
  if(l && x.l!==l) return false; if(o==='x' && x.o!==null) return false; if(o && o!=='x' && String(x.o)!==o) return false;
  if(a && x.a!==a) return false; if(s && x.st!==s) return false; if(m && x.m!==m) return false; if(b && !x.bl) return false; return true;}
function item(x){
  const tags=[x.o?`<span class="tag">onda ${x.o}</span>`:`<span class="tag hist">${REC[x.r]}</span>`,x.g?`<span class="tag">GUT ${x.g}</span>`:'',`<span class="tag hist">${esc(MID[x.m])}</span>`,x.bl?'<span class="tag block">bloqueia peça final</span>':''].join('');
  const kit=x.k.length?`<div class="tbl"><table><thead><tr><th>Entrega</th><th>Mín.</th><th>Responsável</th><th>Situação</th><th>Arquivo</th></tr></thead><tbody>${x.k.map(e=>`<tr><td>${esc(e.e)}</td><td>${e.q??esc(QM[e.rq]||'-')}</td><td>${esc(e.rp)}</td><td class="s-${e.s}">${esc(ST[e.s]||e.s)}</td><td class="f">${esc(e.f||'-')}</td></tr>`).join('')}${x.ka.map(e=>`<tr><td>${esc(e.e)} <small>(acréscimo)</small></td><td>${e.q??'-'}</td><td>${esc(e.rp)}</td><td class="s-${e.s}">${esc(ST[e.s]||e.s)}</td><td class="f">${esc(e.f||'-')}</td></tr>`).join('')}</tbody></table></div>`:'<p class="empty">Sem kit neste recorte.</p>';
  const pe=x.pe.length?`<ul class="pend">${x.pe.map(p=>`<li class="${p.b.includes('peca_final')?'b':''}"><b>${esc(p.ref)}:</b> ${esc(p.d)}</li>`).join('')}</ul>`:'<p class="empty">Nenhuma.</p>';
  const ap=x.ap.length?`<ul class="pend">${x.ap.map(p=>`<li><b>${esc(p.ref)}:</b> ${esc(p.o)}</li>`).join('')}</ul>`:'<p class="empty">Nenhuma aberta.</p>';
  const cam=x.cam.length?`<ul class="pend">${x.cam.map(([k,f,e])=>`<li class="${e==='devolvido'?'b':''}"><b>${esc(k)}:</b> <span class="f">${esc(f)}</span> (${esc(CAM[e]||e)})</li>`).join('')}</ul>`:'<p class="empty">Nenhum.</p>';
  const can=`<div class="chips">${x.can.map(([c,e])=>`<span class="chip ${e}">${esc(c)}: ${esc(e)}</span>`).join('')}</div>`;
  const metas=x.mt&&x.mt.verba?`${x.mt.matriculas_alvo} matrículas; verba de R$ ${x.mt.verba.toLocaleString('pt-BR',{minimumFractionDigits:2})} (${esc(x.mt.fonte)})`:'[CONFIRMAR]';
  return `<details class="item o${x.o??'x'}" data-id="${esc(x.id)}"><summary><span class="code">${esc(x.c==='sem-codigo'?'sem código':x.c)}</span><span class="nm">${esc(x.n)}</span><span class="tags">${tags}</span></summary>
  <div class="det"><dl class="kv"><div><dt>Nome no site</dt><dd>${esc(x.ns)}</dd></div><div><dt>Local e modalidade</dt><dd>${esc(x.loc)} · ${esc(x.mod)}</dd></div><div><dt>Início</dt><dd>${fmt(x.i)} (fonte: ${esc(x.fd)})${x.d!=null&&x.d>=0?`, faltam ${x.d} dias`:''}</dd></div>
  ${(x.tu||x.ch)?`<div><dt>Turma e carga horária</dt><dd>${esc(x.tu??'-')} · ${esc(x.ch??'-')}</dd></div>`:''}<div><dt>Status no catálogo</dt><dd>${esc(x.st)}</dd></div>
  <div><dt>Preço no site</dt><dd>${esc(x.p)} <small>(site em 26/10/2026; conferir antes de publicar)</small></dd></div><div><dt>Meta</dt><dd>${metas}</dd></div>
  ${x.gm?`<div><dt>Prioridade (GUT ${x.g})</dt><dd>${esc(x.gm)}</dd></div>`:''}<div><dt>Ficha</dt><dd class="f">${esc(x.fi||'-')}</dd></div></dl>
  <h4>Kit mínimo${x.kt?' ('+esc(x.kt.split('/').pop())+')':''}</h4>${kit}<h4>Canais</h4>${can}<h4>Pendências</h4>${pe}<h4>Aprovações pedidas</h4>${ap}<h4>Arquivos das camadas</h4>${cam}</div></details>`;}
function render(){
  const sel=D.filter(pass); const out=[];
  for(const l of Object.keys(LIN)){
    const xs=sel.filter(x=>x.l===l); if(!xs.length) continue;
    const grupos={}; for(const x of xs){const k=x.a.startsWith('A')?x.a:(x.r==='planejar'?'sem_area':'fora');(grupos[k]=grupos[k]||[]).push(x);}
    const ordem=Object.keys(grupos).sort((a,b)=>(a.startsWith('A')?+a.slice(1):a==='sem_area'?90:99)-(b.startsWith('A')?+b.slice(1):b==='sem_area'?90:99));
    const bl=xs.filter(x=>x.bl).length;
    out.push(`<details class="l1" open><summary><span class="chev">▸</span><h2>${LIN[l]}</h2><span class="meta">${xs.length} itens · ${xs.filter(x=>x.r==='planejar').length} no recorte · ${bl} com bloqueio</span></summary><div class="body">${ordem.map(k=>{
      const g=grupos[k].sort((a,b)=>(a.o??9)-(b.o??9)||(a.i||'9999').localeCompare(b.i||'9999'));
      const nome=k.startsWith('A')?k+' '+AREAS[k]:k==='sem_area'?'Plano próprio':'Fora do recorte (histórico e pendência)';
      return `<details class="l2"${k!=='fora'?' open':''}><summary><span class="chev">▸</span><h3>${esc(nome)}</h3><span class="meta">${g.length} itens</span></summary><div class="items">${g.map(item).join('')}</div></details>`;}).join('')}</div></details>`);}
  $('#tree').innerHTML=out.join('')||'<p class="empty">Nenhum item com estes filtros. Limpe a busca ou escolha outra linha.</p>';
  $('#count').textContent=`${sel.length} de ${D.length} itens`;}
const rec=D.filter(x=>x.r==='planejar'), recG=rec.filter(x=>x.l==='graduacao'), recS=rec.filter(x=>x.l!=='graduacao');
// B11: o recorte do plano é contado sem a Graduação, que é ramo à parte (plano geral, 2.2)
$('#t-total').textContent=D.length; $('#t-rec').textContent=`${recS.length} + ${recG.length}`;
$('#t-o1').textContent=`${recS.filter(x=>x.o===1).length} + ${recG.filter(x=>x.o===1).length}`; $('#t-o2').textContent=rec.filter(x=>x.o===2).length; $('#t-o3').textContent=rec.filter(x=>x.o===3).length;
$('#t-bl').textContent=D.filter(x=>x.bl).length;
$('#t-ag').textContent=rec.filter(x=>x.k.length&&x.k.every(e=>e.s==='aguardando_aprovacao')).length;
document.querySelectorAll('.bar input,.bar select').forEach(el=>el.addEventListener('input',render));
render();
"""

HTML = f"""<title>Mapa de marketing Ufape</title>
<meta name="claude:viewport-fit-sides" content="cover">
<style>{CSS}</style>
<header class="top"><div class="wrap">
<span class="eyebrow">Plano de marketing · recorte de 26/10/2026 · versão 1 de 27/10/2026</span>
<h1>Mapa de marketing Ufape</h1>
<p class="lede">Todos os cursos, turmas, provas e eventos da planilha, com a onda de trabalho, a área, o kit mínimo, os canais, as pendências e o que espera aprovação. Datas vêm da planilha; preço e demais dados vêm do site. Nada aqui foi publicado, enviado ou pago.</p>
</div></header>
<div class="bar"><div class="wrap">
<input id="f-q" type="search" placeholder="Buscar por nome, código ou local" aria-label="Buscar">
<select id="f-linha" aria-label="Linha"></select><select id="f-onda" aria-label="Onda"></select><select id="f-area" aria-label="Área"></select>
<select id="f-status" aria-label="Status do catálogo"></select><select id="f-midia" aria-label="Mídia"></select>
<label class="chk" for="f-block"><input id="f-block" type="checkbox"> Só com bloqueio</label>
<span class="meta" id="count" style="color:var(--muted);font-size:13px"></span>
</div></div>
<main><div class="wrap">
<section class="summary" aria-label="Resumo">
<div class="tile"><b id="t-total"></b><span>itens no catálogo</span></div>
<div class="tile"><b id="t-rec"></b><span>no recorte do plano + Graduação (ramo à parte)</span></div>
<div class="tile"><b id="t-o1"></b><span>onda 1 (27/10 a 06/11) + Graduação</span></div>
<div class="tile"><b id="t-o2"></b><span>onda 2 (07/11 a 27/11)</span></div>
<div class="tile"><b id="t-o3"></b><span>onda 3 (a partir de 30/11)</span></div>
<div class="tile"><b id="t-ag"></b><span>com kit inteiro aprovado pelo qa, à espera da aprovação humana</span></div>
<div class="tile"><b id="t-bl"></b><span>com pendência que bloqueia peça final</span></div>
</section>
<div class="legend"><span><i class="dot" style="background:var(--o1)"></i>Onda 1</span><span><i class="dot" style="background:var(--o2)"></i>Onda 2</span><span><i class="dot" style="background:var(--o3)"></i>Onda 3</span><span><i class="dot" style="background:var(--hist)"></i>Fora do recorte</span><span><i class="dot" style="background:var(--block)"></i>Bloqueia peça final</span></div>
<section id="tree" aria-label="Itens por linha e área"></section>
</div></main>
<footer><div class="wrap">
<p>Fontes: contexto/catalogo-de-cursos.md (planilha "DATAS CURSOS E PÓS" e site lidos em 26/10/2026), plano geral do cmo, planos das ondas 2 e 3 da Pós e revisões do qa-de-marketing. Um JSON por item em saidas/10-operacoes-de-marketing/cursos/.</p>
<p>Prioridade GUT é avaliação do cmo. Metas em reais, vagas restantes, leads e matrículas ainda não foram informados pela Ufape e aparecem como [CONFIRMAR]. Nenhum dado pessoal de aluno ou candidato.</p>
</div></footer>
<script>{JS.replace('__DATA__', DATA).replace('__AREAS__', json.dumps(AREAS, ensure_ascii=False))}</script>
"""
open(S + 'mapa-artifact.html', 'w', encoding='utf-8').write(HTML)
full = '<!doctype html>\n<html lang="pt-BR">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n' + HTML.split('<header')[0] + '</head>\n<body>\n<header' + HTML.split('<header', 1)[1] + '</body>\n</html>\n'
open('saidas/02-estrategia-e-posicionamento/cmo-geral-2026-10-27.html', 'w', encoding='utf-8').write(full)
print('tamanho', len(full))
