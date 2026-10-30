# `BCHIDBrtControl`

- Image: [`/System/Library/PrivateFrameworks/BrightnessControl.framework/BrightnessControl`](../userland/System__Library__PrivateFrameworks__BrightnessControl.framework__BrightnessControl.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BCBrtControl`
- 13 instance variables, 1 properties, 17 instance methods, 2 class methods

## Instance variables

```
I _hidBrightnessService;
@"HIDDevice" _hidBrightnessDevice;
@"HIDElement" _brightnessElement;
@"HIDElement" _brightnessFadeElement;
f _nitsScaler;
d _nits;
f _brightnessUpdateTarget;
Q _brighntessUpdateCounter;
@"NSObject<OS_dispatch_queue>" _brightnessUpdateQueue;
^{IONotificationPort=} _boostFactorNotificationPort;
I _boostFactorNotification;
f _nitsBoostFactor;
Q _registryID;
```

## Properties

```
@property (TQ,R,V_registryID) registryID;
```

## Class methods

```
+[BCHIDBrtControl copyAvailableControls];
+[BCHIDBrtControl newMonitorWithHandler:error:];
```

## Instance methods

```
-[BCHIDBrtControl init];
-[BCHIDBrtControl dealloc];
-[BCHIDBrtControl copyProperty:error:];
-[BCHIDBrtControl registryID];
-[BCHIDBrtControl initWithService:];
-[BCHIDBrtControl setBoostFactor:];
-[BCHIDBrtControl _getDeviceNits:];
-[BCHIDBrtControl _setDeviceNits:];
-[BCHIDBrtControl addDisplayService:];
-[BCHIDBrtControl boostFactorFromIOFixed:];
-[BCHIDBrtControl copyModuleIdentifier];
-[BCHIDBrtControl getNitsWithError:];
-[BCHIDBrtControl refreshBoostFactor];
-[BCHIDBrtControl removeDisplayService];
-[BCHIDBrtControl setDisplayService:];
-[BCHIDBrtControl setNits:error:];
-[BCHIDBrtControl setProperty:value:error:];
```
