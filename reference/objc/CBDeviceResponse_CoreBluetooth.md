# `CBDeviceResponse`

- Image: [`/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth`](../userland/System__Library__Frameworks__CoreBluetooth.framework__CoreBluetooth.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CUXPCCodable`
- 10 instance variables, 10 properties, 24 instance methods, 0 class methods

## Instance variables

```
C _btBand;
c _core0TargetPower;
c _core1TargetPower;
c _currentPCAP;
c _rssi;
c _txPower;
c _txPowerMax;
S _connectionHandle;
I _sniffInterval;
@"NSString" _identifier;
```

## Properties

```
@property (TC,N,V_btBand) btBand;
@property (TS,N,V_connectionHandle) connectionHandle;
@property (Tc,N,V_core0TargetPower) core0TargetPower;
@property (Tc,N,V_core1TargetPower) core1TargetPower;
@property (Tc,N,V_currentPCAP) currentPCAP;
@property (T@"NSString",C,N,V_identifier) identifier;
@property (Tc,N,V_rssi) rssi;
@property (TI,N,V_sniffInterval) sniffInterval;
@property (Tc,N,V_txPower) txPower;
@property (Tc,N,V_txPowerMax) txPowerMax;
```

## Instance methods

```
-[CBDeviceResponse rssi];
-[CBDeviceResponse encodeWithXPCObject:];
-[CBDeviceResponse txPower];
-[CBDeviceResponse initWithXPCObject:error:];
-[CBDeviceResponse descriptionWithLevel:];
-[CBDeviceResponse identifier];
-[CBDeviceResponse setRssi:];
-[CBDeviceResponse setIdentifier:];
-[CBDeviceResponse description];
-[CBDeviceResponse setTxPower:];
-[CBDeviceResponse setCurrentPCAP:];
-[CBDeviceResponse btBand];
-[CBDeviceResponse connectionHandle];
-[CBDeviceResponse core0TargetPower];
-[CBDeviceResponse core1TargetPower];
-[CBDeviceResponse currentPCAP];
-[CBDeviceResponse setBtBand:];
-[CBDeviceResponse setConnectionHandle:];
-[CBDeviceResponse setCore0TargetPower:];
-[CBDeviceResponse setCore1TargetPower:];
-[CBDeviceResponse setSniffInterval:];
-[CBDeviceResponse setTxPowerMax:];
-[CBDeviceResponse sniffInterval];
-[CBDeviceResponse txPowerMax];
```
