/**
 * Manuale Operativo - Landing Page JS
 * Gestisce: menu mobile, toggle pricing, form registrazione, checkout Stripe
 */

const API_BASE = 'https://api-test.geniusmile.com/api/v1';

// ============================================================
// Mobile Menu
// ============================================================
document.addEventListener('DOMContentLoaded', () => {
    const menuBtn = document.getElementById('mobile-menu-btn');
    const mobileMenu = document.getElementById('mobile-menu');

    if (menuBtn && mobileMenu) {
        menuBtn.addEventListener('click', () => {
            mobileMenu.classList.toggle('hidden');
        });

        // Chiudi menu al click su un link
        mobileMenu.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', () => {
                mobileMenu.classList.add('hidden');
            });
        });
    }
});

// ============================================================
// Pricing Toggle (Mensile / Annuale)
// ============================================================
document.addEventListener('DOMContentLoaded', () => {
    const toggle = document.getElementById('billing-toggle');
    if (!toggle) return;

    const monthlyPrices = document.querySelectorAll('.price-monthly');
    const yearlyPrices = document.querySelectorAll('.price-yearly');
    const periodLabels = document.querySelectorAll('.billing-period');

    toggle.addEventListener('change', () => {
        const isYearly = toggle.checked;

        monthlyPrices.forEach(el => el.classList.toggle('hidden', isYearly));
        yearlyPrices.forEach(el => el.classList.toggle('hidden', !isYearly));
        periodLabels.forEach(el => {
            el.textContent = isYearly ? '/anno' : '/mese';
        });
    });
});

// ============================================================
// Smooth scroll per CTA buttons
// ============================================================
document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', (e) => {
            const target = document.querySelector(anchor.getAttribute('href'));
            if (target) {
                e.preventDefault();
                target.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        });
    });
});

// ============================================================
// Registration Form
// ============================================================
document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('registration-form');
    if (!form) return;

    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        const btn = form.querySelector('button[type="submit"]');
        const msgDiv = document.getElementById('form-message');

        // Honeypot check (bot trap)
        const honeypot = form.querySelector('[name="website"]');
        if (honeypot && honeypot.value) return;

        // Raccogli dati
        const data = {
            nome: form.querySelector('[name="nome"]').value.trim(),
            cognome: form.querySelector('[name="cognome"]').value.trim(),
            email: form.querySelector('[name="email"]').value.trim(),
            telefono: form.querySelector('[name="telefono"]')?.value.trim() || '',
            nome_clinica: form.querySelector('[name="nome_clinica"]').value.trim(),
            piano: form.querySelector('[name="piano"]')?.value || 'trial',
        };

        // Validazione base
        if (!data.nome || !data.cognome || !data.email || !data.nome_clinica) {
            showMessage(msgDiv, 'Compila tutti i campi obbligatori.', 'error');
            return;
        }

        if (!isValidEmail(data.email)) {
            showMessage(msgDiv, 'Inserisci un indirizzo email valido.', 'error');
            return;
        }

        // Invio
        btn.classList.add('btn-loading');
        btn.disabled = true;

        try {
            const res = await fetch(`${API_BASE}/manuale/register`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
                body: JSON.stringify(data),
            });

            const result = await res.json();

            if (!res.ok) {
                throw new Error(result.message || result.error || 'Errore durante la registrazione');
            }

            // Se il piano è a pagamento, redirect a Stripe Checkout
            if (result.checkout_url) {
                window.location.href = result.checkout_url;
                return;
            }

            // Trial: mostra successo
            showMessage(msgDiv, 'Registrazione completata! Controlla la tua email per accedere al manuale.', 'success');
            form.reset();

        } catch (err) {
            showMessage(msgDiv, err.message || 'Errore di connessione. Riprova.', 'error');
        } finally {
            btn.classList.remove('btn-loading');
            btn.disabled = false;
        }
    });
});

// ============================================================
// Piano selezionato dal pricing
// ============================================================
function selectPlan(planSlug) {
    const planInput = document.querySelector('[name="piano"]');
    if (planInput) planInput.value = planSlug;

    const section = document.getElementById('registrazione');
    if (section) section.scrollIntoView({ behavior: 'smooth', block: 'start' });
}

// ============================================================
// Helpers
// ============================================================
function isValidEmail(email) {
    return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
}

function showMessage(el, text, type) {
    if (!el) return;
    el.textContent = text;
    el.className = type === 'error'
        ? 'mt-4 p-3 rounded-lg bg-red-50 text-red-700 text-sm'
        : 'mt-4 p-3 rounded-lg bg-green-50 text-green-700 text-sm';
    el.classList.remove('hidden');

    if (type === 'success') {
        setTimeout(() => el.classList.add('hidden'), 8000);
    }
}
