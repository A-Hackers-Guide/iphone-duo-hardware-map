# `BKSMousePointerServiceClientToServerInterface` (protocol)

- Image: [`/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`](../userland/System__Library__PrivateFrameworks__BackBoardServices.framework__BackBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 0 properties, 19 instance methods, 0 class methods

## Instance methods

```
-[BKSMousePointerServiceClientToServerInterface normalizedGlobalPointerPosition];
-[BKSMousePointerServiceClientToServerInterface acquireButtonDownPointerRepositionAssertionWithUniqueIdentifier:forReason:contextRelativePointerPosition:onDisplay:restrictingToPID:];
-[BKSMousePointerServiceClientToServerInterface applyAssertionParametersOnDisplay:withOptionsMask:];
-[BKSMousePointerServiceClientToServerInterface getHitTestContextsAtPoint:withAdditionalContexts:onDisplay:withCompletion:];
-[BKSMousePointerServiceClientToServerInterface globalDevicePreferences];
-[BKSMousePointerServiceClientToServerInterface globalPointerPosition];
-[BKSMousePointerServiceClientToServerInterface invalidateButtonDownPointerRepositionAssertionWithUniqueIdentifier:onDisplay:];
-[BKSMousePointerServiceClientToServerInterface preferencesForDevice:];
-[BKSMousePointerServiceClientToServerInterface setContextRelativePointerPosition:onDisplay:withAnimationParameters:restrictingToPID:];
-[BKSMousePointerServiceClientToServerInterface setContextRelativePointerPosition:withInitialVelocity:onDisplay:withDecelerationRate:restrictingToPID:];
-[BKSMousePointerServiceClientToServerInterface setDesignatedMainDisplayUUID:];
-[BKSMousePointerServiceClientToServerInterface setGlobalDevicePreferences:];
-[BKSMousePointerServiceClientToServerInterface setGlobalPointerEventRoutes:forDisplay:];
-[BKSMousePointerServiceClientToServerInterface setGlobalPointerPosition:];
-[BKSMousePointerServiceClientToServerInterface setMousePointerDeviceObservationEnabled:];
-[BKSMousePointerServiceClientToServerInterface setMousePointerPreferenceObservationEnabled:];
-[BKSMousePointerServiceClientToServerInterface setPointerPosition:onDisplay:withAnimationParameters:];
-[BKSMousePointerServiceClientToServerInterface setPreferences:forDevice:];
-[BKSMousePointerServiceClientToServerInterface setSuppressAllEvents:];
```
