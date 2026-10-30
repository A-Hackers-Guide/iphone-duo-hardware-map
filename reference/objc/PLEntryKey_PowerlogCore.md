# `PLEntryKey`

- Image: [`/System/Library/PrivateFrameworks/PowerlogCore.framework/PowerlogCore`](../userland/System__Library__PrivateFrameworks__PowerlogCore.framework__PowerlogCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 9 properties, 19 instance methods, 31 class methods

## Instance variables

```
B _isDynamic;
@"NSString" _entryKey;
@"PLEntryKey" _baseEntryKey;
@"NSString" _operatorName;
# _operatorClass;
@"NSString" _entryType;
@"NSString" _entryName;
@"NSString" _wildCardName;
{_PLTimeIntervalRange="location"d"length"d} _timeIntervalRange;
```

## Properties

```
@property (T@"NSString",C,N,V_wildCardName) wildCardName;
@property (TB,N,V_isDynamic) isDynamic;
@property (T{_PLTimeIntervalRange=dd},N,V_timeIntervalRange) timeIntervalRange;
@property (T@"PLEntryKey",W,V_baseEntryKey) baseEntryKey;
@property (T@"NSString",R,&,V_entryKey) entryKey;
@property (T@"NSString",R,&,V_operatorName) operatorName;
@property (T#,R,&,V_operatorClass) operatorClass;
@property (T@"NSString",R,&,V_entryType) entryType;
@property (T@"NSString",R,&,V_entryName) entryName;
```

## Class methods

```
+[PLEntryKey PLEntryAggregateKeysForOperatorClass:];
+[PLEntryKey PLEntryKeyForEntryKey:];
+[PLEntryKey PLEntryKeyForOperatorName:withType:withName:withWildCardName:isDynamic:];
+[PLEntryKey PLEntryKeyStringsForTaskingReset];
+[PLEntryKey PLEntryAggregateKeysForOperator:];
+[PLEntryKey PLEntryAggregateKeysForOperatorName:];
+[PLEntryKey PLEntryKeyForOperatorName:withType:withName:];
+[PLEntryKey PLEntryKeyStringsForTasking];
+[PLEntryKey PLEntryKeysForEntryType:];
+[PLEntryKey addPLEntryKey:];
+[PLEntryKey addPLEntryKeyStringToTasking:];
+[PLEntryKey baseEntryKeyForEntryKey:];
+[PLEntryKey dynamicEntryKeyForEntryKey:];
+[PLEntryKey entryKeyForOperatorName:withType:withName:];
+[PLEntryKey entryKeyForOperatorName:withType:withName:isDynamic:];
+[PLEntryKey entryKeyForOperatorName:withType:withName:withWildCardName:];
+[PLEntryKey entryKeyForOperatorName:withType:withName:withWildCardName:isDynamic:];
+[PLEntryKey entryKeyStringForOperatorName:withType:withName:];
+[PLEntryKey entryKeysForOperator:];
+[PLEntryKey entryKeysForOperatorClass:];
+[PLEntryKey entryKeysForOperatorName:];
+[PLEntryKey entryKeysForOperatorNameCopy:];
+[PLEntryKey isEntryKeySetup:forOperatorName:];
+[PLEntryKey operatorClassForEntryKey:];
+[PLEntryKey operatorNameForEntryKey:];
+[PLEntryKey setupEntryObjectsForOperatorClass:];
+[PLEntryKey shouldConfigureAdditionalTable:withType:withName:];
+[PLEntryKey shouldConfigureTable:withType:withName:withConfigs:];
+[PLEntryKey timeIntervalRangeForEntryKey:];
+[PLEntryKey timeintervalRangeEntryKeyForEntryKey:withTimeIntervalRange:];
+[PLEntryKey wildCardForEntryKey:];
```

## Instance methods

```
-[PLEntryKey isDynamic];
-[PLEntryKey entryType];
-[PLEntryKey debugDescription];
-[PLEntryKey entryKey];
-[PLEntryKey operatorName];
-[PLEntryKey description];
-[PLEntryKey setIsDynamic:];
-[PLEntryKey baseEntryKey];
-[PLEntryKey copyWithIsDynamic:];
-[PLEntryKey copyWithTimeIntervalRange:];
-[PLEntryKey copyWithWildCardName:];
-[PLEntryKey entryName];
-[PLEntryKey initWithOperatorName:withEntryType:withEntryName:];
-[PLEntryKey operatorClass];
-[PLEntryKey setBaseEntryKey:];
-[PLEntryKey setTimeIntervalRange:];
-[PLEntryKey setWildCardName:];
-[PLEntryKey timeIntervalRange];
-[PLEntryKey wildCardName];
```
