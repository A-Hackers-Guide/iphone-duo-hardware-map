# `SBMinimizeItemFromSplitResizeWindowingModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBWindowingModifier`
- 10 instance variables, 0 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"NSUUID" _transitionID;
@"SBAppLayout" _fromAppLayout;
@"SBDisplayItem" _evictedDisplayItem;
@"SBAppLayout" _appLayoutSlidingOff;
q _dismissalDirection;
@"SBFlexibleWindowingAutoLayoutSpace" _autoLayoutSpaceBeforePairResize;
@"SBDisplayItem" _leftItem;
@"SBDisplayItem" _rightItem;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _initialScreenFrameForMinimizingItem;
d _displacementForMinimizingItem;
```

## Instance methods

```
-[SBMinimizeItemFromSplitResizeWindowingModifier shouldUseAnchorPointToPinLayoutRolesToSpace:];
-[SBMinimizeItemFromSplitResizeWindowingModifier visibleSplitViewHandleNubViews];
-[SBMinimizeItemFromSplitResizeWindowingModifier dimmingAlphaForLayoutRole:inAppLayout:];
-[SBMinimizeItemFromSplitResizeWindowingModifier frameForLayoutRole:inAppLayout:withBounds:];
-[SBMinimizeItemFromSplitResizeWindowingModifier transitionWillBegin:];
-[SBMinimizeItemFromSplitResizeWindowingModifier cornerRadiiForLayoutRole:inAppLayout:withCornerRadii:];
-[SBMinimizeItemFromSplitResizeWindowingModifier frameForSplitViewHandleNubView:];
-[SBMinimizeItemFromSplitResizeWindowingModifier animationAttributesForItem:];
-[SBMinimizeItemFromSplitResizeWindowingModifier isLayoutRoleMatchMovedToScene:inAppLayout:];
-[SBMinimizeItemFromSplitResizeWindowingModifier maskedCornersForLayoutRole:inAppLayout:withMaskedCorners:];
-[SBMinimizeItemFromSplitResizeWindowingModifier frameForItem:];
-[SBMinimizeItemFromSplitResizeWindowingModifier titleStyleForItem:];
-[SBMinimizeItemFromSplitResizeWindowingModifier initWithDismissalDirection:autoLayoutSpaceBeforePairResize:initialScreenFrameForMinimizingItem:leftItem:rightItem:displacementForMinimizingItem:];
-[SBMinimizeItemFromSplitResizeWindowingModifier shouldInterruptForActivity:];
-[SBMinimizeItemFromSplitResizeWindowingModifier transitionDidComplete:];
```
