# `SBBackgroundActivityAssertionServiceManager`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSXPCListenerDelegate`, `SBBackgroundActivityAssertionServer`, `BSDescriptionProviding`
- 11 instance variables, 14 properties, 48 instance methods, 0 class methods

## Instance variables

```
@"NSMutableArray" _runningUpdateTransactions;
@"NSXPCListener" _xpcListener;
@"NSMapTable" _assertionsByIdentifierByClientConnection;
@"NSMapTable" _assertionsByBackgroundActivityIdentifier;
@"NSObject<OS_dispatch_queue>" _internalQueue;
@"NSMutableSet" _backgroundActivityIdentifiers;
@"NSMutableSet" _exclusiveBackgroundActivityIdentifiers;
@"<SBBackgroundActivityAssertionServiceManagerDelegate>" _delegate;
@"NSMapTable" _attributionsByAssertion;
@"NSMutableArray" _coordinatorConnectionsByBackgroundActivity;
@"STBackgroundActivitiesStatusDomainPublisher" _publisher;
```

## Properties

```
@property (T@"NSXPCListener",&,N,V_xpcListener) xpcListener;
@property (T@"NSMapTable",&,N,V_assertionsByIdentifierByClientConnection) assertionsByIdentifierByClientConnection;
@property (T@"NSMapTable",&,N,V_assertionsByBackgroundActivityIdentifier) assertionsByBackgroundActivityIdentifier;
@property (T@"NSMapTable",&,N,V_attributionsByAssertion) attributionsByAssertion;
@property (T@"NSMutableArray",&,N,V_coordinatorConnectionsByBackgroundActivity) coordinatorConnectionsByBackgroundActivity;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_internalQueue) internalQueue;
@property (T@"NSMutableSet",C,N,V_backgroundActivityIdentifiers) backgroundActivityIdentifiers;
@property (T@"NSMutableSet",C,N,V_exclusiveBackgroundActivityIdentifiers) exclusiveBackgroundActivityIdentifiers;
@property (T@"STBackgroundActivitiesStatusDomainPublisher",R,N,V_publisher) publisher;
@property (T@"<SBBackgroundActivityAssertionServiceManagerDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBBackgroundActivityAssertionServiceManager listener:shouldAcceptNewConnection:];
-[SBBackgroundActivityAssertionServiceManager publisher];
-[SBBackgroundActivityAssertionServiceManager succinctDescriptionBuilder];
-[SBBackgroundActivityAssertionServiceManager init];
-[SBBackgroundActivityAssertionServiceManager dealloc];
-[SBBackgroundActivityAssertionServiceManager descriptionWithMultilinePrefix:];
-[SBBackgroundActivityAssertionServiceManager setBackgroundActivityIdentifiers:];
-[SBBackgroundActivityAssertionServiceManager succinctDescription];
-[SBBackgroundActivityAssertionServiceManager setDelegate:];
-[SBBackgroundActivityAssertionServiceManager delegate];
-[SBBackgroundActivityAssertionServiceManager description];
-[SBBackgroundActivityAssertionServiceManager backgroundActivityIdentifiers];
-[SBBackgroundActivityAssertionServiceManager setInternalQueue:];
-[SBBackgroundActivityAssertionServiceManager xpcListener];
-[SBBackgroundActivityAssertionServiceManager internalQueue];
-[SBBackgroundActivityAssertionServiceManager descriptionBuilderWithMultilinePrefix:];
-[SBBackgroundActivityAssertionServiceManager setXpcListener:];
-[SBBackgroundActivityAssertionServiceManager activateBackgroundActivityAssertions:reply:];
-[SBBackgroundActivityAssertionServiceManager deactivateBackgroundActivityAssertionsWithIdentifiers:];
-[SBBackgroundActivityAssertionServiceManager setRegisteredBackgroundActivityIdentifiers:reply:];
-[SBBackgroundActivityAssertionServiceManager setStatusString:forAssertionWithIdentifier:];
-[SBBackgroundActivityAssertionServiceManager _internalQueue_backgroundActivityIdentifiersAddedByAddingAssertionData:];
-[SBBackgroundActivityAssertionServiceManager _internalQueue_backgroundActivityIdentifiersRemovedByRemovingAssertionData:];
-[SBBackgroundActivityAssertionServiceManager _internalQueue_coordinatorClientForBackgroundActivityIdentifiers:];
-[SBBackgroundActivityAssertionServiceManager _internalQueue_coordinatorClientForConnection:];
-[SBBackgroundActivityAssertionServiceManager _internalQueue_coordinatorClientMatchingBackgroundActivityIdentifier:];
-[SBBackgroundActivityAssertionServiceManager _internalQueue_deactivateBackgroundActivityAssertionsWithIdentifiers:forClientConnection:];
-[SBBackgroundActivityAssertionServiceManager _internalQueue_invalidateBackgroundActivityAssertions:];
-[SBBackgroundActivityAssertionServiceManager _internalQueue_publishAttributionsForAddingAssertionData:];
-[SBBackgroundActivityAssertionServiceManager _internalQueue_publishAttributionsForRemovingAssertionData:];
-[SBBackgroundActivityAssertionServiceManager _invalidateAssertionsWithIdentifiers:forClientConnection:];
-[SBBackgroundActivityAssertionServiceManager _notifyDelegateAboutStatusStringChange];
-[SBBackgroundActivityAssertionServiceManager _verifyCoordinatorEntitlementForBackgroundActivityIdentifiers:onConnection:];
-[SBBackgroundActivityAssertionServiceManager assertionsByBackgroundActivityIdentifier];
-[SBBackgroundActivityAssertionServiceManager assertionsByIdentifierByClientConnection];
-[SBBackgroundActivityAssertionServiceManager attributionsByAssertion];
-[SBBackgroundActivityAssertionServiceManager coordinatorConnectionsByBackgroundActivity];
-[SBBackgroundActivityAssertionServiceManager exclusiveBackgroundActivityIdentifiers];
-[SBBackgroundActivityAssertionServiceManager handleTapForBackgroundActivityWithIdentifier:windowScene:];
-[SBBackgroundActivityAssertionServiceManager invalidateBackgroundActivityAssertions:];
-[SBBackgroundActivityAssertionServiceManager invalidateBackgroundActivityAssertionsForAttributions:];
-[SBBackgroundActivityAssertionServiceManager setAssertionsByBackgroundActivityIdentifier:];
-[SBBackgroundActivityAssertionServiceManager setAssertionsByIdentifierByClientConnection:];
-[SBBackgroundActivityAssertionServiceManager setAttributionsByAssertion:];
-[SBBackgroundActivityAssertionServiceManager setCoordinatorConnectionsByBackgroundActivity:];
-[SBBackgroundActivityAssertionServiceManager setExclusiveBackgroundActivityIdentifiers:];
-[SBBackgroundActivityAssertionServiceManager statusStringForBackgroundActivityWithIdentifier:activeAttributions:];
-[SBBackgroundActivityAssertionServiceManager unregisterCoordinatorRegistrationForBackgroundActivityIdentifiers:];
```
