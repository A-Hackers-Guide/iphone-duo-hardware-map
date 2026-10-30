# `CLLocationSmoother`

- Image: [`/System/Library/Frameworks/CoreLocation.framework/CoreLocation`](../userland/System__Library__Frameworks__CoreLocation.framework__CoreLocation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 3 properties, 24 instance methods, 0 class methods

## Instance variables

```
@"_CLLocationSmootherProxy" _locationManagerSmootherProxy;
B fShouldReconstructEntireRoute;
@"NSArray" fTimeIntervalsThatNeedPopulating;
@"NSArray" fActiveTimeIntervals;
Q fWorkoutActivityType;
B fConfigurationForwarded;
```

## Properties

```
@property (T@"_CLLocationSmootherProxy",R,&,N) locationManagerSmootherProxy;
@property (T@"<CLLocationManagerDelegateInternal>",W,N) delegate;
@property (T@?,C) connectionInterruptionHandler;
```

## Instance methods

```
-[CLLocationSmoother dealloc];
-[CLLocationSmoother setConnectionInterruptionHandler:];
-[CLLocationSmoother invalidate];
-[CLLocationSmoother setDelegate:];
-[CLLocationSmoother delegate];
-[CLLocationSmoother connectionInterruptionHandler];
-[CLLocationSmoother _configurationForwardedToDaemon];
-[CLLocationSmoother addWorkoutEvent:eventDate:eventAcceptanceDate:newWorkoutActivityType:];
-[CLLocationSmoother configureWithWorkoutActivityType:shouldReconstructEntireRoute:timeIntervalsThatNeedPopulating:];
-[CLLocationSmoother configureWithWorkoutActivityType:shouldReconstructEntireRoute:timeIntervalsThatNeedPopulating:activeTimeIntervals:];
-[CLLocationSmoother forwardConfigurationIfNeeded];
-[CLLocationSmoother initWithWorkoutActivityType:shouldReconstructEntireRoute:];
-[CLLocationSmoother initWithWorkoutActivityType:shouldReconstructEntireRoute:timeIntervalsThatNeedPopulating:];
-[CLLocationSmoother initWithWorkoutActivityType:shouldReconstructEntireRoute:timeIntervalsThatNeedPopulating:activeTimeIntervals:];
-[CLLocationSmoother locationManagerSmootherProxy];
-[CLLocationSmoother logActiveTimeIntervals:];
-[CLLocationSmoother logTimeIntervalsThatNeedPopulating:];
-[CLLocationSmoother primeForRecoveryWithLastSmoothedTimestamp:recentUnsmoothedLocations:];
-[CLLocationSmoother smoothLocations:];
-[CLLocationSmoother smoothLocations:batchType:handler:];
-[CLLocationSmoother smoothLocations:handler:];
-[CLLocationSmoother smoothLocations:workoutActivityType:handler:];
-[CLLocationSmoother smoothLocations:workoutActivityType:shouldReconstructRoute:handler:];
-[CLLocationSmoother smoothLocations:workoutActivityType:shouldReconstructRoute:timeIntervalsThatNeedPopulated:handler:];
```
