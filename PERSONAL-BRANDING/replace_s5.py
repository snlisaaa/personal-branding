import re

with open(r'c:\Users\lenovo\Desktop\PERSONAL-BRANDING\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

new_slide5 = '''    <section class="slide slide-dark" id="slide-5">
      <div class="slide-tag">INSTAGRAM ANALYTICS</div>
      <div class="slide-header">
        <h2 class="slide-title">Performance <em>Dashboard</em></h2>
        <p class="slide-desc">All posts &middot; 100% organic &middot; Zero paid promotion &middot; Data real dari Post Insights</p>
      </div>

      <div class="s5-layout">

        <div class="s5-left">
          <div class="viral-hero">
            <div class="viral-crown">&#x1F3C6; TOP PERFORMING POST</div>
            <div class="viral-views-label">TOTAL VIEWS</div>
            <div class="viral-views-num counter" data-target="14026">0</div>
            <div class="viral-content-type">&#x1F4F8; Group Photo &middot; Feb 16, 2025</div>
            <div class="viral-divider"></div>
            <div class="viral-stats-row">
              <div class="vstat"><div class="vstat-n vstat-red counter" data-target="350">0</div><div class="vstat-l">&#x2764;&#xFE0F; Likes</div></div>
              <div class="vstat"><div class="vstat-n counter" data-target="361">0</div><div class="vstat-l">&#x26A1; Interact.</div></div>
              <div class="vstat"><div class="vstat-n counter" data-target="3">0</div><div class="vstat-l">&#x1F4AC; Comments</div></div>
            </div>
            <div class="viral-note">
              &#x1F525; <strong>14K+ views</strong> organically &mdash; tertinggi di seluruh konten akun.<br/>
              Bukti bahwa konten komunitas memiliki daya jangkau luar biasa.
            </div>
          </div>
          <div class="acct-overview">
            <div class="ao-title">ACCOUNT OVERVIEW &middot; 30 DAYS</div>
            <div class="ao-stats">
              <div class="ao-s"><span class="ao-val counter" data-target="7536">0</span><span class="ao-lbl">Views</span></div>
              <div class="ao-s"><span class="ao-val counter" data-target="906">0</span><span class="ao-lbl">Reached</span></div>
              <div class="ao-s"><span class="ao-val counter" data-target="806">0</span><span class="ao-lbl">Followers</span></div>
              <div class="ao-s"><span class="ao-val counter" data-target="177">0</span><span class="ao-lbl">Profile Visits</span></div>
            </div>
          </div>
        </div>

        <div class="s5-center">
          <div class="leaderboard-title">ALL POSTS &mdash; RANKED BY VIEWS</div>
          <div class="leaderboard">
            <div class="lb-row lb-row-top">
              <div class="lb-rank">01</div>
              <div class="lb-info">
                <div class="lb-name">&#x1F4F8; Group Photo (Komunitas)</div>
                <div class="lb-bar-wrap"><div class="lb-bar lb-bar-red" style="width:100%"><span class="lb-num">14,026</span></div></div>
              </div>
              <div class="lb-eng">350&#x2764;</div>
            </div>
            <div class="lb-row">
              <div class="lb-rank">02</div>
              <div class="lb-info">
                <div class="lb-name">&#x1F4DA; The Let Them Theory Event</div>
                <div class="lb-bar-wrap"><div class="lb-bar" style="width:15.8%"><span class="lb-num">2,215</span></div></div>
              </div>
              <div class="lb-eng">55&#x2764;</div>
            </div>
            <div class="lb-row">
              <div class="lb-rank">03</div>
              <div class="lb-info">
                <div class="lb-name">&#x1F4F7; Camera Collab (@zmdinataaa)</div>
                <div class="lb-bar-wrap"><div class="lb-bar" style="width:12.4%"><span class="lb-num">1,745</span></div></div>
              </div>
              <div class="lb-eng">44&#x2764;</div>
            </div>
            <div class="lb-row">
              <div class="lb-rank">04</div>
              <div class="lb-info">
                <div class="lb-name">&#x1F4D6; Bedah Buku Diskusi Let Them</div>
                <div class="lb-bar-wrap"><div class="lb-bar" style="width:12.1%"><span class="lb-num">1,692</span></div></div>
              </div>
              <div class="lb-eng">29&#x2764;</div>
            </div>
            <div class="lb-row">
              <div class="lb-rank">05</div>
              <div class="lb-info">
                <div class="lb-name">&#x1F4D7; Bazar Buku Gramedia Cirebon</div>
                <div class="lb-bar-wrap"><div class="lb-bar" style="width:10.3%"><span class="lb-num">1,441</span></div></div>
              </div>
              <div class="lb-eng">20&#x2764;</div>
            </div>
            <div class="lb-row">
              <div class="lb-rank">06</div>
              <div class="lb-info">
                <div class="lb-name">&#x1F3CB;&#xFE0F; Fitness Journey Mirror Selfie</div>
                <div class="lb-bar-wrap"><div class="lb-bar lb-bar-dim" style="width:4.5%"><span class="lb-num">632</span></div></div>
              </div>
              <div class="lb-eng">15&#x2764;</div>
            </div>
          </div>
          <div class="lb-total">
            <div class="lbt-item"><div class="lbt-val">21,751</div><div class="lbt-label">Total Views (6 Posts)</div></div>
            <div class="lbt-sep">|</div>
            <div class="lbt-item"><div class="lbt-val">3,149</div><div class="lbt-label">Total Reached</div></div>
            <div class="lbt-sep">|</div>
            <div class="lbt-item lbt-red"><div class="lbt-val">561</div><div class="lbt-label">Total Engagements</div></div>
          </div>
        </div>

        <div class="s5-right">
          <div class="eng-breakdown-title">ENGAGEMENT PER POST</div>
          <div class="eng-table">
            <div class="et-header"><span>Post</span><span>&#x2764;</span><span>&#x1F4AC;</span><span>&#x2197;</span><span>&#x1F516;</span></div>
            <div class="et-row et-viral"><span class="et-post">Group Photo &#x1F525;</span><span class="et-red">350</span><span>2</span><span>3</span><span>3</span></div>
            <div class="et-row"><span class="et-post">Let Them Event</span><span>55</span><span>7</span><span>14</span><span>10</span></div>
            <div class="et-row"><span class="et-post">Camera Collab</span><span>44</span><span>4</span><span>4</span><span>1</span></div>
            <div class="et-row"><span class="et-post">Bedah Buku</span><span>29</span><span>0</span><span>11</span><span>10</span></div>
            <div class="et-row"><span class="et-post">Bazar Gramedia</span><span>20</span><span>0</span><span>7</span><span>7</span></div>
            <div class="et-row"><span class="et-post">Fitness Mirror</span><span>15</span><span>4</span><span>2</span><span>0</span></div>
          </div>
          <div class="collab-note">
            <div class="cn-title">&#x1F91D; COLLABORATION POSTS</div>
            <div class="cn-items">
              <div class="cn-item">Let Them Event &rarr; <strong>+2 collaborators</strong></div>
              <div class="cn-item">Bedah Buku &rarr; <strong>cirebonmenulis +4</strong></div>
              <div class="cn-item">Bazar Gramedia &rarr; <strong>irma_fang +3</strong></div>
              <div class="cn-item">Camera &rarr; <strong>zmdinataaa</strong></div>
            </div>
            <div class="cn-insight">&#x1F4A1; Kolaborasi = jangkauan <strong>3&times; lebih luas</strong> tanpa biaya</div>
          </div>
          <div class="s5-key-insight">
            <div class="ski-icon">&#x1F3AF;</div>
            <p>Reach rate naik <strong>+98.2%</strong> vs periode sebelumnya &mdash; semua tanpa iklan berbayar</p>
          </div>
        </div>

      </div>
      <div class="slide-number">05</div>
    </section>'''

# Find and replace slide 5
start = html.find('<section class="slide slide-dark" id="slide-5">')
end = html.find('<section class="slide slide-light" id="slide-6">')

if start >= 0 and end > start:
    result = html[:start] + new_slide5 + '\n\n' + html[end:]
    with open(r'c:\Users\lenovo\Desktop\PERSONAL-BRANDING\index.html', 'w', encoding='utf-8') as f:
        f.write(result)
    print(f"SUCCESS! File updated. New size: {len(result)} chars")
    print(f"Slide 5 starts at char {start}, Slide 6 starts at char {end}")
else:
    print(f"ERROR: start={start}, end={end}")
