# `OperatorTask`

- Image: [`/System/Library/PrivateFrameworks/PowerlogCore.framework/PowerlogCore`](../userland/System__Library__PrivateFrameworks__PowerlogCore.framework__PowerlogCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 5 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _operatorQueue;
@? _operatorBlock;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",&,V_operatorQueue) operatorQueue;
@property (T@?,C,V_operatorBlock) operatorBlock;
```

## Instance methods

```
-[OperatorTask initWithQueue:withBlock:];
-[OperatorTask operatorBlock];
-[OperatorTask operatorQueue];
-[OperatorTask setOperatorBlock:];
-[OperatorTask setOperatorQueue:];
```
