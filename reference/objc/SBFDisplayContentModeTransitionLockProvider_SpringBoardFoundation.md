# `SBFDisplayContentModeTransitionLockProvider`

- Image: [`/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation`](../userland/System__Library__PrivateFrameworks__SpringBoardFoundation.framework__SpringBoardFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSInvalidatable`
- 5 instance variables, 5 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"BSCompoundAssertion" _lockAssertion;
@"NSMutableArray" _continuationHandlers;
@? _shouldHoldLockHandler;
@"NSMapTable" _optionsByLock;
B _isInvalid;
```

## Properties

```
@property (TB,R,N,GisLocked) locked;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBFDisplayContentModeTransitionLockProvider isLocked];
-[SBFDisplayContentModeTransitionLockProvider dealloc];
-[SBFDisplayContentModeTransitionLockProvider invalidate];
-[SBFDisplayContentModeTransitionLockProvider __addContinuationHandler:];
-[SBFDisplayContentModeTransitionLockProvider _invalidateLocksWithOptions:];
-[SBFDisplayContentModeTransitionLockProvider acquireContinuationLockWithReason:];
-[SBFDisplayContentModeTransitionLockProvider acquireContinuationLockWithReason:options:invalidationHandler:];
-[SBFDisplayContentModeTransitionLockProvider initWithContinuationHandler:shouldHoldLockHandler:];
```
