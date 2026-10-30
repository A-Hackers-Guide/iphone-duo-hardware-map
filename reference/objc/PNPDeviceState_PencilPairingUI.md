# `PNPDeviceState`

- Image: [`/System/Library/PrivateFrameworks/PencilPairingUI.framework/PencilPairingUI`](../userland/System__Library__PrivateFrameworks__PencilPairingUI.framework__PencilPairingUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 9 instance variables, 10 properties, 27 instance methods, 1 class methods

## Instance variables

```
B _batteryLevelUnknown;
B _isCharging;
@"NSString" _name;
@"NSString" _displayName;
@"NSUUID" _identifier;
d _batteryLevel;
Q _edge;
Q _orientation;
q _deviceType;
```

## Properties

```
@property (TB,R,N) isOnLeftOrRightSide;
@property (T@"NSString",C,N,V_name) name;
@property (T@"NSString",C,N,V_displayName) displayName;
@property (T@"NSUUID",C,N,V_identifier) identifier;
@property (Td,N,V_batteryLevel) batteryLevel;
@property (TQ,N,V_edge) edge;
@property (TQ,N,V_orientation) orientation;
@property (TB,N,V_batteryLevelUnknown) batteryLevelUnknown;
@property (TB,N,V_isCharging) isCharging;
@property (Tq,N,V_deviceType) deviceType;
```

## Class methods

```
+[PNPDeviceState supportsSecureCoding];
```

## Instance methods

```
-[PNPDeviceState isCharging];
-[PNPDeviceState setEdge:];
-[PNPDeviceState setDeviceType:];
-[PNPDeviceState setOrientation:];
-[PNPDeviceState batteryLevel];
-[PNPDeviceState setIsCharging:];
-[PNPDeviceState edge];
-[PNPDeviceState identifier];
-[PNPDeviceState init];
-[PNPDeviceState deviceType];
-[PNPDeviceState displayName];
-[PNPDeviceState orientation];
-[PNPDeviceState setDisplayName:];
-[PNPDeviceState setIdentifier:];
-[PNPDeviceState encodeWithCoder:];
-[PNPDeviceState description];
-[PNPDeviceState setName:];
-[PNPDeviceState initWithCoder:];
-[PNPDeviceState copyWithZone:];
-[PNPDeviceState setBatteryLevel:];
-[PNPDeviceState isEqual:];
-[PNPDeviceState name];
-[PNPDeviceState _deviceTypeDescription];
-[PNPDeviceState _edgeDescription];
-[PNPDeviceState batteryLevelUnknown];
-[PNPDeviceState isOnLeftOrRightSide];
-[PNPDeviceState setBatteryLevelUnknown:];
```
