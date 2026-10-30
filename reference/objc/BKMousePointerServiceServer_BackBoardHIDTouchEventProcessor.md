# `BKMousePointerServiceServer`

- Image: [`/System/Library/PrivateFrameworks/BackBoardHIDTouchEventProcessor.framework/BackBoardHIDTouchEventProcessor`](../userland/System__Library__PrivateFrameworks__BackBoardHIDTouchEventProcessor.framework__BackBoardHIDTouchEventProcessor.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BKMousePointerGlobalDevicePreferencesObserver`, `BKHIDDomainServiceDelegate`, `BSInvalidatable`
- 6 instance variables, 4 properties, 31 instance methods, 0 class methods

## Instance variables

```
@"BKMousePointerController" _mousePointerController;
@"BKHIDDomainServiceServer" _server;
@"NSMutableSet" _deviceObservingConnections;
@"NSMutableSet" _preferenceObservingConnections;
@"BSServiceDispatchQueue" _bsServiceDispatchQueue;
@"NSObject<OS_dispatch_queue>" _queue;
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
-[BKMousePointerServiceServer dealloc];
-[BKMousePointerServiceServer invalidate];
-[BKMousePointerServiceServer connectionDidTerminate:];
-[BKMousePointerServiceServer normalizedGlobalPointerPosition];
-[BKMousePointerServiceServer acquireButtonDownPointerRepositionAssertionWithUniqueIdentifier:forReason:contextRelativePointerPosition:onDisplay:restrictingToPID:];
-[BKMousePointerServiceServer applyAssertionParametersOnDisplay:withOptionsMask:];
-[BKMousePointerServiceServer getHitTestContextsAtPoint:withAdditionalContexts:onDisplay:withCompletion:];
-[BKMousePointerServiceServer globalDevicePreferences];
-[BKMousePointerServiceServer globalPointerPosition];
-[BKMousePointerServiceServer invalidateButtonDownPointerRepositionAssertionWithUniqueIdentifier:onDisplay:];
-[BKMousePointerServiceServer mousePointerGlobalDevicePreferencesDidChange:];
-[BKMousePointerServiceServer pointingDevicesDidChange:];
-[BKMousePointerServiceServer preferencesForDevice:];
-[BKMousePointerServiceServer setContextRelativePointerPosition:onDisplay:withAnimationParameters:restrictingToPID:];
-[BKMousePointerServiceServer setContextRelativePointerPosition:withInitialVelocity:onDisplay:withDecelerationRate:restrictingToPID:];
-[BKMousePointerServiceServer setDesignatedMainDisplayUUID:];
-[BKMousePointerServiceServer setGlobalDevicePreferences:];
-[BKMousePointerServiceServer setGlobalPointerEventRoutes:forDisplay:];
-[BKMousePointerServiceServer setGlobalPointerPosition:];
-[BKMousePointerServiceServer setMousePointerDeviceObservationEnabled:];
-[BKMousePointerServiceServer setMousePointerPreferenceObservationEnabled:];
-[BKMousePointerServiceServer setPointerPosition:onDisplay:withAnimationParameters:];
-[BKMousePointerServiceServer setPreferences:forDevice:];
-[BKMousePointerServiceServer setSuppressAllEvents:];
-[BKMousePointerServiceServer _queue_removeConnection:];
-[BKMousePointerServiceServer connectionWillBegin:];
-[BKMousePointerServiceServer _accessStateForReason:entitlement:logEntitlementOnFailure:usingBlock:];
-[BKMousePointerServiceServer _assertModelUpdatesSuppressed:displayUUID:clientDisplayInfo:];
-[BKMousePointerServiceServer _perDisplayClientInfoForCurrentConnectionWithDisplayUUID:createIfNeeded:];
-[BKMousePointerServiceServer _pointerDevicesFromIOHIDServices:];
-[BKMousePointerServiceServer activateWithMousePointerController:];
```
