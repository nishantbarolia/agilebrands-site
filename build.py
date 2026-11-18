import os
SITE='https://agilebrands.in'
YT='https://www.youtube.com/@Agile_Brands'
IG='https://www.instagram.com/_agilebrands/'

def head(title,desc,path):
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{SITE}{path}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Agile Brands">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{SITE}{path}">
<meta property="og:image" content="{SITE}/img/og.jpg">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0D1014">
<link rel="icon" href="/img/favicon.png" type="image/png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600;9..144,700&family=Inter:wght@400;500;600;700&display=swap">
<link rel="stylesheet" href="/styles.css">
</head>
<body>
'''

def header(cta=True,links=None):
    links=links or [('/#courses','Courses'),('/#who','Who it’s for'),('/#pricing','Pricing'),('/#youtube','Free on YouTube')]
    nav=''.join(f'<a href="{h}">{t}</a>' for h,t in links)
    btn='<a class="btn btn-p" href="#" data-waitlist="Phase-Gate Innovation" data-label="Join the Phase-Gate waitlist">Join the waitlist</a>' if cta else ''
    return f'''<header class="hdr"><div class="wrap">
<a class="brand" href="/" aria-label="Agile Brands home"><img src="/img/mark.svg" alt="" width="58" height="34"><span><b>Agile Brands</b><small>A Brand &amp; Innovation Academy</small></span></a>
<nav class="nav" aria-label="Main">{nav}{btn}</nav>
</div></header>
<main>
'''

FOOT=f'''</main>
<footer class="ftr"><div class="wrap">
<div style="max-width:320px"><a class="brand" href="/"><img src="/img/mark.svg" alt="" width="58" height="34"><span><b>Agile Brands</b><small>A Brand &amp; Innovation Academy</small></span></a>
<p style="margin-top:14px">Real business cases, seen through a real marketing lens.</p></div>
<div><h4>Courses</h4><ul><li><a href="/phase-gate.html">Phase-Gate Innovation</a></li><li><a href="/#courses">Demand Spaces · soon</a></li><li><a href="/#courses">Ecom Listings &amp; Campaigning · soon</a></li></ul></div>
<div><h4>Follow</h4><ul><li><a href="{YT}" rel="noopener" target="_blank">YouTube · @Agile_Brands</a></li><li><a href="{IG}" rel="noopener" target="_blank">Instagram · @_agilebrands</a></li></ul></div>
<div><h4>Contact</h4><ul><li><a href="mailto:learning@agilebrands.in">learning@agilebrands.in</a></li><li><a href="mailto:partner@agilebrands.in">Become a partner · partner@agilebrands.in</a></li><li><a href="/contact.html">Contact us</a></li></ul></div>
<div><h4>Policies</h4><ul><li><a href="/terms.html">Terms of use</a></li><li><a href="/privacy.html">Privacy policy</a></li><li><a href="/refunds.html">Refund &amp; cancellation</a></li><li><a href="/delivery.html">Delivery policy</a></li></ul></div>
<div class="bottom">Agile Brands is a SimpleDesigns brand · © 2026 · All prices in Indian rupees</div>
</div></footer>
<div class="modal" id="waitlist" role="dialog" aria-modal="true" aria-labelledby="wl-title">
<div class="dlg card">
<button class="x" type="button" data-close aria-label="Close">×</button>
<div class="form stack">
<p class="kick">Launching December 2026</p>
<h3 id="wl-title">Join the waitlist</h3>
<p class="mut" style="font-size:15px">We'll email you the day enrolment opens. Nothing else.</p>
<form class="stack" style="gap:12px">
<label>Name<input name="name" required autocomplete="name" maxlength="80"></label>
<label>Email<input name="email" type="email" required autocomplete="email" maxlength="120"></label>
<label>Interested in<select name="course"><option>Phase-Gate Innovation</option><option>Demand Spaces</option><option>Ecom Listings &amp; Campaigning</option><option>All Agile Brands courses</option></select></label>
<input class="hp" type="text" name="_honey" tabindex="-1" autocomplete="off" aria-hidden="true">
<button class="btn btn-p" type="submit">Join the waitlist</button>
<p class="err" style="color:#F4ABA3;font-size:14px">That didn't go through. Please try again, or write to learning@agilebrands.in.</p>
<p class="mut2" style="font-size:13px">By joining you agree to our <a href="/privacy.html">privacy policy</a>.</p>
</form>
</div>
<div class="ok stack" style="flex-direction:column">
<p class="kick">You're on the list</p>
<h3>Thank you</h3>
<p class="mut">We'll write to you the day enrolment opens. Meanwhile, the free episodes are on <a href="{YT}" target="_blank" rel="noopener">YouTube</a>.</p>
<button class="btn btn-o" type="button" data-close>Done</button>
</div>
</div></div>
<script src="/site.js"></script>
</body></html>
'''

ICON={'brand':'<path d="M4 20 L10 12 L14 16 L20 6"/><path d="M15 6 H20 V11"/>',
'rd':'<path d="M9 3 V9 L4 19 A1 1 0 0 0 5 20.5 H19 A1 1 0 0 0 20 19 L15 9 V3"/><path d="M8 3 H16"/><path d="M7 14 H17"/>',
'd2c':'<path d="M4 8 H20 L19 20 H5 Z"/><path d="M9 8 V6 A3 3 0 0 1 15 6 V8"/>'}
def ic(k): return f'<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#F2A93B" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICON[k]}</svg>'

EPS=[('Everyone is launching.','A bird’s-eye view of a world where everyone innovates'),('Same wave, a thousand products.','Why everyone rides the same trends'),('The tweak economy.','How brands stand out on a crowded shelf'),('Expensive lessons.','Every big failure starts as an idea someone believed in'),('What winners do differently.','The surprising answer: it’s rarely the idea')]
eps=''.join(f'<a class="ep" href="{YT}" target="_blank" rel="noopener"><img src="/img/ie{i+1}.jpg" alt="Episode {i+1}: {t}" width="640" height="360" loading="lazy" style="aspect-ratio:16/9;width:100%;object-fit:cover"><span class="meta"><b style="color:var(--ink);display:block;font-size:15px">Ep {i+1} · {t.rstrip(".")}</b>{s}</span></a>' for i,(t,s) in enumerate(EPS))

INDEX=head('Agile Brands · A Brand & Innovation Academy','Advanced FMCG marketing lessons that aren’t taught in classrooms: brand, innovation and quick commerce, taught the way they’re practised. First course: Phase-Gate Innovation.','/')+header()+f'''
<section class="hero"><div class="wrap">
<div class="hero-l">
<p class="kick">An FMCG marketing academy</p>
<h1>Advanced marketing lessons that aren’t taught in classrooms.</h1>
<p class="lead">Brand, innovation and quick commerce, taught the way they’re actually practised in FMCG. Real business cases, seen through a real marketing lens.</p>
<div class="row"><span class="chip">Brand</span><span class="chip">Innovation</span><span class="chip">Quick commerce</span></div>
<div class="row" style="gap:14px;margin-top:6px"><a class="btn btn-p" href="/phase-gate.html">See the first course</a><a class="btn btn-o" href="#youtube">Watch free episodes</a></div>
</div>
<div class="hero-r"><a class="trailer" href="/phase-gate.html" aria-label="Phase-Gate Innovation course"><img src="/img/trailer_thumb.jpg" alt="Phase-Gate Innovation: an idea passing through four gates, with Go, Redo, Hold and Kill decisions" width="1280" height="720"><span class="shade"></span><span class="cap"><span>Course 01 · Phase-Gate Innovation</span><small>DEC 2026</small></span></a></div>
</div></section>

