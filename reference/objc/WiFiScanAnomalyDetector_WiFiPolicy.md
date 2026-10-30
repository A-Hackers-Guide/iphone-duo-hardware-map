# `WiFiScanAnomalyDetector`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 11 instance methods, 1 class methods

## Instance variables

```
s _motionState;
@"NSMutableArray" _scanRequestValidator;
@"NSObject<OS_dispatch_queue>" _internalQueue;
@"WiFiSoftError" _softError;
```

## Properties

```
@property (T@"NSMutableArray",&,N,V_scanRequestValidator) scanRequestValidator;
@property (T@"NSObject<OS_dispatch_queue>",&,V_internalQueue) internalQueue;
@property (Ts,N,V_motionState) motionState;
@property (T@"WiFiSoftError",&,N,V_softError) softError;
```

## Class methods

```
+[WiFiScanAnomalyDetector sharedScanAnomalyDetector];
```

## Instance methods

```
-[WiFiScanAnomalyDetector motionState];
-[WiFiScanAnomalyDetector init];
-[WiFiScanAnomalyDetector setMotionState:];
-[WiFiScanAnomalyDetector setInternalQueue:];
-[WiFiScanAnomalyDetector internalQueue];
-[WiFiScanAnomalyDetector reportMotionStateChange:];
-[WiFiScanAnomalyDetector reportScanRequestForClient:withRequest:andResult:];
-[WiFiScanAnomalyDetector scanRequestValidator];
-[WiFiScanAnomalyDetector setScanRequestValidator:];
-[WiFiScanAnomalyDetector setSoftError:];
-[WiFiScanAnomalyDetector softError];
```
