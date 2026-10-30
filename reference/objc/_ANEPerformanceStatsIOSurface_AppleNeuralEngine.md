# `_ANEPerformanceStatsIOSurface`

- Image: [`/System/Library/PrivateFrameworks/AppleNeuralEngine.framework/AppleNeuralEngine`](../userland/System__Library__PrivateFrameworks__AppleNeuralEngine.framework__AppleNeuralEngine.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 5 instance methods, 2 class methods

## Instance variables

```
q _statType;
@"_ANEIOSurfaceObject" _stats;
```

## Properties

```
@property (Tq,R,N,V_statType) statType;
@property (T@"_ANEIOSurfaceObject",R,N,V_stats) stats;
```

## Class methods

```
+[_ANEPerformanceStatsIOSurface new];
+[_ANEPerformanceStatsIOSurface objectWithIOSurface:statType:];
```

## Instance methods

```
-[_ANEPerformanceStatsIOSurface init];
-[_ANEPerformanceStatsIOSurface stats];
-[_ANEPerformanceStatsIOSurface description];
-[_ANEPerformanceStatsIOSurface initWithIOSurface:statType:];
-[_ANEPerformanceStatsIOSurface statType];
```
