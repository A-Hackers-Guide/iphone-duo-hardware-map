# `WFGasQueryProxy`

- Image: [`/System/Library/PrivateFrameworks/WiFiKit.framework/WiFiKit`](../userland/System__Library__PrivateFrameworks__WiFiKit.framework__WiFiKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `WFWiFiGasProxy`
- 2 instance variables, 6 properties, 6 instance methods, 0 class methods

## Instance variables

```
^{__WiFiDeviceClient=} _device;
@? _handler;
```

## Properties

```
@property (T@?,C,N,V_handler) handler;
@property (T^{__WiFiDeviceClient=},N,V_device) device;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[WFGasQueryProxy setDevice:];
-[WFGasQueryProxy device];
-[WFGasQueryProxy setHandler:];
-[WFGasQueryProxy handler];
-[WFGasQueryProxy _processGasResults:error:];
-[WFGasQueryProxy gasQueryForRecords:request:handler:];
```
