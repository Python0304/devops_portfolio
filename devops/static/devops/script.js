// Fade-in animation on scroll
const elements = document.querySelectorAll('.section-title, .about-content, .skills-grid, .project-grid, .edu-list, .contact-form');

const appearOnScroll = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
    }
  });
}, { threshold: 0.1 });

elements.forEach(el => {
  el.classList.add('fade-in');
  appearOnScroll.observe(el);
});
