# `UIGestureGraphNode`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIGestureGraphElement`
- 4 instance variables, 5 properties, 22 instance methods, 0 class methods

## Instance variables

```
@"NSMutableSet" _inEdges;
@"NSMutableSet" _outEdges;
@"NSMutableSet" _inOutEdges;
@"NSMapTable" _edgesByLabel;
```

## Properties

```
@property (TQ,R,N) edgeCount;
@property (T@"NSSet",R,N) allEdges;
@property (T@"NSSet",R,N) inEdges;
@property (T@"NSSet",R,N) outEdges;
@property (T@"NSSet",R,N) inOutEdges;
```

## Instance methods

```
-[UIGestureGraphNode description];
-[UIGestureGraphNode edgeCount];
-[UIGestureGraphNode inEdges];
-[UIGestureGraphNode _addEdge:];
-[UIGestureGraphNode _edgesForType:createIfNeeded:];
-[UIGestureGraphNode _removeEdge:];
-[UIGestureGraphNode allEdges];
-[UIGestureGraphNode edgeCountForLabel:];
-[UIGestureGraphNode edgesForLabel:];
-[UIGestureGraphNode enumerateEdgesBetweenNode:usingBlock:];
-[UIGestureGraphNode enumerateEdgesFromNode:usingBlock:];
-[UIGestureGraphNode enumerateEdgesTowardNode:usingBlock:];
-[UIGestureGraphNode enumerateNeighborNodesUsingBlock:];
-[UIGestureGraphNode hasEdgeBetweenNode:];
-[UIGestureGraphNode hasEdgeFromNode:];
-[UIGestureGraphNode hasEdgeTowardNode:];
-[UIGestureGraphNode inOutEdges];
-[UIGestureGraphNode isInEdge:];
-[UIGestureGraphNode isInOutEdge:];
-[UIGestureGraphNode isOutEdge:];
-[UIGestureGraphNode outEdges];
-[UIGestureGraphNode typeOfEdge:];
```
