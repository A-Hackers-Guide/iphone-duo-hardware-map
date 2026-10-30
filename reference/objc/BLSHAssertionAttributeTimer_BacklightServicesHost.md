# `BLSHAssertionAttributeTimer`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BLSHLocalAssertionAttributeHandlerEntry`, `BSInvalidatable`, `BSCancellable`
- 6 instance variables, 7 properties, 9 instance methods, 1 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
@"<BSInvalidatable>" _timer;
B _invalidated;
@"<BLSAssertionServiceResponding>" _assertion;
@"<BLSHAssertionAttributeHandlerService>" _service;
@"BLSDurationAttribute" _attribute;
```

## Properties

```
@property (T@"BLSDurationAttribute",R,W,N,V_attribute) attribute;
@property (T@"<BLSAssertionServiceResponding>",R,W,N,V_assertion) assertion;
@property (T@"<BLSHAssertionAttributeHandlerService>",R,W,N,V_service) service;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BLSHAssertionAttributeTimer activateForAttribute:fromAssertion:forService:attributeHandler:];
```

## Instance methods

```
-[BLSHAssertionAttributeTimer assertion];
-[BLSHAssertionAttributeTimer dealloc];
-[BLSHAssertionAttributeTimer invalidate];
-[BLSHAssertionAttributeTimer service];
-[BLSHAssertionAttributeTimer timerFired];
-[BLSHAssertionAttributeTimer attribute];
-[BLSHAssertionAttributeTimer cancel];
-[BLSHAssertionAttributeTimer initForAttribute:fromAssertion:forService:];
-[BLSHAssertionAttributeTimer reactivateIfPossible];
```
