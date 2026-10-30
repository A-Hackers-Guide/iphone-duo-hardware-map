# `CBConnectionRSSIMonitoringData`

- Image: [`/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth`](../userland/System__Library__Frameworks__CoreBluetooth.framework__CoreBluetooth.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CUXPCCodable`
- 9 instance variables, 9 properties, 21 instance methods, 0 class methods

## Instance variables

```
c _averageRSSI;
c _maxRSSI;
C _indexRSSI;
C _channelIndex;
S _varRSSI;
S _reason;
I _spmiCMStatus;
@"NSData" _rawRSSIValues;
@"NSData" _pastRSSIValues;
```

## Properties

```
@property (TI,N,V_spmiCMStatus) spmiCMStatus;
@property (T@"NSData",C,N,V_rawRSSIValues) rawRSSIValues;
@property (Tc,N,V_averageRSSI) averageRSSI;
@property (Tc,N,V_maxRSSI) maxRSSI;
@property (TC,N,V_indexRSSI) indexRSSI;
@property (TS,N,V_varRSSI) varRSSI;
@property (TC,N,V_channelIndex) channelIndex;
@property (TS,N,V_reason) reason;
@property (T@"NSData",C,N,V_pastRSSIValues) pastRSSIValues;
```

## Instance methods

```
-[CBConnectionRSSIMonitoringData encodeWithXPCObject:];
-[CBConnectionRSSIMonitoringData initWithXPCObject:error:];
-[CBConnectionRSSIMonitoringData setReason:];
-[CBConnectionRSSIMonitoringData description];
-[CBConnectionRSSIMonitoringData reason];
-[CBConnectionRSSIMonitoringData channelIndex];
-[CBConnectionRSSIMonitoringData setChannelIndex:];
-[CBConnectionRSSIMonitoringData setAverageRSSI:];
-[CBConnectionRSSIMonitoringData varRSSI];
-[CBConnectionRSSIMonitoringData maxRSSI];
-[CBConnectionRSSIMonitoringData averageRSSI];
-[CBConnectionRSSIMonitoringData indexRSSI];
-[CBConnectionRSSIMonitoringData pastRSSIValues];
-[CBConnectionRSSIMonitoringData rawRSSIValues];
-[CBConnectionRSSIMonitoringData setIndexRSSI:];
-[CBConnectionRSSIMonitoringData setMaxRSSI:];
-[CBConnectionRSSIMonitoringData setPastRSSIValues:];
-[CBConnectionRSSIMonitoringData setRawRSSIValues:];
-[CBConnectionRSSIMonitoringData setSpmiCMStatus:];
-[CBConnectionRSSIMonitoringData setVarRSSI:];
-[CBConnectionRSSIMonitoringData spmiCMStatus];
```
