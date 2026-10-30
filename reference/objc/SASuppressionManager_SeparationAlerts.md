# `SASuppressionManager`

- Image: [`/System/Library/PrivateFrameworks/SeparationAlerts.framework/SeparationAlerts`](../userland/System__Library__PrivateFrameworks__SeparationAlerts.framework__SeparationAlerts.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SASuppressionManagerProtocol`
- 19 instance variables, 23 properties, 58 instance methods, 0 class methods

## Instance variables

```
B _familiarLocationPolicyEnabled;
B _shortReunionTimePolicyEnabled;
B _personalVehicleWhileTravelingPolicyEnabled;
B _vehicularMotionWhileTravelingPolicyEnabled;
B _bookendedTravelBTHintPolicyEnabled;
B _insufficientScanAirTimeWhileTravelingPolicyEnabled;
B _insufficientScanAirTimeForLBAndBookendedPolicyEnabled;
B _zeroSafeLocationsOverridePolicyEnabled;
d _maxDistanceFromHomeForFamiliar;
d _maxPredictedReunionTime;
d _minPredictedReunionProbability;
d _minScanAirTimeWhileTravelingForAlert;
d _minScanAirTimeForLBAndBookendedAlert;
d _minHistoricalFamiliarity;
@"<SATimeServiceProtocol>" _clock;
@"SAFamiliarityManager" _familiarityManager;
@"NSMutableArray" _currentTAPredictedContexts;
@"TALocationOfInterest" _lastKnownHomeLOI;
@"NSDictionary" _cachedConfiguration;
```

## Properties

```
@property (T@"<SATimeServiceProtocol>",&,N,V_clock) clock;
@property (T@"SAFamiliarityManager",&,N,V_familiarityManager) familiarityManager;
@property (T@"NSMutableArray",&,N,V_currentTAPredictedContexts) currentTAPredictedContexts;
@property (T@"TALocationOfInterest",&,N,V_lastKnownHomeLOI) lastKnownHomeLOI;
@property (T@"NSDictionary",&,N,V_cachedConfiguration) cachedConfiguration;
@property (TB,N,V_familiarLocationPolicyEnabled) familiarLocationPolicyEnabled;
@property (TB,N,V_shortReunionTimePolicyEnabled) shortReunionTimePolicyEnabled;
@property (TB,N,V_personalVehicleWhileTravelingPolicyEnabled) personalVehicleWhileTravelingPolicyEnabled;
@property (TB,N,V_vehicularMotionWhileTravelingPolicyEnabled) vehicularMotionWhileTravelingPolicyEnabled;
@property (TB,N,V_bookendedTravelBTHintPolicyEnabled) bookendedTravelBTHintPolicyEnabled;
@property (TB,N,V_zeroSafeLocationsOverridePolicyEnabled) zeroSafeLocationsOverridePolicyEnabled;
@property (TB,N,V_insufficientScanAirTimeWhileTravelingPolicyEnabled) insufficientScanAirTimeWhileTravelingPolicyEnabled;
@property (TB,N,V_insufficientScanAirTimeForLBAndBookendedPolicyEnabled) insufficientScanAirTimeForLBAndBookendedPolicyEnabled;
@property (Td,N,V_maxDistanceFromHomeForFamiliar) maxDistanceFromHomeForFamiliar;
@property (Td,N,V_maxPredictedReunionTime) maxPredictedReunionTime;
@property (Td,N,V_minPredictedReunionProbability) minPredictedReunionProbability;
@property (Td,N,V_minScanAirTimeWhileTravelingForAlert) minScanAirTimeWhileTravelingForAlert;
@property (Td,N,V_minScanAirTimeForLBAndBookendedAlert) minScanAirTimeForLBAndBookendedAlert;
@property (Td,N,V_minHistoricalFamiliarity) minHistoricalFamiliarity;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SASuppressionManager clock];
-[SASuppressionManager cachedConfiguration];
-[SASuppressionManager setClock:];
-[SASuppressionManager ingestTAEvent:];
-[SASuppressionManager setCachedConfiguration:];
-[SASuppressionManager handleTrialConfigurationUpdate:];
-[SASuppressionManager _boolForFactor:defaultValue:];
-[SASuppressionManager _doubleForFactor:defaultValue:];
-[SASuppressionManager _evaluateConfiguration];
-[SASuppressionManager bookendedTravelBTHintPolicyEnabled];
-[SASuppressionManager calculateDistanceToHome:];
-[SASuppressionManager currentTAPredictedContexts];
-[SASuppressionManager evaluateSuppressionForDevice:atLocation:alertType:isBookendingTravel:foundAtLocation:isBTHintOn:userActivityType:travelType:btHintCountDuringTravel:totalScanRxTime:numSafeLocations:];
-[SASuppressionManager familiarLocationPolicyEnabled];
-[SASuppressionManager familiarityManager];
-[SASuppressionManager findMatchingPredictedContextForLocation:withRadiusMeters:];
-[SASuppressionManager getSecondsUntilReturnToPredictedContext:];
-[SASuppressionManager handleLocationOfInterest:];
-[SASuppressionManager handleNewTAPredictedContext:];
-[SASuppressionManager initWithClock:familiarityManager:];
-[SASuppressionManager insufficientScanAirTimeForLBAndBookendedPolicyEnabled];
-[SASuppressionManager insufficientScanAirTimeWhileTravelingPolicyEnabled];
-[SASuppressionManager lastKnownHomeLOI];
-[SASuppressionManager maxDistanceFromHomeForFamiliar];
-[SASuppressionManager maxPredictedReunionTime];
-[SASuppressionManager minHistoricalFamiliarity];
-[SASuppressionManager minPredictedReunionProbability];
-[SASuppressionManager minScanAirTimeForLBAndBookendedAlert];
-[SASuppressionManager minScanAirTimeWhileTravelingForAlert];
-[SASuppressionManager personalVehicleWhileTravelingPolicyEnabled];
-[SASuppressionManager setBookendedTravelBTHintPolicyEnabled:];
-[SASuppressionManager setCurrentTAPredictedContexts:];
-[SASuppressionManager setFamiliarLocationPolicyEnabled:];
-[SASuppressionManager setFamiliarityManager:];
-[SASuppressionManager setInsufficientScanAirTimeForLBAndBookendedPolicyEnabled:];
-[SASuppressionManager setInsufficientScanAirTimeWhileTravelingPolicyEnabled:];
-[SASuppressionManager setLastKnownHomeLOI:];
-[SASuppressionManager setMaxDistanceFromHomeForFamiliar:];
-[SASuppressionManager setMaxPredictedReunionTime:];
-[SASuppressionManager setMinHistoricalFamiliarity:];
-[SASuppressionManager setMinPredictedReunionProbability:];
-[SASuppressionManager setMinScanAirTimeForLBAndBookendedAlert:];
-[SASuppressionManager setMinScanAirTimeWhileTravelingForAlert:];
-[SASuppressionManager setPersonalVehicleWhileTravelingPolicyEnabled:];
-[SASuppressionManager setShortReunionTimePolicyEnabled:];
-[SASuppressionManager setVehicularMotionWhileTravelingPolicyEnabled:];
-[SASuppressionManager setZeroSafeLocationsOverridePolicyEnabled:];
-[SASuppressionManager shortReunionTimePolicyEnabled];
-[SASuppressionManager shouldOverrideDueToNumSafeLocations:];
-[SASuppressionManager shouldSuppressDueToBookendedTravelBTHintWithAlertType:isBookendingTravel:btHintCountDuringTravel:];
-[SASuppressionManager shouldSuppressDueToFamiliarLocationWithAlertType:recentFamiliarity:historicalFamiliarity:distanceFromHome:foundAtLocation:];
-[SASuppressionManager shouldSuppressDueToInsufficientScanAirTimeForLBAndBookendedWithAlertType:isBookendingTravel:totalScanRxTime:];
-[SASuppressionManager shouldSuppressDueToInsufficientScanAirTimeWhileTravelingWithAlertType:isBookendingTravel:totalScanRxTime:];
-[SASuppressionManager shouldSuppressDueToPersonalVehicleWhileTravelingWithAlertType:isBookendingTravel:isBTHintOn:userActivityType:];
-[SASuppressionManager shouldSuppressDueToShortReunionTimeWithAlertType:predictedReturnTime:contextProbability:];
-[SASuppressionManager shouldSuppressDueToVehicularMotionWhileTravelingWithAlertType:isBookendingTravel:travelType:];
-[SASuppressionManager vehicularMotionWhileTravelingPolicyEnabled];
-[SASuppressionManager zeroSafeLocationsOverridePolicyEnabled];
```
