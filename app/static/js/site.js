(() => {
  const btn = document.getElementById("navbtn");
  const nav = document.getElementById("nav");
  if (!btn || !nav) return;

  btn.addEventListener("click", () => {
    nav.classList.toggle("open");
  });

  document.addEventListener("click", (e) => {
    const t = e.target;
    if (!nav.contains(t) && !btn.contains(t)) nav.classList.remove("open");
  });
})();
