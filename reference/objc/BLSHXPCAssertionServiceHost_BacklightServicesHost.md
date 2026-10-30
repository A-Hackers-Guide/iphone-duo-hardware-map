# `BLSHXPCAssertionServiceHost`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BLSXPCAssertionServiceHostInterface`, `BSInvalidatable`
- 6 instance variables, 4 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"<BLSAssertionService>" _localService;
@"<BLSHBacklightOSInterfaceProviding>" _osInterfaceProvider;
@"BSAuditToken" _remoteToken;
@"NSMutableDictionary" _assertionProxies;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
B _valid;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BLSHXPCAssertionServiceHost dealloc];
-[BLSHXPCAssertionServiceHost restartAssertionTimeoutTimer:];
-[BLSHXPCAssertionServiceHost acquireAssertion:];
-[BLSHXPCAssertionServiceHost invalidate];
-[BLSHXPCAssertionServiceHost displays];
-[BLSHXPCAssertionServiceHost cancelAssertion:withError:];
-[BLSHXPCAssertionServiceHost acquireAssertionForDescriptor:error:];
-[BLSHXPCAssertionServiceHost destroyAssertion:];
-[BLSHXPCAssertionServiceHost initWithLocalService:peer:osInterfaceProvider:];
```
