# `ANLocationMonitor`

- Image: [`/System/Library/PrivateFrameworks/AccessoryInteraction.framework/AccessoryInteraction`](../userland/System__Library__PrivateFrameworks__AccessoryInteraction.framework__AccessoryInteraction.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CLLocationManagerDelegate`
- 10 instance variables, 8 properties, 31 instance methods, 1 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _queue;
@"<ANSystemUtilsProtocol>" _systemUtils;
@"CLLocationManager" _locationManager;
B _enabled;
B _leechingLocation;
@"NSObject<OS_dispatch_source>" _stopActiveLocationRequestTimer;
@"NSDate" lastEvaluationDate;
@"<ANLocationMonitorDelegate>" _delegate;
@"CLLocation" _lastlocation;
@"NSMutableArray" _currentLocationRequests;
```

## Properties

```
@property (T@"CLLocation",&,N,V_lastlocation) lastlocation;
@property (T@"NSDate",&,N,VlastEvaluationDate) lastEvaluationDate;
@property (T@"NSMutableArray",&,N,V_currentLocationRequests) currentLocationRequests;
@property (T@"<ANLocationMonitorDelegate>",V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[ANLocationMonitor isSupported];
```

## Instance methods

```
-[ANLocationMonitor locationManager:didUpdateLocations:];
-[ANLocationMonitor locationManager:didFailWithError:];
-[ANLocationMonitor dealloc];
-[ANLocationMonitor setDelegate:];
-[ANLocationMonitor locationManager:didChangeAuthorizationStatus:];
-[ANLocationMonitor delegate];
-[ANLocationMonitor currentLocationRequests];
-[ANLocationMonitor fetchCurrentLocationWithHandler:];
-[ANLocationMonitor fetchEstimatedLocationAtDate:handler:];
-[ANLocationMonitor setCurrentLocationRequests:];
-[ANLocationMonitor setDesiredAccuracy:];
-[ANLocationMonitor _fetchEstimatedLocationAtDate:withReply:];
-[ANLocationMonitor binTimeInterval:];
-[ANLocationMonitor evaluateLastLocation];
-[ANLocationMonitor initWithQueue:systemUtils:];
-[ANLocationMonitor isLocation:validOnDate:maxHorizontalAccuracy:];
-[ANLocationMonitor lastEvaluationDate];
-[ANLocationMonitor lastValidLocationWithHorizontalAccuracy:evaluationDate:error:];
-[ANLocationMonitor lastlocation];
-[ANLocationMonitor logFaultIfFutureLocation:];
-[ANLocationMonitor onStopActiveLocationRequestTimerExpiry];
-[ANLocationMonitor sendEstimatedLocationMetricsAfterLocationScanWithFirstEstimatedLocation:newLocation:secondEstimatedLocation:error:timeOfInterest:referenceTime:responseTime:];
-[ANLocationMonitor sendEstimatedLocationMetricsAtFirstAttemptForEstimatedLocation:estimationError:timeOfInterest:referenceTime:responseTime:];
-[ANLocationMonitor sendLastLocation:error:];
-[ANLocationMonitor setLastEvaluationDate:];
-[ANLocationMonitor setLastlocation:];
-[ANLocationMonitor startActiveLocationRequest];
-[ANLocationMonitor startLeechingLocation];
-[ANLocationMonitor stopActiveLocationRequest];
-[ANLocationMonitor stopLeechingLocation];
-[ANLocationMonitor updateEstimatedLocationMetrics:currentLocation:estimatedLocation:];
```
