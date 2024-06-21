Drupal 7 - Content Management Framework
=======================================

**IMPORTANT NOTE:** Drupal 7 is EOL Jan 2025 (extended life support). If you
are starting a new Drupal project, DO **NOT** use this appliance. Instead use
the `Drupal 10 appliance`_.

`Drupal`_ is an open source content management platform licensed under
the GPL. Equipped with a powerful blend of features, Drupal can support
a variety of websites ranging from personal blogs, corporate brochures
and large community-driven websites.

This appliance includes all the standard features in `TurnKey Core`_,
and on top of that:

- Drupal 7 configurations:
   
   - Installed (using drush) from upstream source code to /var/www/drupal7

     **Security note**: Updates to Drupal may require supervision so
     they **ARE NOT** configured to install automatically. See below for
     updating Drupal.

   - Includes drush for command line administration and configuration.

   - Drupal security update alerts delivered to your inbox - requires 
     `Security Alerts`_ ('secalerts') be enabled on firstboot with a valid 
     email address.

- Bundled popular Drupal 7 modules and dependencies (installed to
  /var/www/drupal7/sites/all/modules):

   - `Admin menu`_: Adds dropdown administration menu to the top of the
     screen.
   - `Admin views`_: Replaces administrative overview/listing pages 
     with actual views for superior usability.
   - `Advanced\_help`_: Improves the Drupal help system.
   - `Backup and migrate`_: Backup and restore your Drupal site
     on-demand or on a schedule.
   - `CKEditor`_: Enables CKEditor (a WYSIWYG editor) instead of plain
     text fields.
   - `Colorbox`_: Light-weight customizable plugin to provide overlayed 
     images (replaces previous inclusion of Lightbox2).
   - `Drush`_: a command line shell and Unix scripting interface for
     Drupal.
   - `Field group`_: Allows fields to be grouped together.
   - `GlobalRedirect`_: Alias 301 redirects, prevents duplicate content.
     (SEO)
   - `Google analytics`_: Adds Google Analytics js tracking code to all
     your site's pages.
   - `Honeypot`_: A honeypot for deterring spam bots from completing 
     forms on your site  (additionally uses timestamp method).
   - `Imce`_: Powerful image file uploader and browser, with support for
     on the fly resizing.
   - `Module filter`_: Allows modules on the modules list page to be 
     filtered for easier reading.
   - `PathAuto`_: Auto-generate search engine friendly URLs (SEO).
   - `Rules`_: Lets you define conditionally executed actions based on
     occurring events.
   - `Token`_: Provides a shared API for replacement of textual
     placeholders with actual data.
   - `Views`_: Allows creation of dynamic pages ("views") of existing 
     content.
   
   Note: Only some modules are enabled by default. To enable/disable 
     modules, navigate to **Administer > Modules** (or 
     http://example.com/admin/modules). Some modules may require
     additional configuration and/or permissions settings.

- SSL support out of the box.
- `Adminer`_ administration frontend for MySQL (listening on port
  12322 - uses SSL).
- Postfix MTA (bound to localhost) to allow sending of email (e.g.,
  password recovery).
- Webmin modules for configuring Apache2, PHP, MySQL and Postfix.

Supervised Manual Drupal Update
-------------------------------

It is possible to check for and install updates from the Drupal Admin 
UI:: **Admin > Reports > Available Updates**

Or from the command line::

    drush pm-refresh
    drush pm-update --security-only --simulate
    drush pm-update --security-only

We also recommend that you  subscribe to the drupal.org security 
newsletter (create a user account on drupal.org and within your drupal.org 
profile:: **Edit > My newsletter** tab).

Credentials *(passwords set at first boot)*
-------------------------------------------

-  Webmin, SSH, MySQL: username **root**
-  Adminer: username **adminer**
-  Drupal 7: username **admin**

.. _Drupal 10 appliance: https://www.turnkeylinux.org/drupal10
.. _Drupal: https://drupal.org
.. _TurnKey Core: https://www.turnkeylinux.org/core
.. _Security Alerts: https://www.turnkeylinux.org/docs/automatic-security-alerts
.. _Admin menu: https://drupal.org/project/admin_menu
.. _Admin views: https://www.drupal.org/project/admin_views
.. _Advanced\_help: https://drupal.org/project/advanced_help
.. _Backup and migrate: https://drupal.org/project/backup_migrate
.. _CKEditor: https://drupal.org/project/ckeditor
.. _Colorbox: https://www.drupal.org/project/colorbox
.. _Drush: https://drupal.org/project/drush
.. _Field group: https://www.drupal.org/project/field_group
.. _GlobalRedirect: https://drupal.org/project/globalredirect
.. _Google analytics: https://drupal.org/project/google_analytics
.. _Honeypot: https://www.drupal.org/project/honeypot
.. _Imce: https://drupal.org/project/imce
.. _Module filter: https://www.drupal.org/project/module_filter
.. _PathAuto: https://drupal.org/project/pathauto
.. _Rules: https://drupal.org/project/rules
.. _Token: https://drupal.org/project/token
.. _Views: https://www.drupal.org/project/views
.. _Adminer: https://www.adminer.org
