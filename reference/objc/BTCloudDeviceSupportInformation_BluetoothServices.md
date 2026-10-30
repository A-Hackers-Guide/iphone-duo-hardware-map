# `BTCloudDeviceSupportInformation`

- Image: [`/System/Library/PrivateFrameworks/BluetoothServices.framework/BluetoothServices`](../userland/System__Library__PrivateFrameworks__BluetoothServices.framework__BluetoothServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 9 instance variables, 9 properties, 22 instance methods, 2 class methods

## Instance variables

```
@"NSString" _bluetoothAddress;
@"NSString" _budsFirmwareVersion;
@"NSString" _caseName;
@"NSString" _caseFirmwareVersion;
@"NSString" _caseSerialNumber;
@"NSString" _hardwareVersion;
@"NSString" _leftBudSerialNumber;
@"NSString" _rightBudSerialNumber;
@"NSString" _ancAssetVersion;
```

## Properties

```
@property (T@"NSString",&,N,V_bluetoothAddress) bluetoothAddress;
@property (T@"NSString",&,N,V_budsFirmwareVersion) budsFirmwareVersion;
@property (T@"NSString",&,N,V_caseName) caseName;
@property (T@"NSString",&,N,V_caseFirmwareVersion) caseFirmwareVersion;
@property (T@"NSString",&,N,V_caseSerialNumber) caseSerialNumber;
@property (T@"NSString",&,N,V_hardwareVersion) hardwareVersion;
@property (T@"NSString",&,N,V_leftBudSerialNumber) leftBudSerialNumber;
@property (T@"NSString",&,N,V_rightBudSerialNumber) rightBudSerialNumber;
@property (T@"NSString",&,N,V_ancAssetVersion) ancAssetVersion;
```

## Class methods

```
+[BTCloudDeviceSupportInformation supportsSecureCoding];
+[BTCloudDeviceSupportInformation deviceSupportInformationWithBluetoothAddress:];
```

## Instance methods

```
-[BTCloudDeviceSupportInformation hardwareVersion];
-[BTCloudDeviceSupportInformation setBluetoothAddress:];
-[BTCloudDeviceSupportInformation bluetoothAddress];
-[BTCloudDeviceSupportInformation encodeWithCoder:];
-[BTCloudDeviceSupportInformation description];
-[BTCloudDeviceSupportInformation initWithCoder:];
-[BTCloudDeviceSupportInformation setHardwareVersion:];
-[BTCloudDeviceSupportInformation ancAssetVersion];
-[BTCloudDeviceSupportInformation budsFirmwareVersion];
-[BTCloudDeviceSupportInformation caseFirmwareVersion];
-[BTCloudDeviceSupportInformation caseName];
-[BTCloudDeviceSupportInformation caseSerialNumber];
-[BTCloudDeviceSupportInformation initWithBluetoothAddress:];
-[BTCloudDeviceSupportInformation leftBudSerialNumber];
-[BTCloudDeviceSupportInformation rightBudSerialNumber];
-[BTCloudDeviceSupportInformation setAncAssetVersion:];
-[BTCloudDeviceSupportInformation setBudsFirmwareVersion:];
-[BTCloudDeviceSupportInformation setCaseFirmwareVersion:];
-[BTCloudDeviceSupportInformation setCaseName:];
-[BTCloudDeviceSupportInformation setCaseSerialNumber:];
-[BTCloudDeviceSupportInformation setLeftBudSerialNumber:];
-[BTCloudDeviceSupportInformation setRightBudSerialNumber:];
```
