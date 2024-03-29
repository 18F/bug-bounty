# Your Project's Bug Bounty

Want to have a bug bounty for your project? This document outlines the
instructions and requirement for joining.

We aim for our bug bounties to be a win for everyone involved: the project, the
researchers, and everyone that depends on our software. This means we have some
rules designed to set you up for success.

Please note that at the moment, we only have space in the program for **five**
apps. So we may need to turn down some qualified programs. Sorry!

### How we'll prioritize among potential participants

If we get more than five interested programs, we'll select for more mature
programs. Our partner, HackerOne, has [a maturity model for vulnerability
coordination](https://www.hackerone.com/blog/vulnerability-coordination-maturity-model)
that we'll use to define "mature" for these purposes. It may be worth reviewing 
this model and thinking about where you fit in.

### Requirements To Join

To guarantee that your project's participation in the bug bounty program is a
success, we expect you to be willing to have:

* **Dedicated staff**, on a possibly rotating basis, to responding to vulnerability
reports and fixing reported issues. The staff need not be security experts, but
for availability, you must have two or more staff dedicated to responding and
they must be reachable through
[#bug-bounty-partners](https://gsa-tts.slack.com/messages/C5JQCD9PH).

* **A private GitHub repo for tracking vulnerability reports to resolution.** It
could be an [issues-only repo](https://help.github.com/articles/creating-an-issues-only-repository/), or a full code repository, *but it must be private.* You may use the [security-incidents](https://github.com/18F/security-incidents)
repo if you don't have a project-specific one.
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
Policy](https://github.com/18F/vulnerability-disclosure-policy/blob/main/vulnerability-disclosure-policy.md)**. We can add you as part of your
onboarding to the program, but you'll need to be OK to be listed. Note that
this probably rules out any apps developed for partners, since we can't
unilaterally take vulnerability reports for other agencies.

* **Sufficient funding and staffing for at least three months** (and preferably
nine months) of participation in the program. We want you to be able to
guarantee you can fix any reported issues!

* **Be comfortable with a fully-public bounty.** Our intent is for these bounties
to be fully-public (that is, open to any researcher on HackerOne's platform).
If you want, we can _start_ with a private, invite-only bounty (where
HackerOne selects and invites a few highly-qualified researchers), but only
as a stepping stone towards a fully-public bounty.

In a nutshell, projects will have bugs reported to them, and their ability to
deal with them gracefully will be the key to success.

Your project needs to be mature enough to address any reported issues in a
reasonable amount of time, and to ensure that it isn't having the same kind of
issues reported over time. 18F's Bug Bounty Team is here to provide assistance,
but not oversight! Your project will own all the responsibilities, from making
sure the reports get a response, to making sure the incentives are properly
aligned.

### SLAs Your Program Must Meet

Projects that participate in the bug bounty program inherit an SLA: **Issues must
be resolved within 90 (calendar) days of being reported.** 

Ideally "resolved" means "fixed" but note that "resolved" for the purposes of 
the bug bounty program could mean something else. For example, vulnerabilities
that you determine will not be fixed within 90 days can be resolved by paying 
the reporter and communicating your plan. Also, note that bug bounty resolution
is entirely separate from any federal policy and compliance with one does not
confer compliance with the other.

If you miss this SLA, that'll prompt a review of the SLA and your involvement
with the bug bounty team. This review will do a few things:

1. Review this 90-day SLA with you and make sure that it is still aligned with
   everyone's goals. It is entirely possible that it might not be. The real
   world is complicated; the SLA may be an over-simplification.

2. Conduct a retrospective with the team that missed the SLA  to determine if
   the reason for missing the SLA and how to avoid it in the future. If we can't
   make changes to meet the SLA in the future, then participation in the bug
   bounty would be put on hold.

The Bug Bounty Team will notify you about unresolved reports on every half-life
(i.e. Day 45, 22, 11, 5, 3, 2, and 1) to help you track issues as they get
closer to the SLA.

#### Suggested timelines

Though the 90-day SLA above is the only _required_ timeline, we do (strongly)
suggest that your program aims for faster remediation of more severe issues:

* High severity: within 7 days
* Medium severity: within 30 days

If you miss these timelines, it should prompt you to deliver an update to
stakeholders and to review the issue and decide whether it is appropriately
ranked. If you consistently can't meet these timelines, that should prompt
a conversation with the bug bounty team about why this is happening.

#### Your Project's Participation

Regardless of what level of maturity your project has, you can expect the
following tasks to come your way:

* __Validation__: As issues are reported, you'll need to review the reports to
validate them. HackerOne will be performing initial triage to reproduce the
issue and assign a severity. While they strive for accuracy, you know your
application best and you play a critical role in the final validation of the issue.
Some may contain all the information you need, others may be lacking and require
follow-up. Some will be serious, others may be invalid.  Some of the serious
ones may qualify as a [security
incident](https://handbook.18f.gov/security-incidents/). Sometimes you may see
duplicates, serious or invalid. In any case, we recommend you validate issues
within a week, if not daily. Validation is complete when you have enough
information from the reporter to implement a fix and assign it a priority, or
enough information to dismiss it as not a bug.

* __Tracking__: Once you've qualified a report as a vulnerability, you'll
need to track it to its conclusion. This is especially important for
lower-risk vulnerabilities as they are at high risk of not being prioritized
above other work. Tracking is complete when you have a permanent, searchable
record of the decisions that were made leading up to the resolution, deferral,
or acceptance of the bug.

* __Communication__: Reporters expect updates on the issues they've
reported. Usually, nothing more at the beginning than "thanks we got it, expect a
fix $whenever", and then "ok it's fixed!" at the end. If something changes
while the vulnerability is still open, though, you should communicate that to
the reporter. You may also have to communicate with customers, partners, and
others depending on the scope of the bug. Communication is complete once all
of the impacted parties have been informed of the steps you've taken to resolve
the bug, and any additional steps they may need to take in response.

#### Time Commitment And Billing

Time spent on those bug bounty tasks should be Tocked as `411 - TTS Acq / Customer Acq / Bug Bounty`,
but time spent on actually resolving the issues should be Tocked to the project
itself. In other words: if you're doing work that you would have done if
_your team_ had discovered the bug, Tock it to your own project as usual.
But if it's work you have to do specifically because the bounty program found
the bug, Tock it to Bug Bounty.

Expect to spend on the order of 4-8 hours a week on bounty management
tasks. If at any point you're spending more, that might indicate something is
wrong and you should let the bug bounty team know.

## Ready To Participate?

**Yay!** Contact us in [`#bug-bounty`](https://gsa-tts.slack.com/messages/bug-bounty/) to start the conversation!
