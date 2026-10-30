# `BKSHIDEventDeliveryPolicyObserver`

- Image: [`/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`](../userland/System__Library__PrivateFrameworks__BackBoardServices.framework__BackBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionStreaming`, `BKSHIDEventDeferringObserving`
- 12 instance variables, 13 properties, 29 instance methods, 0 class methods

## Instance variables

```
@"BKSHIDEventObserver" _observer;
@"<BSInvalidatable>" _observingAssertion;
@"NSObject<OS_dispatch_queue>" _asyncObserverCalloutQueue;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
@"BKSHIDEventDisplay" _lock_display;
@"BKSHIDEventDeferringEnvironment" _lock_environment;
@"BKSHIDEventDeferringToken" _lock_token;
@"BKSHIDEventDeferringSelectionPathIdentifier" _lock_selectionPathIdentifier;
@"NSSet" _lock_observations;
@"BKSHIDEventDeliveryPolicy" _lock_currentPolicy;
@"NSHashTable" _lock_observers;
@"NSString" _lock_debugLabel;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",R,N) asyncObserverCalloutQueue;
@property (TB,R,N) canReceiveEvents;
@property (Tq,R,N) policyStatus;
@property (TB,R,N) finalStringTokenInChain;
@property (T@"BKSHIDEventDisplay",C,N) display;
@property (T@"BKSHIDEventDeferringEnvironment",C,N) deferringEnvironment;
@property (T@"BKSHIDEventDeferringSelectionPathIdentifier",C,N) selectionPathIdentifier;
@property (T@"BKSHIDEventDeferringToken",C,N) deferringToken;
@property (T@"BKSHIDEventDeliveryPolicy",R,N) currentPolicy;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BKSHIDEventDeliveryPolicyObserver setDisplay:];
-[BKSHIDEventDeliveryPolicyObserver selectionPathIdentifier];
-[BKSHIDEventDeliveryPolicyObserver _lock_appendDescriptionToStream:];
-[BKSHIDEventDeliveryPolicyObserver policyStatus];
-[BKSHIDEventDeliveryPolicyObserver deferringEnvironment];
-[BKSHIDEventDeliveryPolicyObserver display];
-[BKSHIDEventDeliveryPolicyObserver deferringToken];
-[BKSHIDEventDeliveryPolicyObserver _replacePolicySpecificationObject:withObject:replaceIvarBlock:];
-[BKSHIDEventDeliveryPolicyObserver debugDescription];
-[BKSHIDEventDeliveryPolicyObserver _initWithObserver:];
-[BKSHIDEventDeliveryPolicyObserver _lock_effectivePolicyObservation];
-[BKSHIDEventDeliveryPolicyObserver removeObserver:];
-[BKSHIDEventDeliveryPolicyObserver init];
-[BKSHIDEventDeliveryPolicyObserver dealloc];
-[BKSHIDEventDeliveryPolicyObserver _lock_description];
-[BKSHIDEventDeliveryPolicyObserver canReceiveEvents];
-[BKSHIDEventDeliveryPolicyObserver _lock_buildCurrentPolicy];
-[BKSHIDEventDeliveryPolicyObserver addObserver:];
-[BKSHIDEventDeliveryPolicyObserver currentPolicy];
-[BKSHIDEventDeliveryPolicyObserver setSelectionPathIdentifier:];
-[BKSHIDEventDeliveryPolicyObserver _notifyAsyncObservers:didUpdatePolicy:];
-[BKSHIDEventDeliveryPolicyObserver deferringResolutionsChanged];
-[BKSHIDEventDeliveryPolicyObserver setDeferringToken:];
-[BKSHIDEventDeliveryPolicyObserver description];
-[BKSHIDEventDeliveryPolicyObserver appendDescriptionToStream:];
-[BKSHIDEventDeliveryPolicyObserver finalStringTokenInChain];
-[BKSHIDEventDeliveryPolicyObserver asyncObserverCalloutQueue];
-[BKSHIDEventDeliveryPolicyObserver _lock_updatePolicyWithBlock:];
-[BKSHIDEventDeliveryPolicyObserver setDeferringEnvironment:];
```
