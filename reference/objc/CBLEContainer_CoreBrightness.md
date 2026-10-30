# `CBLEContainer`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CBContainer`
- Protocols: `CBLEContainerProtocol`, `CBHIDServiceProtocol`
- 10 instance variables, 6 properties, 22 instance methods, 2 class methods

## Instance variables

```
@"NSMutableArray" _relevantServices;
@"NSMutableArray<CBContainerModuleProtocol><CBHIDServiceProtocol>" _modules;
@"CBLEControlModule" _brightnessModule;
@"CBLEAutoBrightnessModule" _autoBrightnessModule;
I _backlightService;
Q _registryID;
B _running;
B _alsServiceReady;
@"<CBSystemContext>" _systemContext;
Q _type;
```

## Properties

```
@property (TQ,R,GgetType,V_type) type;
@property (TQ,R,GgetBacklightServiceID) backlightServiceID;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CBLEContainer copyBacklightMatchingDictionary];
+[CBLEContainer isValidBacklightService:];
```

## Instance methods

```
-[CBLEContainer copyPropertyForKey:];
-[CBLEContainer copyStatusInfo];
-[CBLEContainer sendNotificationForKey:andValue:];
-[CBLEContainer setProperty:forKey:];
-[CBLEContainer handleEvent:];
-[CBLEContainer registerNotificationBlock:];
-[CBLEContainer addHIDServiceClient:];
-[CBLEContainer copyIdentifiers];
-[CBLEContainer removeHIDServiceClient:];
-[CBLEContainer copyPropertyInternalForKey:];
-[CBLEContainer _setProperty:forKey:];
-[CBLEContainer stop];
-[CBLEContainer dealloc];
-[CBLEContainer start];
-[CBLEContainer getType];
-[CBLEContainer handleNotificationForKey:withProperty:from:];
-[CBLEContainer unregisterNotificationBlock];
-[CBLEContainer _initializeType];
-[CBLEContainer _initializeInternalModules];
-[CBLEContainer _teardownInternalModules];
-[CBLEContainer getBacklightServiceID];
-[CBLEContainer initWithBacklightService:andSystemContext:];
```
