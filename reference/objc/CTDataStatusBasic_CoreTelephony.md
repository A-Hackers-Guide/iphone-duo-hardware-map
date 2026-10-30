# `CTDataStatusBasic`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 6 instance variables, 6 properties, 16 instance methods, 1 class methods

## Instance variables

```
B _attached;
B _hasIndicator;
B _inHomeCountry;
B _roamAllowed;
B _cellularDataPossible;
B _newRadioCoverage;
```

## Properties

```
@property (TB,N,V_attached) attached;
@property (TB,N,V_hasIndicator) hasIndicator;
@property (TB,N,V_inHomeCountry) inHomeCountry;
@property (TB,N,V_roamAllowed) roamAllowed;
@property (TB,N,V_cellularDataPossible) cellularDataPossible;
@property (TB,N,V_newRadioCoverage) newRadioCoverage;
```

## Class methods

```
+[CTDataStatusBasic supportsSecureCoding];
```

## Instance methods

```
-[CTDataStatusBasic hasIndicator];
-[CTDataStatusBasic roamAllowed];
-[CTDataStatusBasic setCellularDataPossible:];
-[CTDataStatusBasic cellularDataPossible];
-[CTDataStatusBasic encodeWithCoder:];
-[CTDataStatusBasic setInHomeCountry:];
-[CTDataStatusBasic setHasIndicator:];
-[CTDataStatusBasic description];
-[CTDataStatusBasic initWithCoder:];
-[CTDataStatusBasic setNewRadioCoverage:];
-[CTDataStatusBasic newRadioCoverage];
-[CTDataStatusBasic setRoamAllowed:];
-[CTDataStatusBasic copyWithZone:];
-[CTDataStatusBasic inHomeCountry];
-[CTDataStatusBasic setAttached:];
-[CTDataStatusBasic attached];
```
