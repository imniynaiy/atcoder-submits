https://en.wikipedia.org/wiki/2-satisfiability

## Purpose of cmp:
- cmp[i] stores an integer that represents the “component ID” of the node i. Each strongly connected component in the graph is assigned a unique ID (starting from 0 and incrementing with each new component).
- If two nodes have the same value in cmp, it means they are part of the same strongly connected component.

The line solution[i] = (cmp[i] > cmp[take_not(i)]); works based on a key property of the strongly connected components (SCCs) and the order in which they are processed in the SCC graph (also known as the “condensation” of the graph). Here’s an explanation of why this approach is correct:

## Key Insight

When solving 2-SAT using SCCs, we transform the problem into checking the implication graph of variables. This graph will have each variable  x_i  and its negation  \neg x_i  as nodes. If the graph has a valid SCC ordering, then it’s possible to assign truth values to satisfy all constraints.

## How the SCC Order Helps

1.	Topological Order of Components:
	In the SCC decomposition, the components (i.e., SCCs) are ordered in a way that if there’s an edge from component  A  to component  B , then  A  will appear before  B  in the order.
	

This ordering is useful for 2-SAT because we can resolve the values of variables in a way that respects all implications in the graph.
2.	Decision Rule for Truth Values:
	

For each variable  x , if  x  and  \neg x  belong to the same SCC, then no valid solution exists because it means both  x  and  \neg x  are mutually dependent.
	

If they are in different SCCs, the topological ordering of SCCs allows us to assign truth values based on which component comes first.
3.	The Assignment Step:
	

When we check cmp[i] > cmp[take_not(i)], we’re leveraging the fact that the variable with the “larger” SCC ID can be safely assigned true, as it will not cause conflicts with its negation.
	

If cmp[i] > cmp[take_not(i)] is true, it means the SCC for  x_i  comes after  \neg x_i , so we set  x_i  to true.
	

Conversely, if cmp[i] < cmp[take_not(i)],  x_i  is assigned false because it implies that  \neg x_i  should come later in the order.

## Why This Works

The assignment of true or false in this way ensures that all implications are respected. By processing variables in the order of their SCCs, we ensure that each variable assignment is consistent with the constraints of the problem.