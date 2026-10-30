# `CMOdometer`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"<CMOdometerDelegate>" _delegate;
@"CMOdometerProxy" _odometerProxy;
```

## Properties

```
@property (T@"CMOdometerProxy",R,N,V_odometerProxy) odometerProxy;
@property (T@"<CMOdometerDelegate>",W,N,V_delegate) delegate;
```

## Instance methods

```
-[CMOdometer init];
-[CMOdometer dealloc];
-[CMOdometer setDelegate:];
-[CMOdometer delegate];
-[CMOdometer odometerProxy];
-[CMOdometer startCyclingWorkoutDistanceUpdatesWithHandler:];
-[CMOdometer startOdometerUpdatesForActivity:withHandler:];
-[CMOdometer stopCyclingWorkoutDistanceUpdates];
-[CMOdometer stopOdometerUpdates];
```
