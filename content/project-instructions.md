## Your Project's Bug Bounty

We aim for our bug bounties to be a win for everyone involved: the project, the
researchers, and everyone that depends on our software.

### Vulnerability Maturity Model

Our partner, HackerOne, has [a maturity model for vulnerability coordination](https://www.hackerone.com/blog/vulnerability-coordination-maturity-model).  It
is not strictly necessary that your project have expert-level maturity in every
capability to participate, but in general, more maturity is better.

__Organizational__: How does your project respond to vulnerability reports?
* Basic: Executive support to respond to reports.
* Advanced: Defined policies/processes/etc. for responding to reports.
* Expert: Dedicated staff for responding to reports.

__Engineering__: How does your project manage vulnerabilities?
* Basic: All bugs are tracked to resolution.
* Advanced: Security bugs are tracked to resolution, deferral, or acceptance.
* Expert: Security bug classes are tracked.

__Communications__: How does your project communicate about its vulnerabilities?
* Basic: You have a channel to distribute advisories to impacted parties.
* Advanced: You have tailored channels for each of your audiences.
* Expert: You have an information sharing program to coordinate disclosure.

__Analytics__: How does your project improve its security?
* Basic: Bug tracking data is used to measure code quality over time.
* Advanced: Automated development practices eliminate security bug classes.
* Expert: Instrumentation captures exploit attempts and triggers mitigation.

__Incentives__: How does your project encourage engagement?
* Basic: Clear legal statement that protects researchers who report bugs.
* Advanced: Financial rewards.
* Expert: Financial rewards tailored to your project's vulnerability market.

In a nutshell, projects will have bugs reported to them, and their ability to
deal with them gracefully will be the key to success.  Your project needs to be
mature enough to address any reported issues in a reasonable amount of time.
18F's Bug Bounty Team is here to provide assistance, but not oversight!  Your
project will own all the responsibilities, from making sure the reports get a
response, to making sure the incentives are properly aligned.

### SLAs

Projects that participate in the bug bounty program inherit a SLA.  Issues
must be resolved within 90 days of being reported, but note that "resolved" for
the purposes of the bug bounty program does not necessarily mean fixed.  For
example, vulnerabilities that you determine will not be fixed within 90 days can
be resolved by paying the reporter and communicating your plan.  Also note that
bug bounty resolution is entirely separate from any federal policy and
compliance with one does not confer compliance with the other.

The Bug Bounty Team will notify you about unresolved reports on every half-life 
(i.e. Day 45, 22, 11, 5, 3, 2, and 1) to help you track issues as they get
closer to the SLA.

#### Your Project's Participation

Regardless of what level of maturity your project has, you can expect the
following tasks to come your way:

* __Triage__: As issues are reported, you'll need to review the reports to
qualify them.  Some may contain all the information you need, others may be
lacking and require follow-up.  Some will be serious, others may be invalid.
Some of the serious ones may qualify as a
[security incident](https://handbook.18f.gov/security-incidents/) .   Sometimes
you may see duplicates, of both the serious and the invalid.  In any case, we
recommend you triage issues within a week, if not daily.  Triaging is complete
when you have enough information from the reporter to implement a fix and assign
it a priority, or enough information to dismiss it as not a bug.

* __Tracking__: Once you've qualified a report as a vulnerability, you'll
need to track it to its conclusion.  This is especially important for
lower-risk vulnerabilities as they are at high risk of not being prioritized
above other work.  Tracking is complete when you have a permanent, searchable
record of the decisions that were made leading up to the resolution, deferral,
or acceptance of the bug.

* __Communication__: Reporters expect updates on the issues they've
reported. Usually nothing more at the beginning than "thanks we got it, expect a
fix $whenever", and then "ok it's fixed!" at the end. If something changes
while the vulnerability is still open, though, you should communicate that to
the reporter.  You may also have to communicate with customers, partners, and
others depending on the scope of the bug.  Communications is complete once all
of the impacted parties have been informed of the steps you've taken to resolve
the bug, and any additional steps they may need to take in response.

#### Time Commitment

Time spent on those bug bounty tasks should be Tocked as `FIXME / Bug Bounty`,
but time spent on actually resolving the issues should be Tocked to the project 
itself.  Expect to spend on the order of 4-8 hours a week on bounty management
tasks. If at any point you're spending more, that might indicate something is
wrong and you should let the bug bounty team know.

## Ready To Participate?

**Yay!** Contact us in `#bug-bounty` to start the conversation! 
