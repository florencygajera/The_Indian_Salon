(() => {
  // Mobile menu
  const btn = document.getElementById("navbtn");
  const nav = document.getElementById("nav");
  if (btn && nav) {
    btn.addEventListener("click", () => nav.classList.toggle("open"));
    document.addEventListener("click", (e) => {
      const t = e.target;
      if (!nav.contains(t) && !btn.contains(t)) nav.classList.remove("open");
    });
  }

  // HERO SLIDER
  const slides = document.querySelectorAll("[data-slide]");
  let idx = 0;
  const show = (i) => {
    slides.forEach((s, k) => s.classList.toggle("is-active", k === i));
  };
  if (slides.length) {
    show(0);
    setInterval(() => {
      idx = (idx + 1) % slides.length;
      show(idx);
    }, 4500);
  }

  // LIGHTBOX for gallery
  const lb = document.getElementById("lightbox");
  const lbImg = document.getElementById("lightboxImg");
  const closeBtn = document.getElementById("lbClose");

  const openLB = (src) => {
    if (!lb || !lbImg) return;
    lbImg.src = src;
    lb.classList.add("open");
    document.body.style.overflow = "hidden";
  };
  const closeLB = () => {
    if (!lb) return;
    lb.classList.remove("open");
    if (lbImg) lbImg.src = "";
    document.body.style.overflow = "";
  };

  document.querySelectorAll("[data-lightbox]").forEach((el) => {
    el.addEventListener("click", (e) => {
      e.preventDefault();
      const src = el.getAttribute("data-lightbox");
      if (src) openLB(src);
    });
  });

  if (closeBtn) closeBtn.addEventListener("click", closeLB);
  if (lb) lb.addEventListener("click", (e) => { if (e.target === lb) closeLB(); });
  document.addEventListener("keydown", (e) => { if (e.key === "Escape") closeLB(); });
})();
