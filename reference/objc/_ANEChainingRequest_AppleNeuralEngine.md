# `_ANEChainingRequest`

- Image: [`/System/Library/PrivateFrameworks/AppleNeuralEngine.framework/AppleNeuralEngine`](../userland/System__Library__PrivateFrameworks__AppleNeuralEngine.framework__AppleNeuralEngine.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 9 instance variables, 9 properties, 14 instance methods, 2 class methods

## Instance variables

```
@"NSArray" _inputBuffer;
@"NSArray" _outputSets;
@"NSArray" _loopbackInputSymbolIndex;
@"NSArray" _loopbackOutputSymbolIndex;
@"NSArray" _signalEvents;
@"NSNumber" _transactionHandle;
@"NSNumber" _procedureIndex;
@"NSNumber" _fwEnqueueDelay;
@"NSNumber" _memoryPoolId;
```

## Properties

```
@property (T@"NSArray",R,N,V_inputBuffer) inputBuffer;
@property (T@"NSArray",R,N,V_outputSets) outputSets;
@property (T@"NSArray",R,N,V_loopbackInputSymbolIndex) loopbackInputSymbolIndex;
@property (T@"NSArray",R,N,V_loopbackOutputSymbolIndex) loopbackOutputSymbolIndex;
@property (T@"NSArray",R,N,V_signalEvents) signalEvents;
@property (T@"NSNumber",R,N,V_transactionHandle) transactionHandle;
@property (T@"NSNumber",R,N,V_procedureIndex) procedureIndex;
@property (T@"NSNumber",R,N,V_fwEnqueueDelay) fwEnqueueDelay;
@property (T@"NSNumber",R,N,V_memoryPoolId) memoryPoolId;
```

## Class methods

```
+[_ANEChainingRequest supportsSecureCoding];
+[_ANEChainingRequest chainingRequestWithInputs:outputSets:lbInputSymbolId:lbOutputSymbolId:procedureIndex:signalEvents:transactionHandle:fwEnqueueDelay:memoryPoolId:];
```

## Instance methods

```
-[_ANEChainingRequest validate];
-[_ANEChainingRequest memoryPoolId];
-[_ANEChainingRequest inputBuffer];
-[_ANEChainingRequest transactionHandle];
-[_ANEChainingRequest encodeWithCoder:];
-[_ANEChainingRequest description];
-[_ANEChainingRequest initWithCoder:];
-[_ANEChainingRequest procedureIndex];
-[_ANEChainingRequest fwEnqueueDelay];
-[_ANEChainingRequest initWithInputs:outputs:lbInputSymbolId:lbOutputSymbolId:procedureIndex:signalEvents:transactionHandle:fwEnqueueDelay:memoryPoolId:];
-[_ANEChainingRequest loopbackInputSymbolIndex];
-[_ANEChainingRequest loopbackOutputSymbolIndex];
-[_ANEChainingRequest outputSets];
-[_ANEChainingRequest signalEvents];
```
