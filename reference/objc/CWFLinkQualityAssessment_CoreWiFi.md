# `CWFLinkQualityAssessment`

- Image: [`/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`](../userland/System__Library__PrivateFrameworks__CoreWiFi.framework__CoreWiFi.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CWFJSONEncodable`, `NSCopying`, `NSSecureCoding`
- 5 instance variables, 9 properties, 21 instance methods, 2 class methods

## Instance variables

```
@"NSDate" _updatedAt;
q _qualityAssessment;
Q _estimatedMaxThroughputMbps;
Q _estimatedMedianLatencyMs;
q _RSSI;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (Tq,N,V_qualityAssessment) qualityAssessment;
@property (TQ,N,V_estimatedMaxThroughputMbps) estimatedMaxThroughputMbps;
@property (TQ,N,V_estimatedMedianLatencyMs) estimatedMedianLatencyMs;
@property (Tq,N,V_RSSI) RSSI;
@property (T@"NSDate",C,N,V_updatedAt) updatedAt;
```

## Class methods

```
+[CWFLinkQualityAssessment supportsSecureCoding];
+[CWFLinkQualityAssessment descriptionForQualityAssessment:];
```

## Instance methods

```
-[CWFLinkQualityAssessment JSONCompatibleKeyValueMap];
-[CWFLinkQualityAssessment setEstimatedMedianLatencyMs:];
-[CWFLinkQualityAssessment isEqualToLinkQualityAssessment:];
-[CWFLinkQualityAssessment setRSSI:];
-[CWFLinkQualityAssessment initWithLinkQualityMetric:];
-[CWFLinkQualityAssessment RSSI];
-[CWFLinkQualityAssessment qualityAssessment];
-[CWFLinkQualityAssessment updatedAt];
-[CWFLinkQualityAssessment initWithLSMData:andlinkQualityMetric:];
-[CWFLinkQualityAssessment setUpdatedAt:];
-[CWFLinkQualityAssessment initWithAssessmentData:];
-[CWFLinkQualityAssessment encodeWithCoder:];
-[CWFLinkQualityAssessment hash];
-[CWFLinkQualityAssessment description];
-[CWFLinkQualityAssessment setQualityAssessment:];
-[CWFLinkQualityAssessment initWithCoder:];
-[CWFLinkQualityAssessment estimatedMedianLatencyMs];
-[CWFLinkQualityAssessment copyWithZone:];
-[CWFLinkQualityAssessment isEqual:];
-[CWFLinkQualityAssessment setEstimatedMaxThroughputMbps:];
-[CWFLinkQualityAssessment estimatedMaxThroughputMbps];
```
