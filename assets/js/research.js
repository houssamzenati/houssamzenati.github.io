(() => {
  // A link to a research section should reveal its discussion as well as its title.
  function revealLinkedSection() {
    let id;
    try {
      id = decodeURIComponent(window.location.hash.slice(1));
    } catch {
      return;
    }
    const target = document.getElementById(id);
    const section = target && target.closest(".research-collapsible");
    if (!section) return;
    section.open = true;
    target.scrollIntoView({ block: "start" });
  }

  window.addEventListener("hashchange", revealLinkedSection);
  revealLinkedSection();
  if (window.MathJax && window.MathJax.startup && window.MathJax.startup.promise) {
    window.MathJax.startup.promise.then(revealLinkedSection);
  }
})();
