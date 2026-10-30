# `_BKSHIDUISensorServiceReference`

- Image: [`/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`](../userland/System__Library__PrivateFrameworks__BackBoardServices.framework__BackBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BKSHIDUISensorService`
- Protocols: `BKSHIDUISensorInternalServicing`
- 1 instance variables, 5 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"_BKSHIDUISensorDisplayAssociatedService" _service;
```

## Properties

```
@property (T@"BKSHIDUISensorCharacteristics",R,N) sensorCharacteristics;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_BKSHIDUISensorServiceReference dealloc];
-[_BKSHIDUISensorServiceReference acquireTransactionForReason:];
-[_BKSHIDUISensorServiceReference proximityDidUnoccludeAfterWake];
-[_BKSHIDUISensorServiceReference recalibrateProximitySensor];
-[_BKSHIDUISensorServiceReference requestEstimatedProximityEventWithTimeout:];
-[_BKSHIDUISensorServiceReference requestProximityDetectionMode:];
-[_BKSHIDUISensorServiceReference requestProximityStatusEventForReason:];
-[_BKSHIDUISensorServiceReference requestUISensorMode:];
-[_BKSHIDUISensorServiceReference sensorCharacteristics];
-[_BKSHIDUISensorServiceReference suppressUISensorChangesForReason:];
```
