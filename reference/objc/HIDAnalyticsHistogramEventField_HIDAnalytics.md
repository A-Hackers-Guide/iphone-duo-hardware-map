# `HIDAnalyticsHistogramEventField`

- Image: [`/System/Library/PrivateFrameworks/HIDAnalytics.framework/HIDAnalytics`](../userland/System__Library__PrivateFrameworks__HIDAnalytics.framework__HIDAnalytics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `HIDAnalyticsEventFieldProtocol`
- 3 instance variables, 6 properties, 7 instance methods, 0 class methods

## Instance variables

```
C _segmentCount;
^{_HIDAnalyticsHistogramSegment=C^{_HIDAnalyticsHistogramBucket}} _segments;
@"NSString" _fieldName;
```

## Properties

```
@property (T@"NSString",R,V_fieldName) fieldName;
@property (T@,W) value;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[HIDAnalyticsHistogramEventField dealloc];
-[HIDAnalyticsHistogramEventField value];
-[HIDAnalyticsHistogramEventField setValue:];
-[HIDAnalyticsHistogramEventField setIntegerValue:];
-[HIDAnalyticsHistogramEventField fieldName];
-[HIDAnalyticsHistogramEventField createBuckets:count:];
-[HIDAnalyticsHistogramEventField initWithAttributes:segments:count:];
```
