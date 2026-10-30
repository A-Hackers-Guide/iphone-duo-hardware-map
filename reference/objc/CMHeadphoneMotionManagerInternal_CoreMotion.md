# `CMHeadphoneMotionManagerInternal`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 18 instance variables, 2 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _dispatchQueue;
@"RMConnectionClient" _connectionClient;
@"NSOperationQueue" _callbackQueue;
@? _callbackHandler;
Q _availableReferenceFrames;
Q _referenceFrame;
q _bodyFrame;
B _shouldApplyInitialReference;
B _deviceMotionActive;
B _deviceMotionStreaming;
B _deviceConnected;
d _deviceConnectionTimestamp;
d _firstValidDeviceMotionTimestamp;
@"RMConnectionClient" _statusConnectionClient;
B _statusActive;
B _statusStreaming;
@"CMDeviceMotion" _deviceMotion;
@"CMAttitude" _initialReferenceAttitude;
```

## Properties

```
@property (T@"CMDeviceMotion",&,V_deviceMotion) deviceMotion;
@property (T@"CMAttitude",&,N,V_initialReferenceAttitude) initialReferenceAttitude;
```

## Instance methods

```
-[CMHeadphoneMotionManagerInternal connect];
-[CMHeadphoneMotionManagerInternal init];
-[CMHeadphoneMotionManagerInternal dealloc];
-[CMHeadphoneMotionManagerInternal disconnect];
-[CMHeadphoneMotionManagerInternal deviceMotion];
-[CMHeadphoneMotionManagerInternal connectStatus];
-[CMHeadphoneMotionManagerInternal disconnectStatus];
-[CMHeadphoneMotionManagerInternal initialReferenceAttitude];
-[CMHeadphoneMotionManagerInternal setDeviceMotion:];
-[CMHeadphoneMotionManagerInternal setInitialReferenceAttitude:];
```
