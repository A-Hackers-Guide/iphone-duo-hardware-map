# `CTDataSettings`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 3 instance variables, 3 properties, 10 instance methods, 1 class methods

## Instance variables

```
B _cellularDataEnabled;
B _airplaneModeEnabled;
B _cellularDataCapable;
```

## Properties

```
@property (TB,N,GisCellularDataEnabled,V_cellularDataEnabled) cellularDataEnabled;
@property (TB,N,GisAirplaneModeEnabled,V_airplaneModeEnabled) airplaneModeEnabled;
@property (TB,N,GisCellularDataCapable,V_cellularDataCapable) cellularDataCapable;
```

## Class methods

```
+[CTDataSettings supportsSecureCoding];
```

## Instance methods

```
-[CTDataSettings setAirplaneModeEnabled:];
-[CTDataSettings setCellularDataCapable:];
-[CTDataSettings encodeWithCoder:];
-[CTDataSettings isCellularDataEnabled];
-[CTDataSettings description];
-[CTDataSettings isCellularDataCapable];
-[CTDataSettings isAirplaneModeEnabled];
-[CTDataSettings initWithCoder:];
-[CTDataSettings copyWithZone:];
-[CTDataSettings setCellularDataEnabled:];
```
