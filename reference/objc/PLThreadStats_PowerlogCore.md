# `PLThreadStats`

- Image: [`/System/Library/PrivateFrameworks/PowerlogCore.framework/PowerlogCore`](../userland/System__Library__PrivateFrameworks__PowerlogCore.framework__PowerlogCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 14 instance methods, 1 class methods

## Instance variables

```
@"NSDictionary" _processThreadMap;
d _absoluteTimeFilter;
Q _percentTimeFilter;
@"NSDictionary" _currentSnapshot;
```

## Properties

```
@property (T@"NSDictionary",&,V_processThreadMap) processThreadMap;
@property (Td,V_absoluteTimeFilter) absoluteTimeFilter;
@property (TQ,V_percentTimeFilter) percentTimeFilter;
@property (T@"NSDictionary",&,V_currentSnapshot) currentSnapshot;
```

## Class methods

```
+[PLThreadStats getThreadName:inProcess:isNamed:];
```

## Instance methods

```
-[PLThreadStats currentSnapshot];
-[PLThreadStats setCurrentSnapshot:];
-[PLThreadStats absoluteTimeFilter];
-[PLThreadStats diffSinceLastSnapshot];
-[PLThreadStats diffSnapshotWithNew:andOld:];
-[PLThreadStats filterDiff:];
-[PLThreadStats initWithTimeFilter:withPercentFilter:withProcessThreadMapping:withError:];
-[PLThreadStats percentTimeFilter];
-[PLThreadStats processThreadMap];
-[PLThreadStats setAbsoluteTimeFilter:];
-[PLThreadStats setPercentTimeFilter:];
-[PLThreadStats setProcessThreadMap:];
-[PLThreadStats shouldGatherStatsForProcessName:];
-[PLThreadStats shouldIncludeThread:withTotalSystemTime:withTotalUserTime:];
```
