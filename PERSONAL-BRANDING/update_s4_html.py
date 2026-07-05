with open(r"c:\Users\lenovo\Desktop\PERSONAL-BRANDING\index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Let's define the new objectives grid content
new_grid = """      <div class="objectives-grid">
        <div class="obj-card" data-n="01">
          <div class="obj-icon-wrap">
            <svg width="32" height="32" viewBox="0 0 32 32" fill="none"><circle cx="16" cy="16" r="12" stroke="#E53E3E" stroke-width="2"/><circle cx="16" cy="16" r="7" stroke="#E53E3E" stroke-width="1.5" stroke-dasharray="3 2"/><circle cx="16" cy="16" r="3" fill="#E53E3E"/></svg>
          </div>
          <h4>Awareness</h4>
          <p>Measure how far content reaches beyond existing followers</p>
          <div class="obj-metric-img-wrap">
            <img class="obj-metric-img" src="assets/images/obj_awareness.jpg" alt="Awareness Metric">
          </div>
        </div>
        <div class="obj-card" data-n="02">
          <div class="obj-icon-wrap">
            <svg width="32" height="32" viewBox="0 0 32 32" fill="none"><path d="M4 20l6-8 5 5 5-7 8 10" stroke="#E53E3E" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><rect x="2" y="2" width="28" height="28" rx="3" stroke="#E53E3E" stroke-width="1.5"/></svg>
          </div>
          <h4>Engagement</h4>
          <p>Track interactions, saves, shares, and DMs generated</p>
          <div class="obj-metric-img-wrap">
            <img class="obj-metric-img" src="assets/images/obj_engagement.jpg" alt="Engagement Metric">
          </div>
        </div>
        <div class="obj-card" data-n="03">
          <div class="obj-icon-wrap">
            <svg width="32" height="32" viewBox="0 0 32 32" fill="none"><path d="M16 4v4M16 24v4M4 16H8M24 16h4" stroke="#E53E3E" stroke-width="2" stroke-linecap="round"/><circle cx="16" cy="16" r="8" stroke="#E53E3E" stroke-width="2"/><path d="M13 16l2 2 4-4" stroke="#E53E3E" stroke-width="1.5" stroke-linecap="round"/></svg>
          </div>
          <h4>Lead Generation</h4>
          <p>Identify how many DMs convert into qualified leads</p>
          <div class="obj-metric-img-wrap">
            <img class="obj-metric-img" src="assets/images/obj_leadgen.jpg" alt="Lead Gen Metric">
          </div>
        </div>
        <div class="obj-card" data-n="04">
          <div class="obj-icon-wrap">
            <svg width="32" height="32" viewBox="0 0 32 32" fill="none"><rect x="4" y="8" width="24" height="18" rx="2" stroke="#E53E3E" stroke-width="2"/><path d="M10 8V6a2 2 0 014 0v2M18 8V6a2 2 0 014 0v2" stroke="#E53E3E" stroke-width="2" stroke-linecap="round"/><path d="M10 18h12M10 22h8" stroke="#E53E3E" stroke-width="1.5" stroke-linecap="round"/></svg>
          </div>
          <h4>Lead Quality</h4>
          <p>Assess intent level and conversion potential of each lead</p>
          <div class="obj-metric-img-wrap">
            <img class="obj-metric-img" src="assets/images/obj_leadquality.jpg" alt="Lead Quality Metric">
          </div>
        </div>
        <div class="obj-card" data-n="05">
          <div class="obj-icon-wrap">
            <svg width="32" height="32" viewBox="0 0 32 32" fill="none"><path d="M16 6C16 6 8 12 8 18a8 8 0 0016 0c0-6-8-12-8-12z" stroke="#E53E3E" stroke-width="2"/><path d="M16 22v-8M13 17l3-3 3 3" stroke="#E53E3E" stroke-width="1.5" stroke-linecap="round"/></svg>
          </div>
          <h4>Pain Points</h4>
          <p>Uncover real barriers preventing people from joining gym</p>
          <div class="obj-metric-img-wrap">
            <img class="obj-metric-img" src="assets/images/obj_painpoints.jpg" alt="Pain Points Metric">
          </div>
        </div>
      </div>"""

# Replace the grid in Slide 4
start_tag = '<div class="objectives-grid">'
end_tag = '</div>\n      <div class="slide-number">04</div>'

start_idx = html.find(start_tag)
end_idx = html.find(end_tag)

if start_idx >= 0 and end_idx > start_idx:
    result = html[:start_idx] + new_grid + html[end_idx + len('</div>'):]
    with open(r"c:\Users\lenovo\Desktop\PERSONAL-BRANDING\index.html", "w", encoding="utf-8") as f:
        f.write(result)
    print("SUCCESS! Slide 4 HTML updated with cropped metrics images!")
else:
    print(f"ERROR: could not find Slide 4 grid tags. start_idx={start_idx}, end_idx={end_idx}")
