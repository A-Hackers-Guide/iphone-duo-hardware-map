# `CMOdometerSuitability`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SRSampling`, `NSSecureCoding`, `NSCopying`
- 3 instance variables, 7 properties, 11 instance methods, 1 class methods

## Instance variables

```
B _suitableForRunning;
B _suitableForWalking;
@"NSDate" _startDate;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSDate",R,N,V_startDate) startDate;
@property (TB,R,N,V_suitableForRunning) suitableForRunning;
@property (TB,R,N,V_suitableForWalking) suitableForWalking;
```

## Class methods

```
+[CMOdometerSuitability supportsSecureCoding];
```

## Instance methods

```
-[CMOdometerSuitability startDate];
-[CMOdometerSuitability dealloc];
-[CMOdometerSuitability encodeWithCoder:];
-[CMOdometerSuitability description];
-[CMOdometerSuitability initWithCoder:];
-[CMOdometerSuitability copyWithZone:];
-[CMOdometerSuitability binarySampleRepresentation];
-[CMOdometerSuitability initWithBinarySampleRepresentation:metadata:timestamp:];
-[CMOdometerSuitability initWithStartDate:suitableForRunning:suitableForWalking:];
-[CMOdometerSuitability suitableForRunning];
-[CMOdometerSuitability suitableForWalking];
```
