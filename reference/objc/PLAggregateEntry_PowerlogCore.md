# `PLAggregateEntry`

- Image: [`/System/Library/PrivateFrameworks/PowerlogCore.framework/PowerlogCore`](../userland/System__Library__PrivateFrameworks__PowerlogCore.framework__PowerlogCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 6 properties, 17 instance methods, 0 class methods

## Instance variables

```
s _aggregateFunction;
@"NSString" _entryKey;
@"NSMutableDictionary" _matchingKeyToValue;
@"NSArray" _otherAggregateKeys;
@"NSString" _aggregateKey;
d _aggregateValue;
```

## Properties

```
@property (T@"NSString",&,V_entryKey) entryKey;
@property (T@"NSMutableDictionary",&,N,V_matchingKeyToValue) matchingKeyToValue;
@property (T@"NSArray",&,V_otherAggregateKeys) otherAggregateKeys;
@property (T@"NSString",&,V_aggregateKey) aggregateKey;
@property (Td,V_aggregateValue) aggregateValue;
@property (Ts,V_aggregateFunction) aggregateFunction;
```

## Instance methods

```
-[PLAggregateEntry aggregateKey];
-[PLAggregateEntry otherAggregateKeys];
-[PLAggregateEntry matchingPairs];
-[PLAggregateEntry setAggregateKey:];
-[PLAggregateEntry entryKey];
-[PLAggregateEntry setAggregateValue:];
-[PLAggregateEntry setAggregateFunction:];
-[PLAggregateEntry aggregateValue];
-[PLAggregateEntry aggregateFunction];
-[PLAggregateEntry setEntryKey:];
-[PLAggregateEntry query];
-[PLAggregateEntry updateWithValue:];
-[PLAggregateEntry description];
-[PLAggregateEntry aggregateOperationWithMatchingPairs:];
-[PLAggregateEntry matchingKeyToValue];
-[PLAggregateEntry setMatchingKeyToValue:];
-[PLAggregateEntry setOtherAggregateKeys:];
```
