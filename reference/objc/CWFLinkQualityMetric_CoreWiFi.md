# `CWFLinkQualityMetric`

- Image: [`/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`](../userland/System__Library__PrivateFrameworks__CoreWiFi.framework__CoreWiFi.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CWFJSONEncodable`, `NSCopying`, `NSSecureCoding`
- 2 instance variables, 13 properties, 19 instance methods, 1 class methods

## Instance variables

```
@"NSDate" _updatedAt;
@"NSData" _linkQualityMetricData;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSDate",C,N,V_updatedAt) updatedAt;
@property (Tq,R,D,N) RSSI;
@property (Tq,R,D,N) noise;
@property (Td,R,D,N) txRate;
@property (Td,R,D,N) rxRate;
@property (TQ,R,N) txPacketErrorRate;
@property (TQ,R,D,N) CCA;
@property (T@"NSArray",R,N) mLOLinks;
@property (T@"NSData",C,N,V_linkQualityMetricData) linkQualityMetricData;
```

## Class methods

```
+[CWFLinkQualityMetric supportsSecureCoding];
```

## Instance methods

```
-[CWFLinkQualityMetric rxRate];
-[CWFLinkQualityMetric txRate];
-[CWFLinkQualityMetric JSONCompatibleKeyValueMap];
-[CWFLinkQualityMetric CCA];
-[CWFLinkQualityMetric noise];
-[CWFLinkQualityMetric RSSI];
-[CWFLinkQualityMetric updatedAt];
-[CWFLinkQualityMetric setUpdatedAt:];
-[CWFLinkQualityMetric encodeWithCoder:];
-[CWFLinkQualityMetric hash];
-[CWFLinkQualityMetric description];
-[CWFLinkQualityMetric initWithCoder:];
-[CWFLinkQualityMetric copyWithZone:];
-[CWFLinkQualityMetric isEqual:];
-[CWFLinkQualityMetric linkQualityMetricData];
-[CWFLinkQualityMetric isEqualToLinkQualityMetric:];
-[CWFLinkQualityMetric mLOLinks];
-[CWFLinkQualityMetric setLinkQualityMetricData:];
-[CWFLinkQualityMetric txPacketErrorRate];
```
