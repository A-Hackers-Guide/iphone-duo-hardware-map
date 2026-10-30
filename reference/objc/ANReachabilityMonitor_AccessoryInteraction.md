# `ANReachabilityMonitor`

- Image: [`/System/Library/PrivateFrameworks/AccessoryInteraction.framework/AccessoryInteraction`](../userland/System__Library__PrivateFrameworks__AccessoryInteraction.framework__AccessoryInteraction.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 1 properties, 5 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _queue;
^{__SCNetworkReachability=} _networkReachability;
@? _onReachabilityChanged;
```

## Properties

```
@property (T@?,C,N,V_onReachabilityChanged) onReachabilityChanged;
```

## Instance methods

```
-[ANReachabilityMonitor initWithQueue:];
-[ANReachabilityMonitor dealloc];
-[ANReachabilityMonitor isReachableWithFlags:];
-[ANReachabilityMonitor onReachabilityChanged];
-[ANReachabilityMonitor setOnReachabilityChanged:];
```
