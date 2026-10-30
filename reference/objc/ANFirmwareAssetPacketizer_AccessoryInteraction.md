# `ANFirmwareAssetPacketizer`

- Image: [`/System/Library/PrivateFrameworks/AccessoryInteraction.framework/AccessoryInteraction`](../userland/System__Library__PrivateFrameworks__AccessoryInteraction.framework__AccessoryInteraction.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 8 properties, 20 instance methods, 0 class methods

## Instance variables

```
B _hasSentAssetData;
B _hasSentCRCPacket;
i _assetType;
@"NSData" _assetData;
Q _assetDataCRC;
@"NSData" _assetTargetHeader;
Q _maxPayloadSize;
Q _payloadOffset;
```

## Properties

```
@property (T@"NSData",&,V_assetData) assetData;
@property (TQ,N,V_assetDataCRC) assetDataCRC;
@property (T@"NSData",&,V_assetTargetHeader) assetTargetHeader;
@property (TB,N,V_hasSentAssetData) hasSentAssetData;
@property (TB,N,V_hasSentCRCPacket) hasSentCRCPacket;
@property (TQ,N,V_maxPayloadSize) maxPayloadSize;
@property (TQ,N,V_payloadOffset) payloadOffset;
@property (Ti,N,V_assetType) assetType;
```

## Instance methods

```
-[ANFirmwareAssetPacketizer assetType];
-[ANFirmwareAssetPacketizer dealloc];
-[ANFirmwareAssetPacketizer setAssetType:];
-[ANFirmwareAssetPacketizer maxPayloadSize];
-[ANFirmwareAssetPacketizer assetData];
-[ANFirmwareAssetPacketizer setAssetData:];
-[ANFirmwareAssetPacketizer payloadOffset];
-[ANFirmwareAssetPacketizer _buildCRCPacket];
-[ANFirmwareAssetPacketizer assetDataCRC];
-[ANFirmwareAssetPacketizer assetTargetHeader];
-[ANFirmwareAssetPacketizer getNextPacket];
-[ANFirmwareAssetPacketizer hasSentAssetData];
-[ANFirmwareAssetPacketizer hasSentCRCPacket];
-[ANFirmwareAssetPacketizer initWithAssetType:assetData:maxPacketSize:];
-[ANFirmwareAssetPacketizer setAssetDataCRC:];
-[ANFirmwareAssetPacketizer setAssetTargetHeader:];
-[ANFirmwareAssetPacketizer setHasSentAssetData:];
-[ANFirmwareAssetPacketizer setHasSentCRCPacket:];
-[ANFirmwareAssetPacketizer setMaxPayloadSize:];
-[ANFirmwareAssetPacketizer setPayloadOffset:];
```
