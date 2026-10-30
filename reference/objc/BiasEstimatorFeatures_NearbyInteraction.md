# `BiasEstimatorFeatures`

- Image: [`/System/Library/Frameworks/NearbyInteraction.framework/NearbyInteraction`](../userland/System__Library__Frameworks__NearbyInteraction.framework__NearbyInteraction.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 21 instance variables, 21 properties, 50 instance methods, 1 class methods

## Instance variables

```
i _antennaMask;
i _rxAntennaPacket1;
i _rxAntennaPacket2;
d _timestamp;
d _uwbTime;
d _tofPicSecond;
d _rssiDbm;
d _soiRssiDbm;
d _toaNoiseRms;
d _toaPpwinRms;
d _toaPpwinPeak;
d _rttInitiator;
d _tatInitiator;
d _rttResponder;
d _tatResponder;
@"NSArray" _cirPacket1;
d _leadingEdgePacket1;
d _firstPathIndexPacket1;
@"NSArray" _cirPacket2;
d _leadingEdgePacket2;
d _firstPathIndexPacket2;
```

## Properties

```
@property (Ti,N,V_antennaMask) antennaMask;
@property (Td,N,V_timestamp) timestamp;
@property (Td,N,V_uwbTime) uwbTime;
@property (Td,N,V_tofPicSecond) tofPicSecond;
@property (Td,N,V_rssiDbm) rssiDbm;
@property (Td,N,V_soiRssiDbm) soiRssiDbm;
@property (Td,N,V_toaNoiseRms) toaNoiseRms;
@property (Td,N,V_toaPpwinRms) toaPpwinRms;
@property (Td,N,V_toaPpwinPeak) toaPpwinPeak;
@property (Td,N,V_rttInitiator) rttInitiator;
@property (Td,N,V_tatInitiator) tatInitiator;
@property (Td,N,V_rttResponder) rttResponder;
@property (Td,N,V_tatResponder) tatResponder;
@property (T@"NSArray",C,N,V_cirPacket1) cirPacket1;
@property (Td,N,V_leadingEdgePacket1) leadingEdgePacket1;
@property (Td,N,V_firstPathIndexPacket1) firstPathIndexPacket1;
@property (Ti,N,V_rxAntennaPacket1) rxAntennaPacket1;
@property (T@"NSArray",C,N,V_cirPacket2) cirPacket2;
@property (Td,N,V_leadingEdgePacket2) leadingEdgePacket2;
@property (Td,N,V_firstPathIndexPacket2) firstPathIndexPacket2;
@property (Ti,N,V_rxAntennaPacket2) rxAntennaPacket2;
```

## Class methods

```
+[BiasEstimatorFeatures supportsSecureCoding];
```

## Instance methods

```
-[BiasEstimatorFeatures setTimestamp:];
-[BiasEstimatorFeatures timestamp];
-[BiasEstimatorFeatures encodeWithCoder:];
-[BiasEstimatorFeatures hash];
-[BiasEstimatorFeatures description];
-[BiasEstimatorFeatures initWithCoder:];
-[BiasEstimatorFeatures copyWithZone:];
-[BiasEstimatorFeatures isEqual:];
-[BiasEstimatorFeatures setToaNoiseRms:];
-[BiasEstimatorFeatures rssiDbm];
-[BiasEstimatorFeatures setAntennaMask:];
-[BiasEstimatorFeatures setToaPpwinRms:];
-[BiasEstimatorFeatures uwbTime];
-[BiasEstimatorFeatures antennaMask];
-[BiasEstimatorFeatures cirPacket1];
-[BiasEstimatorFeatures cirPacket2];
-[BiasEstimatorFeatures firstPathIndexPacket1];
-[BiasEstimatorFeatures firstPathIndexPacket2];
-[BiasEstimatorFeatures initWithBiasEstimatorFeatures:];
-[BiasEstimatorFeatures leadingEdgePacket1];
-[BiasEstimatorFeatures leadingEdgePacket2];
-[BiasEstimatorFeatures populateOrderedInputFeature];
-[BiasEstimatorFeatures rttInitiator];
-[BiasEstimatorFeatures rttResponder];
-[BiasEstimatorFeatures rxAntennaPacket1];
-[BiasEstimatorFeatures rxAntennaPacket2];
-[BiasEstimatorFeatures setCirPacket1:];
-[BiasEstimatorFeatures setCirPacket2:];
-[BiasEstimatorFeatures setFirstPathIndexPacket1:];
-[BiasEstimatorFeatures setFirstPathIndexPacket2:];
-[BiasEstimatorFeatures setLeadingEdgePacket1:];
-[BiasEstimatorFeatures setLeadingEdgePacket2:];
-[BiasEstimatorFeatures setRssiDbm:];
-[BiasEstimatorFeatures setRttInitiator:];
-[BiasEstimatorFeatures setRttResponder:];
-[BiasEstimatorFeatures setRxAntennaPacket1:];
-[BiasEstimatorFeatures setRxAntennaPacket2:];
-[BiasEstimatorFeatures setSoiRssiDbm:];
-[BiasEstimatorFeatures setTatInitiator:];
-[BiasEstimatorFeatures setTatResponder:];
-[BiasEstimatorFeatures setToaPpwinPeak:];
-[BiasEstimatorFeatures setTofPicSecond:];
-[BiasEstimatorFeatures setUwbTime:];
-[BiasEstimatorFeatures soiRssiDbm];
-[BiasEstimatorFeatures tatInitiator];
-[BiasEstimatorFeatures tatResponder];
-[BiasEstimatorFeatures toaNoiseRms];
-[BiasEstimatorFeatures toaPpwinPeak];
-[BiasEstimatorFeatures toaPpwinRms];
-[BiasEstimatorFeatures tofPicSecond];
```
