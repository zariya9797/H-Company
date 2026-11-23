<!-- coderabbit-ai-generated:v1 -->

# H Company site

The site is static. From the repository root, run `python3 -m http.server 4173` and open `http://localhost:4173/h-company-website.html`. Vercel uses `vercel.json` to serve the same page at the main address.

## Change the contact and payment details

Edit the `content` values at the top of `h-company-website.html`. The existing shared phone, email, UPI ID and QR are the defaults.

| Service | Phone | UPI ID or UPI payment link | QR filename |
| --- | --- | --- | --- |
| Fabrication | `hcompany-fab-phone` | `hcompany-fab-upi` | `hcompany-fab-qr` |
| Electrical work and supplies | `hcompany-elec-phone` | `hcompany-elec-upi` | `hcompany-elec-qr` |
| Technology | `hcompany-tech-phone` | `hcompany-tech-upi` | `hcompany-tech-qr` |

<!-- coderabbit-ai-generated:v1 -->

<!-- coderabbit-ai-generated-section:v1:62e21ec3bfacc548c3a09880d3a47e271b39757a5a293bbbe0b820365b650a6f -->

For a separate phone, enter the business number with its country code, for example `+91XXXXXXXXXX` with the Xs replaced by digits. Leave the phone field blank to use the shared phone. Visitors call the number for their selected service. The existing email setting is retained for future use.

<!-- /coderabbit-ai-generated:v1 -->

To give a service its own payment recipient, fill in both its UPI and QR fields. Save the QR beside the HTML file, for example as `electrical-qr.png`, and enter that filename, including its extension. Check that it points to the same payee as the UPI ID and uses ₹149. If both fields are blank, the service uses the existing shared payment details. If you fill in only one, the other payment option stays unavailable for that service. Phone settings are independent of UPI and QR settings.

The old `update-csp.py` refreshed security hashes for CSS and JavaScript embedded in the page. The redesigned site loads them from `assets/` instead, so you can edit those files and the contact fields without running a script.

## Photos

<!-- coderabbit-ai-generated:v1 -->

<!-- coderabbit-ai-generated-section:v1:b48c22e8f799bbbe27967ecaa1dbff86bae9dcffd54bf094eb7ba834a0196a9b -->

Stock photography from Pexels: [metal fabrication](https://www.pexels.com/photo/2381463/), [electrical panel](https://www.pexels.com/photo/257736/) and [technology](https://www.pexels.com/photo/4705628/). The photos illustrate the service categories.

Fonts: Barlow Condensed and DM Sans, distributed under the SIL Open Font License; the license files are in `assets/fonts/`.

<!-- /coderabbit-ai-generated:v1 -->
