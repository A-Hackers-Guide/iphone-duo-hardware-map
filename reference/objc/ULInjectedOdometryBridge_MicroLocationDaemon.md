# `ULInjectedOdometryBridge`

- Image: [`/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon`](../userland/System__Library__PrivateFrameworks__MicroLocationDaemon.framework__MicroLocationDaemon.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `ULOdometrySource`
- 2 instance variables, 7 properties, 10 instance methods, 2 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _queue;
@"<ULOdometryDelegate>" _delegate;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_queue) queue;
@property (T@"<ULOdometryDelegate>",W,N,V_delegate) delegate;
@property (Tq,R,N) odometrySourceType;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[ULInjectedOdometryBridge isBackgroundAvailable];
+[ULInjectedOdometryBridge isNeuralPDRAvailable];
```

## Instance methods

```
-[ULInjectedOdometryBridge requestNPDRUpdate];
-[ULInjectedOdometryBridge queue];
-[ULInjectedOdometryBridge stopBackgroundUpdates];
-[ULInjectedOdometryBridge setDelegate:];
-[ULInjectedOdometryBridge delegate];
-[ULInjectedOdometryBridge startBackgroundUpdates];
-[ULInjectedOdometryBridge odometrySourceType];
-[ULInjectedOdometryBridge injectOdometryState:];
-[ULInjectedOdometryBridge setQueue:];
-[ULInjectedOdometryBridge initWithDelegateQueue:delegate:];
```
