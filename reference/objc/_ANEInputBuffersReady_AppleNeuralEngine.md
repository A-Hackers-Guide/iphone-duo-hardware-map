# `_ANEInputBuffersReady`

- Image: [`/System/Library/PrivateFrameworks/AppleNeuralEngine.framework/AppleNeuralEngine`](../userland/System__Library__PrivateFrameworks__AppleNeuralEngine.framework__AppleNeuralEngine.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 7 instance methods, 2 class methods

## Instance variables

```
I _procedureIndex;
@"NSArray" _inputBufferInfoIndex;
@"NSArray" _inputFreeValue;
Q _executionDelay;
```

## Properties

```
@property (TI,R,N,V_procedureIndex) procedureIndex;
@property (T@"NSArray",R,N,V_inputBufferInfoIndex) inputBufferInfoIndex;
@property (T@"NSArray",R,N,V_inputFreeValue) inputFreeValue;
@property (TQ,R,N,V_executionDelay) executionDelay;
```

## Class methods

```
+[_ANEInputBuffersReady new];
+[_ANEInputBuffersReady inputBuffersWithProcedureIndex:inputBufferInfoIndex:inputFreeValue:executionDelay:];
```

## Instance methods

```
-[_ANEInputBuffersReady validate];
-[_ANEInputBuffersReady init];
-[_ANEInputBuffersReady procedureIndex];
-[_ANEInputBuffersReady executionDelay];
-[_ANEInputBuffersReady initInputsProcedureIndex:inputBufferInfoIndex:inputFreeValue:executionDelay:];
-[_ANEInputBuffersReady inputBufferInfoIndex];
-[_ANEInputBuffersReady inputFreeValue];
```
