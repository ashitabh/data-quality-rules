==================
data-quality-rules
==================

.. image:: https://img.shields.io/github/release/DeNederlandscheBank/data-quality-rules.svg
           :target: https://github.com/DeNederlandscheBank/data-quality-rules/releases/
           :alt: Github release
.. image:: https://img.shields.io/travis/DeNederlandscheBank/data-quality-rules.svg
        :target: https://travis-ci.org/DeNederlandscheBank/data-quality-rules
        :alt: Build Status
.. image:: https://img.shields.io/badge/License-MIT/X-blue.svg
        :target: https://github.com/DeNederlandscheBank/data-quality-rules/blob/master/LICENSE
        :alt: License

This is Data Quality Rules repository for the Solvency 2 and the Financial Assessment Framework (FTK) quantitative reporting templates (QRTs). In this repository De Nederlandsche Bank publishes additional validation rules to improve the data quality of the QRTs.

This repository is part of the iForum pilot 'Data Quality Rules'. Want to know more? Please contact P.M.Willems@dnb.nl

* Free software: MIT/X license

Features
========

Here is what the package contains:

* (Statistical) validation rules for Solvency 2 and FTK

* Source code to extract csv-, Pandas pickles- and html-files from XBRL instance files

* Source code to evaluate validation rules on Pandas pickle-files

* Notebook tutorials to get you started


Installation
============

Online installation
-------------------

Clone the project::

  git clone https://github.com/DeNederlandscheBank/data-quality-rules.git

Then start with a clean environment::

  conda create -n your_env_name python=3.6

And activate the environment::

  conda activate your_env_name

Make sure you are in the root of the cloned project. Install the code and the required packages::

  pip install -e .

Offline installation
--------------------

We included all the required packages in the project, so you should be able to do an offline installation. Make sure you have at least Anaconda 5.3.1 installed.

To do an offline installation you need some files from the internet downloaded in advance: 

* the zip file with the data-quality-rules repository from https://github.com/DeNederlandscheBank/data-quality-rules.git;

* the zip files with the taxonomy and example instances from the EIOPA website (https://dev.eiopa.europa.eu/Taxonomy/Full/2.4.0/S2/EIOPA_SolvencyII_XBRL_Taxonomy_2.4.0_with_external_hotfix.zip; and https://dev.eiopa.europa.eu/Taxonomy/Full/2.4.0/S2/EIOPA_SolvencyII_XBRL_Instance_documents_2.4.0.zip)


Install data-quality-rules repository
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Extract the zip file from the data-quality-rules repository to the desired location.

Then start with a clean and empty environment::

  conda create -n your_env_name --offline

And activate the environment::

  conda activate your_env_name

Install the following packages::

  conda install pkgs/vc-14-0.tar.bz2

  conda install pkgs/vs2015_runtime-14.0.25420-0.tar.bz2

Then install the following packages::

  conda install pkgs/python-3.6.6-he025d50_0.tar.bz2

  conda install pkgs/pip-18.1-py36_1000.tar.bz2

  conda install pkgs/setuptools-40.6.3-py36_0.tar.bz2

(if you get an error you need to copy the required packages from internet)

Make sure you are in the root of the cloned project. Then install the project with the packages in pkgs/.::

  pip install -e . --no-index --find-links pkgs/


Copy taxonomy and instance files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Copy the Solvency 2 XBRL taxonomy file and the Solvency 2 XBRL instance examples (both zip files) to the directory data/downloaded files.


Installing taxonomy and example instance files
==============================================

For Solvency 2 execute (in the root of the project)::

  python src/solvency2_data.py

This downloads the Solvency 2 XBRL taxonomy 2.4 and the corresponding example instance files and extracts them in the proper directories.

For FTK, execute (in the root of the project)::

  python src/ftk_data.py

This downloads the FTK taxonomy and the corresponding example instance files and extracts them in the proper directories.


Data format requirements
========================

We added a tutorial that converts an XBRL instance file to csv files for all reporting template in the instance. If you want to use data from another source you have to make sure that the data is in the correct format.

Solvency 2
----------

- the template name follows the standard Solvency 2 code, for example S.02.01.02.01 and S.28.02.01.02;
- the file names of the individual templates is the template name plus an extension (.csv or .pickle), for example S.01.02.07.01.pickle;
- the file name of all closed axes templates combined is the instance file name plus an extension, for example qrs_240_instance.pickle (the example instance for qrs);
- the column names and the index names for all templates have the following format: {reporting template name},R????,C???? or {reporting template name},C????, depending on the definition; for example S.02.01.02.01,R0030,C0010 or S.06.02.01.01,C0040;
 
FTK
---

- the template name follows the standard FTK code with prefix FTK, for example FTK.K101-1 or FTK.K209B;
- the file names of the individual templates is the template name plus an extension (.csv or .pickle), for example FTK.K101-1.pickle;
- the file name of all closed axes templates combined is the instance file name plus an extension, for example DNB-NR_FTK-2019-06_2019-12-31_MOD_FTK-BEL.pickle (the example instance for FTK-BEL);
- the column names and the index names for all templates have the following format: {reporting template name},R???,C??? or {reporting template name},C???, depending on the definition; for example FTK.K101-1,R010,C010 or FTK.K209B,C150;


Contributing
============

You can contribute in many ways:

Types of Contributions
----------------------

Report Bugs
~~~~~~~~~~~

Report bugs at https://github.com/DeNederlandscheBank/data-quality-rules/issues.

If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

Fix Bugs
~~~~~~~~

Look through the GitHub issues for bugs. Anything tagged with "bug" and "help
wanted" is open to whoever wants to implement it.

Implement Features
~~~~~~~~~~~~~~~~~~

Look through the GitHub issues for features. Anything tagged with "enhancement"
and "help wanted" is open to whoever wants to implement it.

Submit Feedback
~~~~~~~~~~~~~~~

The best way to send feedback is to file an issue at https://github.com/DeNederlandscheBank/data-quality-rules/issues.

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.


Credits
=======

Development Lead
----------------

| Willem Jan Willemse <w.j.willemse@dnb.nl>
| Expert Centre on Data Analysis & Operational Management
| Division Insurance Supervision
| De Nederlandsche Bank (DNB)

Contributors
------------

* Annick van Ool (DNB)
* Richard Lieverse (DNB)
* Jan Huiskes (DNB)

Your name could be here, see how to contribute in the text above.
