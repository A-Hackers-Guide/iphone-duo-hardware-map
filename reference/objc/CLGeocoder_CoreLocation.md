# `CLGeocoder`

- Image: [`/System/Library/Frameworks/CoreLocation.framework/CoreLocation`](../userland/System__Library__Frameworks__CoreLocation.framework__CoreLocation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 2 properties, 29 instance methods, 2 class methods

## Instance variables

```
@"CLGeocoderInternal" _internal;
```

## Properties

```
@property (T@"CLSilo",S_setResponseSilo:) _responseSilo;
@property (TB,R,N,GisGeocoding) geocoding;
```

## Class methods

```
+[CLGeocoder _timeZoneAtLocation:];
+[CLGeocoder hydrateGeoMapItemLocallyFromHandle:completionHandler:];
```

## Instance methods

```
-[CLGeocoder isGeocoding];
-[CLGeocoder cancelGeocode];
-[CLGeocoder geocodeAddressString:inRegion:completionHandler:];
-[CLGeocoder reverseGeocodeLocation:heading:localResultsOnly:completionHandler:];
-[CLGeocoder _ticket:didReturnError:partialResultForLocation:];
-[CLGeocoder init];
-[CLGeocoder dealloc];
-[CLGeocoder _ticket:didReturnError:];
-[CLGeocoder _notifyResult:error:];
-[CLGeocoder _notifyPartialResult:];
-[CLGeocoder _notifyCancel];
-[CLGeocoder reverseGeocodeLocation:preferredLocale:heading:localResultsOnly:completionHandler:];
-[CLGeocoder geocodePostalAddress:preferredLocale:completionHandler:];
-[CLGeocoder geocodeAddressString:inRegion:preferredLocale:completionHandler:];
-[CLGeocoder _notifyNoResult];
-[CLGeocoder _responseSilo];
-[CLGeocoder reverseGeocodeLocation:preferredLocale:completionHandler:];
-[CLGeocoder geocodeAddressDictionary:preferredLocale:completionHandler:];
-[CLGeocoder reverseGeocodeLocation:heading:completionHandler:];
-[CLGeocoder _notifyResult:];
-[CLGeocoder geocodeAddressString:completionHandler:];
-[CLGeocoder geocodeAddressDictionary:completionHandler:];
-[CLGeocoder _ticket:didReturnGeoMapItems:];
-[CLGeocoder _notifyError:];
-[CLGeocoder geocodePostalAddress:completionHandler:];
-[CLGeocoder reverseGeocodeLocation:localResultsOnly:completionHandler:];
-[CLGeocoder geocodeAddressString:inRegionCenteredAt:inRegionRadius:preferredLocale:completionHandler:];
-[CLGeocoder reverseGeocodeLocation:completionHandler:];
-[CLGeocoder _setResponseSilo:];
```
