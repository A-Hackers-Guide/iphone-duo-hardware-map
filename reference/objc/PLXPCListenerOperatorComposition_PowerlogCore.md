# `PLXPCListenerOperatorComposition`

- Image: [`/System/Library/PrivateFrameworks/PowerlogCore.framework/PowerlogCore`](../userland/System__Library__PrivateFrameworks__PowerlogCore.framework__PowerlogCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"NSDictionary" _registration;
@? _operatorBlock;
@"PLOperator" _operator;
```

## Properties

```
@property (T@"PLOperator",W,V_operator) operator;
@property (T@"NSDictionary",R,V_registration) registration;
@property (T@?,C,N,V_operatorBlock) operatorBlock;
```

## Instance methods

```
-[PLXPCListenerOperatorComposition registration];
-[PLXPCListenerOperatorComposition operator];
-[PLXPCListenerOperatorComposition description];
-[PLXPCListenerOperatorComposition setOperator:];
-[PLXPCListenerOperatorComposition messageRecievedForClientID:withProcessName:withKey:withPayload:];
-[PLXPCListenerOperatorComposition initWithOperator:withRegistration:withBlock:];
-[PLXPCListenerOperatorComposition operatorBlock];
-[PLXPCListenerOperatorComposition setOperatorBlock:];
```
