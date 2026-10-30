# `SBSAContainerDynamicsPulseAnimationProvider`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBSABasePreferencesProvider`
- 7 instance variables, 1 properties, 13 instance methods, 1 class methods

## Instance variables

```
q _phase;
q _pulseStyle;
@"NSUUID" _waitingToExpandTimerIdentifier;
@"NSUUID" _expandingTimerIdentifier;
@"SBSAInterfaceElementPropertyIdentity" _contractionCompletionMilestonePropertyIdentity;
@"NSUUID" _expandedInterfaceElementIdentifier;
@"<SAElementIdentifying>" _elementIdentity;
```

## Properties

```
@property (T@"<SAElementIdentifying>",R,C,N,V_elementIdentity) elementIdentity;
```

## Class methods

```
+[SBSAContainerDynamicsPulseAnimationProvider initialize];
```

## Instance methods

```
-[SBSAContainerDynamicsPulseAnimationProvider elementIdentity];
-[SBSAContainerDynamicsPulseAnimationProvider membersForCoder];
-[SBSAContainerDynamicsPulseAnimationProvider _checkContextForCompletedContractionAnimationMilestone:];
-[SBSAContainerDynamicsPulseAnimationProvider _isTimerExpiredWithIdentifier:context:];
-[SBSAContainerDynamicsPulseAnimationProvider _pulseContractWithPreferencesMutator:context:];
-[SBSAContainerDynamicsPulseAnimationProvider _pulseExpandWithPreferencesMutator:context:];
-[SBSAContainerDynamicsPulseAnimationProvider _pulseSettings];
-[SBSAContainerDynamicsPulseAnimationProvider _pulseWaitingToExpandWithPreferencesMutator:context:];
-[SBSAContainerDynamicsPulseAnimationProvider _startTimerForDuration:preferencesMutator:];
-[SBSAContainerDynamicsPulseAnimationProvider _updatePreferencesContainerWithInterfaceElementIdentifier:toScale:settings:preferencesMutator:context:];
-[SBSAContainerDynamicsPulseAnimationProvider didRequestAdditionalPulse:];
-[SBSAContainerDynamicsPulseAnimationProvider initWithElementIdentity:pulseStyle:];
-[SBSAContainerDynamicsPulseAnimationProvider preferencesFromContext:];
```
