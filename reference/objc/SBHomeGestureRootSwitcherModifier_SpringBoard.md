# `SBHomeGestureRootSwitcherModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBGestureRootSwitcherModifier`
- 5 instance variables, 2 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"SBSwitcherModifier" _multitaskingModifier;
@"SBGestureSwitcherModifierEvent" _lastGestureEvent;
B _shouldAccelerateHomeGesture;
B _resignsTransitionIntoAppSwitcher;
B _ensuresSelectedAppLayoutUsesAnchorPointSpacePinning;
```

## Properties

```
@property (TB,N,V_resignsTransitionIntoAppSwitcher) resignsTransitionIntoAppSwitcher;
@property (TB,N,V_ensuresSelectedAppLayoutUsesAnchorPointSpacePinning) ensuresSelectedAppLayoutUsesAnchorPointSpacePinning;
```

## Instance methods

```
-[SBHomeGestureRootSwitcherModifier handleGestureEvent:];
-[SBHomeGestureRootSwitcherModifier shouldUseAnchorPointToPinLayoutRolesToSpace:];
-[SBHomeGestureRootSwitcherModifier ensuresSelectedAppLayoutUsesAnchorPointSpacePinning];
-[SBHomeGestureRootSwitcherModifier transitionChildModifierForMainTransitionEvent:activeGestureModifier:];
-[SBHomeGestureRootSwitcherModifier _newMultitaskingModifier];
-[SBHomeGestureRootSwitcherModifier handleTransitionEvent:];
-[SBHomeGestureRootSwitcherModifier shouldPinLayoutRolesToSpace:];
-[SBHomeGestureRootSwitcherModifier resignsTransitionIntoAppSwitcher];
-[SBHomeGestureRootSwitcherModifier initWithStartingEnvironmentMode:multitaskingModifier:];
-[SBHomeGestureRootSwitcherModifier gestureChildModifierForGestureEvent:activeTransitionModifier:];
-[SBHomeGestureRootSwitcherModifier gestureType];
-[SBHomeGestureRootSwitcherModifier setEnsuresSelectedAppLayoutUsesAnchorPointSpacePinning:];
-[SBHomeGestureRootSwitcherModifier isPendingInvalidatablesForAcceleratedHomeGesture];
-[SBHomeGestureRootSwitcherModifier setResignsTransitionIntoAppSwitcher:];
-[SBHomeGestureRootSwitcherModifier wantsAsynchronousSurfaceRetentionAssertion];
```
