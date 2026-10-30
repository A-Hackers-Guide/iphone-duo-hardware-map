# `SBContinuousExposeArcSwipeSwitcherModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBTransitionSwitcherModifier`
- 7 instance variables, 0 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"SBAppLayout" _toAppLayout;
@"SBAppLayout" _fromAppLayout;
@"SBAppLayout" _selectedAppLayout;
@"SBArcSwipeSwitcherModifier" _arcSwipeModifier;
@"NSSet" _initialVisibleDisplayItems;
B _hideSplitViewHandles;
@"NSString" _uniqueTimerReason;
```

## Instance methods

```
-[SBContinuousExposeArcSwipeSwitcherModifier didMoveToParentModifier:];
-[SBContinuousExposeArcSwipeSwitcherModifier visibleSplitViewHandleNubViews];
-[SBContinuousExposeArcSwipeSwitcherModifier visibleSplitViewHandleDimmingViews];
-[SBContinuousExposeArcSwipeSwitcherModifier topMostLayoutElements];
-[SBContinuousExposeArcSwipeSwitcherModifier transitionWillUpdate];
-[SBContinuousExposeArcSwipeSwitcherModifier fadeInDelayForSplitViewHandles];
-[SBContinuousExposeArcSwipeSwitcherModifier opacityForLayoutRole:inAppLayout:atIndex:];
-[SBContinuousExposeArcSwipeSwitcherModifier handleTimerEvent:];
-[SBContinuousExposeArcSwipeSwitcherModifier _selectedAppLayout];
-[SBContinuousExposeArcSwipeSwitcherModifier initWithTransitionID:fromAppLayout:toAppLayout:selectedAppLayout:initialVisibleAppLayouts:pinSpaceCornerRadiiToDisplayCornerRadii:];
```
