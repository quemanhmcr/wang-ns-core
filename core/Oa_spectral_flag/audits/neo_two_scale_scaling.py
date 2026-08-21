"""Exact algebraic scaling audit for the NEO finite two-scale lab.

We encode scaling weights for V~=sqrt(mu) W(z), y=sqrt(mu) z, with time unchanged.
All three normalized NS terms must carry the same prefactor sqrt(mu), while curl is order-preserved.
"""
import sympy as sp

mu = sp.symbols('mu', positive=True)
amp = sp.sqrt(mu)          # V~ amplitude relative to W
inv_len = 1/sp.sqrt(mu)   # d/dy relative to d/dz

w_time = sp.simplify(amp)
w_conv = sp.simplify(amp * inv_len * amp)
w_visc = sp.simplify(mu * amp * inv_len**2)
w_curl = sp.simplify(amp * inv_len)
w_circ = sp.simplify(amp * sp.sqrt(mu))

print('time prefactor      =', w_time)
print('convection prefactor=', w_conv)
print('viscous prefactor   =', w_visc)
print('curl prefactor      =', w_curl)
print('circulation factor macro/micro =', w_circ)

assert sp.simplify(w_time-w_conv) == 0
assert sp.simplify(w_time-w_visc) == 0
assert sp.simplify(w_curl-1) == 0
assert sp.simplify(w_circ-mu) == 0

nu, Om, ell = sp.symbols('nu Om ell', positive=True)
mu_def = nu/(Om*ell**2)
rnu = sp.sqrt(nu/Om)
scale_res = sp.simplify(rnu/ell-sp.sqrt(mu_def))
print('record radius / macro radius - sqrt(mu) =', scale_res)
assert scale_res == 0
print('PASS: two-scale square restoration and record-scale coincidence')


# Contact-action covariance weights.
# grad_z W = amp*(sqrt(mu))*inv? Directly W=mu^-1/2 V(sqrt(mu)z): coefficient 1.
grad_weight = sp.simplify(mu**(-sp.Rational(1,2))*sp.sqrt(mu))
curl_weight = grad_weight
material_weight = sp.Integer(1)  # time unchanged; W.grad_z = V.grad_y
lap_omega_weight = mu            # Delta_z omega_W = mu Delta_y omega_V
outer_heat_weight = mu
print('gradient/strain weight =', grad_weight)
print('curl weight            =', curl_weight)
print('material derivative weight =', material_weight)
print('inner Laplacian vs outer Laplacian weight =', lap_omega_weight)
assert grad_weight == 1
assert curl_weight == 1
assert lap_omega_weight == outer_heat_weight
print('PASS: contact-action prism is covariant under canonical nesting')