<section id="courses" class="band"><div class="wrap stack" style="gap:32px">
<div class="stack" style="gap:10px"><p class="kick">Courses</p><h2>One course at a time, built to be used at work</h2></div>
<div class="grid3">
<article class="card course"><span class="tag next">LAUNCHING DEC 2026</span><span class="num">COURSE 01</span><h3>Phase-Gate Innovation</h3><p>Decide which launches deserve to reach the shelf, before a senior opinion carries them there.</p><a class="lnk" href="/phase-gate.html">View course →</a></article>
<article class="card course"><span class="tag soon">COMING SOON</span><span class="num">COURSE 02</span><h3>Demand Spaces</h3><p>Find where your brand can really win.</p><button class="lnk" type="button" data-waitlist="Demand Spaces" data-label="Get notified: Demand Spaces">Notify me at launch →</button></article>
<article class="card course"><span class="tag soon">COMING SOON</span><span class="num">COURSE 03</span><h3>Ecom Listings &amp; Campaigning</h3><p>Win the digital and quick-commerce shelf.</p><button class="lnk" type="button" data-waitlist="Ecom Listings &amp; Campaigning" data-label="Get notified: Ecom Listings &amp; Campaigning">Notify me at launch →</button></article>
</div></div></section>

<section id="who"><div class="wrap stack" style="gap:28px">
<div class="stack" style="gap:10px"><p class="kick">Who it’s for</p><h2>Built for the people who make brands move</h2><p class="mut">Tap a role to see what it gets you.</p></div>
<div class="roles">
<button class="role" type="button" aria-pressed="false" data-panel="r1">{ic('brand')}Brand &amp; marketing managers</button>
<button class="role" type="button" aria-pressed="false" data-panel="r2">{ic('rd')}Innovation &amp; R&amp;D teams</button>
<button class="role" type="button" aria-pressed="false" data-panel="r3">{ic('d2c')}D2C founders &amp; entrepreneurs</button>
</div>
<div class="card rpanel" id="r1"><h3>Brand &amp; marketing managers</h3><p class="mut" style="margin-top:8px">You own the launch calendar, the brand story and the numbers behind them. These lessons give you the decision tools that sit behind the job, not the textbook version of it.</p><ul><li>Run gate reviews that end in a clear call</li><li>Read demand before you brief a new product</li><li>Plan listings and campaigns for the digital shelf</li></ul></div>
<div class="card rpanel" id="r2"><h3>Innovation &amp; R&amp;D teams</h3><p class="mut" style="margin-top:8px">Overloaded with requests, many of which will never reach the market. Learn how the business side decides, so the right projects reach your bench and the wrong ones stop early.</p><ul><li>Filter briefs early with clear gate criteria</li><li>Speak the language of the business case</li><li>Spend lab time on projects with a real path to shelf</li></ul></div>
<div class="card rpanel" id="r3"><h3>D2C founders &amp; entrepreneurs</h3><p class="mut" style="margin-top:8px">Every launch bet is your own money, so every call has to count. Get the processes large FMCG companies use, sized for a team of a few people.</p><ul><li>Launch with a decision process, not a hunch</li><li>Pick the listings and campaigns that convert</li><li>Learn from real brand cases, decision by decision</li></ul></div>
</div></section>

