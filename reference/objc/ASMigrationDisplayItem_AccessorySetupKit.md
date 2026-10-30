# `ASMigrationDisplayItem`

- Image: [`/System/Library/Frameworks/AccessorySetupKit.framework/AccessorySetupKit`](../userland/System__Library__Frameworks__AccessorySetupKit.framework__AccessorySetupKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `ASPickerDisplayItem`
- Protocols: `CUXPCCodable`
- 5 instance variables, 5 properties, 17 instance methods, 1 class methods

## Instance variables

```
B _upgradeAccessory;
@"NSUUID" _peripheralIdentifier;
@"NSString" _hotspotSSID;
Q _wifiAwarePairedDeviceID;
@"NSString" _accessoryIdentifier;
```

## Properties

```
@property (T@"NSString",C,N,V_accessoryIdentifier) accessoryIdentifier;
@property (TB,N,V_upgradeAccessory) upgradeAccessory;
@property (T@"NSUUID",C,N,V_peripheralIdentifier) peripheralIdentifier;
@property (T@"NSString",C,N,V_hotspotSSID) hotspotSSID;
@property (TQ,N,V_wifiAwarePairedDeviceID) wifiAwarePairedDeviceID;
```

## Class methods

```
+[ASMigrationDisplayItem supportsSecureCoding];
```

## Instance methods

```
-[ASMigrationDisplayItem encodeWithXPCObject:];
-[ASMigrationDisplayItem initWithXPCObject:error:];
-[ASMigrationDisplayItem descriptionWithLevel:];
-[ASMigrationDisplayItem encodeWithCoder:];
-[ASMigrationDisplayItem initWithCoder:];
-[ASMigrationDisplayItem copyWithZone:];
-[ASMigrationDisplayItem isEqual:];
-[ASMigrationDisplayItem accessoryIdentifier];
-[ASMigrationDisplayItem setAccessoryIdentifier:];
-[ASMigrationDisplayItem setHotspotSSID:];
-[ASMigrationDisplayItem hotspotSSID];
-[ASMigrationDisplayItem peripheralIdentifier];
-[ASMigrationDisplayItem setPeripheralIdentifier:];
-[ASMigrationDisplayItem setUpgradeAccessory:];
-[ASMigrationDisplayItem setWifiAwarePairedDeviceID:];
-[ASMigrationDisplayItem upgradeAccessory];
-[ASMigrationDisplayItem wifiAwarePairedDeviceID];
```
