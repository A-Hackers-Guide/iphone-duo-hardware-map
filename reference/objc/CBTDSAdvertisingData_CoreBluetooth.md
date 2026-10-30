# `CBTDSAdvertisingData`

- Image: [`/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth`](../userland/System__Library__Frameworks__CoreBluetooth.framework__CoreBluetooth.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `CUXPCCodable`, `NSCopying`
- 10 instance variables, 10 properties, 31 instance methods, 7 class methods

## Instance variables

```
C _frameRole;
C _transportState;
B _randomization;
B _dataMatched;
I _headerFlags;
@"NSNumber" _channelInfo;
@"NSArray" _serviceElements;
@"NSData" _sourceTIK;
@"NSData" _destinationGroupTIK;
@"NSData" _rawData;
```

## Properties

```
@property (TI,N,V_headerFlags) headerFlags;
@property (T@"NSData",C,N,V_rawData) rawData;
@property (TB,N,V_dataMatched) dataMatched;
@property (T@"NSNumber",C,N,V_channelInfo) channelInfo;
@property (TC,N,V_frameRole) frameRole;
@property (TC,N,V_transportState) transportState;
@property (T@"NSArray",C,N,V_serviceElements) serviceElements;
@property (T@"NSData",C,N,V_sourceTIK) sourceTIK;
@property (T@"NSData",C,N,V_destinationGroupTIK) destinationGroupTIK;
@property (TB,N,V_randomization) randomization;
```

## Class methods

```
+[CBTDSAdvertisingData supportsSecureCoding];
+[CBTDSAdvertisingData CBTDSHeaderFlagsFromByte:];
+[CBTDSAdvertisingData CBTDSFlagsToByteFrom:with:];
+[CBTDSAdvertisingData CBTDSHeaderFlagsToByte:];
+[CBTDSAdvertisingData calculateNANITag:tdsPacket:];
+[CBTDSAdvertisingData constructTDSPacketWithAddress:tdsFlags:bloomFilter:bloomFilterSize:channelInfo:headerFlags:TIK:];
+[CBTDSAdvertisingData populateBloomFilter:withSize:serviceElements:headerFlags:TIK:nonConnectableAddress:];
```

## Instance methods

```
-[CBTDSAdvertisingData encodeWithXPCObject:];
-[CBTDSAdvertisingData channelInfo];
-[CBTDSAdvertisingData initWithXPCObject:error:];
-[CBTDSAdvertisingData descriptionWithLevel:];
-[CBTDSAdvertisingData setChannelInfo:];
-[CBTDSAdvertisingData encodeWithCoder:];
-[CBTDSAdvertisingData rawData];
-[CBTDSAdvertisingData hash];
-[CBTDSAdvertisingData description];
-[CBTDSAdvertisingData initWithCoder:];
-[CBTDSAdvertisingData copyWithZone:];
-[CBTDSAdvertisingData isEqual:];
-[CBTDSAdvertisingData setRawData:];
-[CBTDSAdvertisingData setDataMatched:];
-[CBTDSAdvertisingData serviceElements];
-[CBTDSAdvertisingData setHeaderFlags:];
-[CBTDSAdvertisingData dataMatched];
-[CBTDSAdvertisingData destinationGroupTIK];
-[CBTDSAdvertisingData frameRole];
-[CBTDSAdvertisingData headerFlags];
-[CBTDSAdvertisingData isClassDataValid];
-[CBTDSAdvertisingData randomization];
-[CBTDSAdvertisingData setDestinationGroupTIK:];
-[CBTDSAdvertisingData setFrameRole:];
-[CBTDSAdvertisingData setRandomization:];
-[CBTDSAdvertisingData setServiceElements:];
-[CBTDSAdvertisingData setSourceTIK:];
-[CBTDSAdvertisingData setTransportState:];
-[CBTDSAdvertisingData sourceTIK];
-[CBTDSAdvertisingData transportState];
-[CBTDSAdvertisingData updateHeaderFlags];
```
