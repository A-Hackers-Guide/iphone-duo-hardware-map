# `SBFlexibleWindowingAutoLayoutSpace`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSMutableCopying`
- 12 instance variables, 12 properties, 37 instance methods, 0 class methods

## Instance variables

```
B _stripVisible;
B _dockVisible;
@"NSArray" _autoLayoutItems;
@"SBContinuousExposeAutoLayoutConfiguration" _configuration;
@"NSSet" _groups;
@"SBFlexibleWindowingAutoLayoutGroup" _stageSpanningSplit;
Q _ownedDisplayRectCorners;
d _occupiedAreaPercentage;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _boundingBox;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _stageArea;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _compactedBoundingBox;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _exposeBoundingBox;
```

## Properties

```
@property (T@"SBContinuousExposeAutoLayoutConfiguration",&,N,V_configuration) configuration;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_boundingBox) boundingBox;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_stageArea) stageArea;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_compactedBoundingBox) compactedBoundingBox;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_exposeBoundingBox) exposeBoundingBox;
@property (TB,N,GisStripVisible,V_stripVisible) stripVisible;
@property (TB,N,GisDockVisible,V_dockVisible) dockVisible;
@property (T@"NSSet",&,N,V_groups) groups;
@property (T@"SBFlexibleWindowingAutoLayoutGroup",&,N,V_stageSpanningSplit) stageSpanningSplit;
@property (TQ,N,V_ownedDisplayRectCorners) ownedDisplayRectCorners;
@property (Td,N,V_occupiedAreaPercentage) occupiedAreaPercentage;
@property (T@"NSArray",R,N,V_autoLayoutItems) autoLayoutItems;
```

## Instance methods

```
-[SBFlexibleWindowingAutoLayoutSpace mutableCopyWithZone:];
-[SBFlexibleWindowingAutoLayoutSpace isDockVisible];
-[SBFlexibleWindowingAutoLayoutSpace setBoundingBox:];
-[SBFlexibleWindowingAutoLayoutSpace succinctDescriptionBuilder];
-[SBFlexibleWindowingAutoLayoutSpace setConfiguration:];
-[SBFlexibleWindowingAutoLayoutSpace boundingBox];
-[SBFlexibleWindowingAutoLayoutSpace descriptionWithMultilinePrefix:];
-[SBFlexibleWindowingAutoLayoutSpace setGroups:];
-[SBFlexibleWindowingAutoLayoutSpace succinctDescription];
-[SBFlexibleWindowingAutoLayoutSpace groups];
-[SBFlexibleWindowingAutoLayoutSpace configuration];
-[SBFlexibleWindowingAutoLayoutSpace hash];
-[SBFlexibleWindowingAutoLayoutSpace description];
-[SBFlexibleWindowingAutoLayoutSpace copyWithZone:];
-[SBFlexibleWindowingAutoLayoutSpace isEqual:];
-[SBFlexibleWindowingAutoLayoutSpace initWithItems:];
-[SBFlexibleWindowingAutoLayoutSpace descriptionBuilderWithMultilinePrefix:];
-[SBFlexibleWindowingAutoLayoutSpace _copyWithClass:];
-[SBFlexibleWindowingAutoLayoutSpace autoLayoutItems];
-[SBFlexibleWindowingAutoLayoutSpace setDockVisible:];
-[SBFlexibleWindowingAutoLayoutSpace compactedBoundingBox];
-[SBFlexibleWindowingAutoLayoutSpace containsDisplayItem:];
-[SBFlexibleWindowingAutoLayoutSpace exposeBoundingBox];
-[SBFlexibleWindowingAutoLayoutSpace flexibleAutoLayoutItemForDisplayItem:];
-[SBFlexibleWindowingAutoLayoutSpace flexibleAutoLayoutItemForDisplayItemIfExists:];
-[SBFlexibleWindowingAutoLayoutSpace isStripVisible];
-[SBFlexibleWindowingAutoLayoutSpace occupiedAreaPercentage];
-[SBFlexibleWindowingAutoLayoutSpace ownedDisplayRectCorners];
-[SBFlexibleWindowingAutoLayoutSpace setCompactedBoundingBox:];
-[SBFlexibleWindowingAutoLayoutSpace setExposeBoundingBox:];
-[SBFlexibleWindowingAutoLayoutSpace setOccupiedAreaPercentage:];
-[SBFlexibleWindowingAutoLayoutSpace setOwnedDisplayRectCorners:];
-[SBFlexibleWindowingAutoLayoutSpace setStageArea:];
-[SBFlexibleWindowingAutoLayoutSpace setStageSpanningSplit:];
-[SBFlexibleWindowingAutoLayoutSpace setStripVisible:];
-[SBFlexibleWindowingAutoLayoutSpace stageArea];
-[SBFlexibleWindowingAutoLayoutSpace stageSpanningSplit];
```
