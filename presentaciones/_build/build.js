const pptxgen = require("pptxgenjs");
const fs = require("fs");
const path = require("path");

const W = 13.333, H = 7.5, MX = 0.6;
const INK = "0B1F33", PAPER = "F6F4EF", CARD = "FFFFFF", TEXT = "1B2A3A", MUTED = "5B6B7B", AMBER = "F5B83D", SOFT = "E6E1D6", LIGHT = "C9D7E4";
const ACCENT = { 1: "12A5A0", 2: "2F6FED", 3: "E8743B" };
const DAYTAG = { 1: "DÍA 1 · L100", 2: "DÍA 2 · L200", 3: "DÍA 3 · L300" };
const HF = "Segoe UI Semibold", BF = "Segoe UI", CF = "Consolas";
const LOGO_PATH = path.join(__dirname, "assets", "logo_bci.png");
const LOGO = fs.existsSync(LOGO_PATH) ? LOGO_PATH : null;

function est(text, fs, wIn) {
  const cpl = Math.max(6, Math.floor((wIn * 72) / (fs * 0.53)));
  let lines = 0;
  for (const para of String(text).split("\n")) {
    let cur = 0, l = 1;
    for (const w of para.split(/\s+/)) {
      if (!w) continue;
      if (w.length > cpl) { l += Math.ceil(w.length / cpl); cur = w.length % cpl; continue; }
      if (cur + w.length + (cur ? 1 : 0) > cpl) { l++; cur = w.length; } else cur += w.length + (cur ? 1 : 0);
    }
    lines += l;
  }
  return lines;
}
function fit(text, wIn, hIn, max, min = 10, lh = 1.25) {
  for (let f = max; f >= min; f--) if (est(text, f, wIn) * f * lh / 72 <= hIn) return f;
  return min;
}
function fitOne(text, wIn, max, min = 14) {
  for (let f = max; f >= min; f--) if (text.length * f * 0.56 / 72 <= wIn) return f;
  return min;
}
function fitList(items, wIn, hIn, max, min = 11, gapPt = 8) {
  for (let f = max; f >= min; f--) {
    let h = 0;
    for (const t of items) h += est(t, f, wIn) * f * 1.25 / 72 + gapPt / 72;
    if (h <= hIn) return f;
  }
  return min;
}
function mix(c1, c2, t) {
  const a = [0, 2, 4].map(i => parseInt(c1.substr(i, 2), 16));
  const b = [0, 2, 4].map(i => parseInt(c2.substr(i, 2), 16));
  return a.map((v, i) => Math.round(v + (b[i] - v) * t).toString(16).padStart(2, "0")).join("").toUpperCase();
}

