# Canned responses to certain kinds of vuln reports

## cloud.gov customer apps

```
Hi {reporter},

Thanks for reporting this vulnerability to us!

However, this is a customer application, and falls outside of the scope of our
vulnerability disclosure program as described at
https://18f.gsa.gov/vulnerability-disclosure-policy/. The scope for cloud.gov
is described as:

    cloud.gov and the following subdomains: account.fr.cloud.gov,
    api.fr.cloud.gov, ci.fr.cloud.gov, community.fr.cloud.gov,
    dashboard.fr.cloud.gov, login.fr.cloud.gov, logs.fr.cloud.gov,
    metrics.fr.cloud.gov. Any other subdomain of cloud.gov and all
    customer applications are excluded from this policy.

The domain you reported, {domain}, is outside of this scope.

We'll do our best to contact the customer and pass your report on to them, but
we can't guarantee anything about their response.

Thanks again, we really appreciate your work and your report!

{signature}
```

## Out of scope

```
Thanks for your report, we appreciate your effort.

However, this domain isn't in scope for Vulnerability Disclosure Policy (see https://hackerone.com/tts, and https://github.com/18F/vulnerability-disclosure-policy/blob/main/vulnerability-disclosure-policy.md). In the future, please limit your testing to domains explicitly listed in that scope. This is for your own safety: we want to be sure that everyone's on the same page about your activities being authorized.

If possible, we'll make an effort to pass this on to the appropriate parties, but we can't guarantee any further follow-up.
```
