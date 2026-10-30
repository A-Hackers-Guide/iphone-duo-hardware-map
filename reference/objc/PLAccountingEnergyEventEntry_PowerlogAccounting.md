# `PLAccountingEnergyEventEntry`

- Image: [`/System/Library/PrivateFrameworks/PowerlogAccounting.framework/PowerlogAccounting`](../userland/System__Library__PrivateFrameworks__PowerlogAccounting.framework__PowerlogAccounting.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PLEntry`
- 1 instance variables, 3 properties, 4 instance methods, 2 class methods

## Instance variables

```
@"PLAccountingRange" _range;
```

## Properties

```
@property (T@"NSNumber",R,N) nodeID;
@property (Td,R,N) energy;
@property (T@"PLAccountingRange",R,N,V_range) range;
```

## Class methods

```
+[PLAccountingEnergyEventEntry load];
+[PLAccountingEnergyEventEntry entryKey];
```

## Instance methods

```
-[PLAccountingEnergyEventEntry range];
-[PLAccountingEnergyEventEntry energy];
-[PLAccountingEnergyEventEntry initWithNodeID:withEnergy:withRange:withEntryDate:];
-[PLAccountingEnergyEventEntry nodeID];
```
