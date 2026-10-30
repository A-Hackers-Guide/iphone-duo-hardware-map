# `BKSHIDUISensorService`

- Image: [`/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`](../userland/System__Library__PrivateFrameworks__BackBoardServices.framework__BackBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BKSHIDUISensorInternalServicing`, `BKSHIDUISensorSystemShellServicing`, `BKSHIDUISensorServicing`
- 0 instance variables, 5 properties, 9 instance methods, 3 class methods

## Properties

```
@property (T@"BKSHIDUISensorCharacteristics",R,N) sensorCharacteristics;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BKSHIDUISensorService sharedInstance];
+[BKSHIDUISensorService acquireTransactionForReason:];
+[BKSHIDUISensorService serviceForDisplayUUID:];
```

## Instance methods

```
-[BKSHIDUISensorService acquireTransactionForReason:];
-[BKSHIDUISensorService proximityDidUnoccludeAfterWake];
-[BKSHIDUISensorService recalibrateProximitySensor];
-[BKSHIDUISensorService requestEstimatedProximityEventWithTimeout:];
-[BKSHIDUISensorService requestProximityDetectionMode:];
-[BKSHIDUISensorService requestProximityStatusEventForReason:];
-[BKSHIDUISensorService requestUISensorMode:];
-[BKSHIDUISensorService sensorCharacteristics];
-[BKSHIDUISensorService suppressUISensorChangesForReason:];
```
