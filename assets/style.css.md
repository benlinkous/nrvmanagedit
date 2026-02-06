/* =========================================================
   NRV Managed IT — Site Styling
   Clean, professional, readable
   ========================================================= */

/* ---------- Base page ---------- */
body {
  background-color: #eef1f4;   /* light gray background */
  color: #111827;              /* near-black text */
  font-family: -apple-system, BlinkMacSystemFont,
               "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
}

/* ---------- Main content card ---------- */
.page-content .wrapper {
  background-color: #ffffff;   /* white content area */
  padding: 2.5rem;
  border-radius: 12px;
  box-shadow: 0 12px 32px rgba(0,0,0,0.08);
}

/* ---------- Header ---------- */
.site-header {
  background: transparent;
  border-top: none;
  border-bottom: none;
  padding-top: 1rem;
  padding-bottom: 1rem;
}

/* Logo in header */
.site-logo {
  height: 48px;
  width: auto;
  vertical-align: middle;
  filter: drop-shadow(0 4px 10px rgba(0,0,0,0.25));
}

/* ---------- Hero (home page) ---------- */
.hero {
  margin-bottom: 2.5rem;
  border-radius: 16px;
  background: linear-gradient(135deg, #0b1e2d, #102a3f);
  color: #ffffff;
  overflow: hidden;
}

.hero-inner {
  padding: 3rem 2.5rem;
  text-align: center;
}

.hero-logo {
  max-width: 240px;
  margin-bottom: 1.5rem;
  filter: drop-shadow(0 10px 22px rgba(0,0,0,0.55));
}

.hero h1 {
  margin-bottom: 0.75rem;
  letter-spacing: -0.025em;
}

.hero-sub {
  max-width: 760px;
  margin: 0 auto 1.75rem auto;
  font-size: 1.05rem;
  opacity: 0.92;
}

/* ---------- Buttons ---------- */
.btn {
  display: inline-block;
  padding: 0.75rem 1.2rem;
  border-radius: 12px;
  text-decoration: none !important;
  font-weight: 600;
  background-color: #e5e7eb;
  color: #0b1e2d !important;
  margin: 0 0.4rem;
  transition: all 0.15s ease-in-out;
}

.btn:hover {
  background-color: #ffffff;
  transform: translateY(-1px);
}

.btn-outline {
  background: transparent;
  border: 1px solid rgba(255,255,255,0.55);
  color: #ffffff !important;
}

.btn-outline:hover {
  background: rgba(255,255,255,0.15);
}

/* ---------- Headings ---------- */
h1, h2, h3 {
  letter-spacing: -0.015em;
}

h2 {
  margin-top: 2.25rem;
}

h3 {
  margin-top: 1.75rem;
}

/* ---------- Links ---------- */
a {
  text-underline-offset: 3px;
}

/* ---------- Footer ---------- */
.site-footer {
  margin-top: 3rem;
  font-size: 0.9rem;
  opacity: 0.85;
}

/* ---------- Mobile tuning ---------- */
@media (max-width: 640px) {

  .page-content .wrapper {
    padding: 1.75rem;
  }

  .hero-inner {
    padding: 2.25rem 1.5rem;
  }

  .hero-logo {
    max-width: 200px;
  }

}
