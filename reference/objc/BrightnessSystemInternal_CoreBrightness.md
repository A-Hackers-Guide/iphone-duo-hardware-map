# `BrightnessSystemInternal`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSXPCListenerDelegate`
- 12 instance variables, 4 properties, 23 instance methods, 0 class methods

## Instance variables

```
@"BLControl" bl;
@? _callback;
@"NSMutableArray" _callbackProps;
f _cachedSlider;
@"NSXPCListener" _listener;
@"NSMutableDictionary" _clients;
@"NSMutableDictionary" _ownedProps;
@"NSMutableDictionary" _combinableProps;
B _checkConnections;
@? connectionCheckBlock;
@"NSObject<OS_os_log>" _logHandle;
d _initDuration;
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
-[BrightnessSystemInternal registerNotificationBlock:];
-[BrightnessSystemInternal listener:shouldAcceptNewConnection:];
-[BrightnessSystemInternal init];
-[BrightnessSystemInternal dealloc];
-[BrightnessSystemInternal copyPropertyForKey:client:handle:error:];
-[BrightnessSystemInternal registerNotificationBlock:forProperties:];
-[BrightnessSystemInternal setOwnedProperty:forKey:client:];
-[BrightnessSystemInternal adjustDictionaryToBeValidPropertyList:];
-[BrightnessSystemInternal clientConnectedWithExpObj:];
-[BrightnessSystemInternal clientDisconnectedWithExpObj:];
-[BrightnessSystemInternal copyPropertyForKey:client:];
-[BrightnessSystemInternal destroyServer];
-[BrightnessSystemInternal getDefaultPropertyValueForOwnedKey:];
-[BrightnessSystemInternal initBLControl:];
-[BrightnessSystemInternal isACombinableProperty:];
-[BrightnessSystemInternal isAlsSupported];
-[BrightnessSystemInternal newAggregatedPropertyForCombinablePropertiesForKey:];
-[BrightnessSystemInternal notifyClientsForProperty:key:origin:];
-[BrightnessSystemInternal setCombinableProperty:forKey:client:];
-[BrightnessSystemInternal setProperty:forKey:andClient:andHandle:error:];
-[BrightnessSystemInternal setProperty:forKey:client:];
-[BrightnessSystemInternal undoCombinablePropertiesForClient:];
-[BrightnessSystemInternal undoOwnedPropertiesForClient:];
```
