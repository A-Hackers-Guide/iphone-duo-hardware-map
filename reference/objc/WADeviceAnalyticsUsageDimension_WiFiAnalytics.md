# `WADeviceAnalyticsUsageDimension`

- Image: [`/System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics`](../userland/System__Library__PrivateFrameworks__WiFiAnalytics.framework__WiFiAnalytics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 5 instance variables, 5 properties, 14 instance methods, 4 class methods

## Instance variables

```
@"NSString" _dimension;
q _inf;
Q _useAs;
@"NSPredicate" _filterPredicate;
@"NSEntityDescription" _entity;
```

## Properties

```
@property (T@"NSString",&,V_dimension) dimension;
@property (TQ,V_useAs) useAs;
@property (T@"NSPredicate",&,V_filterPredicate) filterPredicate;
@property (Tq,V_inf) inf;
@property (T@"NSEntityDescription",&,V_entity) entity;
```

## Class methods

```
+[WADeviceAnalyticsUsageDimension dimensionWith:forEntity:];
+[WADeviceAnalyticsUsageDimension dimensionsUsedAsFilterIn:];
+[WADeviceAnalyticsUsageDimension dimensionsUsedAsGroupBy:];
+[WADeviceAnalyticsUsageDimension usedDimensionsIn:];
```

## Instance methods

```
-[WADeviceAnalyticsUsageDimension dimension];
-[WADeviceAnalyticsUsageDimension filterPredicate];
-[WADeviceAnalyticsUsageDimension setFilterPredicate:];
-[WADeviceAnalyticsUsageDimension setEntity:];
-[WADeviceAnalyticsUsageDimension setUseAs:];
-[WADeviceAnalyticsUsageDimension setDimension:];
-[WADeviceAnalyticsUsageDimension entity];
-[WADeviceAnalyticsUsageDimension description];
-[WADeviceAnalyticsUsageDimension copyWithZone:];
-[WADeviceAnalyticsUsageDimension useAs];
-[WADeviceAnalyticsUsageDimension setInf:];
-[WADeviceAnalyticsUsageDimension inf];
-[WADeviceAnalyticsUsageDimension useDimensionAs:withPredicate:withError:];
-[WADeviceAnalyticsUsageDimension useDimensionAsGroupBy];
```
