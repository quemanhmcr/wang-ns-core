"""Symbolic audit of the angular polynomial invariant J = omega x A omega.

For trace-free A, omega is the axial curl vector determined by the skew part of A.
Under restricted Riccati A_t=-A^2+tr(A^2)I/3, verify omega_t=A omega
and J_t=0 identically.
"""
import sympy as s

a11,a12,a13,a21,a22,a23,a31,a32=s.symbols('a11 a12 a13 a21 a22 a23 a31 a32', real=True)
a33=-a11-a22
A=s.Matrix([[a11,a12,a13],[a21,a22,a23],[a31,a32,a33]])
g=s.trace(A*A)
At=-A*A+g*s.eye(3)/3

def axial_curl(M):
    return s.Matrix([M[2,1]-M[1,2], M[0,2]-M[2,0], M[1,0]-M[0,1]])

def cross(x,y): return s.Matrix([x[1]*y[2]-x[2]*y[1],x[2]*y[0]-x[0]*y[2],x[0]*y[1]-x[1]*y[0]])

w=axial_curl(A)
wt=axial_curl(At)
assert all(s.simplify(x)==0 for x in wt-A*w)
q=A*w
qt=At*w+A*wt
assert all(s.simplify(x)==0 for x in qt-g*w/3)
J=cross(w,q)
Jt=cross(wt,q)+cross(w,qt)
assert all(s.simplify(x)==0 for x in Jt)
print('PASS: restricted Riccati implies omega_t=A omega')
print('PASS: restricted Riccati implies (A omega)_t=(g/3) omega')
print('PASS: angular polynomial J=omega x A omega is exactly invariant')
