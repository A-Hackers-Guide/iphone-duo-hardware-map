# `BKSTouchEventService`

- Image: [`/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`](../userland/System__Library__PrivateFrameworks__BackBoardServices.framework__BackBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BKSTouchEventClient_IPC`
- 7 instance variables, 4 properties, 20 instance methods, 1 class methods

## Instance variables

```
B _isNonLaunchingServer;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
@"BSServiceInitiatingConnection" _connection;
B _lock_waitingOnServerHandshake;
@"NSMutableDictionary" _lock_registrationsByContextID;
@"BSCompoundAssertion" _contextIDsForAXZoom;
@"BSCompoundAssertion" _hitTestFilterParameters;
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
+[BKSTouchEventService sharedInstance];
```

## Instance methods

```
-[BKSTouchEventService _initWithConnectionFactory:];
-[BKSTouchEventService addTouchAuthenticationSpecifications:forReason:];
-[BKSTouchEventService excludeEventsFromSenders:fromHitTestingToContextIDs:];
-[BKSTouchEventService _initConnectionWithConnectionFactory:];
-[BKSTouchEventService _lock_flushStateToServer];
-[BKSTouchEventService _lock_repostAllRegistrations];
-[BKSTouchEventService _lock_updateServerHitTestCategoryContextIDs];
-[BKSTouchEventService _lock_updateServerHitTestFilterParameters];
-[BKSTouchEventService _updateServerHitTestCategoryContextIDs];
-[BKSTouchEventService _updateServerHitTestFilterParameters];
-[BKSTouchEventService _updateTouchDetachmentOffset:userIdentifier:];
-[BKSTouchEventService _updateTouchDetachmentRoutingPolicy:userIdentifier:];
-[BKSTouchEventService addAuthenticationSpecifications:forReason:];
-[BKSTouchEventService detachTouchIdentifiers:userIdentifier:];
-[BKSTouchEventService detachTouchIdentifiers:userIdentifier:initialRoutingPolicy:];
-[BKSTouchEventService detachTouchIdentifiers:userIdentifier:initialRoutingPolicy:initialTouchOffset:];
-[BKSTouchEventService excludeEventsFromStimulus:fromHitTestingToContextIDs:];
-[BKSTouchEventService registerSceneHostSettings:forCAContextID:];
-[BKSTouchEventService setContextIDs:forHitTestContextCategory:];
-[BKSTouchEventService transformForDisplayUUID:layerID:contextID:];
```
