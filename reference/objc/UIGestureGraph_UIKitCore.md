# `UIGestureGraph`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 4 properties, 35 instance methods, 0 class methods

## Instance variables

```
@"NSMapTable" _nodesByLabel;
@"NSMapTable" _edgesByLabel;
```

## Properties

```
@property (TQ,R,N) nodeCount;
@property (T@"NSSet",R,N) nodeLabels;
@property (TQ,R,N) edgeCount;
@property (T@"NSSet",R,N) edgeLabels;
```

## Instance methods

```
-[UIGestureGraph init];
-[UIGestureGraph removeNode:];
-[UIGestureGraph description];
-[UIGestureGraph edgeLabels];
-[UIGestureGraph nodeLabels];
-[UIGestureGraph edgeCount];
-[UIGestureGraph removeAllObjects];
-[UIGestureGraph nodeCount];
-[UIGestureGraph _edgesForLabel:];
-[UIGestureGraph _nodesForLabel:];
-[UIGestureGraph _addEdge:];
-[UIGestureGraph _addNode:];
-[UIGestureGraph _allEdges];
-[UIGestureGraph _allNodes];
-[UIGestureGraph addEdgeWithLabel:sourceNode:targetNode:directed:];
-[UIGestureGraph addNodeWithLabel:];
-[UIGestureGraph addNodeWithLabel:properties:];
-[UIGestureGraph addUniqueEdgeWithLabel:sourceNode:targetNode:directed:properties:];
-[UIGestureGraph addUniqueNodeWithLabel:properties:];
-[UIGestureGraph edgeCountForLabel:];
-[UIGestureGraph edgesForLabel:];
-[UIGestureGraph edgesForLabel:properties:];
-[UIGestureGraph enumerateEdgesWithBlock:];
-[UIGestureGraph enumerateEdgesWithLabel:usingBlock:];
-[UIGestureGraph enumerateNodesWithBlock:];
-[UIGestureGraph enumerateNodesWithLabel:usingBlock:];
-[UIGestureGraph nodeCountForLabel:];
-[UIGestureGraph nodesForLabel:];
-[UIGestureGraph nodesForLabel:properties:];
-[UIGestureGraph removeEdge:];
-[UIGestureGraph removeEdges:];
-[UIGestureGraph removeNodeEdges:];
-[UIGestureGraph removeNodes:];
-[UIGestureGraph traverseGraphBreadthFirstFromNode:directed:usingBlock:];
-[UIGestureGraph traverseGraphDepthFirstFromNode:directed:usingBlock:];
```
