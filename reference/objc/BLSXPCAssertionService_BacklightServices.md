# `BLSXPCAssertionService`

- Image: [`/System/Library/PrivateFrameworks/BacklightServices.framework/BacklightServices`](../userland/System__Library__PrivateFrameworks__BacklightServices.framework__BacklightServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BLSAssertionService`, `BLSXPCAssertionServiceClientInterface`, `BSInvalidatable`
- 6 instance variables, 4 properties, 15 instance methods, 1 class methods

## Instance variables

```
@"BSServiceDispatchQueue" _requestQueue;
@"BSServiceInitiatingConnection" _connection;
@"NSMapTable" _queue_assertions;
@"NSMutableSet" _queue_assertionsToReacquire;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
B _lock_invalidated;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BLSXPCAssertionService defaultEndpoint];
```

## Instance methods

```
-[BLSXPCAssertionService assertionDidCancel:withError:];
-[BLSXPCAssertionService init];
-[BLSXPCAssertionService assertionPaused:];
-[BLSXPCAssertionService dealloc];
-[BLSXPCAssertionService restartAssertionTimeoutTimer:];
-[BLSXPCAssertionService acquireAssertion:];
-[BLSXPCAssertionService assertionWillCancel:];
-[BLSXPCAssertionService initWithEndpoint:];
-[BLSXPCAssertionService invalidate];
-[BLSXPCAssertionService replaceWithService:];
-[BLSXPCAssertionService assertion:failedToAcquireWithError:];
-[BLSXPCAssertionService displays];
-[BLSXPCAssertionService cancelAssertion:withError:];
-[BLSXPCAssertionService assertionResumed:];
-[BLSXPCAssertionService assertionAcquired:];
```
