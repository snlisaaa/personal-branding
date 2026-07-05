import re

with open(r'c:\Users\lenovo\Desktop\PERSONAL-BRANDING\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Find the leaderboard div and replace it
old_lb_start = html.find('<div class="leaderboard">')
old_lb_end = html.find('</div>\n          <div class="lb-total">')
if old_lb_end < 0:
    old_lb_end = html.find('</div>\n          <div class="lb-total">', old_lb_start)

print(f"leaderboard start: {old_lb_start}, end: {old_lb_end}")

# Also update lb-total and eng-table
print("Checking structure...")

# Find the entire s5-center block
center_start = html.find('<div class="s5-center">')
center_end = html.find('</div>\n\n        <div class="s5-right">')
print(f"center: {center_start} to {center_end}")

# Find and replace just the center column
new_center = '''        <div class="s5-center">
          <div class="leaderboard-title">ALL POSTS &mdash; RANKED BY VIEWS (10 Posts)</div>
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
                <div class="lb-name">&#x1F9D5; Portrait Photo (Feb 16)</div>
                <div class="lb-bar-wrap"><div class="lb-bar" style="width:18.2%"><span class="lb-num">2,550</span></div></div>
              </div>
              <div class="lb-eng">78&#x2764;</div>
            </div>
            <div class="lb-row">
              <div class="lb-rank">03</div>
              <div class="lb-info">
                <div class="lb-name">&#x1F4DA; The Let Them Theory Event</div>
                <div class="lb-bar-wrap"><div class="lb-bar" style="width:15.8%"><span class="lb-num">2,215</span></div></div>
              </div>
              <div class="lb-eng">55&#x2764;</div>
            </div>
            <div class="lb-row">
              <div class="lb-rank">04</div>
              <div class="lb-info">
                <div class="lb-name">&#x1F4F7; Camera Collab (@zmdinataaa)</div>
                <div class="lb-bar-wrap"><div class="lb-bar" style="width:12.4%"><span class="lb-num">1,745</span></div></div>
              </div>
              <div class="lb-eng">44&#x2764;</div>
            </div>
            <div class="lb-row">
              <div class="lb-rank">05</div>
              <div class="lb-info">
                <div class="lb-name">&#x1F4D6; Bedah Buku Diskusi Let Them</div>
                <div class="lb-bar-wrap"><div class="lb-bar" style="width:12.1%"><span class="lb-num">1,692</span></div></div>
              </div>
              <div class="lb-eng">29&#x2764;</div>
            </div>
            <div class="lb-row">
              <div class="lb-rank">06</div>
              <div class="lb-info">
                <div class="lb-name">&#x1F4D7; Bazar Buku Gramedia Cirebon</div>
                <div class="lb-bar-wrap"><div class="lb-bar" style="width:10.3%"><span class="lb-num">1,441</span></div></div>
              </div>
              <div class="lb-eng">20&#x2764;</div>
            </div>
            <div class="lb-row">
              <div class="lb-rank">07</div>
              <div class="lb-info">
                <div class="lb-name">&#x1F3C6; Intl. Business Case Competition</div>
                <div class="lb-bar-wrap"><div class="lb-bar lb-bar-dim" style="width:5.5%"><span class="lb-num">766</span></div></div>
              </div>
              <div class="lb-eng">56&#x2764;</div>
            </div>
            <div class="lb-row">
              <div class="lb-rank">08</div>
              <div class="lb-info">
                <div class="lb-name">&#x1F3CB;&#xFE0F; Fitness Journey Mirror Selfie</div>
                <div class="lb-bar-wrap"><div class="lb-bar lb-bar-dim" style="width:4.5%"><span class="lb-num">632</span></div></div>
              </div>
              <div class="lb-eng">15&#x2764;</div>
            </div>
            <div class="lb-row">
              <div class="lb-rank">09</div>
              <div class="lb-info">
                <div class="lb-name">&#x1F303; Dark Sky / Landscape</div>
                <div class="lb-bar-wrap"><div class="lb-bar lb-bar-dim" style="width:4.0%"><span class="lb-num">566</span></div></div>
              </div>
              <div class="lb-eng">18&#x2764;</div>
            </div>
            <div class="lb-row">
              <div class="lb-rank">10</div>
              <div class="lb-info">
                <div class="lb-name">&#x1F4D4; Book Page (Jun 15)</div>
                <div class="lb-bar-wrap"><div class="lb-bar lb-bar-dim" style="width:2.9%"><span class="lb-num">406</span></div></div>
              </div>
              <div class="lb-eng">7&#x2764;</div>
            </div>
          </div>
          <div class="lb-total">
            <div class="lbt-item"><div class="lbt-val">26,039</div><div class="lbt-label">Total Views (10 Posts)</div></div>
            <div class="lbt-sep">|</div>
            <div class="lbt-item"><div class="lbt-val">3,149+</div><div class="lbt-label">Total Reached</div></div>
            <div class="lbt-sep">|</div>
            <div class="lbt-item lbt-red"><div class="lbt-val">789</div><div class="lbt-label">Total Engagements</div></div>
          </div>
        </div>'''

if center_start >= 0 and center_end > center_start:
    # Find the actual end of the center div (closing </div>)
    center_end_actual = center_end + len('</div>')
    result = html[:center_start] + new_center + html[center_end_actual:]
    
    # Now update the engagement table in s5-right
    old_eng_table = '''<div class="et-header"><span>Post</span><span>&#x2764;</span><span>&#x1F4AC;</span><span>&#x2197;</span><span>&#x1F516;</span></div>
            <div class="et-row et-viral"><span class="et-post">Group Photo &#x1F525;</span><span class="et-red">350</span><span>2</span><span>3</span><span>3</span></div>
            <div class="et-row"><span class="et-post">Let Them Event</span><span>55</span><span>7</span><span>14</span><span>10</span></div>
            <div class="et-row"><span class="et-post">Camera Collab</span><span>44</span><span>4</span><span>4</span><span>1</span></div>
            <div class="et-row"><span class="et-post">Bedah Buku</span><span>29</span><span>0</span><span>11</span><span>10</span></div>
            <div class="et-row"><span class="et-post">Bazar Gramedia</span><span>20</span><span>0</span><span>7</span><span>7</span></div>
            <div class="et-row"><span class="et-post">Fitness Mirror</span><span>15</span><span>4</span><span>2</span><span>0</span></div>'''
    
    new_eng_table = '''<div class="et-header"><span>Post</span><span>&#x2764;</span><span>&#x1F4AC;</span><span>&#x2197;</span><span>&#x1F516;</span></div>
            <div class="et-row et-viral"><span class="et-post">Group Photo &#x1F525;</span><span class="et-red">350</span><span>2</span><span>3</span><span>3</span></div>
            <div class="et-row"><span class="et-post">Portrait Feb 16</span><span>78</span><span>9</span><span>2</span><span>2</span></div>
            <div class="et-row"><span class="et-post">Let Them Event</span><span>55</span><span>7</span><span>14</span><span>10</span></div>
            <div class="et-row"><span class="et-post">Business Comp.</span><span>56</span><span>4</span><span>0</span><span>0</span></div>
            <div class="et-row"><span class="et-post">Camera Collab</span><span>44</span><span>4</span><span>4</span><span>1</span></div>
            <div class="et-row"><span class="et-post">Bedah Buku</span><span>29</span><span>0</span><span>11</span><span>10</span></div>
            <div class="et-row"><span class="et-post">Bazar Gramedia</span><span>20</span><span>0</span><span>7</span><span>7</span></div>
            <div class="et-row"><span class="et-post">Dark Sky</span><span>18</span><span>0</span><span>2</span><span>1</span></div>
            <div class="et-row"><span class="et-post">Fitness Mirror</span><span>15</span><span>4</span><span>2</span><span>0</span></div>
            <div class="et-row"><span class="et-post">Book Page</span><span>7</span><span>0</span><span>0</span><span>0</span></div>'''
    
    result = result.replace(old_eng_table, new_eng_table)
    
    with open(r'c:\Users\lenovo\Desktop\PERSONAL-BRANDING\index.html', 'w', encoding='utf-8') as f:
        f.write(result)
    print(f"SUCCESS! Updated to 10 posts. File size: {len(result)}")
else:
    print(f"ERROR finding center div: start={center_start}, end={center_end}")
    # Fallback: show context
    if center_start >= 0:
        print("Context around center_start:")
        print(repr(html[center_start:center_start+200]))
