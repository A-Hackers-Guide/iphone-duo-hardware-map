# `SBTransitionSwitcherModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBSwitcherModifier`
- 7 instance variables, 3 properties, 33 instance methods, 0 class methods

## Instance variables

```
B _wantsResignActiveAndAsyncRenderingAssertions;
B _isTransitioningToSwitcher;
B _isInterrupted;
@"NSArray" _appLayoutsToEnsureExist;
B _asyncRenderingDisabled;
@"NSUUID" _transitionID;
Q _transitionPhase;
```

## Properties

```
@property (TQ,R,N,V_transitionPhase) transitionPhase;
@property (TB,R,N,V_asyncRenderingDisabled) asyncRenderingDisabled;
@property (T@"NSUUID",R,N,V_transitionID) transitionID;
```

## Instance methods

```
-[SBTransitionSwitcherModifier handleGestureEvent:];
-[SBTransitionSwitcherModifier isInterrupted];
-[SBTransitionSwitcherModifier maskedCornersForIndex:];
-[SBTransitionSwitcherModifier clipsToUnobscuredMarginAtIndex:];
-[SBTransitionSwitcherModifier shouldAsyncRenderUntilDelay:];
-[SBTransitionSwitcherModifier animationAttributesForLayoutElement:];
-[SBTransitionSwitcherModifier adjustedAppLayoutsForAppLayouts:];
-[SBTransitionSwitcherModifier handleTransitionEvent:];
-[SBTransitionSwitcherModifier transitionWillUpdate];
-[SBTransitionSwitcherModifier transitionDidEnd];
-[SBTransitionSwitcherModifier handleTimerEvent:];
-[SBTransitionSwitcherModifier transitionWillBegin];
-[SBTransitionSwitcherModifier keyboardSuppressionMode];
-[SBTransitionSwitcherModifier visibleMarginForItemContainerAtIndex:];
-[SBTransitionSwitcherModifier shouldPerformCrossfadeForReduceMotion];
-[SBTransitionSwitcherModifier handleRemovalEvent:];
-[SBTransitionSwitcherModifier asyncRenderingDisabled];
-[SBTransitionSwitcherModifier appLayoutsToResignActive];
-[SBTransitionSwitcherModifier handleScrollEvent:];
-[SBTransitionSwitcherModifier asyncRenderingAttributesForAppLayout:];
-[SBTransitionSwitcherModifier transitionID];
-[SBTransitionSwitcherModifier maskedCornersForLayoutRole:inAppLayout:withMaskedCorners:];
-[SBTransitionSwitcherModifier wantsAsynchronousSurfaceRetentionAssertion];
-[SBTransitionSwitcherModifier descriptionBuilderWithMultilinePrefix:];
-[SBTransitionSwitcherModifier transitionPhase];
-[SBTransitionSwitcherModifier shouldInterruptForRemovalEvent:];
-[SBTransitionSwitcherModifier _setTransitionPhase:];
-[SBTransitionSwitcherModifier initWithTransitionID:];
-[SBTransitionSwitcherModifier interruptAndEndTransition];
-[SBTransitionSwitcherModifier isPreparingLayout];
-[SBTransitionSwitcherModifier isUpdatingLayout];
-[SBTransitionSwitcherModifier requireStripContentsInViewHierarchy];
-[SBTransitionSwitcherModifier transitionWillPrepare];
```
