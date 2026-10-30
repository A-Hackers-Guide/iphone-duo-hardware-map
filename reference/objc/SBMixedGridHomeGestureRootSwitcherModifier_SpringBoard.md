# `SBMixedGridHomeGestureRootSwitcherModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBGestureRootSwitcherModifier`
- Protocols: `SBChainableModifierDelegate`
- 6 instance variables, 4 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"SBAppLayout" _selectedAppLayout;
@"SBSwitcherModifier<SBMixedGridSwitcherProviding>" _mixedGridModifier;
@"SBGestureSwitcherModifier" _gestureModifier;
B _continuingGesture;
B _lastGestureWasAnArcSwipe;
@"SBGestureSwitcherModifierEvent" _lastGestureEvent;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBMixedGridHomeGestureRootSwitcherModifier handleGestureEvent:];
-[SBMixedGridHomeGestureRootSwitcherModifier handleEvent:];
-[SBMixedGridHomeGestureRootSwitcherModifier transitionChildModifierForMainTransitionEvent:activeGestureModifier:];
-[SBMixedGridHomeGestureRootSwitcherModifier _newMultitaskingModifier];
-[SBMixedGridHomeGestureRootSwitcherModifier completesWhenChildrenComplete];
-[SBMixedGridHomeGestureRootSwitcherModifier gestureChildModifierForGestureEvent:activeTransitionModifier:];
-[SBMixedGridHomeGestureRootSwitcherModifier gestureType];
-[SBMixedGridHomeGestureRootSwitcherModifier wantsAsynchronousSurfaceRetentionAssertion];
-[SBMixedGridHomeGestureRootSwitcherModifier canTransitionWithoutGestureModifier];
-[SBMixedGridHomeGestureRootSwitcherModifier initWithStartingEnvironmentMode:selectedAppLayout:mixedGridModifier:];
```
