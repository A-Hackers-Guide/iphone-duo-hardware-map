# `CLRecentLocationsFetchOptions`

- Image: [`/System/Library/Frameworks/CoreLocation.framework/CoreLocation`](../userland/System__Library__Frameworks__CoreLocation.framework__CoreLocation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 6 instance variables, 6 properties, 25 instance methods, 1 class methods

## Instance variables

```
B _returnSparseLocations;
B _allowDelayedResponse;
B _requireWirelessClientLocation;
@"NSDate" _date;
@"NSNumber" _machContinuousTimeSeconds;
@"NSNumber" _numberOfSeconds;
```

## Properties

```
@property (T@"NSDate",R,C,N,V_date) date;
@property (T@"NSNumber",R,C,N,V_machContinuousTimeSeconds) machContinuousTimeSeconds;
@property (T@"NSNumber",R,C,N,V_numberOfSeconds) numberOfSeconds;
@property (TB,R,N,V_returnSparseLocations) returnSparseLocations;
@property (TB,R,N,V_allowDelayedResponse) allowDelayedResponse;
@property (TB,R,N,V_requireWirelessClientLocation) requireWirelessClientLocation;
```

## Class methods

```
+[CLRecentLocationsFetchOptions supportsSecureCoding];
```

## Instance methods

```
-[CLRecentLocationsFetchOptions initWithDate:];
-[CLRecentLocationsFetchOptions dealloc];
-[CLRecentLocationsFetchOptions isEqualToFetchOptions:];
-[CLRecentLocationsFetchOptions date];
-[CLRecentLocationsFetchOptions encodeWithCoder:];
-[CLRecentLocationsFetchOptions hash];
-[CLRecentLocationsFetchOptions description];
-[CLRecentLocationsFetchOptions initWithCoder:];
-[CLRecentLocationsFetchOptions copyWithZone:];
-[CLRecentLocationsFetchOptions isEqual:];
-[CLRecentLocationsFetchOptions numberOfSeconds];
-[CLRecentLocationsFetchOptions allowDelayedResponse];
-[CLRecentLocationsFetchOptions initRequireWirelessClientLocationWithAllowDelayedResponse:];
-[CLRecentLocationsFetchOptions initWithDate:allowDelayedResponse:];
-[CLRecentLocationsFetchOptions initWithDate:machContinuousTimeSeconds:numberOfSeconds:allowDelayedResponse:returnSparseLocations:requireWirelessClientLocation:];
-[CLRecentLocationsFetchOptions initWithMachContinuousTimeSeconds:];
-[CLRecentLocationsFetchOptions initWithMachContinuousTimeSeconds:allowDelayedResponse:];
-[CLRecentLocationsFetchOptions initWithNumberOfSeconds:];
-[CLRecentLocationsFetchOptions initWithNumberOfSeconds:allowDelayedResponse:];
-[CLRecentLocationsFetchOptions initWithNumberOfSeconds:allowDelayedResponse:returnSparseLocations:];
-[CLRecentLocationsFetchOptions initWithNumberOfSeconds:allowDelayedResponse:returnSparseLocations:requireWirelessClientLocation:];
-[CLRecentLocationsFetchOptions initWithNumberOfSeconds:returnSparseLocations:];
-[CLRecentLocationsFetchOptions machContinuousTimeSeconds];
-[CLRecentLocationsFetchOptions requireWirelessClientLocation];
-[CLRecentLocationsFetchOptions returnSparseLocations];
```
