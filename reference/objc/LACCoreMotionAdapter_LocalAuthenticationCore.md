# `LACCoreMotionAdapter`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LACAccelerometerProviding`
- 2 instance variables, 5 properties, 4 instance methods, 0 class methods

## Instance variables

```
@"CMMotionManager" _manager;
@"NSOperationQueue" _accelerometerQueue;
```

## Properties

```
@property (TB,R,D,N) isAccelerometerAvailable;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[LACCoreMotionAdapter isAccelerometerAvailable];
-[LACCoreMotionAdapter stopUpdates];
-[LACCoreMotionAdapter initWithWorkQueue:];
-[LACCoreMotionAdapter startUpdatesWithHandler:];
```
