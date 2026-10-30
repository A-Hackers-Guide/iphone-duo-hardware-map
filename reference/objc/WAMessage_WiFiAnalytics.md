# `WAMessage`

- Image: [`/System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics`](../userland/System__Library__PrivateFrameworks__WiFiAnalytics.framework__WiFiAnalytics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 3 instance variables, 3 properties, 13 instance methods, 1 class methods

## Instance variables

```
@"NSString" _metricName;
@"NSMutableDictionary" _metricInfo;
q _options;
```

## Properties

```
@property (T@"NSString",C,N,V_metricName) metricName;
@property (T@"NSMutableDictionary",C,N,V_metricInfo) metricInfo;
@property (Tq,N,V_options) options;
```

## Class methods

```
+[WAMessage supportsSecureCoding];
```

## Instance methods

```
-[WAMessage setOptions:];
-[WAMessage metricName];
-[WAMessage encodeWithCoder:];
-[WAMessage initWithCoder:];
-[WAMessage metricInfo];
-[WAMessage options];
-[WAMessage copyWithZone:];
-[WAMessage setMetricInfo:];
-[WAMessage setMetricName:];
-[WAMessage addFieldForKey:value:options:];
-[WAMessage addFieldsForChannelFlagLikeKey:value:options:];
-[WAMessage addFieldsFromDictionary:options:];
-[WAMessage initWithMetricName:options:];
```
