# `PLAccountingRange`

- Image: [`/System/Library/PrivateFrameworks/PowerlogAccounting.framework/PowerlogAccounting`](../userland/System__Library__PrivateFrameworks__PowerlogAccounting.framework__PowerlogAccounting.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 3 properties, 9 instance methods, 2 class methods

## Instance variables

```
@"NSDate" _startDate;
@"NSDate" _endDate;
```

## Properties

```
@property (T@"NSDate",R,N,V_startDate) startDate;
@property (T@"NSDate",R,N,V_endDate) endDate;
@property (Td,R,N) length;
```

## Class methods

```
+[PLAccountingRange emptyRange];
+[PLAccountingRange rangeWithStartDate:withEndDate:];
```

## Instance methods

```
-[PLAccountingRange startDate];
-[PLAccountingRange endDate];
-[PLAccountingRange length];
-[PLAccountingRange containsDate:];
-[PLAccountingRange description];
-[PLAccountingRange isEqual:];
-[PLAccountingRange intersect:];
-[PLAccountingRange overlaps:];
-[PLAccountingRange initWithStartDate:withEndDate:];
```
