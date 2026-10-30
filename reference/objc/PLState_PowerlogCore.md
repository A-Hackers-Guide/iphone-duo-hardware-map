# `PLState`

- Image: [`/System/Library/PrivateFrameworks/PowerlogCore.framework/PowerlogCore`](../userland/System__Library__PrivateFrameworks__PowerlogCore.framework__PowerlogCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 12 instance methods, 1 class methods

## Instance variables

```
@ _lastValue;
@ _currValue;
@"NSDate" _stateChangeTime;
Q _stateId;
@"NSString" _entryKey;
```

## Properties

```
@property (T@,&,V_lastValue) lastValue;
@property (T@,&,V_currValue) currValue;
@property (T@"NSDate",&,V_stateChangeTime) stateChangeTime;
@property (TQ,R,V_stateId) stateId;
@property (T@"NSString",R,V_entryKey) entryKey;
```

## Class methods

```
+[PLState load];
```

## Instance methods

```
-[PLState entryKey];
-[PLState updateWithValue:];
-[PLState lastValue];
-[PLState updateWithEntry:];
-[PLState stateChangeTime];
-[PLState stateId];
-[PLState currValue];
-[PLState initWithStateId:entryKey:currValue:];
-[PLState setCurrValue:];
-[PLState setLastValue:];
-[PLState setStateChangeTime:];
-[PLState updateWithLastEntry];
```
