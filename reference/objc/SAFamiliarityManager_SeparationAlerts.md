# `SAFamiliarityManager`

- Image: [`/System/Library/PrivateFrameworks/SeparationAlerts.framework/SeparationAlerts`](../userland/System__Library__PrivateFrameworks__SeparationAlerts.framework__SeparationAlerts.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SAFamiliarityManagerProtocol`
- 8 instance variables, 12 properties, 25 instance methods, 1 class methods

## Instance variables

```
B _hasPendingShortLookback;
B _hasPendingLongLookback;
@"<SAFamiliarityIndexRequestProtocol>" _familiarityIndexRequester;
d _lastVisitRecentScore;
d _lastVisitHistoricalScore;
@"CLLocation" _pendingRequestLocation;
d _pendingRecentScore;
d _pendingHistoricalScore;
```

## Properties

```
@property (T@"<SAFamiliarityIndexRequestProtocol>",&,N,V_familiarityIndexRequester) familiarityIndexRequester;
@property (Td,N,V_lastVisitRecentScore) lastVisitRecentScore;
@property (Td,N,V_lastVisitHistoricalScore) lastVisitHistoricalScore;
@property (T@"CLLocation",&,N,V_pendingRequestLocation) pendingRequestLocation;
@property (TB,N,V_hasPendingShortLookback) hasPendingShortLookback;
@property (TB,N,V_hasPendingLongLookback) hasPendingLongLookback;
@property (Td,N,V_pendingRecentScore) pendingRecentScore;
@property (Td,N,V_pendingHistoricalScore) pendingHistoricalScore;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SAFamiliarityManager dateIntervalForLookback:];
```

## Instance methods

```
-[SAFamiliarityManager ingestTAEvent:];
-[SAFamiliarityManager handleLocationOfInterestEvent:];
-[SAFamiliarityManager pendingRecentScore];
-[SAFamiliarityManager pendingRequestLocation];
-[SAFamiliarityManager lastVisitRecentFamiliarity];
-[SAFamiliarityManager setFamiliarityIndexRequester:];
-[SAFamiliarityManager hasPendingShortLookback];
-[SAFamiliarityManager lastVisitHistoricalScore];
-[SAFamiliarityManager setHasPendingShortLookback:];
-[SAFamiliarityManager familiarityIndexRequester];
-[SAFamiliarityManager setPendingHistoricalScore:];
-[SAFamiliarityManager requestFamiliarityIndexForLocation:];
-[SAFamiliarityManager lastVisitRecentScore];
-[SAFamiliarityManager handleVisitEvent:];
-[SAFamiliarityManager setPendingRecentScore:];
-[SAFamiliarityManager setPendingRequestLocation:];
-[SAFamiliarityManager setLastVisitRecentScore:];
-[SAFamiliarityManager hasPendingLongLookback];
-[SAFamiliarityManager lastVisitHistoricalFamiliarity];
-[SAFamiliarityManager finalizeAssessmentWithRecentScore:historicalScore:];
-[SAFamiliarityManager setHasPendingLongLookback:];
-[SAFamiliarityManager handleFamiliarityIndexEvent:];
-[SAFamiliarityManager setLastVisitHistoricalScore:];
-[SAFamiliarityManager initWithFamiliarityIndexRequester:];
-[SAFamiliarityManager pendingHistoricalScore];
```
