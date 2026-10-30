# `CAFGroupRequest`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CAFCacheableDescription`
- 11 instance variables, 17 properties, 30 instance methods, 0 class methods

## Instance variables

```
B _performed;
B _forced;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
@"CAFCar" _car;
@"NSUUID" _uniqueIdentifier;
@"NSMutableDictionary" _requests;
@"NSMutableDictionary" _errors;
Q _pendingGroups;
@"CAFCachedDescription" _cachedDescription;
@"CAFCachedDescription" _cachedRequestsDescription;
@"CAFCachedDescription" _cachedFullDescription;
```

## Properties

```
@property (T@"CAFCar",R,W,N,V_car) car;
@property (T@"NSUUID",R,N,V_uniqueIdentifier) uniqueIdentifier;
@property (T@"NSMutableDictionary",R,N,V_requests) requests;
@property (T@"NSMutableDictionary",R,N,V_errors) errors;
@property (TB,N,V_performed) performed;
@property (TQ,N,V_pendingGroups) pendingGroups;
@property (T{os_unfair_lock_s=I},N,V_lock) lock;
@property (T@"CAFCachedDescription",&,N,V_cachedDescription) cachedDescription;
@property (T@"CAFCachedDescription",&,N,V_cachedRequestsDescription) cachedRequestsDescription;
@property (T@"CAFCachedDescription",&,N,V_cachedFullDescription) cachedFullDescription;
@property (TB,N,V_forced) forced;
@property (TQ,R,N) count;
@property (T@"NSString",R,N) fullDescription;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CAFGroupRequest errors];
-[CAFGroupRequest cachedDescription];
-[CAFGroupRequest setLock:];
-[CAFGroupRequest performWithCompletion:];
-[CAFGroupRequest requests];
-[CAFGroupRequest count];
-[CAFGroupRequest fullDescription];
-[CAFGroupRequest uniqueIdentifier];
-[CAFGroupRequest setForced:];
-[CAFGroupRequest setCachedDescription:];
-[CAFGroupRequest description];
-[CAFGroupRequest lock];
-[CAFGroupRequest pendingGroups];
-[CAFGroupRequest setPendingGroups:];
-[CAFGroupRequest car];
-[CAFGroupRequest forced];
-[CAFGroupRequest addCharacteristics:];
-[CAFGroupRequest _addRequest:];
-[CAFGroupRequest _currentDescriptionForFull];
-[CAFGroupRequest _currentDescriptionForRequests];
-[CAFGroupRequest _lockedPerformBlock:];
-[CAFGroupRequest addCharacteristic:];
-[CAFGroupRequest cachedFullDescription];
-[CAFGroupRequest cachedRequestsDescription];
-[CAFGroupRequest currentDescriptionForCache:];
-[CAFGroupRequest initWithCar:];
-[CAFGroupRequest performed];
-[CAFGroupRequest setCachedFullDescription:];
-[CAFGroupRequest setCachedRequestsDescription:];
-[CAFGroupRequest setPerformed:];
```
