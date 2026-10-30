# `W5PowerStatus`

- Image: [`/System/Library/PrivateFrameworks/WiFiVelocity.framework/WiFiVelocity`](../userland/System__Library__PrivateFrameworks__WiFiVelocity.framework__WiFiVelocity.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 4 instance variables, 4 properties, 16 instance methods, 1 class methods

## Instance variables

```
i _batteryWarningLevel;
I _powerStateCaps;
q _powerSourceType;
d _internalBatteryLevel;
```

## Properties

```
@property (Tq,N,V_powerSourceType) powerSourceType;
@property (Ti,N,V_batteryWarningLevel) batteryWarningLevel;
@property (Td,N,V_internalBatteryLevel) internalBatteryLevel;
@property (TI,N,V_powerStateCaps) powerStateCaps;
```

## Class methods

```
+[W5PowerStatus supportsSecureCoding];
```

## Instance methods

```
-[W5PowerStatus encodeWithCoder:];
-[W5PowerStatus conformsToProtocol:];
-[W5PowerStatus hash];
-[W5PowerStatus description];
-[W5PowerStatus initWithCoder:];
-[W5PowerStatus copyWithZone:];
-[W5PowerStatus isEqual:];
-[W5PowerStatus powerSourceType];
-[W5PowerStatus batteryWarningLevel];
-[W5PowerStatus powerStateCaps];
-[W5PowerStatus setPowerSourceType:];
-[W5PowerStatus setPowerStateCaps:];
-[W5PowerStatus internalBatteryLevel];
-[W5PowerStatus isEqualToPowerStatus:];
-[W5PowerStatus setBatteryWarningLevel:];
-[W5PowerStatus setInternalBatteryLevel:];
```
