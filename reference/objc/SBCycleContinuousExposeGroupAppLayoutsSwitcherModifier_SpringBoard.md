# `SBCycleContinuousExposeGroupAppLayoutsSwitcherModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBSwitcherModifier`
- 6 instance variables, 3 properties, 14 instance methods, 0 class methods

## Instance variables

```
B _isDelayingCompletionForHover;
Q _initialGenerationCount;
@"SBAppLayout" _appLayoutToOrderFront;
@"SBAppLayout" _appLayout;
@"SBAppLayout" _behindAppLayout;
Q _generationCount;
```

## Properties

```
@property (T@"SBAppLayout",R,N,V_appLayout) appLayout;
@property (T@"SBAppLayout",R,N,V_behindAppLayout) behindAppLayout;
@property (TQ,R,N,V_generationCount) generationCount;
```

## Instance methods

```
-[SBCycleContinuousExposeGroupAppLayoutsSwitcherModifier generationCount];
-[SBCycleContinuousExposeGroupAppLayoutsSwitcherModifier appLayoutsForContinuousExposeIdentifier:];
-[SBCycleContinuousExposeGroupAppLayoutsSwitcherModifier handleTransitionEvent:];
-[SBCycleContinuousExposeGroupAppLayoutsSwitcherModifier visibleAppLayouts];
-[SBCycleContinuousExposeGroupAppLayoutsSwitcherModifier appLayout];
-[SBCycleContinuousExposeGroupAppLayoutsSwitcherModifier opacityForLayoutRole:inAppLayout:atIndex:];
-[SBCycleContinuousExposeGroupAppLayoutsSwitcherModifier handleTimerEvent:];
-[SBCycleContinuousExposeGroupAppLayoutsSwitcherModifier handleContinuousExposeIdentifiersChangedEvent:];
-[SBCycleContinuousExposeGroupAppLayoutsSwitcherModifier _completeIfNeededIgnoringHover:];
-[SBCycleContinuousExposeGroupAppLayoutsSwitcherModifier behindAppLayout];
-[SBCycleContinuousExposeGroupAppLayoutsSwitcherModifier _completeIfNeeded];
-[SBCycleContinuousExposeGroupAppLayoutsSwitcherModifier _timeoutReason];
-[SBCycleContinuousExposeGroupAppLayoutsSwitcherModifier handleHighlightEvent:];
-[SBCycleContinuousExposeGroupAppLayoutsSwitcherModifier initWithAppLayout:behindAppLayout:generationCount:];
```
