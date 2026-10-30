# `UIAccelerometer`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 2 properties, 12 instance methods, 1 class methods

## Instance variables

```
d _updateInterval;
@"<UIAccelerometerDelegate>" _delegate;
{?="delegateDidAccelerate"b1"isInert"b1} _accelerometerFlags;
@"CMMotionManager" _motionManager;
```

## Properties

```
@property (Td,N,V_updateInterval) updateInterval;
@property (T@"<UIAccelerometerDelegate>",W,N,V_delegate) delegate;
```

## Class methods

```
+[UIAccelerometer sharedAccelerometer];
```

## Instance methods

```
-[UIAccelerometer init];
-[UIAccelerometer dealloc];
-[UIAccelerometer _motionManager];
-[UIAccelerometer setDelegate:];
-[UIAccelerometer setUpdateInterval:];
-[UIAccelerometer delegate];
-[UIAccelerometer updateInterval];
-[UIAccelerometer _acceleratedInX:y:z:timestamp:];
-[UIAccelerometer _didSuspend:];
-[UIAccelerometer _startAccelerometerIfNecessary];
-[UIAccelerometer _stopAccelerometer];
-[UIAccelerometer _willResume:];
```
