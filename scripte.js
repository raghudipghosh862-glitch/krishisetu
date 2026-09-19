document.addEventListener("DOMContentLoaded", () => {
    // 1. Mobile Menu Drawer Toggle
    const menuToggle = document.getElementById("menuToggle");
    const navLinks = document.getElementById("navLinks");

    if (menuToggle && navLinks) {
        menuToggle.addEventListener("click", () => {
            navLinks.classList.toggle("open");
        });
    }

    // 2. Count-Up Animation for Impact Metrics
    const metricElements = document.querySelectorAll(".metric-value");

    metricElements.forEach(element => {
        const text = element.innerText.trim();
        
        // Extract raw number value
        const rawDigits = text.replace(/[^0-9]/g, "");
        const targetValue = parseInt(rawDigits, 10);
        
        if (isNaN(targetValue)) return;

        // Preserve prefixes (+ or -) and suffixes (% or +)
        const prefix = text.startsWith("+") ? "+" : (text.startsWith("-") ? "-" : "");
        const suffix = text.includes("%") ? "%" : (text.includes("+") && !prefix ? "+" : "");

        animateMetric(element, 0, targetValue, prefix, suffix, 1400);
    });

    function animateMetric(domNode, start, end, prefix, suffix, durationMs) {
        let startTime = null;

        function updateStep(timestamp) {
            if (!startTime) startTime = timestamp;
            const progress = Math.min((timestamp - startTime) / durationMs, 1);
            
            // Ease-out curve
            const easeProgress = 1 - Math.pow(1 - progress, 3);
            const currentVal = Math.floor(easeProgress * (end - start) + start);

            const formattedNumber = currentVal >= 1000 
                ? currentVal.toLocaleString("en-IN") 
                : currentVal.toString();

            domNode.textContent = `${prefix}${formattedNumber}${suffix}`;

            if (progress < 1) {
                window.requestAnimationFrame(updateStep);
            }
        }

        window.requestAnimationFrame(updateStep);
    }
});