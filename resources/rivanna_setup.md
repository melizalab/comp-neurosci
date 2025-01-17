---
title: 'Computational Neuroscience'
subtitle: 'Rivanna Instructions'
documentclass: scrartcl
linkcolor: blue
header-includes:
    - \usepackage[letterpaper, margin=1in]{geometry}
    - \usepackage{mathpazo}
    - \usepackage{eulervm}
---

This document describes how to set up and use your account on Rivanna, the University's high-performance computing cluster. Although you are welcome to use your own laptop to run class notebooks, these instructions will ensure that you have a working software environment and a place to store your project-related data.

### General instructions

Your main method of connecting to Rivanna will be through the OnDemand portal, located at [https://ood.hpc.virginia.edu/](https://ood.hpc.virginia.edu). Use your netbadge login. Contact the instructor if you are unable to login; you may need to be added to the access list.

You will need to start a JupyterLab session. Select JupyterLab from the Interactive Apps dropdown, and set the following options:

- Partition: `Interactive`
- Number of Hours: 2
- Number of Cores: 2
- Memory Request: 16
- Work Directory: `STANDARD`
- Allocation: `psyc5270`

Click Launch and wait for your instance to start up. Once it does, you will be provided with a link to connect to your session.

### Initial setup

You only need to do this once, to install some dependencies.

1. Navigate to `/psyc5270-cdm8j/students`. Click the `New Folder` icon at the
   top of the directory tree and name the newly created directory with your
   computing id. This will be the *personal directory* where you store your work.
2. Use the file tree on the left to navigate to `/psyc5270/comp-neurosci`. Double-click the
   `0-Kernel-Setup.ipynb` notebook to run it. Click on the code cell (the one with a
   pair of brackets on the left), and then press the `Enter` key while holding
   down `Shift`.

Congratulations! You now have a working Python installation.

### Running course notebooks

At the start of each in-class work session (typically Thursdays), your instructor will let you know which notebook to use. There are often last-minute edits to the notebooks before class, so please do not start work beforehand.

1. Start up JupyterLab as above.
2. Navigate to `/psyc5270/comp-neurosci`. Double-click the notebook for that week to start it.
3. Select `Save Notebook As...` from the `File` menu. In the dialog that appears, replace `comp-neurosci` with `students/cdm8j` (use your computing ID, not `cdm8j`) and then click `Save`. This will create a copy of the notebook in your personal directory. This is the copy we will look at for grading. If you omit this step, your work will not be saved.

If you need to work on your notebook after class, make sure to run the copy in your personal folder, not the class copy in `comp-neurosci`.

### General notes and resources

Want to learn more about UNIX or High-Performance Computing? The [Rivanna website](https://www.rc.virginia.edu/) has links to a number of useful resources:

- [FAQs](https://www.rc.virginia.edu/userinfo/faq/rivanna-faq/)
- [Self-guided tutorials](https://learning.rc.virginia.edu/tutorials/)
  - [UNIX tutorial for Beginners](https://learning.rc.virginia.edu/tutorials/unix-tutorial/)
  - [SSH Keys](https://www.rc.virginia.edu/userinfo/howtos/general/sshkeys/)
- [Online workshops](https://www.rc.virginia.edu/education/workshops/)

Our class has been allocated 100,000 CPU hours and 10 TB of shared project space. These resources should be more than enough for our needs, but be aware that they are shared between all of us, so do not use the system for large computations unrelated to class. Contact your instructor if you think you will need more time or disk space.

You are expected to follow Rivanna's [usage policies](https://www.rc.virginia.edu/userinfo/rivanna/overview/#usage-policies).
