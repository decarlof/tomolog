=======
tomolog
=======

**tomolog** is commad-line-interface for extracting tomolog data from `data exchange <https://dxfile.readthedocs.io/en/latest/source/xraytomo.html/>`_ tomographic data used at the `Advanced Photon Source <https://www.aps.anl.gov/>`_  `beamlines <https://dxfile.readthedocs.io/en/latest/source/demo/doc.areadetector.html>`_.

Installation
============

::

    $ git clone https://github.com/xray-imaging/tomolog.git
    $ cd tomolog
    $ python setup.py install

in a prepared virtualenv or as root for system-wide installation.

.. warning:: 
	If your python installation is in a location different from #!/usr/bin/env python please edit the first line of the bin/tomolog file to match yours.


Dependencies
============

- `dxchange <https://github.com/data-exchange/dxchange>`_ version > 0.1.6 
- pandas => ``conda install pandas``
- tabulate => ``conda install tabulate``

Usage
=====

View the tomolog data
-------------------

To view the tomolog data::

    $ tomolog show --h5-name data/base_file_name_001.h5 

	2020-06-12 23:26:19,796 - General
	2020-06-12 23:26:19,797 -   config           ./tomolog.conf
	2020-06-12 23:26:19,797 -   verbose          True

+-----------------------+--------------------------+---------+
|                       | value                    | unit    |
+=======================+==========================+=========+
| 000_resolution        | 4.7                      | microns |
+-----------------------+--------------------------+---------+
| 000_energy            | 20.0                     | keV     |
+-----------------------+--------------------------+---------+
| 000_experimenter_name | Francesco De Carlo       |         |
+-----------------------+--------------------------+---------+
| 000_full_file_name    | base_file_name_001.h5    |         |
+-----------------------+--------------------------+---------+
| 000_end_date          | 2020-06-12T15:11:12-0500 |         |
+-----------------------+--------------------------+---------+
| 000_sample_in_x       | 0.0                      | mm      |
+-----------------------+--------------------------+---------+
| 000_sample_in_y       | 0.0                      | mm      |
+-----------------------+--------------------------+---------+
| 000_start_date        | 2020-06-12T14:02:35-0500 |         |
+-----------------------+--------------------------+---------+

To generate an rst file containing a table compatible sphinx/readthedocs::

    $ tomolog docs --h5-name data/base_file_name_001.h5


.. note:: 
	--h5-name can be also a folder, e.g. --h5-name data/ in this case all hdf files in the folder will be processed.


to list of all available options::

    $ tomolog  -h


Configuration File
------------------

tomolog parameters are stored in **tomolog.conf**. You can create a template with::

    $ tomolog init

**tomolog.conf** is constantly updated to keep track of the last stored parameters, as initalized by **init** or modified by setting a new option value. For example to re-run the last tomolog with identical --h5-name parameters used before just use::

    $ tomolog docs

