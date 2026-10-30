# `CBDisplayContaineriOS`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CBContainer`
- Protocols: `CBContainerProtocol`, `CBHIDServiceProtocol`, `NightShiftSupportProtocol`, `CBStatusInfoProtocol`, `CBDisplayModeProtocol`, `CBDisplayContainerProtocol`
- 35 instance variables, 10 properties, 55 instance methods, 1 class methods

## Instance variables

```
@"NSMutableArray" _relevantServices;
@"NSMutableArray" _modules;
@"NSArray" _allowlist;
@"NSUUID" _displayContainerUUID;
@"NSMutableArray" _missedProperties;
@"NSMutableArray" _missedKeys;
@"CBDisplayPreferences" _preferences;
@"CBPowerManagementModule" _cbpm;
@"<CBContainerModuleProtocol><CBDisplayModeProtocol>" _displayControlModule;
@"<CBContainerModuleProtocol><CBHIDServiceProtocol>" _autoBrightnessModule;
@"<CBContainerModuleProtocol><CBHIDServiceProtocol><NightShiftSupportProtocol>" _harmonyModule;
@"<CBContainerModuleProtocol><CBHIDServiceProtocol>" _edrControlModule;
@"<CBContainerModuleProtocol><CBDisplayModeProtocol>" _AODModule;
@"<CBContainerModuleProtocol>" _SliderCommitTelemetryModule;
@"CBDisplayContext" _context;
I _displayService;
B _running;
B _alsServiceReady;
Q _registryID;
@"NSString" _description;
@"CADisplay" _display;
@"<CBBrightnessProxy>" _brtCtl;
^{IONotificationPort=} _displayArrivalNotificationPort;
I _displayArrivalIterator;
I _displayRemovalIterator;
B _brightnessAdjustedTemporarily;
@"CBCAManager" _displayCAManager;
@"<CBSystemContext>" _systemContext;
@"NSObject<OS_dispatch_source>" _displayModeCompletionTimer;
i _type;
@"CBRingLight" _ringLight;
q _displayMode;
Q _displayID;
@"NSUUID" _displayUUID;
@"CBDisplayHandle" _handle;
```

## Properties

```
@property (T@"NSUUID",R,V_displayUUID) displayUUID;
@property (TB,R) isExternalWired;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (Tq,V_displayMode) displayMode;
@property (TQ,R,N,V_displayID) displayID;
@property (TB,R,N) builtIn;
@property (T@"CBDisplayHandle",R,V_handle) handle;
```

## Class methods

```
+[CBDisplayContaineriOS newDisplayContextWithConfig:andQueue:andSystemContext:andBrtCtl:andCBPM:andCADisplay:andRingLight:];
```

## Instance methods

```
-[CBDisplayContaineriOS setNightShiftFactorDictionary:];
-[CBDisplayContaineriOS copyPreferenceForKey:user:];
-[CBDisplayContaineriOS copyPropertyForKey:];
-[CBDisplayContaineriOS handleDisplayModeUpdate:withDuration:callback:];
-[CBDisplayContaineriOS releaseDisplayModeCompletionTimer];
-[CBDisplayContaineriOS copyStatusInfo];
-[CBDisplayContaineriOS sendNotificationForKey:andValue:];
-[CBDisplayContaineriOS setProperty:forKey:];
-[CBDisplayContaineriOS handleEvent:];
-[CBDisplayContaineriOS registerNotificationBlock:];
-[CBDisplayContaineriOS addHIDServiceClient:];
-[CBDisplayContaineriOS setPreference:forKey:user:];
-[CBDisplayContaineriOS className];
-[CBDisplayContaineriOS copyIdentifiers];
-[CBDisplayContaineriOS handleDisplayModeUpdateInternal:withDuration:callback:];
-[CBDisplayContaineriOS initCommon];
-[CBDisplayContaineriOS createAndAddSliderCommitTelemetryModule];
-[CBDisplayContaineriOS initWithCADisplay:andSystemContext:];
-[CBDisplayContaineriOS removeHIDServiceClient:];
-[CBDisplayContaineriOS isReady];
-[CBDisplayContaineriOS copyPropertyInternalForKey:];
-[CBDisplayContaineriOS handlePresetChange:];
-[CBDisplayContaineriOS setDisplayMode:];
-[CBDisplayContaineriOS setPropertyNoQueue:forKey:];
-[CBDisplayContaineriOS findAARMBLService];
-[CBDisplayContaineriOS tearDownInternalModules];
-[CBDisplayContaineriOS stop];
-[CBDisplayContaineriOS handleCBDisplayContainerStart];
-[CBDisplayContaineriOS displayUUID];
-[CBDisplayContaineriOS dealloc];
-[CBDisplayContaineriOS displayMode];
-[CBDisplayContaineriOS scheduleDisplayModeCompletionTimerIn:withCallback:];
-[CBDisplayContaineriOS start];
-[CBDisplayContaineriOS matchDisplayWithHidService:];
-[CBDisplayContaineriOS findBacklight];
-[CBDisplayContaineriOS displayID];
-[CBDisplayContaineriOS initWithCBBrtControl:andSystemContext:];
-[CBDisplayContaineriOS handleCBBrtCtlDisplayContainerStart];
-[CBDisplayContaineriOS handleDisplayArrival:];
-[CBDisplayContaineriOS isExternalWired];
-[CBDisplayContaineriOS setBrightnessTo:];
-[CBDisplayContaineriOS setupInternalModulesCommon];
-[CBDisplayContaineriOS handle];
-[CBDisplayContaineriOS revertTemporaryBrightnessAdjustment];
-[CBDisplayContaineriOS handleNotificationForKey:withProperty:from:];
-[CBDisplayContaineriOS description];
-[CBDisplayContaineriOS initializeRingLight:];
-[CBDisplayContaineriOS preferencesKey];
-[CBDisplayContaineriOS initialiseHIDDisplay];
-[CBDisplayContaineriOS builtIn];
-[CBDisplayContaineriOS setupInternalBrtCtlModules];
-[CBDisplayContaineriOS setDisplayFactor:withDuration:];
-[CBDisplayContaineriOS setupInternalModules];
-[CBDisplayContaineriOS toggleAutobrightnessTo:];
-[CBDisplayContaineriOS unregisterNotificationBlock];
```
