# `SBContinuousExposeHomeGestureRootSwitcherModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBGestureRootSwitcherModifier`
- 4 instance variables, 0 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"SBSwitcherModifier" _multitaskingModifier;
@"NSSet" _initiallyVisibleAppLayouts;
@"SBGestureSwitcherModifierEvent" _lastGestureEvent;
Q _initialAppLayoutsGenerationCount;
```

## Instance methods

```
-[SBContinuousExposeHomeGestureRootSwitcherModifier handleGestureEvent:];
-[SBContinuousExposeHomeGestureRootSwitcherModifier transitionChildModifierForMainTransitionEvent:activeGestureModifier:];
-[SBContinuousExposeHomeGestureRootSwitcherModifier _newMultitaskingModifier];
-[SBContinuousExposeHomeGestureRootSwitcherModifier initWithStartingEnvironmentMode:multitaskingModifier:];
-[SBContinuousExposeHomeGestureRootSwitcherModifier gestureChildModifierForGestureEvent:activeTransitionModifier:];
-[SBContinuousExposeHomeGestureRootSwitcherModifier gestureType];
-[SBContinuousExposeHomeGestureRootSwitcherModifier preferredAppLayoutToReuseAccessoryForAppLayout:fromAppLayouts:];
-[SBContinuousExposeHomeGestureRootSwitcherModifier wantsAsynchronousSurfaceRetentionAssertion];
```
