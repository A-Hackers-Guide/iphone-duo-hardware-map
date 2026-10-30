# `PLAccountingPowerEventEntry`

- Image: [`/System/Library/PrivateFrameworks/PowerlogAccounting.framework/PowerlogAccounting`](../userland/System__Library__PrivateFrameworks__PowerlogAccounting.framework__PowerlogAccounting.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PLAccountingEventEntry`
- 0 instance variables, 2 properties, 7 instance methods, 4 class methods

## Properties

```
@property (T@"NSNumber",R,N) rootNodeID;
@property (Td,R,N) power;
```

## Class methods

```
+[PLAccountingPowerEventEntry load];
+[PLAccountingPowerEventEntry isValidPower:forRootNodeID:];
+[PLAccountingPowerEventEntry minPowerDifference];
+[PLAccountingPowerEventEntry minPowerPercentageDifference];
```

## Instance methods

```
-[PLAccountingPowerEventEntry power];
-[PLAccountingPowerEventEntry rootNodeID];
-[PLAccountingPowerEventEntry subEntryKey];
-[PLAccountingPowerEventEntry initWithRootNodeID:withPower:withRange:];
-[PLAccountingPowerEventEntry instanceDirectionality];
-[PLAccountingPowerEventEntry isEmptyEvent];
-[PLAccountingPowerEventEntry isEqualContentsWithEvent:];
```
