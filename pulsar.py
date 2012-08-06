#!/usr/bin/python

class Pulsar:
    """ Class to store an individual pulsar"""
    def __init__(self,
                 period=None,
                 dm=None,
                 gl=None,
                 gb=None,
                 galCoords=None,
                 dtrue=None,
                 lum_1400=None,
                 spindex=None,
                 alpha=None,
                 rho=None,
                 width_degree=None,
                 scindex=-3.86):
        """___init___ function for the Pulsar class"""
        self.period = period
        self.dm = dm
        
        self.gl = gl
        self.gb = gb
        self.galCoords = galCoords
        self.dtrue = dtrue

        self.lum_1400 = lum_1400
        self.spindex = spindex
        self.scindex = scindex
        self.alpha = alpha
        self.rho = rho
        self.width_degree = width_degree

    # methods to calculate derived properties
    def s_1400(self):
        """Calculate the flux of the pulsar"""
        return self.lum_1400 / self.dtrue / self.dtrue

    def width_ms(self):
        """Return the pulse width in milliseconds"""
        return self.width_degree * self.period / 360.0

