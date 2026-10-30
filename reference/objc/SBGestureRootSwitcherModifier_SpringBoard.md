# `SBGestureRootSwitcherModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBSwitcherModifier`
- 4 instance variables, 6 properties, 17 instance methods, 0 class methods

## Instance variables

```
@"SBSwitcherModifier" _transitionModifierBeforeHandlingEvent;
@"SBSwitcherModifier" _gestureModifierBeforeHandlingEvent;
@"SBAppLayout" _selectedAppLayout;
@"SBUnlockedEnvironmentState" _currentEnvironmentState;
```

## Properties

```
@property (T@"SBAppLayout",R,N,V_selectedAppLayout) selectedAppLayout;
@property (T@"SBUnlockedEnvironmentState",R,N,V_currentEnvironmentState) currentEnvironmentState;
@property (Tq,R,N) currentEnvironmentMode;
@property (T@"SBSwitcherModifier",R,N) gestureModifier;
@property (T@"SBSwitcherModifier",R,N) transitionModifier;
@property (TB,R,N) canTransitionWithoutGestureModifier;
```

## Instance methods

```
-[SBGestureRootSwitcherModifier handleGestureEvent:];
-[SBGestureRootSwitcherModifier handleEvent:];
-[SBGestureRootSwitcherModifier transitionChildModifierForMainTransitionEvent:activeGestureModifier:];
-[SBGestureRootSwitcherModifier handleTransitionEvent:];
-[SBGestureRootSwitcherModifier selectedAppLayout];
-[SBGestureRootSwitcherModifier completesWhenChildrenComplete];
-[SBGestureRootSwitcherModifier gestureChildModifierForGestureEvent:activeTransitionModifier:];
-[SBGestureRootSwitcherModifier handleRemovalEvent:];
-[SBGestureRootSwitcherModifier gestureType];
-[SBGestureRootSwitcherModifier descriptionBuilderWithMultilinePrefix:];
-[SBGestureRootSwitcherModifier gestureModifier];
-[SBGestureRootSwitcherModifier canTransitionWithoutGestureModifier];
-[SBGestureRootSwitcherModifier currentEnvironmentMode];
-[SBGestureRootSwitcherModifier currentEnvironmentState];
-[SBGestureRootSwitcherModifier initWithStartingEnvironmentMode:];
-[SBGestureRootSwitcherModifier initWithStartingEnvironmentState:];
-[SBGestureRootSwitcherModifier transitionModifier];
```
