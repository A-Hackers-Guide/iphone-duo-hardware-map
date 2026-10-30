# `PLAccountingDistributionRuleEntry`

- Image: [`/System/Library/PrivateFrameworks/PowerlogAccounting.framework/PowerlogAccounting`](../userland/System__Library__PrivateFrameworks__PowerlogAccounting.framework__PowerlogAccounting.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PLAccountingRuleEntry`
- 0 instance variables, 3 properties, 7 instance methods, 2 class methods

## Properties

```
@property (T@"NSNumber",R,N) nodeID;
@property (T@"NSNumber",R,N) rootNodeID;
@property (T@"NSNumber",R,N) distributionID;
```

## Class methods

```
+[PLAccountingDistributionRuleEntry load];
+[PLAccountingDistributionRuleEntry entryKey];
```

## Instance methods

```
-[PLAccountingDistributionRuleEntry rootNodeID];
-[PLAccountingDistributionRuleEntry distributionID];
-[PLAccountingDistributionRuleEntry hash];
-[PLAccountingDistributionRuleEntry description];
-[PLAccountingDistributionRuleEntry initWithNodeID:withRootNodeID:withDistributionID:withEntryDate:];
-[PLAccountingDistributionRuleEntry isEqual:];
-[PLAccountingDistributionRuleEntry nodeID];
```
