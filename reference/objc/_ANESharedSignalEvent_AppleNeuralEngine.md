# `_ANESharedSignalEvent`

- Image: [`/System/Library/PrivateFrameworks/AppleNeuralEngine.framework/AppleNeuralEngine`](../userland/System__Library__PrivateFrameworks__AppleNeuralEngine.framework__AppleNeuralEngine.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 5 instance variables, 5 properties, 13 instance methods, 3 class methods

## Instance variables

```
I _symbolIndex;
Q _value;
Q _agentMask;
q _eventType;
@"IOSurfaceSharedEvent" _sharedEvent;
```

## Properties

```
@property (T@"IOSurfaceSharedEvent",R,N,V_sharedEvent) sharedEvent;
@property (TQ,N,V_value) value;
@property (TI,R,N,V_symbolIndex) symbolIndex;
@property (TQ,N,V_agentMask) agentMask;
@property (Tq,R,N,V_eventType) eventType;
```

## Class methods

```
+[_ANESharedSignalEvent supportsSecureCoding];
+[_ANESharedSignalEvent new];
+[_ANESharedSignalEvent signalEventWithValue:symbolIndex:eventType:sharedEvent:];
```

## Instance methods

```
-[_ANESharedSignalEvent eventType];
-[_ANESharedSignalEvent waitEvent];
-[_ANESharedSignalEvent sharedEvent];
-[_ANESharedSignalEvent init];
-[_ANESharedSignalEvent value];
-[_ANESharedSignalEvent setValue:];
-[_ANESharedSignalEvent encodeWithCoder:];
-[_ANESharedSignalEvent setAgentMask:];
-[_ANESharedSignalEvent description];
-[_ANESharedSignalEvent initWithCoder:];
-[_ANESharedSignalEvent symbolIndex];
-[_ANESharedSignalEvent initWithValue:symbolIndex:eventType:sharedEvent:agentMask:];
-[_ANESharedSignalEvent agentMask];
```
