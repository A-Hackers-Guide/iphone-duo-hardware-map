# `_UIViewVisitor`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 10 instance methods, 3 class methods

## Instance variables

```
B _visitMaskViews;
B _tracksHierarchy;
B __currentlyVisitingHierarchy;
Q _traversalDirection;
```

## Properties

```
@property (TB,N,V_tracksHierarchy) tracksHierarchy;
@property (TB,N,V__currentlyVisitingHierarchy) _currentlyVisitingHierarchy;
@property (TQ,R,N,V_traversalDirection) traversalDirection;
@property (TB,N,V_visitMaskViews) visitMaskViews;
```

## Class methods

```
+[_UIViewVisitor _removeHierarchyTrackingVisitor:];
+[_UIViewVisitor _addHierarchyTrackingVisitor:];
+[_UIViewVisitor _startTraversalOfVisitor:withView:];
```

## Instance methods

```
-[_UIViewVisitor _currentlyVisitingHierarchy];
-[_UIViewVisitor visitMaskViews];
-[_UIViewVisitor set_currentlyVisitingHierarchy:];
-[_UIViewVisitor _prepareToVisitView:changedSubview:previousWindow:previousSuperview:];
-[_UIViewVisitor setTracksHierarchy:];
-[_UIViewVisitor initWithTraversalDirection:];
-[_UIViewVisitor traversalDirection];
-[_UIViewVisitor setVisitMaskViews:];
-[_UIViewVisitor tracksHierarchy];
-[_UIViewVisitor _visitView:];
```
