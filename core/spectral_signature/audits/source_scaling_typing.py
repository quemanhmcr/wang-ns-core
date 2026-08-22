#!/usr/bin/env python3
"""Scaling-type tribunal for the Theory-2 source endgame.

For the whole-space Navier--Stokes scaling
    u_lambda(x,t)=lambda*u(lambda*x,lambda^2*t),
Fourier velocity density has exponent -2.  A quadratic one-derivative
edge-source density f has exponent -3.  The six-dimensional edge square is
therefore instantaneous-scale invariant, while the three-dimensional
resultant J has L2-square exponent +3.

The forced source g=(partial_t+nu*kappa)f has density exponent -1.  Hence
G_alpha=int kappa^alpha |g|^2 d(edge) has instantaneous exponent 4+2*alpha.
After time integration subtract 2.  In particular G_-1 has action exponent 0,
whereas G_-1/2 and int ||J||_2^2 dt both have exponent +1.  This is the exact
scaling reason the historical barrier misses one half heat derivative.
"""


def main():
    uhat = -2
    curl_coeff = 1
    edge_measure = 6
    output_measure = 3
    time_measure = -2

    f = curl_coeff + 2 * uhat
    s2 = 2 * f + edge_measure
    jhat = f + 3  # integrate one parent variable
    j2 = 2 * jhat + output_measure

    g = f + 2  # one parabolic time/heat derivative

    def G(alpha):
        return 2 * g + edge_measure + 2 * alpha

    assert f == -3
    assert s2 == 0
    assert jhat == 0
    assert j2 == 3
    assert G(-1) == 2
    assert G(-0.5) == 3
    assert G(-1) + time_measure == 0
    assert G(-0.5) + time_measure == 1
    assert j2 + time_measure == 1

    print("PASS whole-space scaling: edge source density exponent = -3")
    print("PASS instantaneous S2_edge exponent = 0; ||J||_2^2 exponent = 3")
    print("PASS action G_-1 exponent = 0")
    print("PASS action G_-1/2 exponent = 1 = action ||J||_2^2 exponent")
    print("PASS: raw ||J||^2/S2 amplification is concentration-sensitive, not a projective-coherence invariant")


if __name__ == "__main__":
    main()
