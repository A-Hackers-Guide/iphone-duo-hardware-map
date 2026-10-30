# `PLMetric`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 7 properties, 19 instance methods, 2 class methods

## Instance variables

```
s _metricType;
i _metricValue;
i _numBits;
i _defaultValue;
@"NSString" _metricKey;
@"NSDate" _lastOnTimestamp;
Q _bitPosition;
```

## Properties

```
@property (T@"NSString",&,V_metricKey) metricKey;
@property (Ts,V_metricType) metricType;
@property (T@"NSDate",&,V_lastOnTimestamp) lastOnTimestamp;
@property (Ti,V_metricValue) metricValue;
@property (TQ,V_bitPosition) bitPosition;
@property (Ti,V_numBits) numBits;
@property (Ti,V_defaultValue) defaultValue;
```

## Class methods

```
+[PLMetric binBatteryTemperature:];
+[PLMetric binDurationValue:];
```

## Instance methods

```
-[PLMetric setDefaultValue:];
-[PLMetric setMetricType:];
-[PLMetric metricType];
-[PLMetric defaultValue];
-[PLMetric resetMetric];
-[PLMetric setMetricValue:];
-[PLMetric metricValue];
-[PLMetric setBitPosition:];
-[PLMetric bitPosition];
-[PLMetric metricKey];
-[PLMetric setMetricKey:];
-[PLMetric numBits];
-[PLMetric lastOnTimestamp];
-[PLMetric constructMetricValueForInterval:];
-[PLMetric getBinnedMetricValue];
-[PLMetric initWithKey:withPosition:withNumBits:withDefault:andType:];
-[PLMetric setLastOnTimestamp:];
-[PLMetric setNumBits:];
-[PLMetric updateMetricWithTimestamp:forEvent:withValue:];
```
