# `TimeseriesPoliciesHandler`

- Image: [`/System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics`](../userland/System__Library__PrivateFrameworks__WiFiAnalytics.framework__WiFiAnalytics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 1 properties, 25 instance methods, 0 class methods

## Instance variables

```
@"WAPersistentContainer" _container;
```

## Properties

```
@property (T@"WAPersistentContainer",&,N,V_container) container;
```

## Instance methods

```
-[TimeseriesPoliciesHandler setContainer:];
-[TimeseriesPoliciesHandler container];
-[TimeseriesPoliciesHandler initWithPersistentContainer:];
-[TimeseriesPoliciesHandler calculateThresholdForBand:insideRssiValues:outsideRssiValues:];
-[TimeseriesPoliciesHandler checkInsideOutsideForRoamEvent:In:];
-[TimeseriesPoliciesHandler checkRejoinAfterLeaveEvent:In:];
-[TimeseriesPoliciesHandler classifyRoamBasedOnLeaveEvent:roamDate:inEvents:];
-[TimeseriesPoliciesHandler configureContextAwareTDEventsToFetchWithError:];
-[TimeseriesPoliciesHandler configureInsideOutsideClassifierEventsToFetchWithError:];
-[TimeseriesPoliciesHandler configureKnownChannelsBitmapEventsToFetchWithError:];
-[TimeseriesPoliciesHandler extractMaxRssiForBand:fromRoamCache:];
-[TimeseriesPoliciesHandler findEdgeBSSFromRoamEventBeforeLeaveEvent:In:];
-[TimeseriesPoliciesHandler findEdgeBSSIn:byCheckingLeaveEventsUntil:];
-[TimeseriesPoliciesHandler findEventsIn:aroundIndex:noEarlierThan:noLaterThan:withPredicate:findingAll:];
-[TimeseriesPoliciesHandler findEventsIn:aroundIndex:noEarlierThan:noLaterThan:withPredicate:findingAll:setTrackIndex:];
-[TimeseriesPoliciesHandler findLeaveEventsAfterRoam:inEvents:aroundIndex:];
-[TimeseriesPoliciesHandler findNextLeaveEventFrom:In:];
-[TimeseriesPoliciesHandler findNextRoamEventFrom:In:];
-[TimeseriesPoliciesHandler findRoamEventBeforeLeaveEvent:In:];
-[TimeseriesPoliciesHandler hasJoinEventBeforeRoam:inEvents:aroundIndex:];
-[TimeseriesPoliciesHandler updateBSSMOWithEdgeBSSSet:tdEdgeParamsVersion:withError:];
-[TimeseriesPoliciesHandler updateEdgeBssWithReason:at:timeSpan:];
-[TimeseriesPoliciesHandler updateInsideOutsideClassifierWithReason:at:];
-[TimeseriesPoliciesHandler updateKnownChannelsBitmapsWithReason:];
-[TimeseriesPoliciesHandler updatePoliciesTableWithReason:withPolicyType:withOutcome:];
```
