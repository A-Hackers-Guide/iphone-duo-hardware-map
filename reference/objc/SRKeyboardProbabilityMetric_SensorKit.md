# `SRKeyboardProbabilityMetric`

- Image: [`/System/Library/Frameworks/SensorKit.framework/SensorKit`](../userland/System__Library__Frameworks__SensorKit.framework__SensorKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 3 instance variables, 4 properties, 14 instance methods, 1 class methods

## Instance variables

```
@"NSUnit" _unitType;
q _totalDataSamples;
@"NSMutableArray" _mutableSampleValues;
```

## Properties

```
@property (T@"NSUnit",C,V_unitType) unitType;
@property (Tq,N,V_totalDataSamples) totalDataSamples;
@property (T@"NSMutableArray",&,V_mutableSampleValues) mutableSampleValues;
@property (T@"NSArray",R,C) distributionSampleValues;
```

## Class methods

```
+[SRKeyboardProbabilityMetric supportsSecureCoding];
```

## Instance methods

```
-[SRKeyboardProbabilityMetric setUnitType:];
-[SRKeyboardProbabilityMetric init];
-[SRKeyboardProbabilityMetric dealloc];
-[SRKeyboardProbabilityMetric unitType];
-[SRKeyboardProbabilityMetric encodeWithCoder:];
-[SRKeyboardProbabilityMetric description];
-[SRKeyboardProbabilityMetric initWithCoder:];
-[SRKeyboardProbabilityMetric isEqual:];
-[SRKeyboardProbabilityMetric sr_dictionaryRepresentation];
-[SRKeyboardProbabilityMetric mutableSampleValues];
-[SRKeyboardProbabilityMetric totalDataSamples];
-[SRKeyboardProbabilityMetric distributionSampleValues];
-[SRKeyboardProbabilityMetric setMutableSampleValues:];
-[SRKeyboardProbabilityMetric setTotalDataSamples:];
```
