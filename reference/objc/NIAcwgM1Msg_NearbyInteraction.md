# `NIAcwgM1Msg`

- Image: [`/System/Library/Frameworks/NearbyInteraction.framework/NearbyInteraction`](../userland/System__Library__Frameworks__NearbyInteraction.framework__NearbyInteraction.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 6 instance variables, 6 properties, 14 instance methods, 1 class methods

## Instance variables

```
C _channelBitmask;
C _finalData2Bitmask;
S _selectedProtocolVersion;
I _uwbSessionId;
@"NSArray" _supportedUwbConfigIds;
@"NSArray" _supportedPulseShapeCombos;
```

## Properties

```
@property (T@"NSArray",R,N,V_supportedUwbConfigIds) supportedUwbConfigIds;
@property (T@"NSArray",R,N,V_supportedPulseShapeCombos) supportedPulseShapeCombos;
@property (TC,R,N,V_channelBitmask) channelBitmask;
@property (TI,R,N,V_uwbSessionId) uwbSessionId;
@property (TC,R,N,V_finalData2Bitmask) finalData2Bitmask;
@property (TS,R,N,V_selectedProtocolVersion) selectedProtocolVersion;
```

## Class methods

```
+[NIAcwgM1Msg supportsSecureCoding];
```

## Instance methods

```
-[NIAcwgM1Msg encodeWithCoder:];
-[NIAcwgM1Msg description];
-[NIAcwgM1Msg initWithCoder:];
-[NIAcwgM1Msg copyWithZone:];
-[NIAcwgM1Msg channelBitmask];
-[NIAcwgM1Msg finalData2Bitmask];
-[NIAcwgM1Msg initWithSupportedUwbConfigIds:supportedPulseShapeCombos:channelBitmask:uwbSessionId:];
-[NIAcwgM1Msg initWithSupportedUwbConfigIds:supportedPulseShapeCombos:channelBitmask:uwbSessionId:finalData2Bitmask:];
-[NIAcwgM1Msg initWithSupportedUwbConfigIds:supportedPulseShapeCombos:channelBitmask:uwbSessionId:finalData2Bitmask:selectedProtocolVersion:];
-[NIAcwgM1Msg selectedProtocolVersion];
-[NIAcwgM1Msg supportedPulseShapeCombos];
-[NIAcwgM1Msg supportedUwbConfigIds];
-[NIAcwgM1Msg toStruct];
-[NIAcwgM1Msg uwbSessionId];
```
