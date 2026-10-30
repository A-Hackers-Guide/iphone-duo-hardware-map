# `CLLocationManagerRoutine`

- Image: [`/System/Library/Frameworks/CoreLocation.framework/CoreLocation`](../userland/System__Library__Frameworks__CoreLocation.framework__CoreLocation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 3 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"_CLLocationManagerRoutineProxy" _locationManagerRoutineProxy;
```

## Properties

```
@property (T@"_CLLocationManagerRoutineProxy",&,N,V_locationManagerRoutineProxy) locationManagerRoutineProxy;
@property (T@"<CLLocationManagerDelegate>",W,N) delegate;
@property (T@"<CLInertialDataManagerDelegate>",W,N) inertialDelegate;
```

## Instance methods

```
-[CLLocationManagerRoutine initWithQueue:];
-[CLLocationManagerRoutine init];
-[CLLocationManagerRoutine startUpdatingLocation];
-[CLLocationManagerRoutine dealloc];
-[CLLocationManagerRoutine stopUpdatingLocation];
-[CLLocationManagerRoutine setDelegate:];
-[CLLocationManagerRoutine delegate];
-[CLLocationManagerRoutine setLocationManagerRoutineProxy:];
-[CLLocationManagerRoutine fetchLocationAtDate:withHandler:];
-[CLLocationManagerRoutine fetchLocationAtMachContinuousTime:withHandler:];
-[CLLocationManagerRoutine fetchLocationsInLastSeconds:withHandler:];
-[CLLocationManagerRoutine fetchRecentLocationsWithOptions:withHandler:];
-[CLLocationManagerRoutine inertialDelegate];
-[CLLocationManagerRoutine locationManagerRoutineProxy];
-[CLLocationManagerRoutine setInertialDelegate:];
```
