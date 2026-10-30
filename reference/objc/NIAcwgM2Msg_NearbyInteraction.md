# `NIAcwgM2Msg`

- Image: [`/System/Library/Frameworks/NearbyInteraction.framework/NearbyInteraction`](../userland/System__Library__Frameworks__NearbyInteraction.framework__NearbyInteraction.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 8 instance variables, 8 properties, 15 instance methods, 2 class methods

## Instance variables

```
C _selectedPulseShapeCombo;
C _selectedChannelBitmask;
C _minRanMultiplier;
C _supportedSlotBitmask;
C _supportedHoppingConfigBitmask;
C _selectedFinalData2Bitmask;
S _selectedUwbConfigId;
I _supportedSyncCodeIndexBitmask;
```

## Properties

```
@property (TS,R,N,V_selectedUwbConfigId) selectedUwbConfigId;
@property (TC,R,N,V_selectedPulseShapeCombo) selectedPulseShapeCombo;
@property (TC,R,N,V_selectedChannelBitmask) selectedChannelBitmask;
@property (TI,R,N,V_supportedSyncCodeIndexBitmask) supportedSyncCodeIndexBitmask;
@property (TC,R,N,V_minRanMultiplier) minRanMultiplier;
@property (TC,R,N,V_supportedSlotBitmask) supportedSlotBitmask;
@property (TC,R,N,V_supportedHoppingConfigBitmask) supportedHoppingConfigBitmask;
@property (TC,R,N,V_selectedFinalData2Bitmask) selectedFinalData2Bitmask;
```

## Class methods

```
+[NIAcwgM2Msg supportsSecureCoding];
+[NIAcwgM2Msg fromStruct:];
```

## Instance methods

```
-[NIAcwgM2Msg encodeWithCoder:];
-[NIAcwgM2Msg description];
-[NIAcwgM2Msg initWithCoder:];
-[NIAcwgM2Msg copyWithZone:];
-[NIAcwgM2Msg initWithSelectedUwbConfigId:selectedPulseShapeCombo:selectedChannelBitmask:supportedSyncCodeIndexBitmask:minRanMultiplier:supportedSlotBitmask:supportedHoppingConfigBitmask:];
-[NIAcwgM2Msg initWithSelectedUwbConfigId:selectedPulseShapeCombo:selectedChannelBitmask:supportedSyncCodeIndexBitmask:minRanMultiplier:supportedSlotBitmask:supportedHoppingConfigBitmask:selectedFinalData2Bitmask:];
-[NIAcwgM2Msg minRanMultiplier];
-[NIAcwgM2Msg selectedChannelBitmask];
-[NIAcwgM2Msg selectedFinalData2Bitmask];
-[NIAcwgM2Msg selectedPulseShapeCombo];
-[NIAcwgM2Msg selectedUwbConfigId];
-[NIAcwgM2Msg supportedHoppingConfigBitmask];
-[NIAcwgM2Msg supportedSlotBitmask];
-[NIAcwgM2Msg supportedSyncCodeIndexBitmask];
-[NIAcwgM2Msg toStruct];
```
