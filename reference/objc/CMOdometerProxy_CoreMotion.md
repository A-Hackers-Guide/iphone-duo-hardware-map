# `CMOdometerProxy`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 11 instance variables, 6 properties, 21 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" fInternalQueue;
@"NSObject<OS_dispatch_queue>" fCallbackQueue;
^v fLocationdConnection;
@? fHandler;
q fGpsAvailability;
@"CMOdometer" _odometer;
d _totalDistance;
d _averageSpeed;
d _startDate;
d _totalCyclingDistance;
d _cyclingStartDate;
```

## Properties

```
@property (T@"CMOdometer",N,V_odometer) odometer;
@property (Td,V_totalDistance) totalDistance;
@property (Td,V_averageSpeed) averageSpeed;
@property (Td,V_startDate) startDate;
@property (Td,V_totalCyclingDistance) totalCyclingDistance;
@property (Td,V_cyclingStartDate) cyclingStartDate;
```

## Instance methods

```
-[CMOdometerProxy startDate];
-[CMOdometerProxy setStartDate:];
-[CMOdometerProxy dealloc];
-[CMOdometerProxy totalDistance];
-[CMOdometerProxy odometer];
-[CMOdometerProxy setTotalDistance:];
-[CMOdometerProxy _teardown];
-[CMOdometerProxy _startCyclingWorkoutDistanceUpdatesWithHandler:];
-[CMOdometerProxy _startDaemonConnection];
-[CMOdometerProxy _startOdometerUpdatesWithHandler:];
-[CMOdometerProxy _stopCyclingWorkoutDistanceUpdates];
-[CMOdometerProxy _stopOdometerGpsAvailability];
-[CMOdometerProxy _stopOdometerUpdates];
-[CMOdometerProxy averageSpeed];
-[CMOdometerProxy cyclingStartDate];
-[CMOdometerProxy initWithOdometer:];
-[CMOdometerProxy setAverageSpeed:];
-[CMOdometerProxy setCyclingStartDate:];
-[CMOdometerProxy setOdometer:];
-[CMOdometerProxy setTotalCyclingDistance:];
-[CMOdometerProxy totalCyclingDistance];
```
