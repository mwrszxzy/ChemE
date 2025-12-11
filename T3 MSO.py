Sets
    i   Armazens   / a1, a2 /
    j   Fabricas   / A, B, C /;

Parameters
    supply(i)   / a1 40, a2 30 /
    demand(j)   / A 10, B 20, C 30 /
    cost(i,j);

Table cost(i,j)
          A   B   C
    a1    2   5   3
    a2    5   2   1 ;

Variables
    x(i,j)   quantidade transportada
    z        custo_total;

Positive Variable x;

Equations
    obj         função_objetivo
    supply_con(i)
    demand_con(j);

obj..         z =e= sum((i,j), cost(i,j)*x(i,j));

supply_con(i)..  sum(j, x(i,j)) =l= supply(i);

demand_con(j)..  sum(i, x(i,j)) =e= demand(j);

Model transporte /all/;

Solve transporte using lp minimizing z;

Display x.l, z.l;
