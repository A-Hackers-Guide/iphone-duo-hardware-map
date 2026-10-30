# `CLLocationSmootherServerInterface` (protocol)

- Image: [`/System/Library/Frameworks/CoreLocation.framework/CoreLocation`](../userland/System__Library__Frameworks__CoreLocation.framework__CoreLocation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 0 properties, 10 instance methods, 0 class methods

## Instance methods

```
-[CLLocationSmootherServerInterface smoothLocations:workoutActivity:shouldReconstructRoute:handler:];
-[CLLocationSmootherServerInterface addWorkoutEvent:eventDate:eventAcceptanceDate:newWorkoutActivityType:];
-[CLLocationSmootherServerInterface configureWithWorkoutActivity:shouldReconstructEntireRoute:];
-[CLLocationSmootherServerInterface configureWithWorkoutActivity:shouldReconstructEntireRoute:timeIntervalsThatNeedPopulating:];
-[CLLocationSmootherServerInterface configureWithWorkoutActivity:shouldReconstructEntireRoute:timeIntervalsThatNeedPopulating:activeTimeIntervals:];
-[CLLocationSmootherServerInterface primeForRecoveryWithLastSmoothedTimestamp:recentUnsmoothedLocations:];
-[CLLocationSmootherServerInterface smoothLocations:batchType:handler:];
-[CLLocationSmootherServerInterface smoothLocations:useType:];
-[CLLocationSmootherServerInterface smoothLocations:workoutActivity:handler:];
-[CLLocationSmootherServerInterface smoothLocations:workoutActivity:shouldReconstructRoute:timeIntervalsThatNeedPopulated:handler:];
```