<section id="pricing" class="band"><div class="wrap stack" style="gap:28px">
<div class="stack" style="gap:10px"><p class="kick">Pricing</p><h2>Start with the masterclass, or take the whole course</h2></div>
<p class="note">Enrolment opens in December 2026. Join the waitlist and we'll email you the day it does.</p>
<div class="grid3">
<div class="card price"><span style="font-weight:700;font-size:18px">Masterclass</span><span class="amt">₹449</span><span class="mut2" style="font-size:14px">per course · one-time</span><ul><li>About an hour of lessons</li><li>A quiz after every gate</li><li>Watch at your own pace</li></ul><a class="btn btn-o" href="#" data-waitlist="Phase-Gate Innovation" data-label="Join the Phase-Gate waitlist">Join the waitlist</a></div>
<div class="card price"><span style="font-weight:700;font-size:18px">Full course</span><span class="amt">₹1,550</span><span class="mut2" style="font-size:14px">per course · one-time</span><ul><li>Masterclass included</li><li>Every deep-dive episode for the course</li><li>Downloadable templates</li></ul><a class="btn btn-p" href="#" data-waitlist="Phase-Gate Innovation" data-label="Join the Phase-Gate waitlist">Join the waitlist</a></div>
</div>
<p class="mut" style="font-size:15px">Started with the masterclass? Upgrade to the full course any time and pay only the difference.</p>
</div></section>

