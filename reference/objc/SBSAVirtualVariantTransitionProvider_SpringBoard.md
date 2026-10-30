# `SBSAVirtualVariantTransitionProvider`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBSASequencedBehaviorProvider`
- 2 instance variables, 2 properties, 18 instance methods, 3 class methods

## Instance variables

```
Q _direction;
B _needsContraction;
```

## Properties

```
@property (TB,R,N,GisContentAppearanceMilestoneReached) contentAppearanceMilestoneReached;
@property (TB,R,N,GisCollapsed) collapsed;
```

## Class methods

```
+[SBSAVirtualVariantTransitionProvider initialize];
+[SBSAVirtualVariantTransitionProvider appearanceTransitionProviderWithParticipantIdentifier:];
+[SBSAVirtualVariantTransitionProvider disappearanceTransitionProviderWithParticipantIdentifier:];
```

## Instance methods

```
-[SBSAVirtualVariantTransitionProvider isCollapsed];
-[SBSAVirtualVariantTransitionProvider membersForCoder];
-[SBSAVirtualVariantTransitionProvider _updatedPreferencesForCirclePhase:context:appearing:relevantPropertyIdentity:];
-[SBSAVirtualVariantTransitionProvider _updatedPreferencesForCollapsePhase:context:relevantPropertyIdentity:];
-[SBSAVirtualVariantTransitionProvider _updatedPreferencesForContractPhase:context:relevantPropertyIdentity:];
-[SBSAVirtualVariantTransitionProvider _updatedPreferencesForExpandPhase:context:relevantPropertyIdentity:];
-[SBSAVirtualVariantTransitionProvider _updatedPreferencesForSeedPhase:context:relevantPropertyIdentity:];
-[SBSAVirtualVariantTransitionProvider _updatedPreferencesFromPreferences:context:pinToCircle:targetScale:scaleAnimated:boundsAnimated:appearing:relevantPropertyIdentity:relevantPropertyIdentityPtr:];
-[SBSAVirtualVariantTransitionProvider canPersistAcrossLayoutStateChangesToNewElementContexts:];
-[SBSAVirtualVariantTransitionProvider canProceedWithContext:shouldRetry:];
-[SBSAVirtualVariantTransitionProvider delayForPhase:];
-[SBSAVirtualVariantTransitionProvider finalPhase];
-[SBSAVirtualVariantTransitionProvider isContentAppearanceMilestoneReached];
-[SBSAVirtualVariantTransitionProvider milestoneForPhase:];
-[SBSAVirtualVariantTransitionProvider milestoneForPhaseRequiresAnimationFinished:];
-[SBSAVirtualVariantTransitionProvider nameForPhase:];
-[SBSAVirtualVariantTransitionProvider phaseIsTimeDelayBased:];
-[SBSAVirtualVariantTransitionProvider updatedPreferencesFromPreferences:context:relevantPropertyIdentity:];
```
