# `PLIOReportAgentIOReportStats`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PLIOReportStats`
- 3 instance variables, 3 properties, 10 instance methods, 7 class methods

## Instance variables

```
@"PLAgent" _agent;
Q _sampleAPAwakeTime;
@"PLTimer" _halfHourTimer;
```

## Properties

```
@property (T@"PLAgent",&,V_agent) agent;
@property (TQ,V_sampleAPAwakeTime) sampleAPAwakeTime;
@property (T@"PLTimer",&,V_halfHourTimer) halfHourTimer;
```

## Class methods

```
+[PLIOReportAgentIOReportStats entryEventBackwardDefinitions];
+[PLIOReportAgentIOReportStats shouldLogSoCStatsPMGRCountersID];
+[PLIOReportAgentIOReportStats columnNameForChannelID:];
+[PLIOReportAgentIOReportStats entryEventBackwardDefinitionSoCStatsPMGRCountersDebug];
+[PLIOReportAgentIOReportStats entryEventBackwardDefinitionSoCStatsPMGRCountersID];
+[PLIOReportAgentIOReportStats idNumberFromIDDiff:];
+[PLIOReportAgentIOReportStats maskedNameForChannelID:];
```

## Instance methods

```
-[PLIOReportAgentIOReportStats init];
-[PLIOReportAgentIOReportStats agent];
-[PLIOReportAgentIOReportStats setAgent:];
-[PLIOReportAgentIOReportStats initTaskOperatorDependancies];
-[PLIOReportAgentIOReportStats halfHourTimer];
-[PLIOReportAgentIOReportStats initWithAgent:];
-[PLIOReportAgentIOReportStats logEventBackwardSoCStatsPMGRCounters];
-[PLIOReportAgentIOReportStats sampleAPAwakeTime];
-[PLIOReportAgentIOReportStats setHalfHourTimer:];
-[PLIOReportAgentIOReportStats setSampleAPAwakeTime:];
```
