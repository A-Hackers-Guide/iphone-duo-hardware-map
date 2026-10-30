# `PLBLDService`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PLBatteryBreakdownService`
- 2 instance variables, 2 properties, 8 instance methods, 3 class methods

## Instance variables

```
@"PLXPCResponderOperatorComposition" _batteryBreakdownResponder;
@"PLXPCResponderOperatorComposition" _logBUIResultsResponder;
```

## Properties

```
@property (T@"PLXPCResponderOperatorComposition",&,V_batteryBreakdownResponder) batteryBreakdownResponder;
@property (T@"PLXPCResponderOperatorComposition",&,V_logBUIResultsResponder) logBUIResultsResponder;
```

## Class methods

```
+[PLBLDService entryEventPointDefinitions];
+[PLBLDService load];
+[PLBLDService entryEventPointBLD];
```

## Instance methods

```
-[PLBLDService init];
-[PLBLDService initOperatorDependancies];
-[PLBLDService batteryBreakdownResponder];
-[PLBLDService batteryBreakdownWithPayload:];
-[PLBLDService bldEntryWithBatteryBreakdown:];
-[PLBLDService logBUIResultsResponder];
-[PLBLDService setBatteryBreakdownResponder:];
-[PLBLDService setLogBUIResultsResponder:];
```
