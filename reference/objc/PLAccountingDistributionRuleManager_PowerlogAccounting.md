# `PLAccountingDistributionRuleManager`

- Image: [`/System/Library/PrivateFrameworks/PowerlogAccounting.framework/PowerlogAccounting`](../userland/System__Library__PrivateFrameworks__PowerlogAccounting.framework__PowerlogAccounting.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PLAccountingRuleManager`
- 3 instance variables, 2 properties, 10 instance methods, 3 class methods

## Instance variables

```
@"NSRegularExpression" _regex;
@"NSMutableDictionary" _rootNodeIDToNodeIDToDistributionRule;
@"NSMutableDictionary" _distributionIDToDistributionRules;
```

## Properties

```
@property (T@"NSMutableDictionary",&,N,V_rootNodeIDToNodeIDToDistributionRule) rootNodeIDToNodeIDToDistributionRule;
@property (T@"NSMutableDictionary",&,N,V_distributionIDToDistributionRules) distributionIDToDistributionRules;
```

## Class methods

```
+[PLAccountingDistributionRuleManager sharedInstance];
+[PLAccountingDistributionRuleManager rulesEntryKey];
+[PLAccountingDistributionRuleManager rulesPath];
```

## Instance methods

```
-[PLAccountingDistributionRuleManager regex];
-[PLAccountingDistributionRuleManager setRegex:];
-[PLAccountingDistributionRuleManager distributionIDToDistributionRules];
-[PLAccountingDistributionRuleManager distributionRuleForRootNodeID:andNodeID:];
-[PLAccountingDistributionRuleManager distributionRulesForDistributionID:];
-[PLAccountingDistributionRuleManager indexRule:];
-[PLAccountingDistributionRuleManager rootNodeIDToNodeIDToDistributionRule];
-[PLAccountingDistributionRuleManager ruleWithString:withEntryDate:];
-[PLAccountingDistributionRuleManager setDistributionIDToDistributionRules:];
-[PLAccountingDistributionRuleManager setRootNodeIDToNodeIDToDistributionRule:];
```
