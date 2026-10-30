# `BLSPendingAssertionService`

- Image: [`/System/Library/PrivateFrameworks/BacklightServices.framework/BacklightServices`](../userland/System__Library__PrivateFrameworks__BacklightServices.framework__BacklightServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BLSAssertionService`
- 3 instance variables, 4 properties, 5 instance methods, 0 class methods

## Instance variables

```
@"NSMutableArray" _assertionsToAcquire;
@"<BLSAssertionService>" _replacementService;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
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
-[BLSPendingAssertionService init];
-[BLSPendingAssertionService restartAssertionTimeoutTimer:];
-[BLSPendingAssertionService acquireAssertion:];
-[BLSPendingAssertionService replaceWithService:];
-[BLSPendingAssertionService cancelAssertion:withError:];
```
