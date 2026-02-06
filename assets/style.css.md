/* =========================================================
   NRV Managed IT — Visual Polish
   Theme: metallic / chain / fire / binary
   Clean, professional, restrained
   ========================================================= */

/* Base background */
body {
  background: #f4f6fa;
  color: #111827;
}

/* Main content card */
.page-content .wrapper {
  background: #ffffff;
  padding: 2.5rem;
  border-radius: 12px;
  box-shadow: 0 12px 32px rgba(0,0,0,.08);
}

/* ---------------------------------
   HERO SECTION
----------------------------------*/
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

/* Logo */
.hero-logo {
  max-width: 240px;
  margin-bottom: 1.5rem;
  filter: drop-shadow(0 10px 22px rgba(0,0,0,.55));
}

/* Headline */
.hero h1 {
  margin-bottom: 0.75rem;
  letter-spacing: -0.025em;
}

/* Subheadline */
.hero-sub {
  max-width: 760px;
  margin: 0 auto 1.75rem auto;
  font-size: 1.05rem;
  opacity: 0.92;
}

/* ---------------------------------
   BUTTONS
----------------------------------*/
.btn {
  display: inline-block;
  padding: 0.75rem 1.2rem;
  border-radius: 12px;
  text-decoration: none !important;
  font-weight: 600;
  background: #e5e7eb;
  color: #0b1e2d !important;
  margin: 0 0.4rem;
  transition: all 0.15s ease-in-out;
}

.btn:hover {
  background: #ffffff;
  transform: translateY(-1px);
}

/* Outline button */
.btn-outline {
  background: transparent;
  border: 1px solid rgba(255,255,255,.55);
  color: #ffffff !important;
}

.btn-outline:hover {
  background: rgba(255,255,255,.15);
}

/* ---------------------------------
   HEADINGS
----------------------------------*/
h2 {
  margin-top: 2.25rem;
  letter-spacing: -0.015em;
}

h3 {
  margin-top: 1.75rem;
}

/* ---------------------------------
   LINKS
----------------------------------*/
a {
  text-underline-offset: 3px;
}

/* ---------------------------------
   FOOTER (Minima default tweak)
----------------------------------*/
.site-footer {
  margin-top: 3rem;
  font-size: 0.9rem;
  opacity: 0.85;
}

/* ---------------------------------
   MOBILE TUNING
----------------------------------*/
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
