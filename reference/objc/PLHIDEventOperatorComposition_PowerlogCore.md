# `PLHIDEventOperatorComposition`

- Image: [`/System/Library/PrivateFrameworks/PowerlogCore.framework/PowerlogCore`](../userland/System__Library__PrivateFrameworks__PowerlogCore.framework__PowerlogCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 8 instance methods, 0 class methods

## Instance variables

```
^{__IOHIDEventSystemClient=} _eventSystemClient;
@? _operatorBlock;
@"PLOperator" _operator;
```

## Properties

```
@property (T@"PLOperator",&,V_operator) operator;
@property (T^{__IOHIDEventSystemClient=},V_eventSystemClient) eventSystemClient;
@property (T@?,C,N,V_operatorBlock) operatorBlock;
```

## Instance methods

```
-[PLHIDEventOperatorComposition handleEvent:];
-[PLHIDEventOperatorComposition operator];
-[PLHIDEventOperatorComposition eventSystemClient];
-[PLHIDEventOperatorComposition setEventSystemClient:];
-[PLHIDEventOperatorComposition setOperator:];
-[PLHIDEventOperatorComposition initWithOperator:forUsagePage:andUsage:withBlock:];
-[PLHIDEventOperatorComposition operatorBlock];
-[PLHIDEventOperatorComposition setOperatorBlock:];
```
