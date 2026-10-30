# `SBEntityRemovalSlideOffscreenSwitcherModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBTransitionSwitcherModifier`
- 7 instance variables, 0 properties, 18 instance methods, 0 class methods

## Instance variables

```
B _isSecondStage;
@"NSUUID" _transitionID;
@"SBAppLayout" _appLayout;
@"SBSwitcherModifier" _multitaskingModifier;
Q _direction;
@"SBEntityRemovalToHomeSwitcherModifier" _toHomeRemovalModifier;
@"SBEntityRemovalDosidoSlideOutAnimationSettings" _animationSettings;
```

## Instance methods

```
-[SBEntityRemovalSlideOffscreenSwitcherModifier scaleForIndex:];
-[SBEntityRemovalSlideOffscreenSwitcherModifier anchorPointForIndex:];
-[SBEntityRemovalSlideOffscreenSwitcherModifier shouldUseAnchorPointToPinLayoutRolesToSpace:];
-[SBEntityRemovalSlideOffscreenSwitcherModifier appLayoutsToEnsureExistForMainTransitionEvent:];
-[SBEntityRemovalSlideOffscreenSwitcherModifier didMoveToParentModifier:];
-[SBEntityRemovalSlideOffscreenSwitcherModifier adjustedSpaceAccessoryViewAnchorPoint:forAppLayout:];
-[SBEntityRemovalSlideOffscreenSwitcherModifier animationAttributesForLayoutElement:];
-[SBEntityRemovalSlideOffscreenSwitcherModifier _layoutSettings];
-[SBEntityRemovalSlideOffscreenSwitcherModifier adjustedSpaceAccessoryViewFrame:forAppLayout:];
-[SBEntityRemovalSlideOffscreenSwitcherModifier topMostLayoutElements];
-[SBEntityRemovalSlideOffscreenSwitcherModifier shouldPinLayoutRolesToSpace:];
-[SBEntityRemovalSlideOffscreenSwitcherModifier transitionWillUpdate];
-[SBEntityRemovalSlideOffscreenSwitcherModifier visibleAppLayouts];
-[SBEntityRemovalSlideOffscreenSwitcherModifier perspectiveAngleForIndex:];
-[SBEntityRemovalSlideOffscreenSwitcherModifier opacityForLayoutRole:inAppLayout:atIndex:];
-[SBEntityRemovalSlideOffscreenSwitcherModifier handleTimerEvent:];
-[SBEntityRemovalSlideOffscreenSwitcherModifier frameForIndex:];
-[SBEntityRemovalSlideOffscreenSwitcherModifier initWithTransitionID:appLayout:direction:animationSettings:multitaskingModifier:];
```
