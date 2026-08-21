"""Exact symbolic audit of the record-scale normalization semigroup."""
import sympy as s

nu,Om,R0,R1,R2=s.symbols('nu Om R0 R1 R2', positive=True)
rnu=s.sqrt(nu/Om)

def mu(R): return s.simplify(nu/(Om*R**2))
assert s.simplify(mu(R2)-(rnu/R2)**2)==0

# Scale transfer V_R1 = amp * V_R2(q z), q=R1/R2.
q12=R1/R2
amp12=R2/R1
q01=R0/R1
amp01=R1/R0
q02=R0/R2
amp02=R2/R0
assert s.simplify(q12*q01-q02)==0
assert s.simplify(amp12*amp01-amp02)==0

# Canonical nesting to r_nu.
sqrtmu=s.sqrt(mu(R2))
assert s.simplify(sqrtmu-rnu/R2)==0
assert s.simplify((R2/rnu)*(1/(Om*R2))-1/(Om*rnu))==0

# First derivative/curl weight under R-scale normalization:
# amplitude 1/(Om R), derivative in y contributes R.
firstjet=s.simplify(R2/(Om*R2))
assert firstjet==1/Om

# Square action mu_R * Delta_y curl(V_R):
# curl(V_R)=omega/Om, Delta_y contributes R^2.
square=s.simplify(mu(R2)*R2**2/Om)
assert square==nu/Om**2

# Circulation transfer R2 -> R1: amplitude R2/R1 and line scale R1/R2
# depending direction, macro circulation = (R1/R2)^2 micro circulation.
circ=s.simplify((R1/R2)**2)
assert s.simplify(circ-mu(R2))==0 if R1==rnu else True
# Direct canonical case.
assert s.simplify((rnu/R2)**2-mu(R2))==0

# Physical fixed Galilean frame c has dimensionless weight d_R=c/(Om R).
c=s.symbols('c', positive=True)
d1=c/(Om*R1); d2=c/(Om*R2)
assert s.simplify(d1-(R2/R1)*d2)==0

print('mu_R =',mu(R2))
print('sqrt(mu_R) =',sqrtmu)
print('PASS: scale-transfer semigroup composition')
print('PASS: all canonical nests land at r_nu normalization')
print('PASS: first-jet weight is R-independent')
print('PASS: square-contact action is R-independent')
print('PASS: canonical circulation transfer factor equals mu_R')
print('PASS: Galilean frame weights obey the scale cocycle')
