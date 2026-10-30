# `SBSAAcceptanceBounceBehaviorProvider`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBSASequencedBehaviorProvider`
- 7 instance variables, 0 properties, 28 instance methods, 1 class methods

## Instance variables

```
q _style;
{CGPoint="x"d"y"d} _velocity;
@"NSUUID" _excursionViewIdentifier;
@? _triggeredBlock;
@"SBSAElementLayoutTransition" _lastSeenLastChangingElementTransition;
B _shouldBeRemovedUponLayoutChange;
B _excursionReboundCompleted;
```

## Class methods

```
+[SBSAAcceptanceBounceBehaviorProvider initialize];
```

## Instance methods

```
-[SBSAAcceptanceBounceBehaviorProvider membersForCoder];
-[SBSAAcceptanceBounceBehaviorProvider _collapsedExcursionDescriptionForContext:];
-[SBSAAcceptanceBounceBehaviorProvider _excursionBoundsPropertyIdentity];
-[SBSAAcceptanceBounceBehaviorProvider _excursionDescriptionWithBounds:center:];
-[SBSAAcceptanceBounceBehaviorProvider _excursionRotation];
-[SBSAAcceptanceBounceBehaviorProvider _expandedBouncingContainerViewFrameForBounceStyle:unexpandedFrame:];
-[SBSAAcceptanceBounceBehaviorProvider _isVerticalExpansion];
-[SBSAAcceptanceBounceBehaviorProvider _setExcursionViewTransitionsWithBehaviorSettings:inMutator:];
-[SBSAAcceptanceBounceBehaviorProvider _updateStatusBarAvoidanceWithBehaviorSettings:preferencesMutator:];
-[SBSAAcceptanceBounceBehaviorProvider _updatedPreparingExcursionPreferencesFromPreferences:context:relevantPropertyIdentity:];
-[SBSAAcceptanceBounceBehaviorProvider _updatedReboundingPreferencesFromPreferences:context:relevantPropertyIdentity:];
-[SBSAAcceptanceBounceBehaviorProvider _updatedRevealAcceptedElementPreferencesFromPreferences:context:relevantPropertyIdentity:];
-[SBSAAcceptanceBounceBehaviorProvider _updatedStretchingPreferencesFromPreferences:context:relevantPropertyIdentity:];
-[SBSAAcceptanceBounceBehaviorProvider _updatedVectorReboundingPreferencesFromPreferences:context:relevantPropertyIdentity:];
-[SBSAAcceptanceBounceBehaviorProvider _updatedVectorSettlingExcursionPreferencesFromPreferences:context:relevantPropertyIdentity:];
-[SBSAAcceptanceBounceBehaviorProvider _updatedVectorStretchingPreferencesFromPreferences:context:relevantPropertyIdentity:];
-[SBSAAcceptanceBounceBehaviorProvider canPersistAcrossLayoutStateChangesToNewElementContexts:];
-[SBSAAcceptanceBounceBehaviorProvider canProceedWithContext:shouldRetry:];
-[SBSAAcceptanceBounceBehaviorProvider delayForPhase:];
-[SBSAAcceptanceBounceBehaviorProvider finalPhase];
-[SBSAAcceptanceBounceBehaviorProvider initWithParticipantIdentifier:style:velocity:triggeredBlock:];
-[SBSAAcceptanceBounceBehaviorProvider milestoneForPhase:];
-[SBSAAcceptanceBounceBehaviorProvider milestoneForPhaseRequiresAnimationFinished:];
-[SBSAAcceptanceBounceBehaviorProvider nameForPhase:];
-[SBSAAcceptanceBounceBehaviorProvider phaseIsTimeDelayBased:];
-[SBSAAcceptanceBounceBehaviorProvider removeFromParentProvider];
-[SBSAAcceptanceBounceBehaviorProvider updatedContextFromContext:];
-[SBSAAcceptanceBounceBehaviorProvider updatedPreferencesFromPreferences:context:relevantPropertyIdentity:];
```