function build(contentPath, outDir) {
  const data = JSON.parse(fs.readFileSync(contentPath, "utf8"));
  const day = data.meta.day;
  const AC = ACCENT[day];
  const deck = new pptxgen();
  deck.layout = "LAYOUT_WIDE";
  deck.author = "Microsoft";
  deck.company = "Microsoft";
  deck.title = data.meta.deck_title;
  deck.subject = "Microsoft AI Foundry BCI Training Day";
  deck.lang = "es-CL";
  const SH = () => ({ type: "outer", color: "000000", opacity: 0.12, blur: 6, offset: 2, angle: 90 });

  function light(slide, s) {
    slide.background = { color: PAPER };
    const tfs = fit(s.title, 10.4, 0.95, 32, 22, 1.15);
    slide.addText(s.title, { x: MX, y: 0.4, w: 10.4, h: 1.0, fontFace: HF, fontSize: tfs, bold: true, color: INK, margin: 0, valign: "middle" });
    slide.addShape(deck.ShapeType.roundRect, { x: 11.2, y: 0.55, w: 1.55, h: 0.36, rectRadius: 0.08, fill: { color: AC }, line: { type: "none" } });
    slide.addText(DAYTAG[day], { x: 11.2, y: 0.55, w: 1.55, h: 0.36, fontFace: HF, fontSize: 10.5, bold: true, color: "FFFFFF", align: "center", valign: "middle", margin: 0 });
    slide.addText("Microsoft Foundry · BCI Training Day", { x: MX, y: 7.05, w: 6, h: 0.3, fontFace: BF, fontSize: 10, color: MUTED, margin: 0 });
    slide.slideNumber = { x: 12.2, y: 7.05, w: 0.55, h: 0.3, fontFace: BF, fontSize: 10, color: MUTED, align: "right" };
  }
  function dark(slide) {
    slide.background = { color: INK };
    slide.addShape(deck.ShapeType.ellipse, { x: 9.6, y: -1.6, w: 5.6, h: 5.6, fill: { color: AC, transparency: 82 }, line: { type: "none" } });
    slide.addShape(deck.ShapeType.ellipse, { x: 11.0, y: 4.6, w: 3.8, h: 3.8, fill: { color: AC, transparency: 90 }, line: { type: "none" } });
  }
  function chip(slide, x, y, d, label, color, size = 16) {
    slide.addShape(deck.ShapeType.ellipse, { x, y, w: d, h: d, fill: { color }, line: { type: "none" } });
    slide.addText(String(label), { x, y, w: d, h: d, fontFace: HF, fontSize: size, bold: true, color: "FFFFFF", align: "center", valign: "middle", margin: 0 });
  }
  function card(slide, x, y, w, h, barColor) {
    slide.addShape(deck.ShapeType.rect, { x, y, w, h, fill: { color: CARD }, line: { color: SOFT, width: 0.75 }, shadow: SH() });
    if (barColor) slide.addShape(deck.ShapeType.rect, { x, y, w: 0.09, h, fill: { color: barColor }, line: { type: "none" } });
  }

  for (const s of data.slides) {
    const slide = deck.addSlide();
    const L = s.layout;
    if (L === "title") {
      dark(slide);
      slide.addShape(deck.ShapeType.roundRect, { x: MX, y: 1.0, w: 1.9, h: 0.46, rectRadius: 0.1, fill: { color: AC }, line: { type: "none" } });
      slide.addText(DAYTAG[day], { x: MX, y: 1.0, w: 1.9, h: 0.46, fontFace: HF, fontSize: 14, bold: true, color: "FFFFFF", align: "center", valign: "middle", margin: 0 });
      slide.addText(s.title, { x: MX, y: 1.9, w: 9.0, h: 2.4, fontFace: HF, fontSize: fit(s.title, 9.0, 2.4, 46, 30, 1.12), bold: true, color: "FFFFFF", margin: 0, valign: "top" });
      slide.addText(s.subtitle || "", { x: MX, y: 4.45, w: 8.6, h: 0.9, fontFace: BF, fontSize: fit(s.subtitle || "", 8.6, 0.9, 22, 14), color: LIGHT, margin: 0, valign: "top" });
      slide.addText(s.meta || "", { x: MX, y: 6.2, w: 9, h: 0.4, fontFace: BF, fontSize: 14, color: AMBER, margin: 0 });
      slide.addText("Microsoft · Customer Success", { x: MX, y: 6.65, w: 6, h: 0.35, fontFace: BF, fontSize: 12, color: LIGHT, margin: 0 });
      if (LOGO) {
        slide.addShape(deck.ShapeType.roundRect, { x: 10.15, y: 0.85, w: 2.6, h: 1.4, rectRadius: 0.1, fill: { color: "FFFFFF" }, line: { type: "none" }, shadow: SH() });
        slide.addImage({ path: LOGO, x: 10.15 + (2.6 - 1.75) / 2, y: 0.85 + (1.4 - 0.808) / 2, w: 1.75, h: 0.808 });
      }
    } else if (L === "section") {
      dark(slide);
      slide.addText(String(s.number).padStart(2, "0"), { x: MX, y: 0.85, w: 4, h: 2.4, fontFace: HF, fontSize: 120, bold: true, color: AC, margin: 0, valign: "middle" });
      slide.addText(s.title, { x: MX, y: 3.4, w: 10.2, h: 1.65, fontFace: HF, fontSize: fit(s.title, 10.2, 1.65, 44, 26, 1.12), bold: true, color: "FFFFFF", margin: 0, valign: "top" });
      if (s.subtitle) slide.addText(s.subtitle, { x: MX, y: 5.2, w: 9.4, h: 1.0, fontFace: BF, fontSize: fit(s.subtitle, 9.4, 0.9, 20, 14), color: LIGHT, margin: 0, valign: "top" });
      if (s.duration) {
        const chipW = Math.max(1.5, s.duration.length * 0.125 + 0.5);
        slide.addShape(deck.ShapeType.roundRect, { x: MX, y: 6.4, w: chipW, h: 0.42, rectRadius: 0.1, fill: { color: INK }, line: { color: AMBER, width: 1.25 } });
        slide.addText(s.duration, { x: MX, y: 6.4, w: chipW, h: 0.42, fontFace: HF, fontSize: 13, bold: true, color: AMBER, align: "center", valign: "middle", margin: 0 });
      }
    } else if (L === "closing") {
      dark(slide);
      slide.addText(s.title, { x: MX, y: 2.0, w: 10.0, h: 1.8, fontFace: HF, fontSize: fit(s.title, 10.0, 1.8, 54, 32, 1.12), bold: true, color: "FFFFFF", margin: 0, valign: "middle" });
      if (s.message) slide.addText(s.message, { x: MX, y: 4.0, w: 9.2, h: 1.1, fontFace: BF, fontSize: fit(s.message, 9.2, 1.1, 22, 14), color: LIGHT, margin: 0, valign: "top" });
      slide.addText("Pablo Braconi · Valentina Grajales · Microsoft", { x: MX, y: 6.3, w: 9, h: 0.4, fontFace: BF, fontSize: 14, color: AMBER, margin: 0 });
    } else if (L === "takeaway") {
      dark(slide);
      slide.addText(s.title, { x: MX, y: 0.5, w: 11.5, h: 1.0, fontFace: HF, fontSize: fit(s.title, 11.5, 1.0, 34, 24, 1.15), bold: true, color: "FFFFFF", margin: 0, valign: "middle" });
      const n = s.points.length, top = 1.8, rowH = (6.6 - top) / n;
      s.points.forEach((p, i) => {
        const y = top + i * rowH;
        slide.addText(String(i + 1), { x: MX, y, w: 1.1, h: rowH - 0.15, fontFace: HF, fontSize: 54, bold: true, color: AC, margin: 0, valign: "middle" });
        slide.addText(p, { x: 1.9, y, w: 10.5, h: rowH - 0.15, fontFace: BF, fontSize: fit(p, 10.5, rowH - 0.15, 24, 15), color: "FFFFFF", margin: 0, valign: "middle" });
      });
    } else {
      light(slide, s);
      const top = 1.65, bottom = 6.85, ch = bottom - top, cw = W - 2 * MX;
      if (L === "agenda") {
        const n = s.items.length, rowH = Math.min(0.62, ch / n);
        s.items.forEach((it, i) => {
          const y = top + 0.05 + i * rowH;
          slide.addShape(deck.ShapeType.roundRect, { x: MX, y: y + 0.04, w: 1.9, h: rowH - 0.14, rectRadius: 0.08, fill: { color: i % 2 ? INK : AC }, line: { type: "none" } });
          slide.addText(it.time, { x: MX, y: y + 0.04, w: 1.9, h: rowH - 0.14, fontFace: HF, fontSize: 14, bold: true, color: "FFFFFF", align: "center", valign: "middle", margin: 0 });
          slide.addText(it.title, { x: 2.75, y, w: 5.0, h: rowH - 0.06, fontFace: HF, fontSize: 17, bold: true, color: INK, valign: "middle", margin: 0 });
          if (it.detail) slide.addText(it.detail, { x: 7.8, y, w: 4.95, h: rowH - 0.06, fontFace: BF, fontSize: fit(it.detail, 4.95, rowH - 0.06, 13, 10), color: MUTED, valign: "middle", margin: 0 });
        });
      } else if (L === "bullets") {
        const hasCallout = !!s.callout;
        const bw = hasCallout ? 7.7 : cw;
        card(slide, MX, top, bw, ch, AC);
        const f = fitList(s.bullets, bw - 0.9, ch - 0.5, hasCallout ? 22 : 26, 13, hasCallout ? 10 : 16);
        const runs = s.bullets.map((b, i) => ({ text: b, options: { bullet: { indent: 18 }, breakLine: i < s.bullets.length - 1, paraSpaceAfter: hasCallout ? 10 : 16 } }));
        slide.addText(runs, { x: MX + 0.35, y: top + 0.25, w: bw - 0.7, h: ch - 0.5, fontFace: BF, fontSize: f, color: TEXT, valign: "top", margin: 0 });
        if (hasCallout) {
          const x = MX + bw + 0.3, w = cw - bw - 0.3;
          slide.addShape(deck.ShapeType.rect, { x, y: top, w, h: ch, fill: { color: INK }, line: { type: "none" } });
          slide.addText("CLAVE", { x: x + 0.35, y: top + 0.35, w: w - 0.7, h: 0.35, fontFace: HF, fontSize: 13, bold: true, color: AMBER, margin: 0 });
          slide.addText(s.callout, { x: x + 0.35, y: top + 0.85, w: w - 0.7, h: ch - 1.2, fontFace: BF, fontSize: fit(s.callout, w - 0.7, ch - 1.2, 22, 14), color: "FFFFFF", valign: "top", margin: 0 });
        }
      } else if (L === "cards") {
        const n = s.cards.length, gap = 0.3, cwid = (cw - gap * (n - 1)) / n;
        const chh = s.footer ? ch - 0.8 : ch;
        const fCB = Math.min(...s.cards.map(c => fit(c.body, cwid - 0.55, chh - 2.2, 20, 12)));
        const fCT = Math.min(...s.cards.map(c => fit(c.title, cwid - 0.55, 0.9, 20, 14, 1.15)));
        s.cards.forEach((c, i) => {
          const x = MX + i * (cwid + gap);
          card(slide, x, top, cwid, chh, AC);
          chip(slide, x + 0.3, top + 0.3, 0.6, i + 1, AC, 18);
          slide.addText(c.title, { x: x + 0.3, y: top + 1.05, w: cwid - 0.55, h: 0.9, fontFace: HF, fontSize: fCT, bold: true, color: INK, valign: "top", margin: 0 });
          slide.addText(c.body, { x: x + 0.3, y: top + 1.85, w: cwid - 0.55, h: chh - 2.2, fontFace: BF, fontSize: fCB, color: TEXT, valign: "top", margin: 0 });
        });
        if (s.footer) slide.addText(s.footer, { x: MX, y: top + chh + 0.15, w: cw, h: 0.55, fontFace: BF, fontSize: fit(s.footer, cw, 0.55, 15, 11), italic: true, color: MUTED, valign: "middle", margin: 0 });
      } else if (L === "grid") {
        const n = s.cells.length, cols = n === 4 ? 2 : 3, rows = n === 4 ? 2 : 2, gap = 0.28;
        const tw = (cw - gap * (cols - 1)) / cols, th = (ch - gap * (rows - 1)) / rows;
        const fGB = Math.min(...s.cells.map(c => fit(c.body, tw - 0.55, th - 1.1, 18, 11)));
        const fGT = Math.min(...s.cells.map(c => fit(c.title, tw - 1.2, 0.6, 18, 12, 1.1)));
        s.cells.forEach((c, i) => {
          const x = MX + (i % cols) * (tw + gap), y = top + Math.floor(i / cols) * (th + gap);
          card(slide, x, y, tw, th, i % 2 ? INK : AC);
          chip(slide, x + 0.3, y + 0.25, 0.46, i + 1, i % 2 ? INK : AC, 14);
          slide.addText(c.title, { x: x + 0.95, y: y + 0.2, w: tw - 1.2, h: 0.6, fontFace: HF, fontSize: fGT, bold: true, color: INK, valign: "middle", margin: 0 });
          slide.addText(c.body, { x: x + 0.3, y: y + 0.95, w: tw - 0.55, h: th - 1.1, fontFace: BF, fontSize: fGB, color: TEXT, valign: "top", margin: 0 });
        });
      } else if (L === "compare") {
        const gap = 0.33, cwid = (cw - gap) / 2, hh = 0.7, bh = s.verdict ? ch - hh - 1.0 : ch - hh;
        const fCmp = Math.min(fitList(s.left.items, cwid - 0.9, bh - 0.4, 22, 12, 12), fitList(s.right.items, cwid - 0.9, bh - 0.4, 22, 12, 12));
        [["left", AC], ["right", INK]].forEach(([k, col], idx) => {
          const side = s[k], x = MX + idx * (cwid + gap);
          slide.addShape(deck.ShapeType.rect, { x, y: top, w: cwid, h: hh, fill: { color: col }, line: { type: "none" } });
          slide.addText(side.title, { x: x + 0.3, y: top, w: cwid - 0.6, h: hh, fontFace: HF, fontSize: 20, bold: true, color: "FFFFFF", valign: "middle", margin: 0 });
          card(slide, x, top + hh, cwid, bh, null);
          const f = fCmp;
          slide.addText(side.items.map((b, i) => ({ text: b, options: { bullet: { indent: 16 }, breakLine: i < side.items.length - 1, paraSpaceAfter: 12 } })), { x: x + 0.3, y: top + hh + 0.2, w: cwid - 0.6, h: bh - 0.4, fontFace: BF, fontSize: f, color: TEXT, valign: "top", margin: 0 });
        });
        if (s.verdict) {
          slide.addShape(deck.ShapeType.rect, { x: MX, y: bottom - 0.75, w: cw, h: 0.75, fill: { color: AMBER }, line: { type: "none" } });
          slide.addText(s.verdict, { x: MX + 0.3, y: bottom - 0.75, w: cw - 0.6, h: 0.75, fontFace: HF, fontSize: fit(s.verdict, cw - 0.6, 0.75, 17, 12), bold: true, color: INK, valign: "middle", margin: 0 });
        }
      } else if (L === "process") {
        const n = s.steps.length, colw = cw / n, cy = top + 0.5;
        const fPB = Math.min(...s.steps.map(st => fit(st.body, colw - 0.7, ch - 2.85, 19, 11)));
        const fPT = Math.min(...s.steps.map(st => fit(st.title, colw - 0.25, 0.8, 20, 14, 1.15)));
        slide.addShape(deck.ShapeType.line, { x: MX + 0.4, y: cy + 0.4, w: cw - colw + 0.0, h: 0, line: { color: LIGHT, width: 3 } });
        s.steps.forEach((st, i) => {
          const x = MX + i * colw;
          chip(slide, x, cy, 0.8, i + 1, i % 2 ? INK : AC, 22);
          slide.addText(st.title, { x, y: cy + 1.0, w: colw - 0.25, h: 0.8, fontFace: HF, fontSize: fPT, bold: true, color: INK, valign: "top", margin: 0 });
          card(slide, x, cy + 1.85, colw - 0.25, ch - 2.45, i % 2 ? INK : AC);
          slide.addText(st.body, { x: x + 0.25, y: cy + 2.05, w: colw - 0.58, h: ch - 2.85, fontFace: BF, fontSize: fPB, color: TEXT, valign: "top", margin: 0 });
        });
      } else if (L === "layers") {
        const n = s.layers.length, gap = 0.16, lh = (ch - gap * (n - 1)) / n, lw = 3.6;
        const fLB = Math.min(...s.layers.map(ly => fit(ly.body, cw - lw - 0.6, lh - 0.1, 17, 11)));
        const fLT = Math.min(...s.layers.map(ly => fit(ly.title, lw - 0.5, lh - 0.1, 19, 12, 1.15)));
        s.layers.forEach((ly, i) => {
          const y = top + i * (lh + gap), col = mix(INK, AC, i / Math.max(1, n - 1));
          slide.addShape(deck.ShapeType.rect, { x: MX, y, w: lw, h: lh, fill: { color: col }, line: { type: "none" } });
          slide.addText(ly.title, { x: MX + 0.25, y, w: lw - 0.5, h: lh, fontFace: HF, fontSize: fLT, bold: true, color: "FFFFFF", valign: "middle", margin: 0 });
          card(slide, MX + lw, y, cw - lw, lh, null);
          slide.addText(ly.body, { x: MX + lw + 0.3, y, w: cw - lw - 0.6, h: lh, fontFace: BF, fontSize: fLB, color: TEXT, valign: "middle", margin: 0 });
        });
      } else if (L === "table") {
        const nc = s.columns.length;
        const fs = s.rows.length <= 4 ? 17 : s.rows.length <= 5 ? 16 : s.rows.length <= 6 ? 14.5 : 13.5;
        const longest = (t) => Math.max(...String(t).split(/\s+/).map(w => w.length));
        const minW = s.columns.map((c, ci) => Math.max(longest(c) * 1.1, ...s.rows.map(r => Math.min(longest(r[ci]), 14))) * fs * 0.58 / 72 + 0.45);
        const wts = s.columns.map((c, ci) => Math.min(40, Math.max(8, c.length, ...s.rows.map(r => String(r[ci]).length))));
        const sum = wts.reduce((a, b) => a + b, 0);
        let colW = wts.map(w => (cw * w) / sum);
        colW = colW.map((w, i) => Math.max(w, minW[i]));
        const tot = colW.reduce((a, b) => a + b, 0);
        colW = colW.map(w => (w * cw) / tot);
        const head = s.columns.map(c => ({ text: c, options: { bold: true, color: "FFFFFF", fill: { color: INK }, fontFace: HF, fontSize: fs, valign: "middle" } }));
        const body = s.rows.map((r, ri) => r.map((c, ci) => ({ text: String(c), options: { color: TEXT, fill: { color: ri % 2 ? "EFEBE2" : CARD }, fontFace: ci === 0 ? HF : BF, bold: ci === 0, fontSize: fs, valign: "middle" } })));
        slide.addTable([head, ...body], { x: MX, y: top, w: cw, colW, border: { type: "solid", pt: 0.75, color: SOFT }, margin: [0.07, 0.14, 0.07, 0.14], rowH: Math.min(0.85, (s.note ? 4.6 : 5.1) / (s.rows.length + 1)) });
        if (s.note) slide.addText(s.note, { x: MX, y: 6.45, w: cw, h: 0.45, fontFace: BF, fontSize: 12, italic: true, color: MUTED, margin: 0, valign: "middle" });
      } else if (L === "code") {
        const ph = s.caption ? ch - 0.7 : ch;
        slide.addShape(deck.ShapeType.rect, { x: MX, y: top, w: cw, h: ph, fill: { color: "0D1B2A" }, line: { type: "none" } });
        slide.addShape(deck.ShapeType.roundRect, { x: W - MX - 1.5, y: top + 0.18, w: 1.3, h: 0.34, rectRadius: 0.08, fill: { color: AC }, line: { type: "none" } });
        slide.addText(String(s.language || "code").toUpperCase(), { x: W - MX - 1.5, y: top + 0.18, w: 1.3, h: 0.34, fontFace: HF, fontSize: 10.5, bold: true, color: "FFFFFF", align: "center", valign: "middle", margin: 0 });
        const lines = s.code.split("\n").length;
        const f = Math.min(16, Math.floor(((ph - 0.9) * 72) / (lines * 1.3)), Math.floor(((cw - 0.8) * 72) / (Math.max(...s.code.split("\n").map(l => l.length), 20) * 0.6)));
        slide.addText(s.code, { x: MX + 0.4, y: top + 0.65, w: cw - 0.8, h: ph - 0.85, fontFace: CF, fontSize: Math.max(10, f), color: "E6EDF3", valign: "top", margin: 0, paraSpaceAfter: 0 });
        if (s.caption) slide.addText(s.caption, { x: MX, y: top + ph + 0.1, w: cw, h: 0.5, fontFace: BF, fontSize: 13, italic: true, color: MUTED, margin: 0, valign: "middle" });
      } else if (L === "stats") {
        const n = s.stats.length, gap = 0.3, sw = (cw - gap * (n - 1)) / n, sh = s.note ? ch - 0.8 : ch;
        s.stats.forEach((st, i) => {
          const x = MX + i * (sw + gap);
          card(slide, x, top, sw, sh, i % 2 ? INK : AC);
          slide.addText(st.value, { x: x + 0.35, y: top + 0.5, w: sw - 0.6, h: 1.6, fontFace: HF, fontSize: fitOne(st.value, sw - 0.6, 66, 22), bold: true, color: i % 2 ? INK : AC, valign: "middle", margin: 0 });
          slide.addText(st.label, { x: x + 0.35, y: top + 2.3, w: sw - 0.6, h: sh - 2.6, fontFace: BF, fontSize: fit(st.label, sw - 0.6, sh - 2.6, 18, 12), color: TEXT, valign: "top", margin: 0 });
        });
        if (s.note) slide.addText(s.note, { x: MX, y: top + sh + 0.15, w: cw, h: 0.55, fontFace: BF, fontSize: 13, italic: true, color: MUTED, margin: 0, valign: "middle" });
      } else if (L === "demo") {
        const lw = 4.7, sh = s.expected ? ch - 0.85 : ch;
        slide.addShape(deck.ShapeType.rect, { x: MX, y: top, w: lw, h: sh, fill: { color: INK }, line: { type: "none" } });
        slide.addShape(deck.ShapeType.roundRect, { x: MX + 0.35, y: top + 0.35, w: 1.2, h: 0.4, rectRadius: 0.08, fill: { color: AMBER }, line: { type: "none" } });
        slide.addText("DEMO", { x: MX + 0.35, y: top + 0.35, w: 1.2, h: 0.4, fontFace: HF, fontSize: 13, bold: true, color: INK, align: "center", valign: "middle", margin: 0 });
        slide.addText(s.scenario, { x: MX + 0.35, y: top + 1.0, w: lw - 0.7, h: sh - 1.3, fontFace: BF, fontSize: fit(s.scenario, lw - 0.7, sh - 1.3, 20, 13), color: "FFFFFF", valign: "top", margin: 0 });
        const n = s.steps.length, rx = MX + lw + 0.4, rw = cw - lw - 0.4, rh = sh / n;
        const fDS = Math.min(...s.steps.map(st => fit(st, rw - 0.8, rh - 0.1, 18, 12)));
        s.steps.forEach((st, i) => {
          const y = top + i * rh;
          chip(slide, rx, y + (rh - 0.5) / 2, 0.5, i + 1, AC, 15);
          slide.addText(st, { x: rx + 0.75, y, w: rw - 0.8, h: rh, fontFace: BF, fontSize: fDS, color: TEXT, valign: "middle", margin: 0 });
        });
        if (s.expected) {
          slide.addShape(deck.ShapeType.rect, { x: MX, y: top + sh + 0.15, w: cw, h: 0.7, fill: { color: AMBER }, line: { type: "none" } });
          slide.addText("Resultado esperado: " + s.expected, { x: MX + 0.3, y: top + sh + 0.15, w: cw - 0.6, h: 0.7, fontFace: HF, fontSize: fit("Resultado esperado: " + s.expected, cw - 0.6, 0.7, 15, 11), bold: true, color: INK, valign: "middle", margin: 0 });
        }
      } else if (L === "lab") {
        slide.addShape(deck.ShapeType.rect, { x: MX, y: top, w: cw, h: 0.95, fill: { color: AC }, line: { type: "none" } });
        slide.addText([{ text: "LAB  ", options: { bold: true, color: INK } }, { text: s.objective, options: { color: "FFFFFF", bold: true } }], { x: MX + 0.3, y: top, w: cw - 0.6, h: 0.95, fontFace: HF, fontSize: fit("LAB  " + s.objective, cw - 0.6, 0.9, 20, 13), valign: "middle", margin: 0 });
        const sy = top + 1.2, sh = bottom - sy, lw = 7.9;
        card(slide, MX, sy, lw, sh, AC);
        const n = s.steps.length, rh = (sh - 0.3) / n;
        const fLS = Math.min(...s.steps.map(st => fit(st, lw - 1.2, rh - 0.05, 17, 11)));
        s.steps.forEach((st, i) => {
          const y = sy + 0.15 + i * rh;
          chip(slide, MX + 0.3, y + (rh - 0.46) / 2, 0.46, i + 1, i % 2 ? INK : AC, 14);
          slide.addText(st, { x: MX + 0.95, y, w: lw - 1.2, h: rh, fontFace: BF, fontSize: fLS, color: TEXT, valign: "middle", margin: 0 });
        });
        const rx = MX + lw + 0.3, rw = cw - lw - 0.3;
        card(slide, rx, sy, rw, sh, INK);
        let yy = sy + 0.25;
        if (s.time) {
          slide.addText([{ text: "Tiempo  ", options: { color: MUTED } }, { text: s.time, options: { bold: true, color: INK } }], { x: rx + 0.3, y: yy, w: rw - 0.5, h: 0.4, fontFace: HF, fontSize: 15, margin: 0, valign: "middle" });
          yy += 0.55;
        }
        if (s.deliverables && s.deliverables.length) {
          slide.addText("Entregables", { x: rx + 0.3, y: yy, w: rw - 0.5, h: 0.35, fontFace: HF, fontSize: 13, bold: true, color: AC, margin: 0 });
          yy += 0.4;
          const dh = (s.repoUrl ? sh - (yy - sy) - 1.0 : sh - (yy - sy) - 0.2);
          const f = fitList(s.deliverables, rw - 0.9, dh, 15, 11, 6);
          slide.addText(s.deliverables.map((b, i) => ({ text: b, options: { bullet: { indent: 14 }, breakLine: i < s.deliverables.length - 1, paraSpaceAfter: 6 } })), { x: rx + 0.3, y: yy, w: rw - 0.5, h: dh, fontFace: BF, fontSize: f, color: TEXT, valign: "top", margin: 0 });
        }
        if (s.repoUrl) {
          slide.addText(s.repoLabel || "Repositorio", { x: rx + 0.3, y: sy + sh - 0.95, w: rw - 0.5, h: 0.3, fontFace: HF, fontSize: 12, bold: true, color: AC, margin: 0 });
          slide.addText([{ text: s.repoUrl.replace("https://", ""), options: { hyperlink: { url: s.repoUrl }, color: AC, underline: true } }], { x: rx + 0.3, y: sy + sh - 0.65, w: rw - 0.5, h: 0.5, fontFace: BF, fontSize: 11, margin: 0, valign: "top" });
        }
      } else if (L === "resources") {
        const n = s.links.length, rh = Math.min(0.72, ch / n);
        s.links.forEach((l, i) => {
          const y = top + i * rh;
          chip(slide, MX, y + (rh - 0.4) / 2, 0.4, i + 1, i % 2 ? INK : AC, 12);
          slide.addText(l.label, { x: MX + 0.7, y, w: 5.2, h: rh, fontFace: HF, fontSize: fit(l.label, 5.2, rh - 0.1, 16, 11), bold: true, color: INK, valign: "middle", margin: 0 });
          slide.addText([{ text: l.url.replace("https://", ""), options: { hyperlink: { url: l.url }, color: AC, underline: true } }], { x: 6.5, y, w: 6.25, h: rh, fontFace: BF, fontSize: fit(l.url, 6.25, rh - 0.1, 13, 9), valign: "middle", margin: 0 });
        });
      }
    }
    if (s.notes) slide.addNotes(s.notes);
  }
  fs.mkdirSync(outDir, { recursive: true });
  const out = path.join(outDir, data.meta.filename + ".pptx");
  return deck.writeFile({ fileName: out }).then(() => out);
}

if (require.main === module) {
  const [, , content, outDir] = process.argv;
  build(content, outDir || ".").then(p => console.log("OK", p)).catch(e => { console.error(e); process.exit(1); });
}
module.exports = { build };





