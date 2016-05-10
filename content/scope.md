## Scope and Bounties

### The following sites are in-scope for this bounty:

- `example1.example.gov`
- `example2.example.gov`

Remember, you may only look for vulnerabilities in sites listed above; anything
else is out of scope. Submissions covering other domains/apps are not 
eligable for rewards.

### Bounty rewards

The following guidlines gives some idea of typical bounties for certain
classes of bugs. We'll typically follow these guidlines closely, but we do
reserve the right to adjust our rewards based on our assessment of severity and
the quality of the report. For example, we may pay less for low-quality reports,
or more for low-severity issues that are especially novel or required
significant effort.

#### Tier 1: High Severity - $3,500

- SQL injection
- Remote Code Executioin
- Site-wide authentication bypass
- Site-wide elevation of privilege
- Widespread or complete personal information disclosure

#### Tier 2: Medium Severity - $1,000

- XSS on critical actions
- CSRF on critical functions such as admin or superuser actions
- Significant authentication bypass or elevation of privilege
- Individual or targeted personal information disclosure

#### Tier 3: Low Severity - $500

- All other XSS/CSRF not excluded below
- Server misconfiguration / provisioning errors
- Information leaks other than personal information
- SSL configuration issues, including mixed content issues
- Open redirects

### What doesn't qualify?

Certain types of vulnerabilities/bugs don't qualify. You're welcome to submit
bugs in these categories, but we typically won't fix them, and you won't
be eligable for any rewards.

- Bugs that have already been submitted by another participant, and/or that we're already aware of, and/or that we've previously decided aren't eligable.
- Insecure cookie settings that don't present a security risk.
- Issues such as timing attacks that reveal the existance of an account or a user.
- Brute-force attacks requiring substantial time or cost to exploit.
- Issues generated/discovered by automated security scanners.
- Publically-disclosed bugs in open-source software we re-use.
- Denial-of-service attacks.
- Bugs requiring phsyical access to machines or networks.
- Version information disclosure.
- Clickjacking on pre-authenticated pages, or the non-existence of X-Frame-Options, or other non-exploitable clickjacking issues.
- Reports about Strict Transport Security (HSTS) headers
- Reports about XSS mitigation headers (`X-Content-Type` and `X-XSS-Protection`)
- Reports about `X-Content-Type-Options` headers
- Reports about missing Content Security Policy (CSP) settings, or about CSP when set in report-only mode. Reports about misconfigured CSP on sites that are actually using it are in scope.
- Out of date software versions
- HTTP 404/500 pages that don't disclose sensitive information
- Disclosure of known public files (e.g. `robots.txt`) or directories
- CSRF on non-authenticated forms (such as contact forms)
- Logout CSRF
- Reports about HTTP `OPTIONS` method being enabled

If you have any questions about what's in scope, please [email us](mailto:fixme@example.com) and we'll figure it out.