# `CAFPointOfInterest`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 6 properties, 9 instance methods, 0 class methods

## Instance variables

```
I _locationThreshold;
@"NSArray" _entryPoints;
@"CAFCoordinate" _location;
@"NSString" _userVisibleAddress;
@"NSString" _userVisibleName;
```

## Properties

```
@property (T@"NSArray",R,C,N,V_entryPoints) entryPoints;
@property (T@"CAFCoordinate",R,N,V_location) location;
@property (TI,R,N,V_locationThreshold) locationThreshold;
@property (T@"NSString",R,C,N,V_userVisibleAddress) userVisibleAddress;
@property (T@"NSString",R,C,N,V_userVisibleName) userVisibleName;
@property (T@"NSDictionary",R,N) dictionaryRepresentation;
```

## Instance methods

```
-[CAFPointOfInterest initWithDictionary:];
-[CAFPointOfInterest location];
-[CAFPointOfInterest description];
-[CAFPointOfInterest dictionaryRepresentation];
-[CAFPointOfInterest entryPoints];
-[CAFPointOfInterest userVisibleName];
-[CAFPointOfInterest initWithEntryPoints:location:locationThreshold:userVisibleAddress:userVisibleName:];
-[CAFPointOfInterest locationThreshold];
-[CAFPointOfInterest userVisibleAddress];
```
