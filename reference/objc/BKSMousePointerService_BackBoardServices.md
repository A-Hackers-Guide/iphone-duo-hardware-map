# `BKSMousePointerService`

- Image: [`/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`](../userland/System__Library__PrivateFrameworks__BackBoardServices.framework__BackBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BKSMousePointerServiceServerToClientInterface`
- 10 instance variables, 5 properties, 37 instance methods, 3 class methods

## Instance variables

```
@"BSServiceDispatchQueue" _connectionQueue;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
@"BSServiceInitiatingConnection" _connection;
@"NSMutableDictionary" _displayUUIDToPerDisplayInfo;
@"BSCompoundAssertion" _deviceConnectionObservers;
@"BSCompoundAssertion" _preferencesObservers;
@"BSCompoundAssertion" _suppressMouseEvents;
@"NSSet" _attachedDevices;
B _isObservingDeviceConnection;
B _isObservingPreferences;
```

## Properties

```
@property (T@"BKSMousePointerDevicePreferences",C) globalDevicePreferences;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BKSMousePointerService sharedInstance];
+[BKSMousePointerService new];
+[BKSMousePointerService supportsReadyToReceiveEventServiceProperty];
```

## Instance methods

```
-[BKSMousePointerService init];
-[BKSMousePointerService dealloc];
-[BKSMousePointerService _init];
-[BKSMousePointerService addPointerDeviceObserver:];
-[BKSMousePointerService normalizedGlobalPointerPosition];
-[BKSMousePointerService pointerSuppressionAssertionOnDisplay:forReason:withOptionsMask:];
-[BKSMousePointerService suppressPointerEventsForReason:];
-[BKSMousePointerService _activateServerConnection:];
-[BKSMousePointerService _locked_infoForDisplayUUID:createIfNeeded:];
-[BKSMousePointerService _locked_pointingDevicesDidChange:];
-[BKSMousePointerService _locked_reactivateConnection];
-[BKSMousePointerService _locked_sendCurrentAssertionParameters:forDisplayUUID:];
-[BKSMousePointerService _locked_serverTarget];
-[BKSMousePointerService _locked_setMousePointerDeviceObservationEnabled:];
-[BKSMousePointerService _locked_setMousePointerPreferencesObservationEnabled:];
-[BKSMousePointerService _locked_updateEventRoutesFromContext:forDisplayUUID:];
-[BKSMousePointerService _locked_updateObserver:withPointingDevices:];
-[BKSMousePointerService _locked_updateServerWithPointerDeviceObservationState];
-[BKSMousePointerService _locked_updateServerWithPreferencesObservationState];
-[BKSMousePointerService _unlocked_serverTarget];
-[BKSMousePointerService acquireButtonDownPointerRepositionAssertionForReason:contextRelativePointerPosition:onDisplay:restrictingToPID:];
-[BKSMousePointerService addPointerPreferencesObserver:];
-[BKSMousePointerService getHitTestContextsAtPoint:withAdditionalContexts:onDisplay:withCompletion:];
-[BKSMousePointerService globalDevicePreferences];
-[BKSMousePointerService globalPointerPosition];
-[BKSMousePointerService pointerGlobalDevicePreferencesDidChange:];
-[BKSMousePointerService pointingDevicesDidChange:];
-[BKSMousePointerService preferencesForDevice:];
-[BKSMousePointerService requestGlobalMouseEventsForDisplay:targetContextID:];
-[BKSMousePointerService requestGlobalMouseEventsForDisplay:targetContextID:options:];
-[BKSMousePointerService setContextRelativePointerPosition:onDisplay:withAnimationParameters:restrictingToPID:];
-[BKSMousePointerService setContextRelativePointerPosition:withInitialVelocity:onDisplay:withDecelerationRate:restrictingToPID:];
-[BKSMousePointerService setDesignatedMainDisplayUUID:];
-[BKSMousePointerService setGlobalDevicePreferences:];
-[BKSMousePointerService setGlobalPointerPosition:];
-[BKSMousePointerService setPointerPosition:onDisplay:withAnimationParameters:];
-[BKSMousePointerService setPreferences:forDevice:];
```
