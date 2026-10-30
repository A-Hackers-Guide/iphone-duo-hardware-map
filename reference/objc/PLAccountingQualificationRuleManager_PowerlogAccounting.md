# `PLAccountingQualificationRuleManager`

- Image: [`/System/Library/PrivateFrameworks/PowerlogAccounting.framework/PowerlogAccounting`](../userland/System__Library__PrivateFrameworks__PowerlogAccounting.framework__PowerlogAccounting.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PLAccountingRuleManager`
- 3 instance variables, 2 properties, 10 instance methods, 3 class methods

## Instance variables

```
@"NSRegularExpression" _regex;
@"NSMutableDictionary" _rootNodeIDToQualificationRules;
@"NSMutableDictionary" _qualificationIDToQualificationRules;
```

## Properties

```
@property (T@"NSMutableDictionary",&,N,V_rootNodeIDToQualificationRules) rootNodeIDToQualificationRules;
@property (T@"NSMutableDictionary",&,N,V_qualificationIDToQualificationRules) qualificationIDToQualificationRules;
```

## Class methods

```
+[PLAccountingQualificationRuleManager sharedInstance];
+[PLAccountingQualificationRuleManager rulesEntryKey];
+[PLAccountingQualificationRuleManager rulesPath];
```

## Instance methods

```
-[PLAccountingQualificationRuleManager regex];
-[PLAccountingQualificationRuleManager setRegex:];
-[PLAccountingQualificationRuleManager indexRule:];
-[PLAccountingQualificationRuleManager qualificationIDToQualificationRules];
-[PLAccountingQualificationRuleManager qualificationRulesForQualificationID:];
-[PLAccountingQualificationRuleManager qualificationRulesForRootNodeID:];
-[PLAccountingQualificationRuleManager rootNodeIDToQualificationRules];
-[PLAccountingQualificationRuleManager ruleWithString:withEntryDate:];
-[PLAccountingQualificationRuleManager setQualificationIDToQualificationRules:];
-[PLAccountingQualificationRuleManager setRootNodeIDToQualificationRules:];
```
