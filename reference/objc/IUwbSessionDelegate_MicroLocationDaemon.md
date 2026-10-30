# `IUwbSessionDelegate`

- Image: [`/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon`](../userland/System__Library__PrivateFrameworks__MicroLocationDaemon.framework__MicroLocationDaemon.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NISessionDelegate`
- 1 instance variables, 5 properties, 12 instance methods, 0 class methods

## Instance variables

```
^v _uwbBridge;
```

## Properties

```
@property (T^v,N,V_uwbBridge) uwbBridge;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[IUwbSessionDelegate dealloc];
-[IUwbSessionDelegate session:didInvalidateWithError:];
-[IUwbSessionDelegate session:didFailWithError:];
-[IUwbSessionDelegate session:didUpdateNearbyObjects:];
-[IUwbSessionDelegate session:didDiscoverNearbyObject:];
-[IUwbSessionDelegate session:didRemoveNearbyObjects:withReason:];
-[IUwbSessionDelegate sessionDidStartRunning:];
-[IUwbSessionDelegate sessionSuspensionEnded:];
-[IUwbSessionDelegate sessionWasSuspended:];
-[IUwbSessionDelegate initWithUWBBridge:];
-[IUwbSessionDelegate setUwbBridge:];
-[IUwbSessionDelegate uwbBridge];
```
