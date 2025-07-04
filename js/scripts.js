document.addEventListener('DOMContentLoaded', () => {
    const animatedLinks = document.querySelectorAll('.animated-link, .link-inline');

    animatedLinks.forEach(link => {
        // For links with icons, we handle the icon separately
        const icon = link.querySelector('svg');
        const textSpan = link.querySelector('span');
        
        // If there's no text span, it might be a simple inline link without the original <span> structure
        // This makes the script robust.
        const targetForLetters = textSpan || link;
        const text = targetForLetters.textContent;
        targetForLetters.innerHTML = ''; // Clear the original text

        const letters = text.split('');
        
        let initialDelay = 0;
        // If there was an icon, it animates first. We give it a slight head start.
        if (icon) {
            icon.style.transition = 'color 0.3s ease-out';
            icon.style.transitionDelay = '0ms';
            initialDelay = 50; // Start the text animation slightly after the icon
        }

        letters.forEach((letter, i) => {
            const letterSpan = document.createElement('span');
            letterSpan.className = 'letter';
            // Use non-breaking space for actual spaces to prevent collapsing
            letterSpan.innerHTML = (letter === ' ') ? '&nbsp;' : letter;
            
            // Stagger the animation for each letter
            letterSpan.style.transitionDelay = `${initialDelay + i * 40}ms`;
            
            targetForLetters.appendChild(letterSpan);
        });
    });
});