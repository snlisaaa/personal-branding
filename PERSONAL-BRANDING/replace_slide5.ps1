$html = Get-Content "c:\Users\lenovo\Desktop\PERSONAL-BRANDING\index.html" -Raw -Encoding UTF8

$newSlide5 = @'
    <section class="slide slide-dark" id="slide-5">
      <div class="slide-tag">INSTAGRAM ANALYTICS</div>
      <div class="slide-header">
        <h2 class="slide-title">Performance <em>Dashboard</em></h2>
        <p class="slide-desc">All posts · 100% organic · Zero paid promotion · Data real dari Post Insights</p>
      </div>

      <div class="s5-layout">

        <!-- LEFT — VIRAL HERO CARD -->
        <div class="s5-left">
          <div class="viral-hero">
            <div class="viral-crown">🏆 TOP PERFORMING POST</div>
            <div class="viral-views-label">TOTAL VIEWS</div>
            <div class="viral-views-num counter" data-target="14026">0</div>
            <div class="viral-content-type">📸 Group Photo · Feb 16, 2025</div>
            <div class="viral-divider"></div>
            <div class="viral-stats-row">
              <div class="vstat"><div class="vstat-n vstat-red counter" data-target="350">0</div><div class="vstat-l">❤️ Likes</div></div>
              <div class="vstat"><div class="vstat-n counter" data-target="361">0</div><div class="vstat-l">⚡ Interact.</div></div>
              <div class="vstat"><div class="vstat-n counter" data-target="3">0</div><div class="vstat-l">💬 Comments</div></div>
            </div>
            <div class="viral-note">
              🔥 <strong>14K+ views</strong> organically — tertinggi di seluruh konten akun.<br/>
              Bukti bahwa konten komunitas memiliki daya jangkau luar biasa.
            </div>
          </div>
          <div class="acct-overview">
            <div class="ao-title">ACCOUNT OVERVIEW · 30 DAYS</div>
            <div class="ao-stats">
              <div class="ao-s"><span class="ao-val counter" data-target="7536">0</span><span class="ao-lbl">Views</span></div>
              <div class="ao-s"><span class="ao-val counter" data-target="906">0</span><span class="ao-lbl">Reached</span></div>
              <div class="ao-s"><span class="ao-val counter" data-target="806">0</span><span class="ao-lbl">Followers</span></div>
              <div class="ao-s"><span class="ao-val counter" data-target="177">0</span><span class="ao-lbl">Profile Visits</span></div>
            </div>
          </div>
        </div>

        <!-- CENTER — POST LEADERBOARD -->
        <div class="s5-center">
          <div class="leaderboard-title">ALL POSTS — RANKED BY VIEWS</div>
          <div class="leaderboard">
            <div class="lb-row lb-row-top">
              <div class="lb-rank">01</div>
              <div class="lb-info">
                <div class="lb-name">📸 Group Photo (Komunitas)</div>
                <div class="lb-bar-wrap"><div class="lb-bar lb-bar-red" style="width:100%"><span class="lb-num">14,026</span></div></div>
              </div>
              <div class="lb-eng">350❤</div>
            </div>
            <div class="lb-row">
              <div class="lb-rank">02</div>
              <div class="lb-info">
                <div class="lb-name">📚 The Let Them Theory Event</div>
                <div class="lb-bar-wrap"><div class="lb-bar" style="width:15.8%"><span class="lb-num">2,215</span></div></div>
              </div>
              <div class="lb-eng">55❤</div>
            </div>
            <div class="lb-row">
              <div class="lb-rank">03</div>
              <div class="lb-info">
                <div class="lb-name">📷 Camera Collab (@zmdinataaa)</div>
                <div class="lb-bar-wrap"><div class="lb-bar" style="width:12.4%"><span class="lb-num">1,745</span></div></div>
              </div>
              <div class="lb-eng">44❤</div>
            </div>
            <div class="lb-row">
              <div class="lb-rank">04</div>
              <div class="lb-info">
                <div class="lb-name">📖 Bedah Buku Diskusi Let Them</div>
                <div class="lb-bar-wrap"><div class="lb-bar" style="width:12.1%"><span class="lb-num">1,692</span></div></div>
              </div>
              <div class="lb-eng">29❤</div>
            </div>
            <div class="lb-row">
              <div class="lb-rank">05</div>
              <div class="lb-info">
                <div class="lb-name">📗 Bazar Buku Gramedia Cirebon</div>
                <div class="lb-bar-wrap"><div class="lb-bar" style="width:10.3%"><span class="lb-num">1,441</span></div></div>
              </div>
              <div class="lb-eng">20❤</div>
            </div>
            <div class="lb-row">
              <div class="lb-rank">06</div>
              <div class="lb-info">
                <div class="lb-name">🏋️ Fitness Journey Mirror Selfie</div>
                <div class="lb-bar-wrap"><div class="lb-bar lb-bar-dim" style="width:4.5%"><span class="lb-num">632</span></div></div>
              </div>
              <div class="lb-eng">15❤</div>
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

        <!-- RIGHT — ENGAGEMENT TABLE -->
        <div class="s5-right">
          <div class="eng-breakdown-title">ENGAGEMENT PER POST</div>
          <div class="eng-table">
            <div class="et-header"><span>Post</span><span>❤️</span><span>💬</span><span>↗</span><span>🔖</span></div>
            <div class="et-row et-viral"><span class="et-post">Group Photo 🔥</span><span class="et-red">350</span><span>2</span><span>3</span><span>3</span></div>
            <div class="et-row"><span class="et-post">Let Them Event</span><span>55</span><span>7</span><span>14</span><span>10</span></div>
            <div class="et-row"><span class="et-post">Camera Collab</span><span>44</span><span>4</span><span>4</span><span>1</span></div>
            <div class="et-row"><span class="et-post">Bedah Buku</span><span>29</span><span>0</span><span>11</span><span>10</span></div>
            <div class="et-row"><span class="et-post">Bazar Gramedia</span><span>20</span><span>0</span><span>7</span><span>7</span></div>
            <div class="et-row"><span class="et-post">Fitness Mirror</span><span>15</span><span>4</span><span>2</span><span>0</span></div>
          </div>
          <div class="collab-note">
            <div class="cn-title">🤝 COLLABORATION POSTS</div>
            <div class="cn-items">
              <div class="cn-item">Let Them Event → <strong>+2 collaborators</strong></div>
              <div class="cn-item">Bedah Buku → <strong>cirebonmenulis +4</strong></div>
              <div class="cn-item">Bazar Gramedia → <strong>irma_fang +3</strong></div>
              <div class="cn-item">Camera → <strong>zmdinataaa</strong></div>
            </div>
            <div class="cn-insight">💡 Kolaborasi = jangkauan <strong>3× lebih luas</strong> tanpa biaya</div>
          </div>
          <div class="s5-key-insight">
            <div class="ski-icon">🎯</div>
            <p>Reach rate naik <strong>+98.2%</strong> vs periode sebelumnya — semua tanpa iklan berbayar</p>
          </div>
        </div>

      </div>
      <div class="slide-number">05</div>
    </section>
