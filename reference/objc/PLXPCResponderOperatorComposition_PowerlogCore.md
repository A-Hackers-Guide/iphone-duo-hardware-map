# `PLXPCResponderOperatorComposition`

- Image: [`/System/Library/PrivateFrameworks/PowerlogCore.framework/PowerlogCore`](../userland/System__Library__PrivateFrameworks__PowerlogCore.framework__PowerlogCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"NSDictionary" _registration;
@? _operatorBlock;
@"PLOperator" _operator;
@"NSObject<OS_dispatch_queue>" _workQueue;
```

## Properties

```
@property (T@"PLOperator",W,V_operator) operator;
@property (T@"NSObject<OS_dispatch_queue>",&,V_workQueue) workQueue;
@property (T@"NSDictionary",R,V_registration) registration;
@property (T@?,C,N,V_operatorBlock) operatorBlock;
```

## Instance methods

```
-[PLXPCResponderOperatorComposition setWorkQueue:];
-[PLXPCResponderOperatorComposition workQueue];
-[PLXPCResponderOperatorComposition registration];
-[PLXPCResponderOperatorComposition operator];
-[PLXPCResponderOperatorComposition description];
-[PLXPCResponderOperatorComposition setOperator:];
-[PLXPCResponderOperatorComposition initWithOperator:withRegistration:withBlock:];
-[PLXPCResponderOperatorComposition initWithWorkQueue:withRegistration:withBlock:];
-[PLXPCResponderOperatorComposition operatorBlock];
-[PLXPCResponderOperatorComposition respondToRequestForClientID:withProcessName:withKey:withPayload:];
-[PLXPCResponderOperatorComposition setOperatorBlock:];
```
