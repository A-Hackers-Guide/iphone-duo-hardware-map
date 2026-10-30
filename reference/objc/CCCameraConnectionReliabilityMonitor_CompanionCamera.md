# `CCCameraConnectionReliabilityMonitor`

- Image: [`/System/Library/PrivateFrameworks/CompanionCamera.framework/CompanionCamera`](../userland/System__Library__PrivateFrameworks__CompanionCamera.framework__CompanionCamera.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 0 properties, 5 instance methods, 1 class methods

## Instance variables

```
C _instanceCount;
B _isConnected;
@"NSDate" _lastConnectTime;
```

## Class methods

```
+[CCCameraConnectionReliabilityMonitor sharedInstance];
```

## Instance methods

```
-[CCCameraConnectionReliabilityMonitor didConnect];
-[CCCameraConnectionReliabilityMonitor init];
-[CCCameraConnectionReliabilityMonitor decrementInstanceCount];
-[CCCameraConnectionReliabilityMonitor incrementInstanceCount];
-[CCCameraConnectionReliabilityMonitor didDisconnect];
```
