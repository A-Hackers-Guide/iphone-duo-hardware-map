# `CBAudioLinkQualityInfo`

- Image: [`/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth`](../userland/System__Library__Frameworks__CoreBluetooth.framework__CoreBluetooth.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CUXPCCodable`, `NSSecureCoding`
- 10 instance variables, 10 properties, 29 instance methods, 1 class methods

## Instance variables

```
C _aosState;
C _btBand;
c _codecType;
c _noiseFloor90;
c _rssiAverage;
c _signalToNoiseRatio;
I _bitRate;
@"NSString" _deviceName;
d _jitterBufferSeconds;
d _retransmitRate;
```

## Properties

```
@property (TC,N,V_aosState) aosState;
@property (TI,N,V_bitRate) bitRate;
@property (TC,N,V_btBand) btBand;
@property (Tc,N,V_codecType) codecType;
@property (T@"NSString",C,N,V_deviceName) deviceName;
@property (Td,N,V_jitterBufferSeconds) jitterBufferSeconds;
@property (Tc,N,V_noiseFloor90) noiseFloor90;
@property (Td,N,V_retransmitRate) retransmitRate;
@property (Tc,N,V_rssiAverage) rssiAverage;
@property (Tc,N,V_signalToNoiseRatio) signalToNoiseRatio;
```

## Class methods

```
+[CBAudioLinkQualityInfo supportsSecureCoding];
```

## Instance methods

```
-[CBAudioLinkQualityInfo encodeWithXPCObject:];
-[CBAudioLinkQualityInfo initWithDictionary:error:];
-[CBAudioLinkQualityInfo initWithXPCObject:error:];
-[CBAudioLinkQualityInfo descriptionWithLevel:];
-[CBAudioLinkQualityInfo setCodecType:];
-[CBAudioLinkQualityInfo setDeviceName:];
-[CBAudioLinkQualityInfo encodeWithCoder:];
-[CBAudioLinkQualityInfo description];
-[CBAudioLinkQualityInfo initWithCoder:];
-[CBAudioLinkQualityInfo isEqual:];
-[CBAudioLinkQualityInfo codecType];
-[CBAudioLinkQualityInfo deviceName];
-[CBAudioLinkQualityInfo dictionaryRepresentation];
-[CBAudioLinkQualityInfo bitRate];
-[CBAudioLinkQualityInfo setBitRate:];
-[CBAudioLinkQualityInfo setSignalToNoiseRatio:];
-[CBAudioLinkQualityInfo signalToNoiseRatio];
-[CBAudioLinkQualityInfo setRssiAverage:];
-[CBAudioLinkQualityInfo aosState];
-[CBAudioLinkQualityInfo btBand];
-[CBAudioLinkQualityInfo jitterBufferSeconds];
-[CBAudioLinkQualityInfo noiseFloor90];
-[CBAudioLinkQualityInfo retransmitRate];
-[CBAudioLinkQualityInfo rssiAverage];
-[CBAudioLinkQualityInfo setAosState:];
-[CBAudioLinkQualityInfo setBtBand:];
-[CBAudioLinkQualityInfo setJitterBufferSeconds:];
-[CBAudioLinkQualityInfo setNoiseFloor90:];
-[CBAudioLinkQualityInfo setRetransmitRate:];
```
