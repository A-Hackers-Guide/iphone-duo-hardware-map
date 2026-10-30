# `CBControllerInfo`

- Image: [`/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth`](../userland/System__Library__Frameworks__CoreBluetooth.framework__CoreBluetooth.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CUXPCCodable`, `NSSecureCoding`, `NSCopying`
- 21 instance variables, 21 properties, 52 instance methods, 1 class methods

## Instance variables

```
C _cloudSyncStatus;
C _fastLEConnectionInfoVersion;
c _hciTransportType;
C _leaVersion;
C _lmpVersion;
C _vendorIDSource;
B _fastLEConnectionAllowed;
S _vendorID;
i _discoverableState;
i _inquiryState;
I _productID;
I _supportedFeatures;
I _supportedServices;
@"NSArray" _audioLinkQualityArray;
q _bluetoothState;
@"NSString" _chipsetID;
@"NSData" _fastLEConnectionInfoData;
@"NSString" _firmwareName;
@"NSString" _firmwareVersion;
@"NSData" _hardwareAddressData;
@"NSError" _lastChipsetInitError;
```

## Properties

```
@property (T@"NSArray",C,N,V_audioLinkQualityArray) audioLinkQualityArray;
@property (Tq,N,V_bluetoothState) bluetoothState;
@property (T@"NSString",C,N,V_chipsetID) chipsetID;
@property (TC,N,V_cloudSyncStatus) cloudSyncStatus;
@property (Ti,N,V_discoverableState) discoverableState;
@property (TB,N,V_fastLEConnectionAllowed) fastLEConnectionAllowed;
@property (T@"NSData",C,N,V_fastLEConnectionInfoData) fastLEConnectionInfoData;
@property (TC,N,V_fastLEConnectionInfoVersion) fastLEConnectionInfoVersion;
@property (T@"NSString",C,N,V_firmwareName) firmwareName;
@property (T@"NSString",C,N,V_firmwareVersion) firmwareVersion;
@property (T@"NSData",C,N,V_hardwareAddressData) hardwareAddressData;
@property (Tc,N,V_hciTransportType) hciTransportType;
@property (Ti,N,V_inquiryState) inquiryState;
@property (TC,N,V_leaVersion) leaVersion;
@property (TC,N,V_lmpVersion) lmpVersion;
@property (TI,N,V_productID) productID;
@property (TI,N,V_supportedFeatures) supportedFeatures;
@property (TI,N,V_supportedServices) supportedServices;
@property (TS,N,V_vendorID) vendorID;
@property (TC,N,V_vendorIDSource) vendorIDSource;
@property (T@"NSError",C,N,V_lastChipsetInitError) lastChipsetInitError;
```

## Class methods

```
+[CBControllerInfo supportsSecureCoding];
```

## Instance methods

```
-[CBControllerInfo vendorID];
-[CBControllerInfo setProductID:];
-[CBControllerInfo encodeWithXPCObject:];
-[CBControllerInfo productID];
-[CBControllerInfo inquiryState];
-[CBControllerInfo setLastChipsetInitError:];
-[CBControllerInfo initWithDictionary:error:];
-[CBControllerInfo firmwareVersion];
-[CBControllerInfo initWithXPCObject:error:];
-[CBControllerInfo descriptionWithLevel:];
-[CBControllerInfo leaVersion];
-[CBControllerInfo setLeaVersion:];
-[CBControllerInfo supportedFeatures];
-[CBControllerInfo setFirmwareVersion:];
-[CBControllerInfo setBluetoothState:];
-[CBControllerInfo bluetoothState];
-[CBControllerInfo lastChipsetInitError];
-[CBControllerInfo setSupportedFeatures:];
-[CBControllerInfo discoverableState];
-[CBControllerInfo vendorIDSource];
-[CBControllerInfo firmwareName];
-[CBControllerInfo setFastLEConnectionInfoVersion:];
-[CBControllerInfo setLmpVersion:];
-[CBControllerInfo setVendorID:];
-[CBControllerInfo fastLEConnectionInfoVersion];
-[CBControllerInfo fastLEConnectionInfoData];
-[CBControllerInfo chipsetID];
-[CBControllerInfo setVendorIDSource:];
-[CBControllerInfo audioLinkQualityArray];
-[CBControllerInfo setFastLEConnectionInfoData:];
-[CBControllerInfo lmpVersion];
-[CBControllerInfo fastLEConnectionAllowed];
-[CBControllerInfo setHardwareAddressData:];
-[CBControllerInfo setInquiryState:];
-[CBControllerInfo supportedServices];
-[CBControllerInfo setHciTransportType:];
-[CBControllerInfo setFastLEConnectionAllowed:];
-[CBControllerInfo encodeWithCoder:];
-[CBControllerInfo cloudSyncStatus];
-[CBControllerInfo setDiscoverableState:];
-[CBControllerInfo setChipsetID:];
-[CBControllerInfo description];
-[CBControllerInfo setFirmwareName:];
-[CBControllerInfo initWithCoder:];
-[CBControllerInfo hciTransportType];
-[CBControllerInfo copyWithZone:];
-[CBControllerInfo setSupportedServices:];
-[CBControllerInfo isEqual:];
-[CBControllerInfo setAudioLinkQualityArray:];
-[CBControllerInfo hardwareAddressData];
-[CBControllerInfo setCloudSyncStatus:];
-[CBControllerInfo dictionaryRepresentation];
```
