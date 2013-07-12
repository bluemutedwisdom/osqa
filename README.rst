OSQA - QA system
================

`OSQA`_ is the free, open source Q&A system you've been waiting for.
With OSQA your site is more than just an FAQ page, it is a full-featured
Q&A community. Users earn points and badges for useful participation,
and everyone in the community wins.

This appliance includes all the standard features in `TurnKey Core`_,
and on top of that:

- OSQA configurations:
   
   - Installed from upstream source code to /var/www/osqa
   - Includes hourly cron job to trigger email alerts (convenience).

- SSL support out of the box.
- Postfix MTA (bound to localhost) to allow sending of email (e.g.,
  password recovery).
- Webmin modules for configuring Apache2, MySQL and Postfix.

Credentials *(passwords set at first boot)*
-------------------------------------------

-  Webmin, SSH, MySQL: username **root**


.. _OSQA: http://www.osqa.net/
.. _TurnKey Core: http://www.turnkeylinux.org/core
