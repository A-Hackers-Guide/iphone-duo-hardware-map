# `BKSHIDEventDeliveryManager`

- Image: [`/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`](../userland/System__Library__PrivateFrameworks__BackBoardServices.framework__BackBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionStreaming`
- 38 instance variables, 4 properties, 39 instance methods, 1 class methods

## Instance variables

```
@"BSServiceInitiatingConnection" _serviceConnection;
@"NSObject<OS_dispatch_queue>" _asyncResultQueue;
@"<BKSHIDEventDeliveryManagerServerInterface>" _lock_remoteTargetSafeToMessage;
@"NSMutableArray" _lock_pendingQueriesToBeExecutedInsideLockOnceActivationHappens;
B _forTesting;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
@"NSHashTable" _lock_assertions;
I _lock_discreteDispatchingSeed;
@"NSMutableSet" _lock_discreteDispatchingRoots;
@"NSSet" _lock_lastSentDiscreteDispatchingRoots;
I _lock_keyCommandsDispatchingSeed;
@"NSMutableSet" _lock_keyCommandsDispatchingRoots;
@"NSSet" _lock_lastSentKeyCommandsDispatchingRoots;
I _lock_deferringSeed;
@"NSMutableArray" _lock_deferringRules;
@"NSArray" _lock_lastSentDeferringRules;
I _lock_bufferingSeed;
@"NSMutableDictionary" _lock_bufferingPredicates;
@"NSSet" _lock_lastSentBufferingPredicates;
I _lock_modalityAssertSeed;
@"NSMutableSet" _lock_modalityAsserts;
@"NSSet" _lock_lastSentModalityAsserts;
I _lock_constraintAssertSeed;
@"NSMutableSet" _lock_constraintAsserts;
@"NSSet" _lock_lastSentConstraintAsserts;
@"NSMutableSet" _lock_selectionRequests;
I _lock_grantAssertSeed;
@"NSMutableSet" _lock_grantAsserts;
@"NSSet" _lock_lastSentGrantAsserts;
I _lock_keyCommandsRegistrationSeed;
@"NSMutableDictionary" _lock_keyCommandsRegistrations;
@"NSDictionary" _lock_lastSentKeyCommandsRegistrations;
@"NSSet" _lock_lastSentSetOfKeyCommandsRegistrations;
@"NSObject<OS_dispatch_queue>" _implicitFlushQueue;
^{__CFBoolean=} _lock_needsFlush;
q _lock_preventFlushingSeed;
@"BSMutableIntegerMap" _lock_preventFlushingReasons;
@"<BSInvalidatable>" _lock_implicitPreventFlushingAssertion;
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
+[BKSHIDEventDeliveryManager sharedInstance];
```

## Instance methods

```
-[BKSHIDEventDeliveryManager observeReachabilityOfSelectionTarget:respectingConstraints:handler:];
-[BKSHIDEventDeliveryManager debugDescription];
-[BKSHIDEventDeliveryManager _lock_flushIfNeeded];
-[BKSHIDEventDeliveryManager _lock_noteServerInterruption];
-[BKSHIDEventDeliveryManager init];
-[BKSHIDEventDeliveryManager authenticationMessage:matchesDeferringNamespacePredicate:];
-[BKSHIDEventDeliveryManager registerKeyCommands:];
-[BKSHIDEventDeliveryManager transactionAssertionWithReason:];
-[BKSHIDEventDeliveryManager changeSelectionPath:target:basis:ignoreModalities:];
-[BKSHIDEventDeliveryManager deferEventsMatchingPredicate:priority:restrictedToEventDescriptors:toTarget:withReason:];
-[BKSHIDEventDeliveryManager dealloc];
-[BKSHIDEventDeliveryManager _executeDescriptionFetch:result:];
-[BKSHIDEventDeliveryManager _initWithConnectionFactory:forTesting:];
-[BKSHIDEventDeliveryManager deferEventsMatchingPredicate:toTarget:withReason:];
-[BKSHIDEventDeliveryManager assertSelectionPath:target:grantsSelectionToTarget:reason:];
-[BKSHIDEventDeliveryManager _lock_stateDescription];
-[BKSHIDEventDeliveryManager resolutionDescriptionForEventDescriptor:sender:result:];
-[BKSHIDEventDeliveryManager _lock_pendQuery:];
-[BKSHIDEventDeliveryManager _lock_implicitFlush];
-[BKSHIDEventDeliveryManager authenticateMessage:];
-[BKSHIDEventDeliveryManager deliveryChainsDescription:];
-[BKSHIDEventDeliveryManager dispatchKeyCommandsForReason:withRule:];
-[BKSHIDEventDeliveryManager _lock_transactionAssertionWithReason:];
-[BKSHIDEventDeliveryManager assertSelectionPath:target:imposesConstraint:];
-[BKSHIDEventDeliveryManager deferEventsMatchingPredicate:restrictedToEventDescriptors:toTarget:withReason:];
-[BKSHIDEventDeliveryManager assertSelectionPath:target:hasModality:basis:];
-[BKSHIDEventDeliveryManager validateProvenance:];
-[BKSHIDEventDeliveryManager description];
-[BKSHIDEventDeliveryManager dispatchDiscreteEventsForReason:withRules:];
-[BKSHIDEventDeliveryManager appendDescriptionToStream:];
-[BKSHIDEventDeliveryManager connectionDescriptionForDeferringRuleIdentity:result:];
-[BKSHIDEventDeliveryManager resolutionDescriptionForKeyCommand:sender:result:];
-[BKSHIDEventDeliveryManager observeReachabilityOfSelectionTarget:handler:];
-[BKSHIDEventDeliveryManager connectionDescriptionForDeferringRuleWithSeed:pid:result:];
-[BKSHIDEventDeliveryManager deliveryGraphDescription:];
-[BKSHIDEventDeliveryManager assertSelectionPath:target:imposesConstraint:reason:];
-[BKSHIDEventDeliveryManager _syncServiceFlushState];
-[BKSHIDEventDeliveryManager bufferEventsMatchingPredicate:withReason:];
-[BKSHIDEventDeliveryManager deferEventsMatchingPredicate:priority:toTarget:withReason:];
```
