#=== Configuration Dev/Prod ===
import os

# Active le mode sécurisé (production) si DJANGO_SECURE=true
DJANGO_SECURE = os.getenv("DJANGO_SECURE", "false").lower() == "true"
# DEBUG sera False en production sécurisée
DEBUG = not DJANGO_SECURE

#=== Sécurité des cookies ===
# Seuls les cookies de session sont envoyés sur HTTPS
SESSION_COOKIE_SECURE = DJANGO_SECURE
# Seuls les cookies CSRF sont envoyés sur HTTPS
CSRF_COOKIE_SECURE = DJANGO_SECURE

# JS ne peut pas accéder aux cookies de session
SESSION_COOKIE_HTTPONLY = True
# Le token CSRF doit rester accessible en JS pour fonctionner
CSRF_COOKIE_HTTPONLY = False

# Limitation des cookies pour réduire les risques CSRF
SESSION_COOKIE_SAMESITE = "Lax"
CSRF_COOKIE_SAMESITE = "Lax"

#=== HTTPS et HSTS ===
# Redirection automatique vers HTTPS en production
SECURE_SSL_REDIRECT = DJANGO_SECURE  # True si DJANGO_SECURE
# Durée HSTS (en secondes) : 31536000 = 1 an
SECURE_HSTS_SECONDS = 31536000 if DJANGO_SECURE else 0
# Appliquer HSTS à tous les sous-domaines
SECURE_HSTS_INCLUDE_SUBDOMAINS = True if DJANGO_SECURE else False
# Ajouter le site à la preload list HSTS (optionnel)
SECURE_HSTS_PRELOAD = False

#=== Headers de sécurité ===
# Empêche les navigateurs de deviner le type de contenu
SECURE_CONTENT_TYPE_NOSNIFF = True
# Contrôle l'envoi du header Referer pour réduire la fuite d'URL
SECURE_REFERRER_POLICY = "strict-origin-when-cross-origin"
# Protection contre le clickjacking (interdiction d'afficher le site dans un iframe)
X_FRAME_OPTIONS = "DENY"

#=== CSP (Content Security Policy) ===
# Middleware CSP doit être en première position dans MIDDLEWARE
# MIDDLEWARE = ["csp.middleware.CSPMiddleware"] + MIDDLEWARE

# Politique stricte : n'autorise que les ressources du même domaine
CONTENT_SECURITY_POLICY = {
    'DIRECTIVES': {
        'default-src': ("'self'",),   # Toutes ressources par défaut
        'script-src': ("'self'",),    # Scripts autorisés uniquement depuis notre domaine
        'style-src': ("'self'",),     # CSS autorisé uniquement depuis notre domaine
    }
}
