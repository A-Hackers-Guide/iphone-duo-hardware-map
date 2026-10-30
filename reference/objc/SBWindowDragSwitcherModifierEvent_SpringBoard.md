# `SBWindowDragSwitcherModifierEvent`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBGestureSwitcherModifierEvent`
- 5 instance variables, 5 properties, 12 instance methods, 0 class methods

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
@property (TB,N,GisDraggingFromContinuousExposeStrips,V_draggingFromContinuousExposeStrips) draggingFromContinuousExposeStrips;
@property (T{CGPoint=dd},N,V_locationInSelectedDisplayItem) locationInSelectedDisplayItem;
@property (T{CGSize=dd},N,V_sizeOfSelectedDisplayItem) sizeOfSelectedDisplayItem;
@property (TQ,N,V_selectedEdge) selectedEdge;
@property (TB,N,V_unstashingFromHome) unstashingFromHome;
```

## Instance methods

```
-[SBWindowDragSwitcherModifierEvent setSelectedEdge:];
-[SBWindowDragSwitcherModifierEvent selectedEdge];
-[SBWindowDragSwitcherModifierEvent copyWithZone:];
-[SBWindowDragSwitcherModifierEvent isDraggingFromContinuousExposeStrips];
-[SBWindowDragSwitcherModifierEvent isWindowDragGestureEvent];
-[SBWindowDragSwitcherModifierEvent locationInSelectedDisplayItem];
-[SBWindowDragSwitcherModifierEvent setDraggingFromContinuousExposeStrips:];
-[SBWindowDragSwitcherModifierEvent setLocationInSelectedDisplayItem:];
-[SBWindowDragSwitcherModifierEvent setSizeOfSelectedDisplayItem:];
-[SBWindowDragSwitcherModifierEvent setUnstashingFromHome:];
-[SBWindowDragSwitcherModifierEvent sizeOfSelectedDisplayItem];
-[SBWindowDragSwitcherModifierEvent unstashingFromHome];
```
