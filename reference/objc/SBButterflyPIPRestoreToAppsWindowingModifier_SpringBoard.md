# `SBButterflyPIPRestoreToAppsWindowingModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBWindowingModifier`
- 3 instance variables, 0 properties, 17 instance methods, 0 class methods

## Instance variables

```
@"SBAppLayout" _zoomingAppLayout;
q _zoomingAppLayoutUpcomingScreenRegion;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _zoomingAppLayoutBoundingBox;
```

## Instance methods

```
-[SBButterflyPIPRestoreToAppsWindowingModifier clippingFrameForIndex:withBounds:];
-[SBButterflyPIPRestoreToAppsWindowingModifier clipsToBoundsAtIndex:];
-[SBButterflyPIPRestoreToAppsWindowingModifier transactionCompletionOptions];
-[SBButterflyPIPRestoreToAppsWindowingModifier clippingFrameForLayoutRole:inAppLayout:atIndex:withBounds:];
-[SBButterflyPIPRestoreToAppsWindowingModifier visibleHomeAffordanceLayoutElements];
-[SBButterflyPIPRestoreToAppsWindowingModifier adjustedSpaceAccessoryViewScale:forAppLayout:];
-[SBButterflyPIPRestoreToAppsWindowingModifier transitionWillBegin:];
-[SBButterflyPIPRestoreToAppsWindowingModifier completesWhenChildrenComplete];
-[SBButterflyPIPRestoreToAppsWindowingModifier visibleItems];
-[SBButterflyPIPRestoreToAppsWindowingModifier shouldPerformCrossfadeForReduceMotion];
-[SBButterflyPIPRestoreToAppsWindowingModifier cornersForItem:];
-[SBButterflyPIPRestoreToAppsWindowingModifier animationAttributesForItem:];
-[SBButterflyPIPRestoreToAppsWindowingModifier opacityForItem:];
-[SBButterflyPIPRestoreToAppsWindowingModifier visibleAppSpaces];
-[SBButterflyPIPRestoreToAppsWindowingModifier frameForItem:];
-[SBButterflyPIPRestoreToAppsWindowingModifier _isItemZoomingAppLayout:];
-[SBButterflyPIPRestoreToAppsWindowingModifier initWithTransitionModifier:zoomingAppLayout:];
```
