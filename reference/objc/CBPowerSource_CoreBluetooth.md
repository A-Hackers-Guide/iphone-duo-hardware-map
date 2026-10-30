# `CBPowerSource`

- Image: [`/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth`](../userland/System__Library__Frameworks__CoreBluetooth.framework__CoreBluetooth.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CUXPCCodable`, `NSSecureCoding`, `NSCopying`, `CBDictionaryCodable`
- 24 instance variables, 23 properties, 71 instance methods, 1 class methods

## Instance variables

```
@"NSMutableDictionary" _componentMap;
^{OpaqueIOPSPowerSourceID=} _psID;
C _deviceType;
B _present;
C _vendorIDSource;
S _accessoryCategory;
S _partID;
S _vendorID;
S _batteryInfo;
I _appearanceValue;
I _productID;
I _changeFlags;
I _internalFlags;
@"NSString" _accessoryID;
q _familyCode;
@"NSString" _groupID;
q _lowWarnLevel;
d _maxCapacity;
@"NSString" _name;
@"NSString" _partName;
q _sourceID;
q _temperature;
@"NSString" _transportType;
@"NSString" _type;
```

## Properties

```
@property (TS,N,V_batteryInfo) batteryInfo;
@property (TI,N,V_changeFlags) changeFlags;
@property (TI,N,V_internalFlags) internalFlags;
@property (TS,N,V_accessoryCategory) accessoryCategory;
@property (T@"NSString",C,N,V_accessoryID) accessoryID;
@property (TI,N,V_appearanceValue) appearanceValue;
@property (T@"NSMutableDictionary",R,N) components;
@property (TC,N,V_deviceType) deviceType;
@property (Tq,N,V_familyCode) familyCode;
@property (T@"NSString",C,N,V_groupID) groupID;
@property (Tq,N,V_lowWarnLevel) lowWarnLevel;
@property (Td,N,V_maxCapacity) maxCapacity;
@property (T@"NSString",C,N,V_name) name;
@property (TS,N,V_partID) partID;
@property (T@"NSString",C,N,V_partName) partName;
@property (TB,N,V_present) present;
@property (TI,N,V_productID) productID;
@property (Tq,N,V_sourceID) sourceID;
@property (Tq,N,V_temperature) temperature;
@property (T@"NSString",C,N,V_transportType) transportType;
@property (T@"NSString",C,N,V_type) type;
@property (TS,N,V_vendorID) vendorID;
@property (TC,N,V_vendorIDSource) vendorIDSource;
```

## Class methods

```
+[CBPowerSource supportsSecureCoding];
```

## Instance methods

```
-[CBPowerSource vendorID];
-[CBPowerSource present];
-[CBPowerSource setPresent:];
-[CBPowerSource setProductID:];
-[CBPowerSource publish];
-[CBPowerSource setGroupID:];
-[CBPowerSource encodeWithXPCObject:];
-[CBPowerSource setDeviceType:];
-[CBPowerSource productID];
-[CBPowerSource setInternalFlags:];
-[CBPowerSource internalFlags];
-[CBPowerSource initWithDictionary:error:];
-[CBPowerSource lowWarnLevel];
-[CBPowerSource setPartID:];
-[CBPowerSource groupID];
-[CBPowerSource initWithXPCObject:error:];
-[CBPowerSource familyCode];
-[CBPowerSource setTransportType:];
-[CBPowerSource vendorIDSource];
-[CBPowerSource setPartName:];
-[CBPowerSource init];
-[CBPowerSource deviceType];
-[CBPowerSource setVendorID:];
-[CBPowerSource setTemperature:];
-[CBPowerSource dealloc];
-[CBPowerSource setFamilyCode:];
-[CBPowerSource accessoryID];
-[CBPowerSource setSourceID:];
-[CBPowerSource transportType];
-[CBPowerSource setAccessoryID:];
-[CBPowerSource setVendorIDSource:];
-[CBPowerSource sourceID];
-[CBPowerSource components];
-[CBPowerSource setChangeFlags:];
-[CBPowerSource setLowWarnLevel:];
-[CBPowerSource changeFlags];
-[CBPowerSource invalidate];
-[CBPowerSource setAccessoryCategory:];
-[CBPowerSource setMaxCapacity:];
-[CBPowerSource setType:];
-[CBPowerSource partName];
-[CBPowerSource type];
-[CBPowerSource encodeWithCoder:];
-[CBPowerSource accessoryCategory];
-[CBPowerSource description];
-[CBPowerSource setName:];
-[CBPowerSource partID];
-[CBPowerSource initWithCoder:];
-[CBPowerSource copyWithZone:];
-[CBPowerSource name];
-[CBPowerSource temperature];
-[CBPowerSource maxCapacity];
-[CBPowerSource dictionaryRepresentation];
-[CBPowerSource hasAllComponents];
-[CBPowerSource isAggregateComponent];
-[CBPowerSource isAppleDevice];
-[CBPowerSource setBatteryInfo:];
-[CBPowerSource batteryInfo];
-[CBPowerSource combinedPublish];
-[CBPowerSource appearanceValue];
-[CBPowerSource _setPartName];
-[CBPowerSource _updateAggregateWithComponent:];
-[CBPowerSource componentWithPartID:];
-[CBPowerSource initWithPowerSourceDetails:internalFlags:];
-[CBPowerSource invalidateComponentWithPartID:];
-[CBPowerSource releaseSource];
-[CBPowerSource removeBatteryInfo];
-[CBPowerSource removeFlags];
-[CBPowerSource setAppearanceValue:];
-[CBPowerSource updatePartID];
-[CBPowerSource updateWithCBPowerSource:];
```