'@

# Find boundaries
$startMarker = '    <!-- ═══════════════════════════════════════════ -->' + "`r`n" + '    <!-- SLIDE 05 — INSTAGRAM PERFORMANCE -->' + "`r`n" + '    <!-- ═══════════════════════════════════════════ -->'
$endMarker = '    <!-- ═══════════════════════════════════════════ -->' + "`r`n" + '    <!-- SLIDE 06 — CUSTOMER JOURNEY -->'

$startIdx = $html.IndexOf('<section class="slide slide-dark" id="slide-5">')
$endIdx = $html.IndexOf('<section class="slide slide-light" id="slide-6">')

if ($startIdx -ge 0 -and $endIdx -gt $startIdx) {
    $before = $html.Substring(0, $startIdx)
    $after = $html.Substring($endIdx)
    $newHtml = $before + $newSlide5 + "`r`n`r`n    <!-- ═══════════════════════════════════════════ -->`r`n    <!-- SLIDE 06 — CUSTOMER JOURNEY -->`r`n    <!-- ═══════════════════════════════════════════ -->`r`n    " + $after
    [System.IO.File]::WriteAllText("c:\Users\lenovo\Desktop\PERSONAL-BRANDING\index.html", $newHtml, [System.Text.Encoding]::UTF8)
    Write-Host "SUCCESS: Replaced slide 5. New file size: $($newHtml.Length)"
} else {
    Write-Host "ERROR: Could not find slide boundaries. startIdx=$startIdx endIdx=$endIdx"
}
