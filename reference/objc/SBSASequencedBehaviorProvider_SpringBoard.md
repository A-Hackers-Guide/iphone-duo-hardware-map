# `SBSASequencedBehaviorProvider`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBSABasePreferencesProvider`
- 7 instance variables, 3 properties, 20 instance methods, 1 class methods

## Instance variables

```
q _activePhase;
@"NSArray" _elementContexts;
{?="interfaceOrientation"q"layoutDirection"q"statusBarAxis"q"sensorVariant"Q} _orientationEnvironment;
@"<SBSAInterfaceElementPropertyIdentifying>" _pendingPhaseTransitionPropertyIdentity;
@"NSUUID" _pendingTimerIdentifier;
@"NSUUID" _participatingInterfaceElementIdentifier;
@"<SAElementIdentifying>" _participatingElementIdentification;
```

## Properties

```
@property (Tq,R,N) activePhase;
@property (T@"NSUUID",R,C,N,V_participatingInterfaceElementIdentifier) participatingInterfaceElementIdentifier;
@property (T@"<SAElementIdentifying>",R,C,N,V_participatingElementIdentification) participatingElementIdentification;
```

## Class methods

```
+[SBSASequencedBehaviorProvider initialize];
```

## Instance methods

```
-[SBSASequencedBehaviorProvider encodeWithCoder:];
-[SBSASequencedBehaviorProvider membersForCoder];
-[SBSASequencedBehaviorProvider activePhase];
-[SBSASequencedBehaviorProvider _setActivePhase:context:reason:];
-[SBSASequencedBehaviorProvider _isTimerExpired:duration:];
-[SBSASequencedBehaviorProvider _startTimerIfNecessary:withInterval:];
-[SBSASequencedBehaviorProvider canPersistAcrossLayoutStateChangesToNewElementContexts:];
-[SBSASequencedBehaviorProvider canProceedWithContext:shouldRetry:];
-[SBSASequencedBehaviorProvider delayForPhase:];
-[SBSASequencedBehaviorProvider finalPhase];
-[SBSASequencedBehaviorProvider initWithParticipantIdentifier:];
-[SBSASequencedBehaviorProvider milestoneForPhase:];
-[SBSASequencedBehaviorProvider milestoneForPhaseRequiresAnimationFinished:];
-[SBSASequencedBehaviorProvider nameForPhase:];
-[SBSASequencedBehaviorProvider participatingElementIdentification];
-[SBSASequencedBehaviorProvider participatingInterfaceElementIdentifier];
-[SBSASequencedBehaviorProvider phaseIsTimeDelayBased:];
-[SBSASequencedBehaviorProvider preferencesFromContext:];
-[SBSASequencedBehaviorProvider updatedContextFromContext:];
-[SBSASequencedBehaviorProvider updatedPreferencesFromPreferences:context:relevantPropertyIdentity:];
```
