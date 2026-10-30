# `CBABModuleiOS`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CBModule`
- Protocols: `CBHIDServiceProtocol`, `CBContainerModuleProtocol`, `CBStatusInfoProtocol`, `CBAODProtocol`
- 9 instance variables, 4 properties, 20 instance methods, 0 class methods

## Instance variables

```
^v _AABC;
@"CBDisplayModuleiOS" _display;
@"CBDisplayContext" _context;
@"AABRear" _AABRear;
@"NSMutableArray" _alsServiceClients;
@"NSMutableArray" _otherServiceClients;
@"CBALSTelemetry" _alsTelemetry;
@"<CBAdaptiveAutoBrightnessSettingsProvider>" _settingsProvider;
@"CBBOLTSProvider" _boltsProvider;
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
-[CBABModuleiOS copyPropertyForKey:];
-[CBABModuleiOS setupAABRear];
-[CBABModuleiOS setProperty:forKey:];
-[CBABModuleiOS handleEvent:];
-[CBABModuleiOS addHIDServiceClient:];
-[CBABModuleiOS className];
-[CBABModuleiOS copyIdentifiers];
-[CBABModuleiOS removeHIDServiceClient:];
-[CBABModuleiOS copyPropertyInternalForKey:];
-[CBABModuleiOS observeValueForKeyPath:ofObject:change:context:];
-[CBABModuleiOS stop];
-[CBABModuleiOS dealloc];
-[CBABModuleiOS start];
-[CBABModuleiOS sendNotificationForKey:withValue:];
-[CBABModuleiOS handleNotificationForKey:withProperty:];
-[CBABModuleiOS handleAODStateUpdate:transitionTime:context:];
-[CBABModuleiOS copyPropertyForKey:withParameter:];
-[CBABModuleiOS handleAODConfigurationUpdateWithContext:];
-[CBABModuleiOS initWithDisplayModule:andContext:];
-[CBABModuleiOS updateCurveStrategy:withSettingsProvider:];
```
