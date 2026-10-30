# `CMSuppressionManagerInternal`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 28 instance variables, 0 properties, 3 instance methods, 0 class methods

## Instance variables

```
{CMSuppressionEventStruct="timestamp"d"type"q"reason"Q"facedownState"Q"timeSinceLastFacedownStatic"d} fCurrentSuppressionEvent;
@? fSuppressionEventHandler;
@"NSOperationQueue" fSuppressionEventQueue;
@"NSObject<OS_dispatch_queue>" fInputQueue;
{CMSuppressionEventStruct="timestamp"d"type"q"reason"Q"facedownState"Q"timeSinceLastFacedownStatic"d} fViewObstructedEvent;
^{Dispatcher=^^?@} fSuppressionEventDispatcher;
{CMSuppressionEventStruct="timestamp"d"type"q"reason"Q"facedownState"Q"timeSinceLastFacedownStatic"d} fSmartPowerNapEvent;
{CMSuppressionEventStruct="timestamp"d"type"q"reason"Q"facedownState"Q"timeSinceLastFacedownStatic"d} fDevicePresenceEvent;
{CMSuppressionEventStruct="timestamp"d"type"q"reason"Q"facedownState"Q"timeSinceLastFacedownStatic"d} fDeviceStateEvent;
@"CMDeviceStateManager" fDeviceStateManager;
@"NSOperationQueue" fDeviceStateQueue;
B fAllowSuppressionForConfigTypeDefault;
@"_PMSmartPowerNap" fSmartPowerNap;
@"DPCManager" fDevicePresence;
^v fConnection;
@"NSObject<OS_dispatch_queue>" fConnectionQueue;
B fServiceEnabled;
B fUpdatesRequested;
B fViewObstructedDebugEnabled;
@? fViewObstructedStateHandler;
{ViewObstructedState="fType"C"fSuppress"{Suppress="fType"C"fShouldSuppress"B"fAPAwake"B"fCurrentState"C"fOrientation"C"fMotionType"C"fLux"f"fPocketProbability"f"fFacedownStatic"B"fTimeSinceLastFacedownStatic"f}"fMeanProbabilities"[8f]} fViewObstructedState;
^{Dispatcher=^^?@} fViewObstructedStateDispatcher;
@"NSOperationQueue" fCameraCapturePoseQueue;
@? fCameraCapturePoseHandler;
^{Dispatcher=^^?@} fCameraCapturePoseDispatcher;
Q fSuppressionSources;
@"NSString" fClientID;
q fConfigType;
```

## Instance methods

```
-[CMSuppressionManagerInternal init];
-[CMSuppressionManagerInternal dealloc];
-[CMSuppressionManagerInternal teardownPrivate];
```
