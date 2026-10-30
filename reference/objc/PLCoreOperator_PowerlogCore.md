# `PLCoreOperator`

- Image: [`/System/Library/PrivateFrameworks/PowerlogCore.framework/PowerlogCore`](../userland/System__Library__PrivateFrameworks__PowerlogCore.framework__PowerlogCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 1 properties, 14 instance methods, 3 class methods

## Instance variables

```
@"NSMutableDictionary" _operators;
```

## Properties

```
@property (T@"NSMutableDictionary",&,V_operators) operators;
```

## Class methods

```
+[PLCoreOperator registerOperator:];
+[PLCoreOperator registeredOperators];
+[PLCoreOperator registeredOperatorsOfSuperClassType:];
```

## Instance methods

```
-[PLCoreOperator init];
-[PLCoreOperator dealloc];
-[PLCoreOperator initOperatorDependancies];
-[PLCoreOperator initTaskOperatorDependancies];
-[PLCoreOperator log];
-[PLCoreOperator operators];
-[PLCoreOperator startOperatorsOfSuperClassType:];
-[PLCoreOperator allOperators];
-[PLCoreOperator initOperatorDependanciesSynchronously];
-[PLCoreOperator initOperatorDependanciesWithBlock:];
-[PLCoreOperator setOperators:];
-[PLCoreOperator setupEntryObjectsAndStorage:];
-[PLCoreOperator startServicesForPreUnlockTelemetry];
-[PLCoreOperator tablesToTrimConditionsForTrimDate:];
```
