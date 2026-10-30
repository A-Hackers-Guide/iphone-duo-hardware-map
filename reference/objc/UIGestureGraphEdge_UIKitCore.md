# `UIGestureGraphEdge`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIGestureGraphElement`
- 3 instance variables, 4 properties, 8 instance methods, 0 class methods

## Instance variables

```
B _directed;
@"UIGestureGraphNode" _sourceNode;
@"UIGestureGraphNode" _targetNode;
```

## Properties

```
@property (T@"UIGestureGraphNode",R,N,V_sourceNode) sourceNode;
@property (T@"UIGestureGraphNode",R,N,V_targetNode) targetNode;
@property (TB,R,N,GisDirected,V_directed) directed;
@property (TB,R,N,GisLoop) loop;
```

## Instance methods

```
-[UIGestureGraphEdge sourceNode];
-[UIGestureGraphEdge description];
-[UIGestureGraphEdge targetNode];
-[UIGestureGraphEdge commonNode:];
-[UIGestureGraphEdge initWithLabel:sourceNode:targetNode:directed:];
-[UIGestureGraphEdge isDirected];
-[UIGestureGraphEdge isLoop];
-[UIGestureGraphEdge oppositeNode:];
```
