STL Decompose
=============

This is a relatively naive Python implementation of the "Seasonal and Trend decomposition using Loess" time series decomposition ("STL decomposition," Cleveland et al. 1990 [`pdf <http://cs.wellesley.edu/~cs315/Papers/stl%20statistical%20model.pdf>`_]).  

This implementation is a variation of (and takes inspiration from) the current implementation of the ``seasonal_decompose`` method `in statsmodels <http://www.statsmodels.org/stable/generated/statsmodels.tsa.seasonal.seasonal_decompose.html#statsmodels.tsa.seasonal.seasonal_decompose>`_. In this implementation, the trend component is calculated by substituting a configurable `Loess regression <https://en.wikipedia.org/wiki/Local_regression>`_ for the convolutional method used in ``seasonal_decompose``. It also extends the existing ``DecomposeResult`` from ``statsmodels`` to allow for forecasting based on the calculated decomposition. 


Usage
-----

The ``stldecompose`` package is relatively lightweight, exposing only a couple of primary methods: ``decompose()`` and ``forecast()``, along with a handful of built-in forecasting functions. See `the included IPython notebook <https://github.com/jrmontag/STLDecompose/blob/master/STL%20usage%20example.ipynb>`_ for more details.  



Installation
------------

A Python 3 virtual environment is recommended.

Current installation is via cloning this repo to your local workspace and a local pip install:: 
    
    (env) $ git clone git@github.com:jrmontag/STLDecompose.git 
    (env) $ cd STLDecompose; pip install . 



More Resources
--------------

- ``statsmodels`` `Time Series analysis <http://www.statsmodels.org/stable/tsa.html>`_ package
- Hyndman's `OTexts reference on STL decomposition <https://www.otexts.org/fpp/6/5>`_  
 
