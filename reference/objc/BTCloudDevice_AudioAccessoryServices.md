# `BTCloudDevice`

- Image: [`/System/Library/PrivateFrameworks/AudioAccessoryServices.framework/AudioAccessoryServices`](../userland/System__Library__PrivateFrameworks__AudioAccessoryServices.framework__AudioAccessoryServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 6 instance variables, 6 properties, 16 instance methods, 2 class methods

## Instance variables

```
@"NSString" _bluetoothAddress;
@"NSString" _manufacturer;
@"NSString" _modelNumber;
@"NSString" _nickname;
@"NSString" _productID;
@"NSString" _vendorID;
```

## Properties

```
@property (T@"NSString",&,N,V_bluetoothAddress) bluetoothAddress;
@property (T@"NSString",&,N,V_manufacturer) manufacturer;
@property (T@"NSString",&,N,V_modelNumber) modelNumber;
@property (T@"NSString",&,N,V_nickname) nickname;
@property (T@"NSString",&,N,V_productID) productID;
@property (T@"NSString",&,N,V_vendorID) vendorID;
```

## Class methods

```
+[BTCloudDevice supportsSecureCoding];
+[BTCloudDevice deviceWithBluetoothAddress:];
```

## Instance methods

```
-[BTCloudDevice vendorID];
-[BTCloudDevice modelNumber];
-[BTCloudDevice setProductID:];
-[BTCloudDevice productID];
-[BTCloudDevice setBluetoothAddress:];
-[BTCloudDevice setModelNumber:];
-[BTCloudDevice setVendorID:];
-[BTCloudDevice manufacturer];
-[BTCloudDevice setNickname:];
-[BTCloudDevice nickname];
-[BTCloudDevice bluetoothAddress];
-[BTCloudDevice encodeWithCoder:];
-[BTCloudDevice description];
-[BTCloudDevice initWithCoder:];
-[BTCloudDevice setManufacturer:];
-[BTCloudDevice initWithBluetoothAddress:];
```
