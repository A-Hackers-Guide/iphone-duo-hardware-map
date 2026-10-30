# `ACCiAP2ShimAccessory`

- Image: [`/System/Library/PrivateFrameworks/AccessoryiAP2Shim.framework/AccessoryiAP2Shim`](../userland/System__Library__PrivateFrameworks__AccessoryiAP2Shim.framework__AccessoryiAP2Shim.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 14 instance variables, 14 properties, 29 instance methods, 0 class methods

## Instance variables

```
B _dontPublish;
I _connectionID;
I _featureTypeMask;
@"NSString" _keyTag;
@"NSString" _keyAccessoryUID;
@"NSString" _keyConnectionID;
@"NSString" _accessoryUID;
@"NSString" _name;
@"NSString" _model;
@"NSString" _manufacturer;
@"NSString" _serialNumber;
@"NSString" _firmwareVersion;
@"NSString" _hardwareVersion;
@ _context;
```

## Properties

```
@property (T@"NSString",R,V_keyTag) keyTag;
@property (T@"NSString",R,V_keyAccessoryUID) keyAccessoryUID;
@property (T@"NSString",R,V_keyConnectionID) keyConnectionID;
@property (TI,V_connectionID) connectionID;
@property (TI,R,V_featureTypeMask) featureTypeMask;
@property (T@"NSString",R,V_accessoryUID) accessoryUID;
@property (T@"NSString",&,V_name) name;
@property (T@"NSString",&,V_model) model;
@property (T@"NSString",&,V_manufacturer) manufacturer;
@property (T@"NSString",&,V_serialNumber) serialNumber;
@property (T@"NSString",&,V_firmwareVersion) firmwareVersion;
@property (T@"NSString",&,V_hardwareVersion) hardwareVersion;
@property (T@,&,V_context) context;
@property (TB,V_dontPublish) dontPublish;
```

## Instance methods

```
-[ACCiAP2ShimAccessory hardwareVersion];
-[ACCiAP2ShimAccessory model];
-[ACCiAP2ShimAccessory setSerialNumber:];
-[ACCiAP2ShimAccessory setModel:];
-[ACCiAP2ShimAccessory firmwareVersion];
-[ACCiAP2ShimAccessory setFirmwareVersion:];
-[ACCiAP2ShimAccessory manufacturer];
-[ACCiAP2ShimAccessory serialNumber];
-[ACCiAP2ShimAccessory setContext:];
-[ACCiAP2ShimAccessory description];
-[ACCiAP2ShimAccessory setName:];
-[ACCiAP2ShimAccessory connectionID];
-[ACCiAP2ShimAccessory context];
-[ACCiAP2ShimAccessory name];
-[ACCiAP2ShimAccessory setManufacturer:];
-[ACCiAP2ShimAccessory addFeature:];
-[ACCiAP2ShimAccessory setConnectionID:];
-[ACCiAP2ShimAccessory setHardwareVersion:];
-[ACCiAP2ShimAccessory removeFeature:];
-[ACCiAP2ShimAccessory accessoryUID];
-[ACCiAP2ShimAccessory connectionIDObj];
-[ACCiAP2ShimAccessory accessoryInfoDict];
-[ACCiAP2ShimAccessory initWithUID:keyTag:features:];
-[ACCiAP2ShimAccessory setDontPublish:];
-[ACCiAP2ShimAccessory featureTypeMask];
-[ACCiAP2ShimAccessory keyAccessoryUID];
-[ACCiAP2ShimAccessory keyConnectionID];
-[ACCiAP2ShimAccessory dontPublish];
-[ACCiAP2ShimAccessory keyTag];
```
