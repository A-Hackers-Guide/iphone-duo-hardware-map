# `PLValueComparison`

- Image: [`/System/Library/PrivateFrameworks/PowerlogCore.framework/PowerlogCore`](../userland/System__Library__PrivateFrameworks__PowerlogCore.framework__PowerlogCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 9 properties, 11 instance methods, 0 class methods

## Instance variables

```
s _comparisonOperation;
@"NSString" _key;
@ _value;
```

## Properties

```
@property (T@"NSString",R,V_key) key;
@property (T@,R,V_value) value;
@property (Ts,R,V_comparisonOperation) comparisonOperation;
@property (TB,R) hasNilComparisonComponent;
@property (TB,R) hasEqualComparisonComponent;
@property (TB,R) hasGreaterThanComparisonComponent;
@property (TB,R) hasLessThanComparisonComponent;
@property (T@"NSString",R) comparisonOperationString;
@property (T@"NSString",R) sqlWhereClause;
```

## Instance methods

```
-[PLValueComparison value];
-[PLValueComparison description];
-[PLValueComparison key];
-[PLValueComparison comparisonOperation];
-[PLValueComparison comparisonOperationString];
-[PLValueComparison hasEqualComparisonComponent];
-[PLValueComparison hasGreaterThanComparisonComponent];
-[PLValueComparison hasLessThanComparisonComponent];
-[PLValueComparison hasNilComparisonComponent];
-[PLValueComparison initWithKey:withValue:withComparisonOperation:];
-[PLValueComparison sqlWhereClause];
```
