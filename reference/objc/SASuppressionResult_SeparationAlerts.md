# `SASuppressionResult`

- Image: [`/System/Library/PrivateFrameworks/SeparationAlerts.framework/SeparationAlerts`](../userland/System__Library__PrivateFrameworks__SeparationAlerts.framework__SeparationAlerts.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 15 instance variables, 21 properties, 22 instance methods, 0 class methods

## Instance variables

```
B _suppressedByFamiliarLocation;
B _suppressedByShortReunionTime;
B _suppressedByPersonalVehicleWhileTraveling;
B _suppressedByVehicularMotionWhileTraveling;
B _suppressedByBookendedTravelBTHint;
B _suppressedByInsufficientScanAirTimeWhileTraveling;
B _suppressedByInsufficientScanAirTimeForLBAndBookended;
B _overridenByNumSafeLocations;
d _recentFamiliarity;
d _historicalFamiliarity;
d _distanceFromHome;
d _predictedLocationReturnTime;
d _contextProbability;
d _minPredictedReunionProbability;
d _minHistoricalFamiliarity;
```

## Properties

```
@property (TB,R,N) wasSuppressionCriteriaMet;
@property (TB,R,N) wasOverrideCriteriaMet;
@property (TB,R,N) shouldSuppress;
@property (TB,R,N) wasOverridden;
@property (T@"NSString",R,N) suppressionReason;
@property (T@"NSString",R,N) overrideReason;
@property (TB,R,N,V_suppressedByFamiliarLocation) suppressedByFamiliarLocation;
@property (TB,R,N,V_suppressedByShortReunionTime) suppressedByShortReunionTime;
@property (TB,R,N,V_suppressedByPersonalVehicleWhileTraveling) suppressedByPersonalVehicleWhileTraveling;
@property (TB,R,N,V_suppressedByVehicularMotionWhileTraveling) suppressedByVehicularMotionWhileTraveling;
@property (TB,R,N,V_suppressedByBookendedTravelBTHint) suppressedByBookendedTravelBTHint;
@property (TB,R,N,V_suppressedByInsufficientScanAirTimeWhileTraveling) suppressedByInsufficientScanAirTimeWhileTraveling;
@property (TB,R,N,V_suppressedByInsufficientScanAirTimeForLBAndBookended) suppressedByInsufficientScanAirTimeForLBAndBookended;
@property (TB,R,N,V_overridenByNumSafeLocations) overridenByNumSafeLocations;
@property (Td,R,N,V_recentFamiliarity) recentFamiliarity;
@property (Td,R,N,V_historicalFamiliarity) historicalFamiliarity;
@property (Td,R,N,V_distanceFromHome) distanceFromHome;
@property (Td,R,N,V_predictedLocationReturnTime) predictedLocationReturnTime;
@property (Td,R,N,V_contextProbability) contextProbability;
@property (Td,R,N,V_minPredictedReunionProbability) minPredictedReunionProbability;
@property (Td,R,N,V_minHistoricalFamiliarity) minHistoricalFamiliarity;
```

## Instance methods

```
-[SASuppressionResult distanceFromHome];
-[SASuppressionResult contextProbability];
-[SASuppressionResult suppressionReason];
-[SASuppressionResult shouldSuppress];
-[SASuppressionResult historicalFamiliarity];
-[SASuppressionResult initWithFamiliarLocation:shortReunionTime:personalVehicle:vehicularMotion:bookendedTravelBTHint:insufficientScanAirTimeWhileTraveling:insufficientScanAirTimeForLBAndBookended:numSafeLocations:recentFamiliarity:historicalFamiliarity:distanceFromHome:predictedLocationReturnTime:contextProbability:minPredictedReunionProbability:minHistoricalFamiliarity:];
-[SASuppressionResult minHistoricalFamiliarity];
-[SASuppressionResult minPredictedReunionProbability];
-[SASuppressionResult overrideReason];
-[SASuppressionResult overridenByNumSafeLocations];
-[SASuppressionResult predictedLocationReturnTime];
-[SASuppressionResult recentFamiliarity];
-[SASuppressionResult suppressedByBookendedTravelBTHint];
-[SASuppressionResult suppressedByFamiliarLocation];
-[SASuppressionResult suppressedByInsufficientScanAirTimeForLBAndBookended];
-[SASuppressionResult suppressedByInsufficientScanAirTimeWhileTraveling];
-[SASuppressionResult suppressedByPersonalVehicleWhileTraveling];
-[SASuppressionResult suppressedByShortReunionTime];
-[SASuppressionResult suppressedByVehicularMotionWhileTraveling];
-[SASuppressionResult wasOverridden];
-[SASuppressionResult wasOverrideCriteriaMet];
-[SASuppressionResult wasSuppressionCriteriaMet];
```
