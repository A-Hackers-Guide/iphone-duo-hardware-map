# `ANFirmwareUpdater`

- Image: [`/System/Library/PrivateFrameworks/AccessoryInteraction.framework/AccessoryInteraction`](../userland/System__Library__PrivateFrameworks__AccessoryInteraction.framework__AccessoryInteraction.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CBPeripheralDelegate`
- 21 instance variables, 25 properties, 70 instance methods, 0 class methods

## Instance variables

```
B _hasPreparedForFirmwareDownload;
B _isCustomerFlow;
@"<ANFirmwareUpdaterDelegate>" _delegate;
@"CBPeripheral" _peripheral;
@"NSString" _tagSerialNumber;
@"NSString" _tagFirmwareVersion;
@"CBCharacteristic" _firmwareDownloadAssetsCharacteristic;
@"CBCharacteristic" _firmwareDownloadCommandCharacteristic;
@"CBCharacteristic" _firwmareDownloadStatusCharacteristic;
@"CBCharacteristic" _firmwareDownloadAssetsReadyCharacteristic;
@"CBCharacteristic" _personalizationChipIDCharacteristic;
@"CBCharacteristic" _personalizationBoardIDCharacteristic;
@"CBCharacteristic" _personalizationECIDCharacteristic;
@"CBCharacteristic" _personalizationSecDomainCharacteristic;
@"CBCharacteristic" _personalizationSecModeCharacteristic;
@"CBCharacteristic" _personalizationProdModeCharacteristic;
@"CBCharacteristic" _personalizationBootNonceHashCharacteristic;
@"CBCharacteristic" _personalizationBVERCharacteristic;
@"NSMutableDictionary" _personalizationInformation;
@"NSMutableArray" _assetPacketizerQueue;
@"ANFirmwareAssetPacketizer" _currentAssetPacketizer;
```

## Properties

```
@property (T@"CBPeripheral",&,V_peripheral) peripheral;
@property (T@"NSString",&,V_tagSerialNumber) tagSerialNumber;
@property (T@"NSString",&,V_tagFirmwareVersion) tagFirmwareVersion;
@property (T@"CBCharacteristic",&,V_firmwareDownloadAssetsCharacteristic) firmwareDownloadAssetsCharacteristic;
@property (T@"CBCharacteristic",&,V_firmwareDownloadCommandCharacteristic) firmwareDownloadCommandCharacteristic;
@property (T@"CBCharacteristic",&,V_firwmareDownloadStatusCharacteristic) firwmareDownloadStatusCharacteristic;
@property (T@"CBCharacteristic",&,V_firmwareDownloadAssetsReadyCharacteristic) firmwareDownloadAssetsReadyCharacteristic;
@property (T@"CBCharacteristic",&,V_personalizationChipIDCharacteristic) personalizationChipIDCharacteristic;
@property (T@"CBCharacteristic",&,V_personalizationBoardIDCharacteristic) personalizationBoardIDCharacteristic;
@property (T@"CBCharacteristic",&,V_personalizationECIDCharacteristic) personalizationECIDCharacteristic;
@property (T@"CBCharacteristic",&,V_personalizationSecDomainCharacteristic) personalizationSecDomainCharacteristic;
@property (T@"CBCharacteristic",&,V_personalizationSecModeCharacteristic) personalizationSecModeCharacteristic;
@property (T@"CBCharacteristic",&,V_personalizationProdModeCharacteristic) personalizationProdModeCharacteristic;
@property (T@"CBCharacteristic",&,V_personalizationBootNonceHashCharacteristic) personalizationBootNonceHashCharacteristic;
@property (T@"CBCharacteristic",&,V_personalizationBVERCharacteristic) personalizationBVERCharacteristic;
@property (TB,V_hasPreparedForFirmwareDownload) hasPreparedForFirmwareDownload;
@property (T@"NSMutableDictionary",&,V_personalizationInformation) personalizationInformation;
@property (T@"NSMutableArray",&,V_assetPacketizerQueue) assetPacketizerQueue;
@property (T@"ANFirmwareAssetPacketizer",&,V_currentAssetPacketizer) currentAssetPacketizer;
@property (TB,V_isCustomerFlow) isCustomerFlow;
@property (T@"<ANFirmwareUpdaterDelegate>",W,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[ANFirmwareUpdater _cleanup];
-[ANFirmwareUpdater dealloc];
-[ANFirmwareUpdater setDelegate:];
-[ANFirmwareUpdater delegate];
-[ANFirmwareUpdater peripheral:didDiscoverServices:];
-[ANFirmwareUpdater peripheral];
-[ANFirmwareUpdater peripheral:didDiscoverCharacteristicsForService:error:];
-[ANFirmwareUpdater peripheral:didUpdateValueForCharacteristic:error:];
-[ANFirmwareUpdater setPeripheral:];
-[ANFirmwareUpdater _readPersonalizationInformation];
-[ANFirmwareUpdater tagSerialNumber];
-[ANFirmwareUpdater _createErrorForDownloadStatus:];
-[ANFirmwareUpdater _firmwareAssetTypeToString:];
-[ANFirmwareUpdater _firmwareDownloadCommandToString:];
-[ANFirmwareUpdater _firmwareDownloadStatusToString:];
-[ANFirmwareUpdater _firmwarePersonalizationCharacteristicUUIDToString:];
-[ANFirmwareUpdater _handleDownloadStatusFromDevice:];
-[ANFirmwareUpdater _handlePersonalizationDataFromDevice:];
-[ANFirmwareUpdater _prepareForFirmwareDownload];
-[ANFirmwareUpdater _sendCommandToDevice:];
-[ANFirmwareUpdater _sendFirmwareAsset:assetData:];
-[ANFirmwareUpdater _sendLocalImageAssets:];
-[ANFirmwareUpdater _sendNextAsset];
-[ANFirmwareUpdater _sendNextPacketToDevice:];
-[ANFirmwareUpdater abortFirmwareUpdate];
-[ANFirmwareUpdater assetPacketizerQueue];
-[ANFirmwareUpdater currentAssetPacketizer];
-[ANFirmwareUpdater didRetrieveAllPersonalizationCharacteristics];
-[ANFirmwareUpdater firmwareDownloadAssetsCharacteristic];
-[ANFirmwareUpdater firmwareDownloadAssetsReadyCharacteristic];
-[ANFirmwareUpdater firmwareDownloadCommandCharacteristic];
-[ANFirmwareUpdater firwmareDownloadStatusCharacteristic];
-[ANFirmwareUpdater getPersonalizationInformation];
-[ANFirmwareUpdater hasPreparedForFirmwareDownload];
-[ANFirmwareUpdater initWithDelegate:peripheral:];
-[ANFirmwareUpdater initWithDelegate:peripheral:serialNumber:firmwareVersion:isCustomerFlow:];
-[ANFirmwareUpdater initWithDelegateForProductionFlow:peripheral:serialNumber:firmwareVersion:];
-[ANFirmwareUpdater isCustomerFlow];
-[ANFirmwareUpdater personalizationBVERCharacteristic];
-[ANFirmwareUpdater personalizationBoardIDCharacteristic];
-[ANFirmwareUpdater personalizationBootNonceHashCharacteristic];
-[ANFirmwareUpdater personalizationChipIDCharacteristic];
-[ANFirmwareUpdater personalizationECIDCharacteristic];
-[ANFirmwareUpdater personalizationInformation];
-[ANFirmwareUpdater personalizationProdModeCharacteristic];
-[ANFirmwareUpdater personalizationSecDomainCharacteristic];
-[ANFirmwareUpdater personalizationSecModeCharacteristic];
-[ANFirmwareUpdater setAssetPacketizerQueue:];
-[ANFirmwareUpdater setCurrentAssetPacketizer:];
-[ANFirmwareUpdater setFirmwareDownloadAssetsCharacteristic:];
-[ANFirmwareUpdater setFirmwareDownloadAssetsReadyCharacteristic:];
-[ANFirmwareUpdater setFirmwareDownloadCommandCharacteristic:];
-[ANFirmwareUpdater setFirwmareDownloadStatusCharacteristic:];
-[ANFirmwareUpdater setHasPreparedForFirmwareDownload:];
-[ANFirmwareUpdater setIsCustomerFlow:];
-[ANFirmwareUpdater setPersonalizationBVERCharacteristic:];
-[ANFirmwareUpdater setPersonalizationBoardIDCharacteristic:];
-[ANFirmwareUpdater setPersonalizationBootNonceHashCharacteristic:];
-[ANFirmwareUpdater setPersonalizationChipIDCharacteristic:];
-[ANFirmwareUpdater setPersonalizationECIDCharacteristic:];
-[ANFirmwareUpdater setPersonalizationInformation:];
-[ANFirmwareUpdater setPersonalizationProdModeCharacteristic:];
-[ANFirmwareUpdater setPersonalizationSecDomainCharacteristic:];
-[ANFirmwareUpdater setPersonalizationSecModeCharacteristic:];
-[ANFirmwareUpdater setTagFirmwareVersion:];
-[ANFirmwareUpdater setTagSerialNumber:];
-[ANFirmwareUpdater startFirmwareUpdate:];
-[ANFirmwareUpdater submitDiagnosticReportForMissingPersonalizationCharacteristics];
-[ANFirmwareUpdater submitPersonalizationCharacteristicsMetrics:];
-[ANFirmwareUpdater tagFirmwareVersion];
```
