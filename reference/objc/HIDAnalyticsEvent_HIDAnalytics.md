# `HIDAnalyticsEvent`

- Image: [`/System/Library/PrivateFrameworks/HIDAnalytics.framework/HIDAnalytics`](../userland/System__Library__PrivateFrameworks__HIDAnalytics.framework__HIDAnalytics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 3 properties, 18 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _fields;
B _isUpdated;
B _isLogged;
@"NSString" _name;
@"NSDictionary" _desc;
```

## Properties

```
@property (T@"NSString",&,V_name) name;
@property (T@"NSDictionary",&,V_desc) desc;
@property (TB,V_isLogged) isLogged;
```

## Instance methods

```
-[HIDAnalyticsEvent setStringValue:];
-[HIDAnalyticsEvent setDesc:];
-[HIDAnalyticsEvent value];
-[HIDAnalyticsEvent desc];
-[HIDAnalyticsEvent initWithAttributes:description:];
-[HIDAnalyticsEvent setValue:];
-[HIDAnalyticsEvent activate];
-[HIDAnalyticsEvent addField:];
-[HIDAnalyticsEvent setIsLogged:];
-[HIDAnalyticsEvent description];
-[HIDAnalyticsEvent setName:];
-[HIDAnalyticsEvent setIntegerValue:];
-[HIDAnalyticsEvent setStringValue:forField:];
-[HIDAnalyticsEvent addHistogramFieldWithSegments:segments:count:];
-[HIDAnalyticsEvent isLogged];
-[HIDAnalyticsEvent cancel];
-[HIDAnalyticsEvent name];
-[HIDAnalyticsEvent setIntegerValue:forField:];
```
