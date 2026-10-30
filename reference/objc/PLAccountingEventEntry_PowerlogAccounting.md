# `PLAccountingEventEntry`

- Image: [`/System/Library/PrivateFrameworks/PowerlogAccounting.framework/PowerlogAccounting`](../userland/System__Library__PrivateFrameworks__PowerlogAccounting.framework__PowerlogAccounting.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PLEntry`
- 2 instance variables, 4 properties, 12 instance methods, 1 class methods

## Instance variables

```
B _used;
@"PLAccountingRange" _range;
```

## Properties

```
@property (Ti,R,N) instanceDirectionality;
@property (T@"PLAccountingRange",&,N,V_range) range;
@property (TB,N,V_used) used;
@property (TB,R,N) requiresOrderedDelivery;
```

## Class methods

```
+[PLAccountingEventEntry classDirectionality];
```

## Instance methods

```
-[PLAccountingEventEntry range];
-[PLAccountingEventEntry setRange:];
-[PLAccountingEventEntry used];
-[PLAccountingEventEntry requiresOrderedDelivery];
-[PLAccountingEventEntry initWithRange:];
-[PLAccountingEventEntry canMergeWithEvent:];
-[PLAccountingEventEntry setUsed:];
-[PLAccountingEventEntry mergeWithEvent:];
-[PLAccountingEventEntry instanceDirectionality];
-[PLAccountingEventEntry isEmptyEvent];
-[PLAccountingEventEntry isEqualContentsWithEvent:];
-[PLAccountingEventEntry rangeSinceEvent:];
```
