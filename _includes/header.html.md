<header class="site-header" role="banner">
  <div class="wrapper">

    <a class="site-title" rel="author" href="{{ "/" | relative_url }}">
      <img src="{{ '/assets/nrv-managed-it-logo.png' | relative_url }}"
           alt="NRV Managed IT"
           class="site-logo" />
    </a>

    <nav class="site-nav">
      <input type="checkbox" id="nav-trigger" class="nav-trigger" />
      <label for="nav-trigger">
        <span class="menu-icon" aria-hidden="true">
          <svg viewBox="0 0 18 15" width="18" height="15">
            <path d="M18 1.5a1.5 1.5 0 0 1-1.5 1.5H1.5a1.5 1.5 0 0 1 0-3h15A1.5 1.5 0 0 1 18 1.5ZM18 7.5A1.5 1.5 0 0 1 16.5 9H1.5a1.5 1.5 0 0 1 0-3h15A1.5 1.5 0 0 1 18 7.5ZM18 13.5a1.5 1.5 0 0 1-1.5 1.5H1.5a1.5 1.5 0 0 1 0-3h15a1.5 1.5 0 0 1 1.5 1.5Z"></path>
          </svg>
        </span>
        <span class="visually-hidden">Menu</span>
      </label>

      <div class="trigger">
        {% for page in site.header_pages %}
          {% assign my_page = site.pages | where: "path", page | first %}
          {% if my_page.title %}
            <a class="page-link" href="{{ my_page.url | relative_url }}">{{ my_page.title }}</a>
          {% endif %}
        {% endfor %}
      </div>
    </nav>

  </div>
</header>
