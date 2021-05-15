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
Definition 1: A vector *v* is called a linear combination of the vectors *{v1, v2, ..., vn}* if *v = 𝜶1v1 + 𝜶2v2 + ... + 𝜶nvn* .

Definition 2: The set of all vectors *V* as above is called the **linear span** of the set *{v1, v2, ..., vn}* and is denoted by: 

***span(v1, v2, ..., vn) = <v1, v2, ..., vn>***.

![](https://github.com/mohammadhashemii/ML-RahnemaCollege/blob/master/Week-1/images/0_span.png)

Note: *span(v1, v2, ..., vn)* is itself a vector space over *R*. These kinds of sets are called **subspaces** of *V*.

Fact: *span(v1, v2, ..., vn)* is the smallest subspace of *V* containing *{v1, v2, ..., vn} ⊂ W*.

![](https://github.com/mohammadhashemii/ML-RahnemaCollege/blob/master/Week-1/images/1_span2.png)

Definition 3: A set *{v1, v2, ..., vn}⊂ V* is called **linearly dependant** if there exist *𝜶1, 𝜶2, ..., 𝜶n ∈ R*, not all of which are 0, such that *𝜶1v1, 𝜶2v2, ..., 𝜶nvn= 0*.

Which means that at least one of the vectors like *vi* can be written as the linear combination of other vectors in *{v1, v2, ..., vi, ..., vn}*.