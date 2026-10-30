# `SBMutableFlexibleWindowingAutoLayoutSpace`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBFlexibleWindowingAutoLayoutSpace`
- 1 instance variables, 12 properties, 4 instance methods, 0 class methods

## Instance variables

```
Q ownedDisplayRectCorners;
```

## Properties

```
@property (T@"NSArray",R,D,N) autoLayoutItems;
@property (T@"SBContinuousExposeAutoLayoutConfiguration",&,D,N) configuration;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},D,N) boundingBox;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},D,N) stageArea;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},D,N) compactedBoundingBox;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},D,N) exposeBoundingBox;
@property (TB,D,N,GisStripVisible) stripVisible;
@property (TB,D,N,GisDockVisible) dockVisible;
@property (T@"NSSet",&,D,N) groups;
@property (T@"SBFlexibleWindowingAutoLayoutGroup",&,D,N) stageSpanningSplit;
@property (TQ,N,VownedDisplayRectCorners) ownedDisplayRectCorners;
@property (Td,D,N) occupiedAreaPercentage;
```

## Instance methods

```
-[SBMutableFlexibleWindowingAutoLayoutSpace flexibleAutoLayoutItemForDisplayItem:];
-[SBMutableFlexibleWindowingAutoLayoutSpace flexibleAutoLayoutItemForDisplayItemIfExists:];
-[SBMutableFlexibleWindowingAutoLayoutSpace ownedDisplayRectCorners];
-[SBMutableFlexibleWindowingAutoLayoutSpace setOwnedDisplayRectCorners:];
```
