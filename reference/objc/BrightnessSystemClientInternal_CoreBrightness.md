# `BrightnessSystemClientInternal`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSCIProtocol`
- 6 instance variables, 4 properties, 18 instance methods, 0 class methods

## Instance variables

```
@"NSXPCConnection" _connection;
@"<BacklightdXPCProtocol>" _remote;
@"BrightnessSystemClientExportedObj" exportedObj;
@"NSMutableArray" _clientProperties;
@"NSObject<OS_dispatch_queue>" _serialQueue;
@"NSObject<OS_os_log>" _logHandle;
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
-[BrightnessSystemClientInternal copyPropertyForKey:];
-[BrightnessSystemClientInternal setProperty:forKey:];
-[BrightnessSystemClientInternal registerNotificationBlock:];
-[BrightnessSystemClientInternal init];
-[BrightnessSystemClientInternal dealloc];
-[BrightnessSystemClientInternal setSyncProperty:forKey:handle:error:];
-[BrightnessSystemClientInternal setSyncProperty:forKey:error:];
-[BrightnessSystemClientInternal copyPropertyForKey:handle:error:];
-[BrightnessSystemClientInternal addKeyToClientProperties:];
-[BrightnessSystemClientInternal addPropertiesForNotification:];
-[BrightnessSystemClientInternal addPropertyForNotification:];
-[BrightnessSystemClientInternal removePropertiesFromNotification:];
-[BrightnessSystemClientInternal removeKeyFromClientProperties:];
-[BrightnessSystemClientInternal registerNotificationBlock:forProperties:];
-[BrightnessSystemClientInternal removePropertyFromNotification:];
-[BrightnessSystemClientInternal copyPropertyForKey:error:];
-[BrightnessSystemClientInternal setProperty:forKey:handle:error:];
-[BrightnessSystemClientInternal stopXpcService];
```