<section id="youtube"><div class="wrap stack" style="gap:28px">
<div class="row" style="justify-content:space-between;gap:16px"><div class="stack" style="gap:10px"><p class="kick">Free on YouTube</p><h2>The Innovation Economy</h2><p class="mut">Five short episodes on how India’s brands launch, compete and win.</p></div><a class="btn btn-o" href="{YT}" target="_blank" rel="noopener">Watch on YouTube →</a></div>
<div class="eps">{eps}</div>
</div></section>
'''+FOOT

LESS=[('01','Introduction · Every company is launching','5:50'),('02','Gate 1 · Consumer: do people actually want it?','12:55'),('03','Gate 2 · Business: can we make money making it?','13:55'),('04','Gate 3 · Make: can we make it at scale?','8:05'),('05','Gate 4 · Launch: can we sell it, and keep selling it?','18:12'),('06','Summary · putting the gates to work','4:30')]
lessons=''.join(f'<li><span class="n">{n}</span><span class="t">{t}</span><span class="d">{d}</span></li>' for n,t,d in LESS)
DEEP=[('Gate 1 deep dive','Consumer'),('Gate 2 deep dive','Business'),('Gate 3 deep dive','Make'),('Gate 4 deep dive','Launch'),('The gating process','2-, 3- or 4-gate routing, and when to use which')]
deep=''.join(f'<li class="dash"><span class="n">+</span><span class="t">{a}<span class="mut2" style="font-weight:500"> · {b}</span></span></li>' for a,b in DEEP)

PG=head('Phase-Gate Innovation · Agile Brands','Decide which launches deserve to reach the shelf. A one-hour Phase-Gate masterclass and a full course with a deep dive on every gate. Launching December 2026.','/phase-gate.html')+header(links=[('/','← All courses'),('#curriculum','Curriculum'),('#pricing','Pricing'),('#faq','FAQ')])+f'''
<section class="hero"><div class="wrap">
<div class="hero-l">
<span class="pill-l">LAUNCHING DECEMBER 2026</span>
<p class="kick">Course 01 · Phase-Gate Innovation</p>
<h1>Every company is launching new products. Few decide well which ones deserve to.</h1>
<p class="lead">Phase-Gate kills the bad ones before a senior opinion carries them all the way to shelf. This course takes you through every gate.</p>
<div class="row"><span class="chip">Gates 1–4</span><span class="chip">Quiz after every gate</span><span class="chip">Real FMCG cases</span></div>
<div class="row" style="gap:14px;margin-top:4px"><a class="btn btn-p" href="#" data-waitlist="Phase-Gate Innovation" data-label="Join the Phase-Gate waitlist">Join the waitlist</a><span class="mut2" style="font-size:14px">From ₹449</span></div>
</div>
<div class="hero-r"><a class="trailer" href="{YT}" target="_blank" rel="noopener" aria-label="Phase-Gate trailer, coming soon on YouTube"><img src="/img/trailer_thumb.jpg" alt="Phase-Gate trailer: an idea passing through four gates, with Go, Redo, Hold and Kill decisions" width="1280" height="720"><span class="shade"></span><span class="play"><svg width="28" height="28" viewBox="0 0 24 24" aria-hidden="true"><path d="M8 5 L19 12 L8 19 Z" fill="#17110A"/></svg></span><span class="cap"><span>Watch the trailer</span><small>SOON ON YOUTUBE</small></span></a></div>
</div></section>

