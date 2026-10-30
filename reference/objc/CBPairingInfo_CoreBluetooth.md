# `CBPairingInfo`

- Image: [`/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth`](../userland/System__Library__Frameworks__CoreBluetooth.framework__CoreBluetooth.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CUXPCCodable`
- 5 instance variables, 5 properties, 13 instance methods, 0 class methods

## Instance variables

```
I _flags;
@"CBDevice" _device;
@"NSError" _error;
q _pairingType;
@"NSString" _pin;
```

## Properties

```
@property (T@"CBDevice",&,N,V_device) device;
@property (T@"NSError",C,N,V_error) error;
@property (TI,N,V_flags) flags;
@property (Tq,N,V_pairingType) pairingType;
@property (T@"NSString",C,N,V_pin) pin;
```

## Instance methods

```
-[CBPairingInfo encodeWithXPCObject:];
-[CBPairingInfo setError:];
-[CBPairingInfo initWithXPCObject:error:];
-[CBPairingInfo setDevice:];
-[CBPairingInfo setFlags:];
-[CBPairingInfo flags];
-[CBPairingInfo device];
-[CBPairingInfo error];
-[CBPairingInfo description];
-[CBPairingInfo setPairingType:];
-[CBPairingInfo pairingType];
-[CBPairingInfo pin];
-[CBPairingInfo setPin:];
```
