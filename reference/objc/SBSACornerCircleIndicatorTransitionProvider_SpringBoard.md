# `SBSACornerCircleIndicatorTransitionProvider`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBSABasePreferencesProvider`
- 7 instance variables, 2 properties, 17 instance methods, 1 class methods

## Instance variables

```
B _didPushInitialPreferences;
@"SBSAInterfaceElementPropertyIdentity" _pendingFadeMilestoneProperty;
@"NSUUID" _pendingFadeTimerIdentity;
@"SBSAInterfaceElementPropertyIdentity" _pendingCollapseMilestoneProperty;
@"NSUUID" _pendingCollapseTimerIdentity;
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
+[SBSACornerCircleIndicatorTransitionProvider initialize];
```

## Instance methods

```
-[SBSACornerCircleIndicatorTransitionProvider isReversed];
-[SBSACornerCircleIndicatorTransitionProvider debugDescription];
-[SBSACornerCircleIndicatorTransitionProvider phase];
-[SBSACornerCircleIndicatorTransitionProvider membersForCoder];
-[SBSACornerCircleIndicatorTransitionProvider _advanceWithContext:];
-[SBSACornerCircleIndicatorTransitionProvider _applyAnimationDescriptionsWithPreferencesMutator:containerIdentifier:indicatorElementIdentifier:settings:];
-[SBSACornerCircleIndicatorTransitionProvider _applyTransitionSettingsWithPreferences:context:];
-[SBSACornerCircleIndicatorTransitionProvider _milestoneReachedForProperty:threshold:context:];
-[SBSACornerCircleIndicatorTransitionProvider _pushForwardInterSensorPhaseWithMutator:];
-[SBSACornerCircleIndicatorTransitionProvider _pushInterSensorPhaseForCurrentPhaseWithContext:];
-[SBSACornerCircleIndicatorTransitionProvider _pushReversedInterSensorPhaseWithMutator:];
-[SBSACornerCircleIndicatorTransitionProvider _pushTerminalStateWithContext:];
-[SBSACornerCircleIndicatorTransitionProvider _registerMilestonesIfNeededWithPreferencesMutator:containerIdentifier:indicatorElementIdentifier:context:];
-[SBSACornerCircleIndicatorTransitionProvider _transitionSettings];
-[SBSACornerCircleIndicatorTransitionProvider _updateCornerCircleContainerFrameIfNeededWithPreferencesMutator:containerIdentifier:context:renderedLayoutDirection:];
-[SBSACornerCircleIndicatorTransitionProvider initWithReversed:];
-[SBSACornerCircleIndicatorTransitionProvider preferencesFromContext:];
```
