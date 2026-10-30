# `CBLEAutoBrightnessModule`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CBModule`
- Protocols: `CBHIDServiceProtocol`, `CBContainerModuleProtocol`, `CBStatusInfoProtocol`
- 5 instance variables, 4 properties, 14 instance methods, 0 class methods

## Instance variables

```
^v _AABC;
@"CBLEControlModule" _controlModule;
@"NSMutableArray" _alsServiceClients;
@"NSMutableArray" _otherServiceClients;
@"CBALSTelemetry" _alsTelemetry;
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
-[CBLEAutoBrightnessModule copyPropertyForKey:];
-[CBLEAutoBrightnessModule setProperty:forKey:];
-[CBLEAutoBrightnessModule handleEvent:];
-[CBLEAutoBrightnessModule addHIDServiceClient:];
-[CBLEAutoBrightnessModule copyIdentifiers];
-[CBLEAutoBrightnessModule removeHIDServiceClient:];
-[CBLEAutoBrightnessModule copyPropertyInternalForKey:];
-[CBLEAutoBrightnessModule stop];
-[CBLEAutoBrightnessModule dealloc];
-[CBLEAutoBrightnessModule start];
-[CBLEAutoBrightnessModule sendNotificationForKey:withValue:];
-[CBLEAutoBrightnessModule handleNotificationForKey:withProperty:];
-[CBLEAutoBrightnessModule copyPropertyForKey:withParameter:];
-[CBLEAutoBrightnessModule initWithControlModule:andQueue:];
```
