# `NIDLTDOACoordinatesUpdate`

- Image: [`/System/Library/Frameworks/NearbyInteraction.framework/NearbyInteraction`](../userland/System__Library__Frameworks__NearbyInteraction.framework__NearbyInteraction.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 2 instance variables, 2 properties, 9 instance methods, 1 class methods

## Instance variables

```
q _coordinatesType;
_coordinates;
```

## Properties

```
@property (Tq,R,N,V_coordinatesType) coordinatesType;
@property (T,R,N,V_coordinates) coordinates;
```

## Class methods

```
+[NIDLTDOACoordinatesUpdate supportsSecureCoding];
```

## Instance methods

```
-[NIDLTDOACoordinatesUpdate encodeWithCoder:];
-[NIDLTDOACoordinatesUpdate hash];
-[NIDLTDOACoordinatesUpdate description];
-[NIDLTDOACoordinatesUpdate initWithCoder:];
-[NIDLTDOACoordinatesUpdate copyWithZone:];
-[NIDLTDOACoordinatesUpdate isEqual:];
-[NIDLTDOACoordinatesUpdate coordinates];
-[NIDLTDOACoordinatesUpdate coordinatesType];
-[NIDLTDOACoordinatesUpdate initWithDLTDOACoordinatesType:coordinates:];
```
