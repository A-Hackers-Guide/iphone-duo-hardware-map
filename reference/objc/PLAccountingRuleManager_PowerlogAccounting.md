# `PLAccountingRuleManager`

- Image: [`/System/Library/PrivateFrameworks/PowerlogAccounting.framework/PowerlogAccounting`](../userland/System__Library__PrivateFrameworks__PowerlogAccounting.framework__PowerlogAccounting.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 10 instance methods, 6 class methods

## Instance variables

```
@"NSRegularExpression" _regex;
@"NSMutableDictionary" _ruleIDToRule;
```

## Properties

```
@property (T@"NSMutableDictionary",&,N,V_ruleIDToRule) ruleIDToRule;
@property (T@"NSRegularExpression",&,N,V_regex) regex;
```

## Class methods

```
+[PLAccountingRuleManager sharedInstance];
+[PLAccountingRuleManager decryptData:withKey:];
+[PLAccountingRuleManager firstLineWithFile:];
+[PLAccountingRuleManager rulesEntryKey];
+[PLAccountingRuleManager rulesPath];
+[PLAccountingRuleManager storedHashDefaults];
```

## Instance methods

```
-[PLAccountingRuleManager regex];
-[PLAccountingRuleManager init];
-[PLAccountingRuleManager setRegex:];
-[PLAccountingRuleManager indexRule:];
-[PLAccountingRuleManager loadRules];
-[PLAccountingRuleManager ruleForRuleID:];
-[PLAccountingRuleManager ruleIDToRule];
-[PLAccountingRuleManager ruleWithString:withEntryDate:];
-[PLAccountingRuleManager rulesFromFileWithForceLoad:];
-[PLAccountingRuleManager setRuleIDToRule:];
```
