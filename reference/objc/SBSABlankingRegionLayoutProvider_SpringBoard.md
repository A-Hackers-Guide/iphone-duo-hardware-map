# `SBSABlankingRegionLayoutProvider`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBSABasePreferencesProvider`
- 22 instance variables, 1 properties, 24 instance methods, 1 class methods

## Instance variables

```
@"<SBSAInterfaceElementPropertyIdentifying>" _pendingAppearanceProperty;
@"<SBSAInterfaceElementPropertyIdentifying>" _pendingDisappearanceProperty;
@"<SBSAInterfaceElementPropertyIdentifying>" _pendingRTRCoverageProperty;
@"<SBSAInterfaceElementPropertyIdentifying>" _pendingRTRSettledProperty;
@"<SBSAInterfaceElementPropertyIdentifying>" _pendingIndicatorClearanceProperty;
B _resolutionTransitionSettled;
B _indicatorClearedRRRegion;
@"NSUUID" _indicatorAdmissionBackstopTimer;
B _indicatorAdmissionBackstopExpired;
@"NSUUID" _activeContainerIdentifier;
q _currentAppearancePhase;
B _shouldRemoveFromStack;
B _resolutionTransitionDisabled;
@"NSUUID" _pillExtensionTimerIdentifier;
@"NSUUID" _circleCollapseTimerIdentifier;
@"NSUUID" _displacementEffectIdentifier;
{CGPoint="x"d"y"d} _displacementEffectCenter;
@"NSUUID" _displacementEffectTimer;
B _fixedIndicatorMatchMoveNeedsInitialSnap;
B _fixedIndicatorMatchMoveHoldsAtRestingPosition;
@"NSUUID" _panicWorkaroundContainerIdentifier;
@"<SAElementIdentifying>" _elementIdentity;
```

## Properties

```
@property (T@"<SAElementIdentifying>",R,C,N,V_elementIdentity) elementIdentity;
```

## Class methods

```
+[SBSABlankingRegionLayoutProvider initialize];
```

## Instance methods

```
-[SBSABlankingRegionLayoutProvider elementIdentity];
-[SBSABlankingRegionLayoutProvider membersForCoder];
-[SBSABlankingRegionLayoutProvider _transitionToPhase:preferences:];
-[SBSABlankingRegionLayoutProvider _addMilestonesIfNeededWithPreferences:context:];
-[SBSABlankingRegionLayoutProvider _beginDisplacementEffectIfEnabledWithRegionElementContext:];
-[SBSABlankingRegionLayoutProvider _displacementEffectDescriptionWithRequestedState:animated:];
-[SBSABlankingRegionLayoutProvider _fractionalMilestoneReached:forProperty:context:];
-[SBSABlankingRegionLayoutProvider _indicatorClearanceProgressWithRegionElementContext:context:];
-[SBSABlankingRegionLayoutProvider _isTimerExpiredWithIdentifier:context:];
-[SBSABlankingRegionLayoutProvider _milestoneDidReachExpectedMilestone:property:context:];
-[SBSABlankingRegionLayoutProvider _removeContainerDescriptionAndCleanupWithPreferences:context:];
-[SBSABlankingRegionLayoutProvider _resetIndicatorAdmissionState];
-[SBSABlankingRegionLayoutProvider _startTimerForDuration:preferencesMutator:];
-[SBSABlankingRegionLayoutProvider _transitionDidFinishForProperty:context:];
-[SBSABlankingRegionLayoutProvider _updateBlankingRegionAppearStateWithPreferences:context:];
-[SBSABlankingRegionLayoutProvider _updateContainerLayoutWithPreferences:context:];
-[SBSABlankingRegionLayoutProvider _updateDisplacementEffectWithPreferences:context:];
-[SBSABlankingRegionLayoutProvider _updateFixedIndicatorMatchMoveWithPreferences:context:];
-[SBSABlankingRegionLayoutProvider _updateIndicatorAdmissionWithPreferences:context:];
-[SBSABlankingRegionLayoutProvider _updatedPreferencesForCompletedMilestonesWithContext:];
-[SBSABlankingRegionLayoutProvider behaviorSettingsForProperty:];
-[SBSABlankingRegionLayoutProvider descriptionForStackDepiction];
-[SBSABlankingRegionLayoutProvider initWithElementIdentity:];
-[SBSABlankingRegionLayoutProvider preferencesFromContext:];
```
