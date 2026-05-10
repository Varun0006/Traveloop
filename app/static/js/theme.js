// Theme toggle behavior with saved preference.

(function () {
    const root = document.documentElement;
    const toggle = document.getElementById('theme-toggle');
    const storageKey = 'traveloop-theme';

    const getStoredTheme = () => {
        try {
            return localStorage.getItem(storageKey);
        } catch (error) {
            return null;
        }
    };

    const setStoredTheme = (theme) => {
        try {
            localStorage.setItem(storageKey, theme);
        } catch (error) {
            // Ignore storage write errors.
        }
    };

    const prefersDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
    const initialTheme = getStoredTheme() || (prefersDark ? 'dark' : 'light');

    if (initialTheme === 'dark') {
        root.classList.add('dark');
    } else {
        root.classList.remove('dark');
    }

    if (toggle) {
        toggle.addEventListener('click', () => {
            const nowDark = !root.classList.contains('dark');
            root.classList.toggle('dark', nowDark);
            setStoredTheme(nowDark ? 'dark' : 'light');
        });
    }
})();
