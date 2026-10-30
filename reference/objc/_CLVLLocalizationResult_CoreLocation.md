# `_CLVLLocalizationResult`

- Image: [`/System/Library/Frameworks/CoreLocation.framework/CoreLocation`](../userland/System__Library__Frameworks__CoreLocation.framework__CoreLocation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 7 instance variables, 7 properties, 22 instance methods, 1 class methods

## Instance variables

```
f _confidence;
d _timestamp;
d _continuousTimestamp;
@"_CLVLLocalizationDebugInfo" _debugInfo;
{?="coordinate""horizontalAccuracy"d} _location;
{?="columns"[4]} _transform;
{?="v"[6[6f]]} _covariance;
```

## Properties

```
@property (Td,N,V_timestamp) timestamp;
@property (Td,N,V_continuousTimestamp) continuousTimestamp;
@property (T{?=d},N,V_location) location;
@property (T{?=[4]},N,V_transform) transform;
@property (T{?=[6[6f]]},N,V_covariance) covariance;
@property (Tf,N,V_confidence) confidence;
@property (T@"_CLVLLocalizationDebugInfo",C,N,V_debugInfo) debugInfo;
```

## Class methods

```
+[_CLVLLocalizationResult supportsSecureCoding];
```

## Instance methods

```
-[_CLVLLocalizationResult setTimestamp:];
-[_CLVLLocalizationResult debugInfo];
-[_CLVLLocalizationResult location];
-[_CLVLLocalizationResult setDebugInfo:];
-[_CLVLLocalizationResult dealloc];
-[_CLVLLocalizationResult timestamp];
-[_CLVLLocalizationResult setTransform:];
-[_CLVLLocalizationResult transform];
-[_CLVLLocalizationResult setConfidence:];
-[_CLVLLocalizationResult setLocation:];
-[_CLVLLocalizationResult encodeWithCoder:];
-[_CLVLLocalizationResult description];
-[_CLVLLocalizationResult initWithCoder:];
-[_CLVLLocalizationResult copyWithZone:];
-[_CLVLLocalizationResult confidence];
-[_CLVLLocalizationResult continuousTimestamp];
-[_CLVLLocalizationResult covariance];
-[_CLVLLocalizationResult descriptionWithMemberIndent:endIndent:];
-[_CLVLLocalizationResult initWithTimestamp:continuousTimestamp:localizationResult:];
-[_CLVLLocalizationResult initWithTimestamp:localizationResult:];
-[_CLVLLocalizationResult setContinuousTimestamp:];
-[_CLVLLocalizationResult setCovariance:];
```
