# `ASDiscoveredAccessory`

- Image: [`/System/Library/Frameworks/AccessorySetupKit.framework/AccessorySetupKit`](../userland/System__Library__Frameworks__AccessorySetupKit.framework__AccessorySetupKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `ASAccessory`
- Protocols: `CUXPCCodable`, `NSSecureCoding`, `NSCopying`
- 2 instance variables, 2 properties, 13 instance methods, 1 class methods

## Instance variables

```
@"NSDictionary" _bluetoothAdvertisementData;
@"NSNumber" _bluetoothRSSI;
```

## Properties

```
@property (T@"NSDictionary",C,N,V_bluetoothAdvertisementData) bluetoothAdvertisementData;
@property (T@"NSNumber",C,N,V_bluetoothRSSI) bluetoothRSSI;
```

## Class methods

```
+[ASDiscoveredAccessory supportsSecureCoding];
```

## Instance methods

```
-[ASDiscoveredAccessory encodeWithXPCObject:];
-[ASDiscoveredAccessory initWithXPCObject:error:];
-[ASDiscoveredAccessory descriptionWithLevel:];
-[ASDiscoveredAccessory encodeWithCoder:];
-[ASDiscoveredAccessory description];
-[ASDiscoveredAccessory initWithCoder:];
-[ASDiscoveredAccessory copyWithZone:];
-[ASDiscoveredAccessory isEqual:];
-[ASDiscoveredAccessory bluetoothAdvertisementData];
-[ASDiscoveredAccessory bluetoothRSSI];
-[ASDiscoveredAccessory initWithDADevice:bundleID:];
-[ASDiscoveredAccessory setBluetoothAdvertisementData:];
-[ASDiscoveredAccessory setBluetoothRSSI:];
```
