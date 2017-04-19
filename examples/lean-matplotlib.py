# ==============================================================================
# title           : lean-matplotlib
# description     :
# author          : Julien Reynier
# date            : 31/03/2017
# version         :
# IDE             : PyCharm Community Edition
# ==============================================================================
# GENERAL COMMENTS:
# In python files, comment lines are preceded by # or as multi-line strings
# """ """; in PyCharm, Command+/ is the shortcut to comment lines.
# Any file should start with author name and date
# In the case graph do not display correctly on your system ask a specialist
# (Google?) about "matplotlib backend", they shall understand.
#
# FOR MATLAB USERS:
# matlab equivalents are contained in numpy for computations and matplotlib
# for graphs1
# the following pages may help as well:
# http://mathesaurus.sourceforge.net/matlab-numpy.html
# http://cs231n.github.io/python-numpy-tutorial/
#
# useful default Mac shortcuts
# to browse console Command+Options+E
# to execute selection in console Control+Shift+E
# You may add F5 to evaluate file in console and F9 to execute selection

import matplotlib.pyplot as plt  # import a lib with an alias for the
# namespace (these are standard aliases, it is better to respect them)
import matplotlib.mlab as mlab
from matplotlib.pylab import rcParams

from numpy import *  # import numpy, no namespace !
plt.ion()  # for a non blocking show()

# activate interactive mode
# for more info http://matplotlib.org/faq/usage_faq.html#what-is-interactive-mode
plt.ion()

x = linspace(0., pi, 100)
# a simple plot
x = linspace(0., 2*pi, 100)
plt.plot(cos(x), sin(x))

# needed if not in interactive mode
# plt.show(block=False)

# now a more complex example with multiple plots

n = 1000
titi = random.uniform(size=n)
toto = random.logistic(size=n)

fig1 = plt.figure()
ax11 = fig1.add_subplot(221)
ax11.hist(toto)
plt.ylabel('label for y in current axis')

fig1.add_subplot(222).hist(titi)
fig1.add_subplot(223).plot(cos(x), sin(x))
fig1.add_subplot(224).plot(tan(x), sin(x))

fig2 = plt.figure()
fig2.add_subplot(111).plot(x, x)

# can continue plotting on the first axis
m = min(toto)
M = max(toto)
w = linspace(m, M, n)
print('toto')  # ctrl+shift+E is the default shortcut to execute one line

ax11.plot(w, n * mlab.normpdf(w, 0, 1))
fig1.suptitle('A nice logistic histogram')
# ax11.set_xlable('label for x')
plt.xlabel('label for x')
plt.legend('A', 'B')

# A faster version: rather than changing properties one by one,
# it is possible to batch the process using a dictionnary.
params = {'legend.fontsize': 'x-large',
          'figure.figsize': (15, 5),
          'axes.labelsize': 'x-large',
          'axes.titlesize': 'x-large',
          'xtick.labelsize': 'x-large',
          'ytick.labelsize': 'x-large'}
rcParams.update(params)


# finally
plt.show()
