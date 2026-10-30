# `CTTravelPredictionInfo`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 10 instance variables, 10 properties, 25 instance methods, 1 class methods

## Instance variables

```
B _belongsToUser;
@"NSString" _departureAirportCode;
@"NSNumber" _departureAirportLat;
@"NSNumber" _departureAirportLong;
@"NSNumber" _departureTime;
@"NSString" _arrivalAirportCode;
@"NSNumber" _arrivalAirportLat;
@"NSNumber" _arrivalAirportLong;
@"NSNumber" _arrivalTime;
@"NSString" _extractionSource;
```

## Properties

```
@property (T@"NSString",&,V_departureAirportCode) departureAirportCode;
@property (T@"NSNumber",&,V_departureAirportLat) departureAirportLat;
@property (T@"NSNumber",&,V_departureAirportLong) departureAirportLong;
@property (T@"NSNumber",&,V_departureTime) departureTime;
@property (T@"NSString",&,V_arrivalAirportCode) arrivalAirportCode;
@property (T@"NSNumber",&,V_arrivalAirportLat) arrivalAirportLat;
@property (T@"NSNumber",&,V_arrivalAirportLong) arrivalAirportLong;
@property (T@"NSNumber",&,V_arrivalTime) arrivalTime;
@property (T@"NSString",&,V_extractionSource) extractionSource;
@property (TB,V_belongsToUser) belongsToUser;
```

## Class methods

```
+[CTTravelPredictionInfo supportsSecureCoding];
```

## Instance methods

```
-[CTTravelPredictionInfo departureTime];
-[CTTravelPredictionInfo init];
-[CTTravelPredictionInfo encodeWithCoder:];
-[CTTravelPredictionInfo description];
-[CTTravelPredictionInfo initWithCoder:];
-[CTTravelPredictionInfo setDepartureTime:];
-[CTTravelPredictionInfo isEqual:];
-[CTTravelPredictionInfo setArrivalTime:];
-[CTTravelPredictionInfo arrivalTime];
-[CTTravelPredictionInfo arrivalAirportCode];
-[CTTravelPredictionInfo arrivalAirportLat];
-[CTTravelPredictionInfo arrivalAirportLong];
-[CTTravelPredictionInfo belongsToUser];
-[CTTravelPredictionInfo departureAirportCode];
-[CTTravelPredictionInfo departureAirportLat];
-[CTTravelPredictionInfo departureAirportLong];
-[CTTravelPredictionInfo extractionSource];
-[CTTravelPredictionInfo setArrivalAirportCode:];
-[CTTravelPredictionInfo setArrivalAirportLat:];
-[CTTravelPredictionInfo setArrivalAirportLong:];
-[CTTravelPredictionInfo setBelongsToUser:];
-[CTTravelPredictionInfo setDepartureAirportCode:];
-[CTTravelPredictionInfo setDepartureAirportLat:];
-[CTTravelPredictionInfo setDepartureAirportLong:];
-[CTTravelPredictionInfo setExtractionSource:];
```
