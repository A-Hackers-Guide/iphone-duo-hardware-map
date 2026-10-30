# `BLControl`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BacklightControl`
- Protocols: `SWSystemSleepObserver`, `CBDisplayManagerNotificationObserver`
- 30 instance variables, 4 properties, 52 instance methods, 0 class methods

## Instance variables

```
^{__IOHIDEventSystemClient=} _hidSystemClient;
@"ALSManager" _ALSManager;
@"<ALSClientProtocol>" _ALSClient;
@"NSObject<OS_dispatch_workloop>" _workloop;
B _ignoreBrightnessKey;
B _overrideIgnoreBrightness;
B _ignoreALSEvents;
^v _callbackContext;
B _useMultiCurves;
Q _hidServiceMatchingMask;
i _ecoModePreferencesUpdateNotificationToken;
@? _ecoModePreferencesUpdateNotificationHandler;
@"NSMutableArray" _hidServiceClients;
@"NSMutableSet" _alsNodes;
@"NSObject<OS_os_log>" _logHandle;
@"<CBPrimitiveConfigurationProvider>" _cbConfig;
@"NightModeControl" _nightModeControl;
@"CBDisplayModeOneOf" _displayModeOneOf;
@"NSMutableDictionary" _keyboardContainers;
@"HIDManager" _keyboardBacklightHIDManager;
@"CBCMAngleService" _angleService;
@"CBDisplayTransitionPolicy" _transitionPolicy;
Q _userActiveNotificationHandle;
@"SWSystemSleepMonitor" _systemSleepMonitor;
@"CBSystemContext" _systemContext;
@"CBLowPowerMode" _lpm;
@"CBDisplayManager" _displayManager;
@"CBBrightnessBroadcaster" _brightnessBroadcaster;
@"CBDisplayStatusBroadcaster" _displayStatusBroadcaster;
@"CBLEManager" _LEManager;
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
-[BLControl sendNotificationWithKeyboardIDs];
-[BLControl systemSleepMonitorDidWakeFromSleep:];
-[BLControl handleEvent:from:];
-[BLControl copyPropertyInternalWithKey:forClient:];
-[BLControl sendNotificationFor:withValue:andOrigin:];
-[BLControl useSyncBrightnessTransactionForDisplay:];
-[BLControl copyDisplayInfo];
-[BLControl newDevicePairMatchingDictionaryWithPage:andUsage:];
-[BLControl initKeyboardBacklightHIDManager];
-[BLControl findDisplays];
-[BLControl setupAABRear];
-[BLControl newGlobalConfigProvider];
-[BLControl handleCADisplay:];
-[BLControl handleUsefulEvent:];
-[BLControl systemSleepMonitor:prepareForSleepWithCompletion:];
-[BLControl copyStatusInfo];
-[BLControl startHIDSystemClient];
-[BLControl cancelHIDSystemClient];
-[BLControl setPropertyWithKey:property:client:];
-[BLControl setBLControlPropertyWithKey:property:];
-[BLControl addHIDServiceClient:];
-[BLControl keyboardBacklightHIDDeviceRemoved:];
-[BLControl waitForALSArrival];
-[BLControl copyDisplayList];
-[BLControl stopDisplayLookup];
-[BLControl handleCloningChange:];
-[BLControl handleCAWindowServerDisplay:];
-[BLControl copyBLControlPropertyWithkey:];
-[BLControl handleCADisplayRemoval:];
-[BLControl handleNotificationInternalForKey:withValue:];
-[BLControl removeDisplayContainer:];
-[BLControl removeHIDServiceClient:];
-[BLControl handleExternalDisplayChange];
-[BLControl handleUserIsActiveStateChange:];
-[BLControl hidServiceArrival:];
-[BLControl handlePresetChange];
-[BLControl handleCADisplayArrival:];
-[BLControl setPropertyInternalWithKey:property:client:];
-[BLControl observeValueForKeyPath:ofObject:change:context:];
-[BLControl init];
-[BLControl stop];
-[BLControl removeHIDService:];
-[BLControl dealloc];
-[BLControl copyPropertyForKey:client:handle:error:];
-[BLControl start];
-[BLControl setProperty:forKey:andHandle:error:];
-[BLControl systemSleepMonitorWillWakeFromSleep:];
-[BLControl getNightModeControl];
-[BLControl addDisplayContainer:];
-[BLControl sendNotificationForKey:value:origin:];
-[BLControl keyboardBacklightHIDDeviceArrived:];
-[BLControl copyPropertyWithKey:client:];
```
