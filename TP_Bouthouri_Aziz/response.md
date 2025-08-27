Question: Qu’est-ce que le clickjacking et comment X_FRAME_OPTIONS protège contre cette attaque ?

Réponse:

Clickjacking is an attack where a malicious website tricks a user into clicking something different from what the user perceives, often by overlaying invisible frames or buttons on legitimate content.

X_FRAME_OPTIONS = "DENY" prevents the website from being loaded in a frame or iframe on another site. This stops attackers from embedding your site in a hidden frame to perform clickjacking.



Étape 8: Content Security Policy (CSP)

Question: What happens when you add <script>alert("Test XSS")</script> in your template?

Réponse:

The inline script does not execute because the CSP you set (script-src 'self') blocks any inline JavaScript.


""" Refused to execute inline script because it violates the following Content Security Policy directive: "script-src 'self'". Either the 'unsafe-inline' keyword, a hash ('sha256-1k/2zM9KjaHZKY1yXnUIy5F1oyM8M+cpFSoRKcd+5kQ='), or a nonce ('nonce-...') is required to enable inline execution. """



Question: What headers should you see in headers_after.txt?

Réponse:
When your project is run in secure mode, you should see at least these headers in the HTTPS response:

strict-transport-security → Ensures browsers always use HTTPS

content-security-policy → Defines allowed sources for scripts, styles, etc.

x-content-type-options → Stops MIME sniffing (nosniff)

x-frame-options → Prevents clickjacking


