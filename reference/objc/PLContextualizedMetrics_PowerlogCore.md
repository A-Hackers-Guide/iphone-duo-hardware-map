# `PLContextualizedMetrics`

- Image: [`/System/Library/PrivateFrameworks/PowerlogCore.framework/PowerlogCore`](../userland/System__Library__PrivateFrameworks__PowerlogCore.framework__PowerlogCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 2 instance variables, 2 properties, 6 instance methods, 2 class methods

## Instance variables

```
@"NSDictionary" _stateMetrics;
@"NSDictionary" _chunkMetrics;
```

## Properties

```
@property (T@"NSDictionary",R,N,V_stateMetrics) stateMetrics;
@property (T@"NSDictionary",R,N,V_chunkMetrics) chunkMetrics;
```

## Class methods

```
+[PLContextualizedMetrics supportsSecureCoding];
+[PLContextualizedMetrics fromDictionary:];
```

## Instance methods

```
-[PLContextualizedMetrics toDictionary];
-[PLContextualizedMetrics encodeWithCoder:];
-[PLContextualizedMetrics initWithCoder:];
-[PLContextualizedMetrics chunkMetrics];
-[PLContextualizedMetrics initWithStateMetrics:chunkMetrics:];
-[PLContextualizedMetrics stateMetrics];
```
