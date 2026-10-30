# `CMSedentaryRestingHeartRateData`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 2 instance variables, 2 properties, 10 instance methods, 1 class methods

## Instance variables

```
f fOneDayHR;
f fSevenDayHR;
```

## Properties

```
@property (Tf,R,N) oneDayHR;
@property (Tf,R,N) sevenDayHR;
```

## Class methods

```
+[CMSedentaryRestingHeartRateData supportsSecureCoding];
```

## Instance methods

```
-[CMSedentaryRestingHeartRateData dealloc];
-[CMSedentaryRestingHeartRateData encodeWithCoder:];
-[CMSedentaryRestingHeartRateData hash];
-[CMSedentaryRestingHeartRateData description];
-[CMSedentaryRestingHeartRateData initWithCoder:];
-[CMSedentaryRestingHeartRateData copyWithZone:];
-[CMSedentaryRestingHeartRateData isEqual:];
-[CMSedentaryRestingHeartRateData initWithOneDayHR:sevenDayHR:];
-[CMSedentaryRestingHeartRateData oneDayHR];
-[CMSedentaryRestingHeartRateData sevenDayHR];
```
