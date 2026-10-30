# `SBHomeGestureToSwitcherSwitcherModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBTransitionSwitcherModifier`
- 9 instance variables, 1 properties, 25 instance methods, 0 class methods

## Instance variables

```
@"SBAppLayout" _selectedAppLayout;
@"SBSwitcherModifier" _multitaskingModifier;
q _startingEnvironmentMode;
{CGPoint="x"d"y"d} _liftOffVelocity;
{CGPoint="x"d"y"d} _liftOffTranslation;
B _adjustAppLayoutsBeforeTransition;
B _keepSelectedAppLayoutAsTopMostElement;
q _fromPeekConfiguration;
Q _hidEventSenderID;
```

## Properties

```
@property (TQ,N,V_hidEventSenderID) hidEventSenderID;
```

## Instance methods

```
-[SBHomeGestureToSwitcherSwitcherModifier isSwitcherWindowUserInteractionEnabled];
-[SBHomeGestureToSwitcherSwitcherModifier containerStatusBarAnimationDuration];
-[SBHomeGestureToSwitcherSwitcherModifier isHomeScreenContentRequired];
-[SBHomeGestureToSwitcherSwitcherModifier cornerRadiiForIndex:];
-[SBHomeGestureToSwitcherSwitcherModifier animationAttributesForLayoutElement:];
-[SBHomeGestureToSwitcherSwitcherModifier adjustedAppLayoutsForAppLayouts:];
-[SBHomeGestureToSwitcherSwitcherModifier homeScreenBackdropBlurType];
-[SBHomeGestureToSwitcherSwitcherModifier _layoutSettings];
-[SBHomeGestureToSwitcherSwitcherModifier topMostLayoutElements];
-[SBHomeGestureToSwitcherSwitcherModifier isSwitcherWindowVisible];
-[SBHomeGestureToSwitcherSwitcherModifier appLayoutsToCacheSnapshots];
-[SBHomeGestureToSwitcherSwitcherModifier handleTransitionEvent:];
-[SBHomeGestureToSwitcherSwitcherModifier isWallpaperRequiredForSwitcher];
-[SBHomeGestureToSwitcherSwitcherModifier visibleAppLayouts];
-[SBHomeGestureToSwitcherSwitcherModifier handleTimerEvent:];
-[SBHomeGestureToSwitcherSwitcherModifier contentOffsetForIndex:alignment:];
-[SBHomeGestureToSwitcherSwitcherModifier wallpaperStyle];
-[SBHomeGestureToSwitcherSwitcherModifier transitionWillBegin];
-[SBHomeGestureToSwitcherSwitcherModifier appLayoutsToCacheFullsizeSnapshots];
-[SBHomeGestureToSwitcherSwitcherModifier _appLayoutAlignmentToScrollToDuringTransition];
-[SBHomeGestureToSwitcherSwitcherModifier _appLayoutToScrollToDuringTransition];
-[SBHomeGestureToSwitcherSwitcherModifier _dismissForEmptySwitcherResponseName];
-[SBHomeGestureToSwitcherSwitcherModifier hidEventSenderID];
-[SBHomeGestureToSwitcherSwitcherModifier initWithTransitionID:multitaskingModifier:selectedAppLayout:startingEnvironmentMode:liftOffVelocity:liftOffTranslation:adjustAppLayoutsBeforeTransition:keepSelectedAppLayoutAsTopMostElement:];
-[SBHomeGestureToSwitcherSwitcherModifier setHidEventSenderID:];
```
