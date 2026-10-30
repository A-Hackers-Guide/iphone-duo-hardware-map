# `SBContinuousExposeSwitcherToAppModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBTransitionSwitcherModifier`
- 3 instance variables, 2 properties, 16 instance methods, 0 class methods

## Instance variables

```
@"SBCoplanarSwitcherModifier" _coplanarModifier;
q _direction;
@"SBSwitcherModifier" _multitaskingModifier;
```

## Properties

```
@property (Tq,R,N,V_direction) direction;
@property (T@"SBSwitcherModifier",R,N,V_multitaskingModifier) multitaskingModifier;
```

## Instance methods

```
-[SBContinuousExposeSwitcherToAppModifier appLayoutsToEnsureExistForMainTransitionEvent:];
-[SBContinuousExposeSwitcherToAppModifier didMoveToParentModifier:];
-[SBContinuousExposeSwitcherToAppModifier animationAttributesForLayoutElement:];
-[SBContinuousExposeSwitcherToAppModifier adjustedAppLayoutsForAppLayouts:];
-[SBContinuousExposeSwitcherToAppModifier _layoutSettings];
-[SBContinuousExposeSwitcherToAppModifier appLayoutsForContinuousExposeIdentifier:];
-[SBContinuousExposeSwitcherToAppModifier transitionWillUpdate];
-[SBContinuousExposeSwitcherToAppModifier visibleAppLayouts];
-[SBContinuousExposeSwitcherToAppModifier fadeInDelayForSplitViewHandles];
-[SBContinuousExposeSwitcherToAppModifier contentOffsetForIndex:alignment:];
-[SBContinuousExposeSwitcherToAppModifier frameForIndex:];
-[SBContinuousExposeSwitcherToAppModifier transitionWillBegin];
-[SBContinuousExposeSwitcherToAppModifier direction];
-[SBContinuousExposeSwitcherToAppModifier appLayoutToAttachSlideOverTongue];
-[SBContinuousExposeSwitcherToAppModifier initWithTransitionID:direction:multitaskingModifier:];
-[SBContinuousExposeSwitcherToAppModifier multitaskingModifier];
```
