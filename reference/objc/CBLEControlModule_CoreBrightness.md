# `CBLEControlModule`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CBModule`
- Protocols: `CBContainerModuleProtocol`, `CBStatusInfoProtocol`, `CBHIDServiceProtocol`
- 1 instance variables, 5 properties, 15 instance methods, 0 class methods

## Instance variables

```
^{__Display=} _displayInternal;
```

## Properties

```
@property (T^{__Display=},R,V_displayInternal) displayInternal;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CBLEControlModule copyPropertyForKey:];
-[CBLEControlModule setProperty:forKey:];
-[CBLEControlModule handleEvent:];
-[CBLEControlModule addHIDServiceClient:];
-[CBLEControlModule copyIdentifiers];
-[CBLEControlModule removeHIDServiceClient:];
-[CBLEControlModule copyPropertyInternalForKey:];
-[CBLEControlModule stop];
-[CBLEControlModule dealloc];
-[CBLEControlModule start];
-[CBLEControlModule sendNotificationForKey:withValue:];
-[CBLEControlModule handleNotificationForKey:withProperty:];
-[CBLEControlModule displayInternal];
-[CBLEControlModule copyPropertyForKey:withParameter:];
-[CBLEControlModule initWithBacklight:queue:];
```
