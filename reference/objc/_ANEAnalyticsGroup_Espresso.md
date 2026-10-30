# `_ANEAnalyticsGroup`

- Image: [`/System/Library/PrivateFrameworks/Espresso.framework/Espresso`](../userland/System__Library__PrivateFrameworks__Espresso.framework__Espresso.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 5 instance methods, 1 class methods

## Instance variables

```
@"NSNumber" _groupID;
@"NSArray" _layerInfo;
@"NSArray" _taskInfo;
```

## Properties

```
@property (T@"NSNumber",R,N,V_groupID) groupID;
@property (T@"NSArray",R,N,V_layerInfo) layerInfo;
@property (T@"NSArray",R,N,V_taskInfo) taskInfo;
```

## Class methods

```
+[_ANEAnalyticsGroup objectWithID:layers:tasks:];
```

## Instance methods

```
-[_ANEAnalyticsGroup groupID];
-[_ANEAnalyticsGroup taskInfo];
-[_ANEAnalyticsGroup serialize];
-[_ANEAnalyticsGroup initWithID:layers:tasks:];
-[_ANEAnalyticsGroup layerInfo];
```
