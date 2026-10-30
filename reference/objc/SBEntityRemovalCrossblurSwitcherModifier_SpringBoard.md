# `SBEntityRemovalCrossblurSwitcherModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBTransitionSwitcherModifier`
- 6 instance variables, 0 properties, 19 instance methods, 0 class methods

## Instance variables

```
B _animateOpacity;
@"NSUUID" _transitionID;
@"SBAppLayout" _appLayout;
@"SBAppLayout" _removalAppLayout;
@"SBSwitcherModifier" _multitaskingModifier;
@"SBEntityRemovalToHomeSwitcherModifier" _toHomeRemovalModifier;
```

## Instance methods

```
-[SBEntityRemovalCrossblurSwitcherModifier scaleForIndex:];
-[SBEntityRemovalCrossblurSwitcherModifier anchorPointForIndex:];
-[SBEntityRemovalCrossblurSwitcherModifier shouldUseAnchorPointToPinLayoutRolesToSpace:];
-[SBEntityRemovalCrossblurSwitcherModifier appLayoutsToEnsureExistForMainTransitionEvent:];
-[SBEntityRemovalCrossblurSwitcherModifier didMoveToParentModifier:];
-[SBEntityRemovalCrossblurSwitcherModifier adjustedSpaceAccessoryViewAnchorPoint:forAppLayout:];
-[SBEntityRemovalCrossblurSwitcherModifier animationAttributesForLayoutElement:];
-[SBEntityRemovalCrossblurSwitcherModifier adjustedSpaceAccessoryViewFrame:forAppLayout:];
-[SBEntityRemovalCrossblurSwitcherModifier topMostLayoutElements];
-[SBEntityRemovalCrossblurSwitcherModifier shouldPinLayoutRolesToSpace:];
-[SBEntityRemovalCrossblurSwitcherModifier transitionWillUpdate];
-[SBEntityRemovalCrossblurSwitcherModifier visibleAppLayouts];
-[SBEntityRemovalCrossblurSwitcherModifier perspectiveAngleForIndex:];
-[SBEntityRemovalCrossblurSwitcherModifier opacityForLayoutRole:inAppLayout:atIndex:];
-[SBEntityRemovalCrossblurSwitcherModifier transitionDidEnd];
-[SBEntityRemovalCrossblurSwitcherModifier handleTimerEvent:];
-[SBEntityRemovalCrossblurSwitcherModifier frameForIndex:];
-[SBEntityRemovalCrossblurSwitcherModifier shouldAllowGroupOpacityForAppLayout:];
-[SBEntityRemovalCrossblurSwitcherModifier initWithTransitionID:appLayout:layoutRole:multitaskingModifier:];
```
