# `SBContinuousExposeWindowDragRootSwitcherModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBGestureRootSwitcherModifier`
- 3 instance variables, 1 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"NSUUID" _currentGestureID;
{CGPoint="x"d"y"d} _velocity;
@"SBAppLayout" _initialAppLayout;
```

## Properties

```
@property (T@"SBAppLayout",R,N,V_initialAppLayout) initialAppLayout;
```

## Instance methods

```
-[SBContinuousExposeWindowDragRootSwitcherModifier handleGestureEvent:];
-[SBContinuousExposeWindowDragRootSwitcherModifier appLayoutsToEnsureExistForMainTransitionEvent:];
-[SBContinuousExposeWindowDragRootSwitcherModifier transitionChildModifierForMainTransitionEvent:activeGestureModifier:];
-[SBContinuousExposeWindowDragRootSwitcherModifier handleTransitionEvent:];
-[SBContinuousExposeWindowDragRootSwitcherModifier keyboardSuppressionMode];
-[SBContinuousExposeWindowDragRootSwitcherModifier gestureChildModifierForGestureEvent:activeTransitionModifier:];
-[SBContinuousExposeWindowDragRootSwitcherModifier gestureType];
-[SBContinuousExposeWindowDragRootSwitcherModifier appLayoutsToResignActive];
-[SBContinuousExposeWindowDragRootSwitcherModifier handleSceneReadyEvent:];
-[SBContinuousExposeWindowDragRootSwitcherModifier initWithStartingEnvironmentMode:initialAppLayout:];
-[SBContinuousExposeWindowDragRootSwitcherModifier initialAppLayout];
```