<section class="band"><div class="wrap stack" style="gap:28px">
<h2 style="max-width:22em">Is your next launch rushed and choked? Or delayed, and retracing its steps?</h2>
<p class="mut" style="max-width:40em">It’s rarely a talent problem. It’s a decision problem. Phase-Gate gives every stage one clear call.</p>
<div class="gates"><span style="background:#1F3A2B;color:#9EE2B8">GO</span><span style="background:#1F2E44;color:#A9C8F2">REDO</span><span style="background:#3A3120;color:#F2CF8E">HOLD</span><span style="background:#43221F;color:#F4ABA3">KILL</span></div>
</div></section>

<section id="curriculum"><div class="wrap" style="display:flex;flex-wrap:wrap;gap:48px">
<div class="stack" style="flex:1 1 300px;min-width:0;gap:14px"><p class="kick">Curriculum</p><h2>The masterclass, then the deep dives</h2><p class="mut">The masterclass gives you the whole system in about an hour. The full course adds a deep dive on each gate, and on how to route a project through two, three or four gates.</p></div>
<div class="stack" style="flex:2 1 520px;min-width:0;gap:22px">
<div class="stack" style="gap:10px"><p class="mut2" style="font-size:14px;font-weight:700;letter-spacing:.08em">MASTERCLASS · ABOUT AN HOUR · 6 LESSONS</p><ol class="lessons">{lessons}</ol></div>
<div class="stack" style="gap:10px"><p class="mut2" style="font-size:14px;font-weight:700;letter-spacing:.08em">FULL COURSE ADDS · 5 DEEP-DIVE EPISODES</p><ol class="lessons">{deep}</ol></div>
</div></div></section>

<section class="band"><div class="wrap" style="display:flex;flex-wrap:wrap;gap:48px">
<div class="stack" style="flex:1 1 420px;min-width:0;gap:16px"><p class="kick">Take it back to work</p><h2 style="font-size:clamp(26px,3.2vw,34px)">Templates you can use on Monday</h2>
<ul class="lessons" style="gap:8px"><li><span class="n">✓</span><span class="t">A checklist for every gate</span></li><li><span class="n">✓</span><span class="t">Gate-review presentation templates</span></li><li><span class="n">✓</span><span class="t">A formula-driven Excel Gantt</span></li></ul><p class="mut2" style="font-size:14px">Included with the full course.</p></div>
<div class="stack" style="flex:1 1 420px;min-width:0;gap:16px"><p class="kick">Who’s teaching</p><h2 style="font-size:clamp(26px,3.2vw,34px)">Lessons from the marketing desk, not a classroom podium</h2>
<div class="stats"><div class="card stat"><b>13+</b><span>years across brand, innovation and consulting</span></div><div class="card stat"><b>IIM-A</b><span>MBA, IIM Ahmedabad</span></div></div></div>
</div></section>

<section id="pricing"><div class="wrap stack" style="gap:28px">
<h2>Choose how you learn Phase-Gate</h2>
<p class="note">Enrolment opens in December 2026. Join the waitlist and we'll email you the day it does.</p>
<div class="grid3">
<div class="card price"><span style="font-weight:700;font-size:18px">Masterclass</span><span class="amt">₹449</span><span class="mut2" style="font-size:14px">one-time</span><ul><li>6 lessons, about an hour</li><li>A quiz after every gate</li><li>Watch at your own pace</li></ul><a class="btn btn-o" href="#" data-waitlist="Phase-Gate Innovation" data-label="Join the Phase-Gate waitlist">Join the waitlist</a></div>
<div class="card price"><span style="font-weight:700;font-size:18px">Full course</span><span class="amt">₹1,550</span><span class="mut2" style="font-size:14px">one-time</span><ul><li>The masterclass</li><li>5 deep-dive episodes</li><li>Checklists, templates and the Excel Gantt</li></ul><a class="btn btn-p" href="#" data-waitlist="Phase-Gate Innovation" data-label="Join the Phase-Gate waitlist">Join the waitlist</a></div>
</div>
<p class="mut" style="font-size:15px">Started with the masterclass? Upgrade to the full course any time and pay only the difference: ₹1,101.</p>
</div></section>

