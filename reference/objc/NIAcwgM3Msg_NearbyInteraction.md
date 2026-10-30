# `NIAcwgM3Msg`

- Image: [`/System/Library/Frameworks/NearbyInteraction.framework/NearbyInteraction`](../userland/System__Library__Frameworks__NearbyInteraction.framework__NearbyInteraction.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 7 instance variables, 7 properties, 13 instance methods, 1 class methods

## Instance variables

```
C _selectedRanMultiplier;
C _selectedNumChapsPerSlot;
C _numResponders;
C _numSlotsPerRound;
C _selectedHoppingConfigBitmask;
C _macMode;
I _supportedSyncCodeIndexBitmask;
```

## Properties

```
@property (TC,R,N,V_selectedRanMultiplier) selectedRanMultiplier;
@property (TC,R,N,V_selectedNumChapsPerSlot) selectedNumChapsPerSlot;
@property (TC,R,N,V_numResponders) numResponders;
@property (TC,R,N,V_numSlotsPerRound) numSlotsPerRound;
@property (TI,R,N,V_supportedSyncCodeIndexBitmask) supportedSyncCodeIndexBitmask;
@property (TC,R,N,V_selectedHoppingConfigBitmask) selectedHoppingConfigBitmask;
@property (TC,R,N,V_macMode) macMode;
```

## Class methods

```
+[NIAcwgM3Msg supportsSecureCoding];
```

## Instance methods

```
-[NIAcwgM3Msg encodeWithCoder:];
-[NIAcwgM3Msg description];
-[NIAcwgM3Msg initWithCoder:];
-[NIAcwgM3Msg copyWithZone:];
-[NIAcwgM3Msg macMode];
-[NIAcwgM3Msg initWithSelectedRanMultiplier:selectedNumChapsPerSlot:numResponders:numSlotsPerRound:supportedSyncCodeIndexBitmask:selectedHoppingConfigBitmask:macMode:];
-[NIAcwgM3Msg numResponders];
-[NIAcwgM3Msg numSlotsPerRound];
-[NIAcwgM3Msg selectedHoppingConfigBitmask];
-[NIAcwgM3Msg selectedNumChapsPerSlot];
-[NIAcwgM3Msg selectedRanMultiplier];
-[NIAcwgM3Msg supportedSyncCodeIndexBitmask];
-[NIAcwgM3Msg toStruct];
```
