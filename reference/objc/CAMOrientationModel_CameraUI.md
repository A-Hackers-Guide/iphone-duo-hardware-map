# `CAMOrientationModel`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 16 instance variables, 13 properties, 30 instance methods, 0 class methods

## Instance variables

```
d _desiredUpdateInterval;
q _deviceOrientation;
q _interfaceOrientation;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 _roughOrientation;
B _isLockedUntilUpright;
? _delegate;
q _allowedOrientations;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 _uprightOvershootCalculator;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 _flatOvershootCalculator;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 _lastLandscapeOrientation;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 _lastMotion;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 _flatBaselineYawReference;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 _didFullyProcessGravityReading;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 _gravityStabilityMonitor;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 _gravityAndYawBasedOrientationsAgree;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 _$observationRegistrar;
```

## Properties

```
@property (Td,N,V_desiredUpdateInterval) _desiredUpdateInterval;
@property (Td,N) desiredUpdateInterval;
@property (Tq,N,V_deviceOrientation) _deviceOrientation;
@property (Tq,N) deviceOrientation;
@property (Tq,N,V_interfaceOrientation) _interfaceOrientation;
@property (Tq,N) interfaceOrientation;
@property (TB,N,R) isUpright;
@property (TB,N,V_isLockedUntilUpright) _isLockedUntilUpright;
@property (TB,N) isLockedUntilUpright;
@property (T@"<CAMOrientationModelDelegate>",N,W,V_delegate) _delegate;
@property (T@"<CAMOrientationModelDelegate>",N,W) delegate;
@property (Tq,N,V_allowedOrientations) _allowedOrientations;
@property (Tq,N) allowedOrientations;
```

## Instance methods

```
-[CAMOrientationModel setDeviceOrientation:];
-[CAMOrientationModel deviceOrientation];
-[CAMOrientationModel interfaceOrientation];
-[CAMOrientationModel _interfaceOrientation];
-[CAMOrientationModel setInterfaceOrientation:];
-[CAMOrientationModel init];
-[CAMOrientationModel dealloc];
-[CAMOrientationModel _delegate];
-[CAMOrientationModel allowedOrientations];
-[CAMOrientationModel setDelegate:];
-[CAMOrientationModel delegate];
-[CAMOrientationModel set_delegate:];
-[CAMOrientationModel setAllowedOrientations:];
-[CAMOrientationModel initWithOrientation:];
-[CAMOrientationModel _deviceOrientation];
-[CAMOrientationModel _allowedOrientations];
-[CAMOrientationModel _desiredUpdateInterval];
-[CAMOrientationModel _isLockedUntilUpright];
-[CAMOrientationModel applyDeviceMotion:];
-[CAMOrientationModel desiredUpdateInterval];
-[CAMOrientationModel isLockedUntilUpright];
-[CAMOrientationModel isUpright];
-[CAMOrientationModel setDesiredUpdateInterval:];
-[CAMOrientationModel setIsLockedUntilUpright:];
-[CAMOrientationModel setNeedsReevaluateOrientationFromGravity];
-[CAMOrientationModel set_allowedOrientations:];
-[CAMOrientationModel set_desiredUpdateInterval:];
-[CAMOrientationModel set_deviceOrientation:];
-[CAMOrientationModel set_interfaceOrientation:];
-[CAMOrientationModel set_isLockedUntilUpright:];
```
