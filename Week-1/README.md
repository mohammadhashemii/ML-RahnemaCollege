# Week-1: Mathematics & Probailistics


## TODO

In this week, we will cover some basic yet necessary theories and tools of Linear Algebra and Probabilistics which are needed for Machine Leaning.

Table of contents
==============

<!--ts-->
   * [Linear Algebra](#linear-Algebra)
      * [Vector Spaces](#vector-spaces)
      * [Linear Dependency](#linear-dependency)
      * [Linear Transformation](#linear-transformation)
      * [Determinant](#determinant)
      * [Eigen Value Decomposition](#eigen-value-decomposition)
      * [Singular Value Decomposition](#singular-value-decompostion)
      * [Principal Component Analysis](#principal-component-analysis)
<!--te-->

Linear Algebra
==============
Vector Spaces
--------------

Definition: A vector space over the real numbers *R* consists of 
1. A set *V* whose elements are called vectors.
2. A binary operation called **addition opertaion** on vectors, satisfying the following conditions:
- Addition is commutative: *v + w = w + v*
- Addition is associative: *(v + w) + u = v + (w + u)*
- There is unique vector 0 in *V* called zero vector with property that for each vector *v ∈ V, v + 0 = v*
- For each *v ∈ V* there is a unique vector *-v* in *V*, such that *v + (-v) = 0* 

3. Another operation called **scalar multiplication** which for each *𝜶 ∈ R* and each *v ∈ V* assigns a vector *𝜶.v ∈ V*. Again this operation must satisfy the following properties:
- *1.v = v* for each *v ∈ V*
- *(𝜶1𝜶2).v = 𝜶1.(𝜶2.v)*
- *𝜶.(v1+v2) = 𝜶.v1 + 𝜶.v2*
- *(𝜶1 + 𝜶2).v = 𝜶1.v + 𝜶2.v*

Examples of vector spaces(see the proofs in the course videos):

1. R^n with the usual addition and scalar multiplication.
2. Lines and planes **passing through the origin**.
3. *M_mxn(R)*, the set of all *m x n* matrices over *R* again with the usual addition and scalar multiplication.
4.The set of all functions from a set *X* to *R* with addition and scalar multiplication by the    ones on *R*: 
*(f + g)(x) = f(x) + g(x)*, *(𝜶.f)(x) = 𝜶.(f(x))*.

Linear Dependency
--------------
**Definition 1:** A vector *v* is called a linear combination of the vectors *{v1, v2, ..., vn}* if *v = 𝜶1v1 + 𝜶2v2 + ... + 𝜶nvn* .

**Definition 2:** The set of all vectors *V* as above is called the **linear span** of the set *{v1, v2, ..., vn}* and is denoted by: 

***span(v1, v2, ..., vn) = <v1, v2, ..., vn>***.

![](https://github.com/mohammadhashemii/ML-RahnemaCollege/blob/master/Week-1/images/0_span.png)

Note: *span(v1, v2, ..., vn)* is itself a vector space over *R*. These kinds of sets are called **subspaces** of *V*.

Fact: *span(v1, v2, ..., vn)* is the smallest subspace of *V* containing *{v1, v2, ..., vn} ⊂ W*.

![](https://github.com/mohammadhashemii/ML-RahnemaCollege/blob/master/Week-1/images/1_span2.png)

**Definition 3 - Linear Independency**: A set *{v1, v2, ..., vn}⊂ V* is called **linearly dependant** if there exist *𝜶1, 𝜶2, ..., 𝜶n ∈ R*, not all of which are 0, such that *𝜶1v1, 𝜶2v2, ..., 𝜶nvn= 0*.

Which means that at least one of the vectors like *vi* can be written as the linear combination of other vectors in *{v1, v2, ..., vi, ..., vn}*.

**Definition 4 - Linear Dependency**: A set *{v1, v2, ..., vn}⊂ V* which is not linearly dependent is called linearly independent, i.e. if *𝜶1v1, 𝜶2v2, ..., 𝜶nvn= 0*.

for some *𝜶1, 𝜶2, ..., 𝜶n ∈ R* then all *𝜶i*'s are **zero**.

**Definition 5 - Basis:** Any liearly independence set *{v1, v2, ..., vn} ⊂ V* which spans *V* is called a basis for vector space *V*.

By definition, for every *v ∈ V*

*v = 𝜶1v1 + 𝜶2v2 + ... + 𝜶nvn*

Also this representation is unique.(Proof is in slides)

**Definition 6 - Coordinates in basis:** The vector *v = [𝜶1v1, 𝜶2v2, ..., 𝜶nvn] ^ T* is called the coordinate vector of *v* relative to ordered basis *{v1, v2, ...m vn}*.

Linear Transformation
--------------

Definition: Let *V* and *W* be two vector spaces. A function *T: V -> W* is called linear map or a linear transformation if for all *v, u ∈ V,*:

*T(𝜶v + u) = 𝜶T(v) + T(u)*.

Important note: In the equation above, the addition operation in the left hand side is the one in the *V* vector space, on the other hand the right hand addition operation is in *W*.

Some examples of valid linear transformations:

1. The identity function *I: V -> V* given by *I(v) = v*
2. For any fixed scalar 𝜶, the mapping: *S_𝜶: V -> V* given by *S_𝜶(v) = 𝜶.v*.
3. For *A ∈ M_mxn(R)*, the mapping *T : R^n -> R^m* given by **T(X) = AX** is a linear map. **In fact every other linear map *T': R^n -> R^m* is of this form**.

![](https://github.com/mohammadhashemii/ML-RahnemaCollege/blob/master/Week-1/images/4_linear-transformation.png)

Properties of linear transformation:
1. For each linear map *T: V -> W, T(0_v) = 0_w*
2. Linear maps send linear combination to linear combinations, So the image of a linear map *T: V -> W*  given by *img(T) = {T(v): v ∈ V}* is a subspace of *W*. Dimension of this subspace is called the rank of *T*.
3. If *{v1, ..., vn}* is a basis for *V*, then every linear map from *V* to another vector space *W* is uniquely determined by *{T(v1), ..., T(vn)}*.
4. **Kernel** or null-space of a linear map defined by 

*ker(T) = {v ∈ V: T(v) = 0}*

is a subspace of *V*. Dimension of this subspace is called the nullity of *T*.

![](https://github.com/mohammadhashemii/ML-RahnemaCollege/blob/master/Week-1/images/5_kernel.png)

5. ***Rank(T) + nullity(T) = dim(V)***
6. The set of all linear maps between *V* and *W* denoted by I *L(V, W)* is itself a vector space.

Determinant
--------------
Properties of determinant:
1. If matrix has two equal rows, then *det(A) = 0*.
2. If *A'* is obtained by interchanging two rows of *A*, then *det(A) = - det(A')*.
3. There exists exactly one function with the above properties(See the proof of this theorem in the slides).

Other properties:
- *det(A^T) = det(A)*
- *det(A)* is non zero iff *A* is invertible, in which case *det(A^-1) = 1/det(A)*.
- *det(AB) = det(A).det(B)*.
- For both triangular and diagonal matrices, *det(A) = a00 x a11 x ... x ann*.
- *det(A) != 0* iff the rows(respectively, columns) of *A are linearly indepedent.

Note: See the geometric applications of determinant in the slides.