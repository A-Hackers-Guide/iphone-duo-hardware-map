# `PLAccountingOperator`

- Image: [`/System/Library/PrivateFrameworks/PowerlogCore.framework/PowerlogCore`](../userland/System__Library__PrivateFrameworks__PowerlogCore.framework__PowerlogCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PLOperator`
- 2 instance variables, 2 properties, 9 instance methods, 25 class methods

## Instance variables

```
@"NSSet" _rules;
@"NSMutableDictionary" _ruleIDToPendingJobs;
```

## Properties

```
@property (T@"NSSet",&,N,V_rules) rules;
@property (T@"NSMutableDictionary",&,V_ruleIDToPendingJobs) ruleIDToPendingJobs;
```

## Class methods

```
+[PLAccountingOperator entryEventIntervalDefinitions];
+[PLAccountingOperator entryEventPointDefinitions];
+[PLAccountingOperator entryEventForwardDefinitions];
+[PLAccountingOperator entryEventBackwardDefinitions];
+[PLAccountingOperator entryEventIntervalDefinitionDistributionEvents];
+[PLAccountingOperator entryEventNoneDefinitions];
+[PLAccountingOperator load];
+[PLAccountingOperator entryEventForwardDefinitionPowerEvents];
+[PLAccountingOperator entryEventNoneDefinitionNodes];
+[PLAccountingOperator entryEventNoneDefinitionDistributionRules];
+[PLAccountingOperator entryEventIntervalDefinitionPowerEvents];
+[PLAccountingOperator entryEventBackwardDefinitionQualificationEvents];
+[PLAccountingOperator entryEventPointDefinitionQualificationEvents];
+[PLAccountingOperator entryEventIntervalDefinitionDebugEnergyEstimateEvents];
+[PLAccountingOperator entryEventBackwardDefinitionDistributionEvents];
+[PLAccountingOperator entryEventNoneDefinitionQualificationRules];
+[PLAccountingOperator entryEventIntervalDefinitionQualificationEvents];
+[PLAccountingOperator entryEventForwardDefinitionQualificationEvents];
+[PLAccountingOperator entryEventForwardDefinitionDistributionEvents];
+[PLAccountingOperator entryEventBackwardDefinitionPowerEvents];
+[PLAccountingOperator entryAggregateDefinitionEnergy];
+[PLAccountingOperator entryEventIntervalDefinitionEnergyEstimateEvents];
+[PLAccountingOperator entryAggregateDefinitionQualificationEnergy];
+[PLAccountingOperator entryEventPointDefinitionDistributionEvents];
+[PLAccountingOperator entryAggregateDefinitions];
```

## Instance methods

```
-[PLAccountingOperator rules];
-[PLAccountingOperator init];
-[PLAccountingOperator initOperatorDependancies];
-[PLAccountingOperator setRules:];
-[PLAccountingOperator stopAccounting];
-[PLAccountingOperator trimConditionsForEntryKey:forTrimDate:];
-[PLAccountingOperator startAccounting];
-[PLAccountingOperator ruleIDToPendingJobs];
-[PLAccountingOperator setRuleIDToPendingJobs:];
```
