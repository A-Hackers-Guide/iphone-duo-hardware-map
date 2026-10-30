# `SBFlexibleWindowingAutoLayoutItem`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSMutableCopying`
- 14 instance variables, 14 properties, 38 instance methods, 0 class methods

## Instance variables

```
B _positionIsSystemManaged;
B _overlapped;
B _fullyOccluded;
B _inSlideOver;
@"SBDisplayItem" _displayItem;
@"NSString" _identifier;
d _exposeScale;
Q _ownedDisplayRectCorners;
Q _intersectedDisplayRectCorners;
q _sceneRelevancyHint;
{CGSize="width"d"height"d} _size;
{CGPoint="x"d"y"d} _position;
{CGPoint="x"d"y"d} _compactedPosition;
{CGPoint="x"d"y"d} _exposePosition;
```

## Properties

```
@property (T{CGSize=dd},N,V_size) size;
@property (T{CGPoint=dd},N,V_position) position;
@property (T{CGPoint=dd},N,V_compactedPosition) compactedPosition;
@property (T{CGPoint=dd},N,V_exposePosition) exposePosition;
@property (Td,N,V_exposeScale) exposeScale;
@property (TB,N,V_positionIsSystemManaged) positionIsSystemManaged;
@property (TB,N,GisOverlapped,V_overlapped) overlapped;
@property (TB,N,GisFullyOccluded,V_fullyOccluded) fullyOccluded;
@property (TQ,N,V_ownedDisplayRectCorners) ownedDisplayRectCorners;
@property (TQ,N,V_intersectedDisplayRectCorners) intersectedDisplayRectCorners;
@property (TB,N,GisInSlideOver,V_inSlideOver) inSlideOver;
@property (Tq,N,V_sceneRelevancyHint) sceneRelevancyHint;
@property (T@"SBDisplayItem",R,N,V_displayItem) displayItem;
@property (T@"NSString",R,N,V_identifier) identifier;
```

## Instance methods

```
-[SBFlexibleWindowingAutoLayoutItem position];
-[SBFlexibleWindowingAutoLayoutItem mutableCopyWithZone:];
-[SBFlexibleWindowingAutoLayoutItem identifier];
-[SBFlexibleWindowingAutoLayoutItem succinctDescriptionBuilder];
-[SBFlexibleWindowingAutoLayoutItem descriptionWithMultilinePrefix:];
-[SBFlexibleWindowingAutoLayoutItem setFullyOccluded:];
-[SBFlexibleWindowingAutoLayoutItem size];
-[SBFlexibleWindowingAutoLayoutItem succinctDescription];
-[SBFlexibleWindowingAutoLayoutItem displayItem];
-[SBFlexibleWindowingAutoLayoutItem hash];
-[SBFlexibleWindowingAutoLayoutItem description];
-[SBFlexibleWindowingAutoLayoutItem initWithDisplayItem:];
-[SBFlexibleWindowingAutoLayoutItem setPosition:];
-[SBFlexibleWindowingAutoLayoutItem copyWithZone:];
-[SBFlexibleWindowingAutoLayoutItem isEqual:];
-[SBFlexibleWindowingAutoLayoutItem setSize:];
-[SBFlexibleWindowingAutoLayoutItem descriptionBuilderWithMultilinePrefix:];
-[SBFlexibleWindowingAutoLayoutItem frame];
-[SBFlexibleWindowingAutoLayoutItem isFullyOccluded];
-[SBFlexibleWindowingAutoLayoutItem _copyWithClass:];
-[SBFlexibleWindowingAutoLayoutItem setExposeScale:];
-[SBFlexibleWindowingAutoLayoutItem setInSlideOver:];
-[SBFlexibleWindowingAutoLayoutItem compactedPosition];
-[SBFlexibleWindowingAutoLayoutItem exposePosition];
-[SBFlexibleWindowingAutoLayoutItem exposeScale];
-[SBFlexibleWindowingAutoLayoutItem intersectedDisplayRectCorners];
-[SBFlexibleWindowingAutoLayoutItem isInSlideOver];
-[SBFlexibleWindowingAutoLayoutItem isOverlapped];
-[SBFlexibleWindowingAutoLayoutItem ownedDisplayRectCorners];
-[SBFlexibleWindowingAutoLayoutItem positionIsSystemManaged];
-[SBFlexibleWindowingAutoLayoutItem sceneRelevancyHint];
-[SBFlexibleWindowingAutoLayoutItem setCompactedPosition:];
-[SBFlexibleWindowingAutoLayoutItem setExposePosition:];
-[SBFlexibleWindowingAutoLayoutItem setIntersectedDisplayRectCorners:];
-[SBFlexibleWindowingAutoLayoutItem setOverlapped:];
-[SBFlexibleWindowingAutoLayoutItem setOwnedDisplayRectCorners:];
-[SBFlexibleWindowingAutoLayoutItem setPositionIsSystemManaged:];
-[SBFlexibleWindowingAutoLayoutItem setSceneRelevancyHint:];
```
