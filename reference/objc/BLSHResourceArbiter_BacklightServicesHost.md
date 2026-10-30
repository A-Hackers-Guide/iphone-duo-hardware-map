# `BLSHResourceArbiter`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BLSHResourceArbitrating`
- 4 instance variables, 4 properties, 4 instance methods, 0 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
Q _resourceCount;
@"NSMutableArray" _lock_pendingTokens;
@"NSMutableArray" _lock_currentOwners;
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
-[BLSHResourceArbiter init];
-[BLSHResourceArbiter claimResource:];
-[BLSHResourceArbiter initWithResourceCount:];
-[BLSHResourceArbiter tokenDidInvalidate:];
```
