# `BKHIDEventDeliveryManager`

- Image: [`/System/Library/PrivateFrameworks/BackBoardHIDEventFoundation.framework/BackBoardHIDEventFoundation`](../userland/System__Library__PrivateFrameworks__BackBoardHIDEventFoundation.framework__BackBoardHIDEventFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 22 instance variables, 7 properties, 42 instance methods, 0 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
Q _previousProvenanceTimestamp;
@"<BSInvalidatable>" _chainsStateCapture;
@"<BSInvalidatable>" _deferringRulesStateCapture;
@"<BSInvalidatable>" _dispatchRootsStateCapture;
@"<BSInvalidatable>" _graphStateCapture;
@"NSDictionary" _lock_pendingReachableTargets;
@"NSHashTable" _authenticationMessageNamespaceResolvers;
@"BKSHIDEventDisplay" _mainDisplay;
@"BKSHIDEventAuthenticationOriginator" _authenticationOriginator;
@"BKSHIDEventSimpleProvenanceOriginator" _simpleProvenanceOriginator;
@"NSMutableArray" _deliveryRoots;
Q _deliveryRootsEventTypeMask;
@"NSMutableArray" _keyCommandDeliveryRoots;
@"NSMutableDictionary" _buffersByDispatchTarget;
@"BKEventDeferringGraph" _deferringGraph;
@"BSMutableIntegerMap" _bufferingPredicatesByPID;
@"BSMutableIntegerMap" _clientsByPID;
@"NSSet" _allObserverResolutions;
@"NSMutableDictionary" _destinationCacheBySender;
@"BKHIDEventDeliveryObserverService" _resolutionObserver;
@"<BKHIDEventBufferingHIDSystem>" _bufferingDispatcher;
```

## Properties

```
@property (T@"BKHIDEventDeliveryObserverService",&,N,V_resolutionObserver) resolutionObserver;
@property (T@"<BKHIDEventBufferingHIDSystem>",&,N,V_bufferingDispatcher) bufferingDispatcher;
@property (T@"NSDictionary",R,N) currentBuffersPerDispatchTarget;
@property (T@"BKHIDEventDeliveryObserverService",R,N) observerService;
@property (T@"BKSHIDEventDisplay",&,N,V_mainDisplay) mainDisplay;
@property (T@"BKSHIDEventAuthenticationOriginator",R,N,V_authenticationOriginator) authenticationOriginator;
@property (T@"BKSHIDEventSimpleProvenanceOriginator",R,N,V_simpleProvenanceOriginator) simpleProvenanceOriginator;
```

## Instance methods

```
-[BKHIDEventDeliveryManager init];
-[BKHIDEventDeliveryManager authenticationMessage:matchesDeferringNamespacePredicate:];
-[BKHIDEventDeliveryManager dealloc];
-[BKHIDEventDeliveryManager processDidTerminate:];
-[BKHIDEventDeliveryManager mainDisplay];
-[BKHIDEventDeliveryManager connectionDescriptionForDeferringRuleIdentity:];
-[BKHIDEventDeliveryManager deliveryChainsDescription];
-[BKHIDEventDeliveryManager deliveryGraphDescription];
-[BKHIDEventDeliveryManager descriptionOfResolutionPathForEventDescriptor:senderDescriptor:];
-[BKHIDEventDeliveryManager reevaluateBufferingWithContext:];
-[BKHIDEventDeliveryManager currentBuffersPerDispatchTarget];
-[BKHIDEventDeliveryManager observerService];
-[BKHIDEventDeliveryManager setMainDisplay:];
-[BKHIDEventDeliveryManager _fireTimeoutForPID:bufferingPredicates:client:];
-[BKHIDEventDeliveryManager _test_deliveryRootForIdentifier:];
-[BKHIDEventDeliveryManager addAuthenticationMessageNamespaceResolver:];
-[BKHIDEventDeliveryManager authenticationOriginator];
-[BKHIDEventDeliveryManager bufferingDispatcher];
-[BKHIDEventDeliveryManager deferringSelectionTargetIsReachable:];
-[BKHIDEventDeliveryManager deliveryChainsForDeferringTarget:display:environment:event:];
-[BKHIDEventDeliveryManager descriptionOfResolutionPathForKeyCommand:senderDescriptor:];
-[BKHIDEventDeliveryManager destinationsForEvent:sender:];
-[BKHIDEventDeliveryManager destinationsForKeyCommand:sender:];
-[BKHIDEventDeliveryManager destinationsStartingFromPID:deferringPredicate:];
-[BKHIDEventDeliveryManager evaluateReachability];
-[BKHIDEventDeliveryManager initWithObserverService:];
-[BKHIDEventDeliveryManager reachabilityStatusForSelectionTarget:];
-[BKHIDEventDeliveryManager requestSelectionChanges:forClientWithPID:];
-[BKHIDEventDeliveryManager resolutionObserver];
-[BKHIDEventDeliveryManager sequenceForFirstEvent:sender:processor:dispatcher:additionalContext:];
-[BKHIDEventDeliveryManager sequenceForKeyCommand:sender:processor:dispatcher:additionalContext:];
-[BKHIDEventDeliveryManager setBufferingDispatcher:];
-[BKHIDEventDeliveryManager setConstraintAssertions:forClientWithPID:];
-[BKHIDEventDeliveryManager setDeferringRules:forClientWithPID:];
-[BKHIDEventDeliveryManager setDispatchingRoots:forClientWithPID:];
-[BKHIDEventDeliveryManager setEventBufferingPredicates:forClientWithPID:];
-[BKHIDEventDeliveryManager setGrantAssertions:forClientWithPID:];
-[BKHIDEventDeliveryManager setKeyCommandRoots:forClientWithPID:];
-[BKHIDEventDeliveryManager setKeyCommandsRegistrations:forClientWithPID:];
-[BKHIDEventDeliveryManager setModalityAssertions:forClientWithPID:];
-[BKHIDEventDeliveryManager setResolutionObserver:];
-[BKHIDEventDeliveryManager simpleProvenanceOriginator];
```
