# `SBHomeToSwitcherSwitcherModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBTransitionSwitcherModifier`
- 2 instance variables, 2 properties, 11 instance methods, 0 class methods

## Instance variables

```
q _direction;
@"SBChainableModifier<SBSwitcherMultitaskingQueryProviding>" _multitaskingModifier;
```

## Properties

```
@property (Tq,R,N,V_direction) direction;
@property (T@"SBChainableModifier<SBSwitcherMultitaskingQueryProviding>",R,N,V_multitaskingModifier) multitaskingModifier;
```

## Instance methods

```
-[SBHomeToSwitcherSwitcherModifier containerStatusBarAnimationDuration];
-[SBHomeToSwitcherSwitcherModifier transitionWillUpdate];
-[SBHomeToSwitcherSwitcherModifier fadeInDelayForSplitViewHandles];
-[SBHomeToSwitcherSwitcherModifier handleTimerEvent:];
-[SBHomeToSwitcherSwitcherModifier transitionWillBegin];
-[SBHomeToSwitcherSwitcherModifier direction];
-[SBHomeToSwitcherSwitcherModifier appLayoutToScrollToDuringTransition];
-[SBHomeToSwitcherSwitcherModifier _dismissForEmptySwitcherResponseName];
-[SBHomeToSwitcherSwitcherModifier initWithTransitionID:direction:multitaskingModifier:];
-[SBHomeToSwitcherSwitcherModifier isEffectivelyHome];
-[SBHomeToSwitcherSwitcherModifier multitaskingModifier];
```
