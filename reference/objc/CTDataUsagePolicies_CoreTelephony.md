# `CTDataUsagePolicies`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 6 instance variables, 6 properties, 21 instance methods, 1 class methods

## Instance variables

```
B _isManaged;
B _isRestricted;
@"NSString" _bundleId;
q _cellular;
q _satellite;
q _wifi;
```

## Properties

```
@property (T@"NSString",&,N,V_bundleId) bundleId;
@property (Tq,N,V_cellular) cellular;
@property (Tq,N,V_satellite) satellite;
@property (Tq,N,V_wifi) wifi;
@property (TB,N,V_isManaged) isManaged;
@property (TB,N,V_isRestricted) isRestricted;
```

## Class methods

```
+[CTDataUsagePolicies supportsSecureCoding];
```

## Instance methods

```
-[CTDataUsagePolicies setIsManaged:];
-[CTDataUsagePolicies isRestricted];
-[CTDataUsagePolicies cellular];
-[CTDataUsagePolicies isManaged];
-[CTDataUsagePolicies setWifi:];
-[CTDataUsagePolicies setBundleId:];
-[CTDataUsagePolicies init:withCellularPolicy:andWifiPolicy:];
-[CTDataUsagePolicies setSatellite:];
-[CTDataUsagePolicies init:withCellularPolicy:satellitePolicy:wifiPolicy:isManaged:andIsRestricted:];
-[CTDataUsagePolicies bundleId];
-[CTDataUsagePolicies init:withCellularPolicy:wifiPolicy:isManaged:andIsRestricted:];
-[CTDataUsagePolicies encodeWithCoder:];
-[CTDataUsagePolicies hash];
-[CTDataUsagePolicies setIsRestricted:];
-[CTDataUsagePolicies description];
-[CTDataUsagePolicies satellite];
-[CTDataUsagePolicies initWithCoder:];
-[CTDataUsagePolicies wifi];
-[CTDataUsagePolicies setCellular:];
-[CTDataUsagePolicies copyWithZone:];
-[CTDataUsagePolicies isEqual:];
```
