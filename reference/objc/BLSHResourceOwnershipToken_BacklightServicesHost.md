# `BLSHResourceOwnershipToken`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BLSHResourceOwning`
- 4 instance variables, 8 properties, 10 instance methods, 0 class methods

## Instance variables

```
B _owned;
B _invalidated;
@"BLSHResourceArbiter" _arbiter;
@? _nonImmediateAcquireBlock;
```

## Properties

```
@property (T@"BLSHResourceArbiter",W,N,V_arbiter) arbiter;
@property (T@?,C,N,V_nonImmediateAcquireBlock) nonImmediateAcquireBlock;
@property (TB,N,GisOwned,V_owned) owned;
@property (TB,N,GisInvalidated,V_invalidated) invalidated;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BLSHResourceOwnershipToken dealloc];
-[BLSHResourceOwnershipToken arbiter];
-[BLSHResourceOwnershipToken isInvalidated];
-[BLSHResourceOwnershipToken setInvalidated:];
-[BLSHResourceOwnershipToken invalidate];
-[BLSHResourceOwnershipToken setArbiter:];
-[BLSHResourceOwnershipToken isOwned];
-[BLSHResourceOwnershipToken nonImmediateAcquireBlock];
-[BLSHResourceOwnershipToken setNonImmediateAcquireBlock:];
-[BLSHResourceOwnershipToken setOwned:];
```
