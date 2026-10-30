# `_ANEOutputSetEnqueue`

- Image: [`/System/Library/PrivateFrameworks/AppleNeuralEngine.framework/AppleNeuralEngine`](../userland/System__Library__PrivateFrameworks__AppleNeuralEngine.framework__AppleNeuralEngine.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 7 instance methods, 2 class methods

## Instance variables

```
B _signalNotRequired;
B _isOpenLoop;
I _procedureIndex;
I _setIndex;
Q _signalValue;
```

## Properties

```
@property (TI,R,N,V_procedureIndex) procedureIndex;
@property (TI,R,N,V_setIndex) setIndex;
@property (TQ,R,N,V_signalValue) signalValue;
@property (TB,R,N,V_signalNotRequired) signalNotRequired;
@property (TB,R,N,V_isOpenLoop) isOpenLoop;
```

## Class methods

```
+[_ANEOutputSetEnqueue new];
+[_ANEOutputSetEnqueue outputSetWithProcedureIndex:setIndex:signalValue:signalNotRequired:isOpenLoop:];
```

## Instance methods

```
-[_ANEOutputSetEnqueue init];
-[_ANEOutputSetEnqueue procedureIndex];
-[_ANEOutputSetEnqueue signalValue];
-[_ANEOutputSetEnqueue initOutputSetWithProcedureIndex:setIndex:signalValue:signalNotRequired:isOpenLoop:];
-[_ANEOutputSetEnqueue isOpenLoop];
-[_ANEOutputSetEnqueue setIndex];
-[_ANEOutputSetEnqueue signalNotRequired];
```
