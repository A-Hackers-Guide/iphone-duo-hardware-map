# `PLAWDMetricsService`

- Image: [`/System/Library/PrivateFrameworks/PowerlogFullOperators.framework/PowerlogFullOperators`](../userland/System__Library__PrivateFrameworks__PowerlogFullOperators.framework__PowerlogFullOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PLService`
- 4 instance variables, 4 properties, 13 instance methods, 4 class methods

## Instance variables

```
@"AWDServerConnection" _awdServerConn;
@"NSMutableSet" _currRunningMetrics;
@"NSMutableSet" _updateRunningMetrics;
@"NSMutableDictionary" _classDictionary;
```

## Properties

```
@property (T@"AWDServerConnection",&,V_awdServerConn) awdServerConn;
@property (T@"NSMutableSet",&,V_currRunningMetrics) currRunningMetrics;
@property (T@"NSMutableSet",&,V_updateRunningMetrics) updateRunningMetrics;
@property (T@"NSMutableDictionary",&,V_classDictionary) classDictionary;
```

## Class methods

```
+[PLAWDMetricsService entryEventPointDefinitions];
+[PLAWDMetricsService entryEventNoneDefinitions];
+[PLAWDMetricsService load];
+[PLAWDMetricsService entryAggregateDefinitions];
```

## Instance methods

```
-[PLAWDMetricsService init];
-[PLAWDMetricsService initOperatorDependancies];
-[PLAWDMetricsService classDictionary];
-[PLAWDMetricsService auxClassWrapper:withAction:];
-[PLAWDMetricsService awdServerConn];
-[PLAWDMetricsService connectToAWDServer];
-[PLAWDMetricsService currRunningMetrics];
-[PLAWDMetricsService initAWDInterface];
-[PLAWDMetricsService setAwdServerConn:];
-[PLAWDMetricsService setClassDictionary:];
-[PLAWDMetricsService setCurrRunningMetrics:];
-[PLAWDMetricsService setUpdateRunningMetrics:];
-[PLAWDMetricsService updateRunningMetrics];
```