<section id="faq" style="padding-top:0"><div class="wrap" style="max-width:820px">
<h2 style="margin-bottom:12px">Questions</h2>
<details><summary>When can I enrol?</summary><p>Enrolment opens in December 2026. Join the waitlist and we’ll email you the day it opens.</p></details>
<details><summary>How will I watch the course?</summary><p>After payment you’ll get a login by email. The course plays here, on agilebrands.in, on any device.</p></details>
<details><summary>Can I upgrade from the masterclass later?</summary><p>Yes. Upgrade to the full course whenever you’re ready and pay only the difference.</p></details>
<details><summary>Can I download the videos?</summary><p>The videos stream only. The checklists, templates and Gantt are yours to download.</p></details>
<details><summary>Is there a refund or free trial?</summary><p>Neither. The trailer and our YouTube episodes are free to watch before you decide. See the <a href="/refunds.html">refund policy</a>.</p></details>
<details><summary>I have another question</summary><p>Write to <a href="mailto:learning@agilebrands.in">learning@agilebrands.in</a>.</p></details>
</div></section>
'''+FOOT

def legal(fn,title,desc,body):
    open(fn,'w').write(head(f'{title} · Agile Brands',desc,'/'+fn)+header(cta=False,links=[('/','Home'),('/phase-gate.html','Phase-Gate course')])+f'<div class="legal"><h1>{title}</h1><p class="mut2">Last updated 18 November 2026</p>{body}</div>'+FOOT)

legal('terms.html','Terms of use','Terms of use for agilebrands.in and Agile Brands courses.','''
<p>These terms apply to agilebrands.in and to every course, lesson and download sold on it by Agile Brands, a SimpleDesigns brand (“we”, “us”). By using the site or buying a course you agree to them.</p>
<h2>Courses and access</h2><ul><li>Courses are digital. After payment you get a personal login to stream the lessons on agilebrands.in.</li><li>Your access is for you alone. Sharing your login, recording, downloading or re-uploading the videos is not allowed. We may suspend access that is shared or misused, without a refund.</li><li>Unless a course page says otherwise, access lasts as long as the course is offered on the site.</li></ul>
<h2>Prices and payment</h2><ul><li>Prices are in Indian rupees and shown on each course page at the time you buy. Taxes are applied where the law requires.</li><li>Payments are processed by our payment partner. We do not see or store your card or bank details.</li><li>An upgrade from a masterclass to the full course is charged at the difference between the two prices.</li></ul>
<h2>Content</h2><p>All lessons, scripts, visuals and templates are ours or used with permission. Brand names, products and news shown in lessons belong to their owners and are used for teaching and commentary. Lessons share general frameworks and examples; they are not professional, legal or financial advice for your situation.</p>
<h2>Refunds</h2><p>See our <a href="/refunds.html">refund and cancellation policy</a>.</p>
<h2>Changes</h2><p>We may update courses, prices and these terms. The version on this page applies from the date shown above.</p>
<h2>Law</h2><p>These terms are governed by the laws of India, and disputes are subject to the jurisdiction of the courts in India.</p>
<h2>Contact</h2><p><a href="mailto:learning@agilebrands.in">learning@agilebrands.in</a></p>''')

legal('privacy.html','Privacy policy','How Agile Brands collects and uses your information.','''
<p>This policy explains what we collect on agilebrands.in, why, and what you can ask us to do with it.</p>
<h2>What we collect</h2><ul><li><b>Waitlist:</b> your name, email and the course you’re interested in, when you join a waitlist.</li><li><b>Purchases (once enrolment opens):</b> your name, email and phone number, and the order details. Payments are handled by our payment partner; we never receive your full card or bank details.</li><li><b>Course use:</b> lesson progress and quiz answers, so the course remembers where you are.</li><li><b>Messages:</b> anything you send us by email.</li></ul>
<h2>How we use it</h2><ul><li>To tell you when a course you asked about opens, and to send course updates.</li><li>To give you access to what you bought and to support you.</li><li>To protect courses from shared or misused logins.</li></ul><p>We don’t sell your information. You can unsubscribe from our emails at any time.</p>
<h2>Who processes it</h2><ul><li>Waitlist forms are delivered to our inbox by FormSubmit (formsubmit.co).</li><li>Fonts are served by Google Fonts. The site is hosted on GitHub Pages.</li><li>Payments, once live, are processed by our payment gateway partner.</li></ul>
<h2>Your choices</h2><p>Write to <a href="mailto:learning@agilebrands.in">learning@agilebrands.in</a> to see, correct or delete your information, or to raise a concern. We reply within 7 working days.</p>
<h2>Cookies</h2><p>This site doesn’t set advertising or tracking cookies. If we add analytics or advertising tools later, we’ll update this policy first.</p>''')

legal('refunds.html','Refund & cancellation policy','Refund and cancellation policy for Agile Brands courses.','''
<p>Our courses are digital and you get access straight after payment, so <b>we don’t offer refunds or cancellations once a purchase is complete</b>. Please watch the free trailer and our YouTube episodes before you buy.</p>
<h2>When we will refund</h2><ul><li>You were charged twice for the same order.</li><li>Your payment was debited but the order failed and you didn’t get access.</li><li>We can’t give you access because of a problem on our side that we can’t fix within 7 working days.</li></ul><p>Approved refunds go back to the original payment method within 7–10 working days.</p>
<h2>How to ask</h2><p>Email <a href="mailto:learning@agilebrands.in">learning@agilebrands.in</a> with your order ID within 7 days of payment.</p>''')

legal('delivery.html','Delivery policy','How Agile Brands courses are delivered.','''
<p>We sell digital courses only. Nothing is shipped.</p>
<ul><li>After a successful payment you receive a login email, usually within minutes and always within 24 hours.</li><li>The course streams on agilebrands.in on any device with a browser.</li><li>Didn’t get your login within 24 hours? Check your spam folder, then write to <a href="mailto:learning@agilebrands.in">learning@agilebrands.in</a> with your order ID.</li></ul>''')

legal('contact.html','Contact us','Contact Agile Brands.','''
<p>We read every message and reply within 2 working days.</p>
<h2>Learners</h2><p>Course questions, access and orders: <a href="mailto:learning@agilebrands.in">learning@agilebrands.in</a></p>
<h2>Partners</h2><p>Affiliates, creators and collaborations: <a href="mailto:partner@agilebrands.in">partner@agilebrands.in</a></p>
<h2>Follow</h2><p><a href="https://www.youtube.com/@Agile_Brands" target="_blank" rel="noopener">YouTube · @Agile_Brands</a><br><a href="https://www.instagram.com/_agilebrands/" target="_blank" rel="noopener">Instagram · @_agilebrands</a></p>''')

open('index.html','w').write(INDEX)
open('phase-gate.html','w').write(PG)
open('404.html','w').write(head('Page not found · Agile Brands','Page not found.','/404.html')+header()+'<div class="legal" style="text-align:center"><h1>This page doesn’t exist</h1><p style="margin-top:14px"><a class="btn btn-p" href="/">Go to the homepage</a></p></div>'+FOOT)
open('CNAME','w').write('agilebrands.in\n')
open('robots.txt','w').write('User-agent: *\nAllow: /\nSitemap: https://agilebrands.in/sitemap.xml\n')
urls=['/','/phase-gate.html','/contact.html','/terms.html','/privacy.html','/refunds.html','/delivery.html']
open('sitemap.xml','w').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join(f'<url><loc>{SITE}{u}</loc></url>' for u in urls)+'</urlset>\n')
print('built')
