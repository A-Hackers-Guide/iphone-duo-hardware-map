# `SBWindowDragGestureWorkspaceTransaction`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBFluidSwitcherGestureWorkspaceTransaction`
- 5 instance variables, 5 properties, 10 instance methods, 0 class methods

## Instance variables

```
B _draggingFromContinuousExposeStrips;
B _unstashingFromHome;
Q _selectedEdge;
{CGPoint="x"d"y"d} _locationInSelectedDisplayItem;
{CGSize="width"d"height"d} _sizeOfSelectedDisplayItem;
```

## Properties

```
@property (TB,R,N,GisDraggingFromContinuousExposeStrips,V_draggingFromContinuousExposeStrips) draggingFromContinuousExposeStrips;
@property (T{CGPoint=dd},R,N,V_locationInSelectedDisplayItem) locationInSelectedDisplayItem;
@property (T{CGSize=dd},R,N,V_sizeOfSelectedDisplayItem) sizeOfSelectedDisplayItem;
@property (TQ,R,N,V_selectedEdge) selectedEdge;
@property (TB,R,N,V_unstashingFromHome) unstashingFromHome;
```

## Instance methods

```
-[SBWindowDragGestureWorkspaceTransaction _gestureType];
-[SBWindowDragGestureWorkspaceTransaction _finishWithGesture:];
-[SBWindowDragGestureWorkspaceTransaction shouldInterceptTransitionRequest:];
-[SBWindowDragGestureWorkspaceTransaction _beginWithGesture:];
-[SBWindowDragGestureWorkspaceTransaction selectedEdge];
-[SBWindowDragGestureWorkspaceTransaction interceptTransitionRequest:];
-[SBWindowDragGestureWorkspaceTransaction isDraggingFromContinuousExposeStrips];
-[SBWindowDragGestureWorkspaceTransaction locationInSelectedDisplayItem];
-[SBWindowDragGestureWorkspaceTransaction sizeOfSelectedDisplayItem];
-[SBWindowDragGestureWorkspaceTransaction unstashingFromHome];
```
