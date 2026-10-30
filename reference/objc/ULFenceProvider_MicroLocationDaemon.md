# `ULFenceProvider`

- Image: [`/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon`](../userland/System__Library__PrivateFrameworks__MicroLocationDaemon.framework__MicroLocationDaemon.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"ULPDRFenceBridge" _pdrFenceProvider;
@"ULCMFenceBridge" _cmpdrFenceProvider;
q _fenceType;
@"NSObject<OS_dispatch_queue>" _queue;
```

## Properties

```
@property (T@"ULPDRFenceBridge",&,N,V_pdrFenceProvider) pdrFenceProvider;
@property (T@"ULCMFenceBridge",&,N,V_cmpdrFenceProvider) cmpdrFenceProvider;
@property (Tq,N,V_fenceType) fenceType;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_queue) queue;
```

## Instance methods

```
-[ULFenceProvider queue];
-[ULFenceProvider endSession];
-[ULFenceProvider startSession];
-[ULFenceProvider setQueue:];
-[ULFenceProvider fenceType];
-[ULFenceProvider setFenceType:];
-[ULFenceProvider clearFence];
-[ULFenceProvider setFenceRadius:];
-[ULFenceProvider cmpdrFenceProvider];
-[ULFenceProvider initWithFenceIdentifier:odometryMonitor:queue:radiusInMeters:callback:errorCallback:];
-[ULFenceProvider pdrFenceProvider];
-[ULFenceProvider setCmpdrFenceProvider:];
-[ULFenceProvider setFence];
-[ULFenceProvider setPdrFenceProvider:];
```
