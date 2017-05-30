# Your Project's Bug Bounty

Want to have a bug bounty for your project? This document outlines the
instructions and requirement for joining.

We aim for our bug bounties to be a win for everyone involved: the project, the
researchers, and everyone that depends on our software. This means we have some
rules designed to set you up for success.

Please note that at the moment, we only have space in the program for **five**
apps. So we may need to turn down some qualified programs. Sorry!

### How we'll select: HackerOne's Vulnerability Maturity Model

Our partner, HackerOne, has [a maturity model for vulnerability
coordination](https://www.hackerone.com/blog/vulnerability-coordination-maturity-model).
It's worth reviewing this model and thinking about where you fit in; in general,
we'll prefer more mature programs to less.

### Requirements To Join

To guarantee that your project's participation in the bug bounty program is a
success, we expect you to be willing to have:

* **Dedicated staff**, on a possibly rotating basis, to responding to vulnerability
reports and fixing reported issues. The staff need not be security experts, but
for availability, you must have two or more staff dedicated to responding and
they must be reachable by a [Slack User Group](https://handbook.18f.gov/slack/#groups).

* **A private GitHub repo for tracking vulnerability reports to resolution.** It
could be an [issues-only repo](https://help.github.com/articles/creating-an-issues-only-repository/), or a full code repository, *but it must be private.*
We'll ask you to track both individual vulnerabilities *and* more general
vulnerability classes -- for example a reported cross-site scripting
vulnerability must also generate a separate issue to find and fix all other
related cross-site scripting vulnerabilities, and when found must also be
tracked separately.

* **Methods to inform parties impacted by a reported vulnerability**, which will
depend on the nature of your project. For example, if your project is an
interactive service, this could be a notice on the front page; if your project
is a code library, this could be an update to the release notes. If your
project features both or more, you must be able to inform each of your
audiences.

* Automated development practices that mitigate common classes of
vulnerabilities. For example, for web apps, your project should a framework that
automatically escapes output so that input doesn't have to be manually escaped.
In other words, we'll want you to be confident that you've already covered
the "low hanging fruit".

* **Be listed in in the [18F Vulnerability Disclosure
Policy](https://github.com/18F/vulnerability-disclosure-policy/blob/master/vulnerability-disclosure-policy.md)**. We can add you as part of your
onboarding to the program, but you'll need to be OK to be listed. Note that
this probably rules out any apps developed for partners, since we can't
unilaterally take vulnerability reports for other agencies.

* **Sufficient funding and staffing for at least three months** (and preferably nine months) of participation
in the program. We want you to be able to guarantee you can fix any reported
issues!

* **Be comfortable with a fully-public bounty.** Our intent is for these bounties
to be fully-public (that is, open to any researcher on HackerOne's platform).
If you want, we can _start_ with a private, invite-only bounty (where
HackerOne selects and invites a few highly-qualified researchers), but only
as a stepping stone towards a fully-public bounty.

In a nutshell, projects will have bugs reported to them, and their ability to
deal with them gracefully will be the key to success.

Your project needs to be mature enough to address any reported issues in a
reasonable amount of time, and to ensure that it isn't having the same kind of issues reported over time. 18F's Bug Bounty Team is here to provide assistance,
but not oversight! Your project will own all the responsibilities, from
making sure the reports get a response, to making sure the incentives are
properly aligned.

### SLAs Your Program Must Meet

Projects that participate in the bug bounty program inherit a SLA. Issues must
be **resolved within 90 days** of being reported. Ideally this means "fixed" but
note that "resolved" for the purposes of the bug bounty program could mean
something else. For example, vulnerabilities that you determine will not be
fixed within 90 days can be resolved by paying the reporter and communicating
your plan. Also note that bug bounty resolution is entirely separate from any
federal policy and compliance with one does not confer compliance with the
other.

The Bug Bounty Team will notify you about unresolved reports on every half-life
(i.e. Day 45, 22, 11, 5, 3, 2, and 1) to help you track issues as they get
closer to the SLA.

#### Your Project's Participation

Regardless of what level of maturity your project has, you can expect the
following tasks to come your way:

* __Triage__: As issues are reported, you'll need to review the reports to
qualify them. Some may contain all the information you need, others may be
lacking and require follow-up. Some will be serious, others may be invalid.
Some of the serious ones may qualify as a
[security incident](https://handbook.18f.gov/security-incidents/). Sometimes
you may see duplicates, serious or invalid. In any case, we recommend you
triage issues within a week, if not daily. Triaging is complete when you have
enough information from the reporter to implement a fix and assign it a
priority, or enough information to dismiss it as not a bug.

* __Tracking__: Once you've qualified a report as a vulnerability, you'll
need to track it to its conclusion. This is especially important for
lower-risk vulnerabilities as they are at high risk of not being prioritized
above other work. Tracking is complete when you have a permanent, searchable
record of the decisions that were made leading up to the resolution, deferral,
or acceptance of the bug.

* __Communication__: Reporters expect updates on the issues they've
reported. Usually nothing more at the beginning than "thanks we got it, expect a
fix $whenever", and then "ok it's fixed!" at the end. If something changes
while the vulnerability is still open, though, you should communicate that to
the reporter. You may also have to communicate with customers, partners, and
others depending on the scope of the bug. Communication is complete once all
of the impacted parties have been informed of the steps you've taken to resolve
the bug, and any additional steps they may need to take in response.

#### Time Commitment And Billing

Time spent on those bug bounty tasks should be Tocked as `411 - TTS Acq / Customer Acq / Bug Bounty`,
but time spent on actually resolving the issues should be Tocked to the project
itself. Expect to spend on the order of 4-8 hours a week on bounty management
tasks. If at any point you're spending more, that might indicate something is
wrong and you should let the bug bounty team know.

## Ready To Participate?

**Yay!** Contact us in [`#bug-bounty`](https://gsa-tts.slack.com/messages/bug-bounty/) to start the conversation!
