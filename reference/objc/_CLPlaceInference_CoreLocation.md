# `_CLPlaceInference`

- Image: [`/System/Library/Frameworks/CoreLocation.framework/CoreLocation`](../userland/System__Library__Frameworks__CoreLocation.framework__CoreLocation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 7 instance variables, 7 properties, 14 instance methods, 3 class methods

## Instance variables

```
Q _userType;
Q _placeType;
@"CLPlacemark" _placemark;
@"CLLocation" _referenceLocation;
d _confidence;
@"NSString" _preferredName;
@"NSUUID" __loiIdentifier;
```

## Properties

```
@property (TQ,R,N,V_userType) userType;
@property (TQ,R,N,V_placeType) placeType;
@property (T@"CLPlacemark",R,N,V_placemark) placemark;
@property (T@"CLLocation",R,N,V_referenceLocation) referenceLocation;
@property (Td,R,N,V_confidence) confidence;
@property (T@"NSString",R,N,V_preferredName) preferredName;
@property (T@"NSUUID",R,N,V__loiIdentifier) _loiIdentifier;
```

## Class methods

```
+[_CLPlaceInference supportsSecureCoding];
+[_CLPlaceInference _placeInferencePlaceTypeFromRTPlaceType:];
+[_CLPlaceInference _userSpecificPlaceTypeFromRTUserType:];
```

## Instance methods

```
-[_CLPlaceInference placemark];
-[_CLPlaceInference placeType];
-[_CLPlaceInference dealloc];
-[_CLPlaceInference referenceLocation];
-[_CLPlaceInference _loiIdentifier];
-[_CLPlaceInference _initWithRTPlaceInference:];
-[_CLPlaceInference encodeWithCoder:];
-[_CLPlaceInference description];
-[_CLPlaceInference initWithCoder:];
-[_CLPlaceInference initWithUserType:placeType:placemark:referenceLocation:confidence:preferredName:loiIdentifier:];
-[_CLPlaceInference preferredName];
-[_CLPlaceInference copyWithZone:];
-[_CLPlaceInference userType];
-[_CLPlaceInference confidence];
```
