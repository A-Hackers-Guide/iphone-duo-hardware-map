# `SBButterflyHomeGestureRootWindowingModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBWindowingModifier`
- 11 instance variables, 2 properties, 28 instance methods, 0 class methods

## Instance variables

```
@"SBUnlockedEnvironmentState" _currentEnvironmentState;
@"SBWindowingModifier" _multitaskingModifier;
@"SBGestureSwitcherModifierEvent" _lastGestureEvent;
@"SBAppLayout" _selectedAppLayout;
q _startingScreenRegion;
q _startingEnvironmentMode;
@"SBChainableModifier" _gestureModifierBeforeUpdate;
@"SBChainableModifier" _transitionModifierBeforeUpdate;
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
-[SBButterflyHomeGestureRootWindowingModifier shouldUseAnchorPointToPinLayoutRolesToSpace:];
-[SBButterflyHomeGestureRootWindowingModifier ensuresSelectedAppLayoutUsesAnchorPointSpacePinning];
-[SBButterflyHomeGestureRootWindowingModifier _newMultitaskingModifier];
-[SBButterflyHomeGestureRootWindowingModifier willUpdate];
-[SBButterflyHomeGestureRootWindowingModifier shouldPinLayoutRolesToSpace:];
-[SBButterflyHomeGestureRootWindowingModifier transitionDidUpdate:];
-[SBButterflyHomeGestureRootWindowingModifier _gestureType];
-[SBButterflyHomeGestureRootWindowingModifier resignsTransitionIntoAppSwitcher];
-[SBButterflyHomeGestureRootWindowingModifier didUpdate];
-[SBButterflyHomeGestureRootWindowingModifier transitionWillBegin:];
-[SBButterflyHomeGestureRootWindowingModifier completesWhenChildrenComplete];
-[SBButterflyHomeGestureRootWindowingModifier setEnsuresSelectedAppLayoutUsesAnchorPointSpacePinning:];
-[SBButterflyHomeGestureRootWindowingModifier isPendingInvalidatablesForAcceleratedHomeGesture];
-[SBButterflyHomeGestureRootWindowingModifier setResignsTransitionIntoAppSwitcher:];
-[SBButterflyHomeGestureRootWindowingModifier wantsAsynchronousSurfaceRetentionAssertion];
-[SBButterflyHomeGestureRootWindowingModifier descriptionBuilderWithMultilinePrefix:];
-[SBButterflyHomeGestureRootWindowingModifier _gestureChildModifierForGestureEvent:activeTransitionModifier:];
-[SBButterflyHomeGestureRootWindowingModifier _gestureModifier];
-[SBButterflyHomeGestureRootWindowingModifier _transitionChildModifierForTransitionEvent:activeGestureModifier:];
-[SBButterflyHomeGestureRootWindowingModifier _transitionModifier];
-[SBButterflyHomeGestureRootWindowingModifier _updateShouldAccelerateHomeGestureForTransition:];
-[SBButterflyHomeGestureRootWindowingModifier gestureDidComplete:];
-[SBButterflyHomeGestureRootWindowingModifier gestureDidUpdate:];
-[SBButterflyHomeGestureRootWindowingModifier gestureWillBegin:];
-[SBButterflyHomeGestureRootWindowingModifier initWithStartingEnvironmentState:multitaskingModifier:];
-[SBButterflyHomeGestureRootWindowingModifier itemRemoved:];
-[SBButterflyHomeGestureRootWindowingModifier transitionDidComplete:];
-[SBButterflyHomeGestureRootWindowingModifier transitionWillPrepare:];
```
