# `SBSAIndicatorFadeTransitionProvider`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBSABasePreferencesProvider`
- 7 instance variables, 2 properties, 18 instance methods, 1 class methods

## Instance variables

```
B _didPushInitialPreferences;
@"SBSAInterfaceElementPropertyIdentity" _pendingStaggerPropertyIdentity;
@"NSUUID" _pendingStaggerTimerIdentity;
@"SBSAInterfaceElementPropertyIdentity" _pendingCompletionPropertyIdentity;
@"NSUUID" _pendingCompletionTimerIdentity;
B _reversed;
Q _phase;
```

## Properties

```
@property (TB,R,N,GisReversed,V_reversed) reversed;
@property (TQ,R,N,V_phase) phase;
```

## Class methods

```
+[SBSAIndicatorFadeTransitionProvider initialize];
```

## Instance methods

```
-[SBSAIndicatorFadeTransitionProvider isReversed];
-[SBSAIndicatorFadeTransitionProvider debugDescription];
-[SBSAIndicatorFadeTransitionProvider phase];
-[SBSAIndicatorFadeTransitionProvider membersForCoder];
-[SBSAIndicatorFadeTransitionProvider _advanceWithContext:];
-[SBSAIndicatorFadeTransitionProvider _applyAnimationDescriptionsForPhaseWithPreferencesMutator:containerIdentifier:settings:];
-[SBSAIndicatorFadeTransitionProvider _applyTransitionSettingsWithPreferences:context:];
-[SBSAIndicatorFadeTransitionProvider _fadeSettings];
-[SBSAIndicatorFadeTransitionProvider _milestoneReachedForProperty:threshold:context:];
-[SBSAIndicatorFadeTransitionProvider _pushAcceptedPhaseWithContext:];
-[SBSAIndicatorFadeTransitionProvider _pushElementAnimationDescriptionsWithContext:];
-[SBSAIndicatorFadeTransitionProvider _pushForwardPhasesForCurrentPhaseWithMutator:context:];
-[SBSAIndicatorFadeTransitionProvider _pushPhasesForCurrentPhaseWithContext:];
-[SBSAIndicatorFadeTransitionProvider _pushReversedPhasesForCurrentPhaseWithMutator:context:];
-[SBSAIndicatorFadeTransitionProvider _registerMilestonesIfNeededWithPreferencesMutator:context:];
-[SBSAIndicatorFadeTransitionProvider _targetBlurRadiusForCurrentPhase];
-[SBSAIndicatorFadeTransitionProvider initWithReversed:];
-[SBSAIndicatorFadeTransitionProvider preferencesFromContext:];
```
