document.addEventListener('DOMContentLoaded', function () {
    const animatedLinks = document.querySelectorAll('.animated-link, .link-inline');

    animatedLinks.forEach(link => {
        const span = link.querySelector('span');
        // If a link doesn't have a span for some reason, we skip it.
        if (!span) return;

        const text = span.textContent;
        // Clear the span's content
        span.innerHTML = ''; 

        // Re-create the text with each letter in its own span
        text.split('').forEach((letter, index) => {
            const letterSpan = document.createElement('span');
            letterSpan.className = 'letter';
            letterSpan.style.transitionDelay = `${index * 50}ms`; // Stagger delay
            
            // Use a non-breaking space for space characters
            letterSpan.innerHTML = (letter === ' ') ? '&nbsp;' : letter;
            
            span.appendChild(letterSpan);
        });
    });
});