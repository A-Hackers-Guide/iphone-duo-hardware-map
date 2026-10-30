# `CTDataUsage`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 4 instance variables, 4 properties, 19 instance methods, 1 class methods

## Instance variables

```
Q _cellularHome;
Q _cellularRoaming;
Q _satellite;
Q _wifi;
```

## Properties

```
@property (TQ,N,V_cellularHome) cellularHome;
@property (TQ,N,V_cellularRoaming) cellularRoaming;
@property (TQ,N,V_satellite) satellite;
@property (TQ,N,V_wifi) wifi;
```

## Class methods

```
+[CTDataUsage supportsSecureCoding];
```

## Instance methods

```
-[CTDataUsage setWifi:];
-[CTDataUsage cellularHome];
-[CTDataUsage initWithHome:roaming:wifi:];
-[CTDataUsage setSatellite:];
-[CTDataUsage initWithHome:roaming:satellite:];
-[CTDataUsage isEmpty];
-[CTDataUsage encodeWithCoder:];
-[CTDataUsage hash];
-[CTDataUsage description];
-[CTDataUsage satellite];
-[CTDataUsage initWithCoder:];
-[CTDataUsage wifi];
-[CTDataUsage addUsage:];
-[CTDataUsage copyWithZone:];
-[CTDataUsage cellularRoaming];
-[CTDataUsage initWithHome:roaming:];
-[CTDataUsage isEqual:];
-[CTDataUsage setCellularRoaming:];
-[CTDataUsage setCellularHome:];
```
