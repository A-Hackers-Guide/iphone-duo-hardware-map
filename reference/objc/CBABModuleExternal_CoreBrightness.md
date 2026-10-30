# `CBABModuleExternal`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CBModule`
- Protocols: `CBContainerModuleProtocol`, `CBHIDServiceProtocol`
- 14 instance variables, 5 properties, 24 instance methods, 0 class methods

## Instance variables

```
@"NSMutableArray" _ALSServices;
@"NSString" _containerID;
@"NSString" _uniqueID;
@"NSString" _displayUUID;
B _enabled;
B _available;
B _presetDisableAB;
@"CBABCurve" _curve;
@"CBABRamp" _ramp;
B _updatesFrozen;
B _suspendAutoBrightness;
B _fastRamp;
B _builtIn;
@"CBDisplayModule" _displayModule;
```

## Properties

```
@property (T@"CBDisplayModule",R,V_displayModule) displayModule;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CBABModuleExternal copyPropertyForKey:];
-[CBABModuleExternal setProperty:forKey:];
-[CBABModuleExternal handleEvent:];
-[CBABModuleExternal addHIDServiceClient:];
-[CBABModuleExternal removeHIDServiceClient:];
-[CBABModuleExternal stop];
-[CBABModuleExternal dealloc];
-[CBABModuleExternal start];
-[CBABModuleExternal sendNotificationForKey:withValue:];
-[CBABModuleExternal setPropertyInternal:forKey:];
-[CBABModuleExternal handleNotificationForKey:withProperty:];
-[CBABModuleExternal updateAvailability];
-[CBABModuleExternal copyPropertyForKey:withParameter:];
-[CBABModuleExternal initWithDisplayModule:andQueue:];
-[CBABModuleExternal displayModule];
-[CBABModuleExternal endFastRamp];
-[CBABModuleExternal getAggregatedLux:];
-[CBABModuleExternal newALSService:];
-[CBABModuleExternal storeCurveToPreferences];
-[CBABModuleExternal updateAutoBrightnessState:];
-[CBABModuleExternal updateBrightness];
-[CBABModuleExternal updateBrightnessForce:periodOverride:period:];
-[CBABModuleExternal userBrightnessChangingHandler];
-[CBABModuleExternal userBrightnessCommitHandler];
```
