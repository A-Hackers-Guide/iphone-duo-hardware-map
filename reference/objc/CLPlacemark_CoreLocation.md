# `CLPlacemark`

- Image: [`/System/Library/Frameworks/CoreLocation.framework/CoreLocation`](../userland/System__Library__Frameworks__CoreLocation.framework__CoreLocation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 1 instance variables, 18 properties, 39 instance methods, 3 class methods

## Instance variables

```
@"CLPlacemarkInternal" _internal;
```

## Properties

```
@property (T@"CNPostalAddress",R,N) postalAddress;
@property (T@"CLLocation",R,C,N) location;
@property (T@"CLRegion",R,C,N) region;
@property (T@"NSTimeZone",R,C,N) timeZone;
@property (T@"NSDictionary",R,C,N) addressDictionary;
@property (T@"NSString",R,C,N) name;
@property (T@"NSString",R,C,N) thoroughfare;
@property (T@"NSString",R,C,N) subThoroughfare;
@property (T@"NSString",R,C,N) locality;
@property (T@"NSString",R,C,N) subLocality;
@property (T@"NSString",R,C,N) administrativeArea;
@property (T@"NSString",R,C,N) subAdministrativeArea;
@property (T@"NSString",R,C,N) postalCode;
@property (T@"NSString",R,C,N) ISOcountryCode;
@property (T@"NSString",R,C,N) country;
@property (T@"NSString",R,C,N) inlandWater;
@property (T@"NSString",R,C,N) ocean;
@property (T@"NSArray",R,C,N) areasOfInterest;
```

## Class methods

```
+[CLPlacemark supportsSecureCoding];
+[CLPlacemark placemarkWithGEOMapItem:];
+[CLPlacemark sourceToString:];
```

## Instance methods

```
-[CLPlacemark region];
-[CLPlacemark addressDictionary];
-[CLPlacemark postalCode];
-[CLPlacemark initWithPlacemark:];
-[CLPlacemark country];
-[CLPlacemark category];
-[CLPlacemark location];
-[CLPlacemark areasOfInterest];
-[CLPlacemark dealloc];
-[CLPlacemark thoroughfare];
-[CLPlacemark muid];
-[CLPlacemark timeZone];
-[CLPlacemark encodeWithCoder:];
-[CLPlacemark locality];
-[CLPlacemark description];
-[CLPlacemark initWithCoder:];
-[CLPlacemark _geoMapItem];
-[CLPlacemark subThoroughfare];
-[CLPlacemark copyWithZone:];
-[CLPlacemark mapItemSource];
-[CLPlacemark name];
-[CLPlacemark formattedAddressLines];
-[CLPlacemark initWithLocation:addressDictionary:region:areasOfInterest:];
-[CLPlacemark postalAddress];
-[CLPlacemark ISOcountryCode];
-[CLPlacemark administrativeArea];
-[CLPlacemark subAdministrativeArea];
-[CLPlacemark subLocality];
-[CLPlacemark fullThoroughfare];
-[CLPlacemark inlandWater];
-[CLPlacemark ocean];
-[CLPlacemark _geoMapItemHandle];
-[CLPlacemark _initWithGeoMapItem:];
-[CLPlacemark _initWithRTMapItem:location:];
-[CLPlacemark fetchFormattedAddress:queue:];
-[CLPlacemark initWithLocation:addressDictionary:region:areasOfInterest:mapItemSource:geoMapItemHandle:category:meCardAddress:];
-[CLPlacemark initWithLocation:addressDictionary:region:areasOfInterest:mapItemSource:geoMapItemHandle:category:meCardAddress:muid:];
-[CLPlacemark initWithLocation:addressDictionary:region:areasOfInterest:mapItemSource:geoMapItemHandle:meCardAddress:];
-[CLPlacemark mecardAddress];
```
