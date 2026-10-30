# `PLUrsaViolationContext`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 6 properties, 13 instance methods, 0 class methods

## Instance variables

```
B _mitigationsEnabled;
B _internalOnlyRule;
i _issueType;
i _ruleID;
@"NSString" _procName;
@"NSDate" _violationTime;
```

## Properties

```
@property (T@"NSString",C,N,V_procName) procName;
@property (T@"NSDate",&,N,V_violationTime) violationTime;
@property (Ti,N,V_issueType) issueType;
@property (TB,N,V_mitigationsEnabled) mitigationsEnabled;
@property (Ti,N,V_ruleID) ruleID;
@property (TB,N,V_internalOnlyRule) internalOnlyRule;
```

## Instance methods

```
-[PLUrsaViolationContext init];
-[PLUrsaViolationContext procName];
-[PLUrsaViolationContext ruleID];
-[PLUrsaViolationContext issueType];
-[PLUrsaViolationContext setIssueType:];
-[PLUrsaViolationContext setRuleID:];
-[PLUrsaViolationContext internalOnlyRule];
-[PLUrsaViolationContext mitigationsEnabled];
-[PLUrsaViolationContext setInternalOnlyRule:];
-[PLUrsaViolationContext setMitigationsEnabled:];
-[PLUrsaViolationContext setProcName:];
-[PLUrsaViolationContext setViolationTime:];
-[PLUrsaViolationContext violationTime];
```
