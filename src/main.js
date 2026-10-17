/* Atelier Nordfeld — scripts minimaux, sans dépendance ni traceur. */
(function () {
  "use strict";

  /* Menu mobile */
  var toggle = document.querySelector(".nav-toggle");
  var nav = document.getElementById("main-nav");
  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = nav.classList.toggle("open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
  }
  var subToggle = document.querySelector(".sub-toggle");
  if (subToggle) {
    subToggle.addEventListener("click", function () {
      var li = subToggle.parentElement;
      var open = li.classList.toggle("open");
      subToggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape") {
        subToggle.parentElement.classList.remove("open");
        subToggle.setAttribute("aria-expanded", "false");
      }
    });
  }

  /* Page de choix de langue : met en avant la langue du navigateur, sans redirection forcée */
  if (document.body.classList.contains("chooser")) {
    var pref = (navigator.language || "").slice(0, 2);
    var de = document.querySelector('a[hreflang="de"]');
    var fr = document.querySelector('a[hreflang="fr"]');
    if (pref === "de" && de && fr) {
      de.classList.replace("btn-outline", "btn-primary");
      fr.classList.replace("btn-primary", "btn-outline");
    }
  }

  /* Formulaire de contact */
  var form = document.getElementById("contact-form");
  if (!form) return;
  var msgs = {};
  try { msgs = JSON.parse(form.getAttribute("data-msgs")); } catch (e) {}
  var status = form.querySelector(".form-status");
  var endpoint = document.body.getAttribute("data-form-endpoint") || "";

  var params = new URLSearchParams(window.location.search);
  var preset = params.get("metier");
  var select = form.querySelector("#f-trade");
  if (preset && select) {
    for (var i = 0; i < select.options.length; i++) {
      if (select.options[i].value === preset) select.selectedIndex = i;
    }
  }

  function setError(field, text) {
    var wrap = field.closest(".field");
    var old = wrap.querySelector(".err");
    if (old) old.remove();
    if (text) {
      wrap.classList.add("invalid");
      var span = document.createElement("span");
      span.className = "err";
      span.textContent = text;
      wrap.appendChild(span);
      field.setAttribute("aria-invalid", "true");
    } else {
      wrap.classList.remove("invalid");
      field.removeAttribute("aria-invalid");
    }
  }

  function validate() {
    var ok = true;
    var checks = [
      ["name", function (v) { return v.trim().length > 1 ? "" : msgs.required; }],
      ["phone", function (v) {
        if (!v.trim()) return msgs.required;
        return /^[+()\d][\d\s().\-]{6,}$/.test(v.trim()) ? "" : msgs.invalid_phone;
      }],
      ["email", function (v) {
        if (!v.trim()) return msgs.required;
        return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v.trim()) ? "" : msgs.invalid_email;
      }],
      ["message", function (v) { return v.trim().length > 5 ? "" : msgs.required; }]
    ];
    checks.forEach(function (c) {
      var el = form.elements[c[0]];
      var err = c[1](el.value);
      setError(el, err);
      if (err) ok = false;
    });
    var consent = form.elements.consent;
    setError(consent, consent.checked ? "" : msgs.required);
    if (!consent.checked) ok = false;
    return ok;
  }

  form.addEventListener("submit", function (e) {
    e.preventDefault();
    status.className = "form-status";
    status.textContent = "";
    if (form.elements.website && form.elements.website.value) return; /* anti-spam */
    if (!validate()) {
      var first = form.querySelector(".invalid input, .invalid textarea, .invalid select");
      if (first) first.focus();
      return;
    }
    if (!endpoint) {
      status.className = "form-status ko";
      status.textContent = msgs.unavailable;
      return;
    }
    var data = new FormData(form);
    data.delete("website");
    fetch(endpoint, { method: "POST", body: data, headers: { Accept: "application/json" } })
      .then(function (r) {
        if (!r.ok) throw new Error("http " + r.status);
        form.reset();
        status.className = "form-status ok";
        status.textContent = msgs.success;
      })
      .catch(function () {
        status.className = "form-status ko";
        status.textContent = msgs.error;
      });
  });
})();
