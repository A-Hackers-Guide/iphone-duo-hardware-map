# `CTEnhancedDataLinkQualityMetric`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CTEnhancedLinkQualityMetric`
- Protocols: `CTXPCLogging`
- 1 instance variables, 3 properties, 9 instance methods, 1 class methods

## Instance variables

```
q _metricType;
```

## Properties

```
@property (Tq,N,V_metricType) metricType;
@property (T@"NSString",R,N) ct_shortName;
@property (T@"NSString",R,N) ct_shortDescription;
```

## Class methods

```
+[CTEnhancedDataLinkQualityMetric supportsSecureCoding];
```

## Instance methods

```
-[CTEnhancedDataLinkQualityMetric ct_shortDescription];
-[CTEnhancedDataLinkQualityMetric setMetricType:];
-[CTEnhancedDataLinkQualityMetric metricType];
-[CTEnhancedDataLinkQualityMetric ct_shortName];
-[CTEnhancedDataLinkQualityMetric encodeWithCoder:];
-[CTEnhancedDataLinkQualityMetric description];
-[CTEnhancedDataLinkQualityMetric initWithCoder:];
-[CTEnhancedDataLinkQualityMetric copyWithZone:];
-[CTEnhancedDataLinkQualityMetric initWithType:enhancedLinkQuality:];
```
