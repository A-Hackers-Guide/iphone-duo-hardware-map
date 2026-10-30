# `BTAudioRoutingResponse`

- Image: [`/System/Library/PrivateFrameworks/BluetoothServices.framework/BluetoothServices`](../userland/System__Library__PrivateFrameworks__BluetoothServices.framework__BluetoothServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 6 instance variables, 6 properties, 15 instance methods, 1 class methods

## Instance variables

```
i _action;
I _clientID;
@"NSString" _deviceAddress;
@"NSDictionary" _wxInfo;
@"NSError" _error;
@"NSString" _reason;
```

## Properties

```
@property (Ti,N,V_action) action;
@property (TI,N,V_clientID) clientID;
@property (T@"NSString",C,N,V_deviceAddress) deviceAddress;
@property (T@"NSError",C,N,V_error) error;
@property (T@"NSString",C,N,V_reason) reason;
@property (T@"NSDictionary",C,N,V_wxInfo) wxInfo;
```

## Class methods

```
+[BTAudioRoutingResponse supportsSecureCoding];
```

## Instance methods

```
-[BTAudioRoutingResponse clientID];
-[BTAudioRoutingResponse setError:];
-[BTAudioRoutingResponse setClientID:];
-[BTAudioRoutingResponse setAction:];
-[BTAudioRoutingResponse action];
-[BTAudioRoutingResponse setReason:];
-[BTAudioRoutingResponse error];
-[BTAudioRoutingResponse encodeWithCoder:];
-[BTAudioRoutingResponse description];
-[BTAudioRoutingResponse initWithCoder:];
-[BTAudioRoutingResponse reason];
-[BTAudioRoutingResponse deviceAddress];
-[BTAudioRoutingResponse setDeviceAddress:];
-[BTAudioRoutingResponse wxInfo];
-[BTAudioRoutingResponse setWxInfo:];
```
