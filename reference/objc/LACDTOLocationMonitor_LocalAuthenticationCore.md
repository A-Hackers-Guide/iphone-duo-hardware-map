# `LACDTOLocationMonitor`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LACDTOLocationMonitor`
- 4 instance variables, 5 properties, 5 instance methods, 0 class methods

## Instance variables

```
@"<LACDTOLocationProvider>" _locationProvider;
@"NSObject<OS_dispatch_queue>" _workQueue;
@"LACTimer" _timer;
@"<LACDTOLocationMonitorDelegate>" _delegate;
```

## Properties

```
@property (T@"<LACDTOLocationMonitorDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[LACDTOLocationMonitor setDelegate:];
-[LACDTOLocationMonitor delegate];
-[LACDTOLocationMonitor initWithLocationProvider:workQueue:];
-[LACDTOLocationMonitor startMonitoringWithReason:];
-[LACDTOLocationMonitor stopMonitoringWithReason:];
```
