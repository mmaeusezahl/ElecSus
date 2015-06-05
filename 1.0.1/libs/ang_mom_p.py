# Copyright 2014 M. A. Zentile, J. Keaveney, L. Weller, D. Whiting,
# C. S. Adams and I. G. Hughes.

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""return J_+ matrix for angular momentum j

Calculates the + ladder operator for a given angular momentum.

Called by ang_mom.py

"""

from numpy import zeros,sqrt,arange

def jp(jj):
    b=0
    dim=2.0*jj+1.0
    jp=zeros((dim,dim))
    z=arange(dim)
    m=jj-z
    while b<dim-1.0:
        mm=m[b+1]
        jp[b,b+1]=sqrt(jj*(jj+1)-mm*(mm+1)) 
        b=b+1.0
    return jp

