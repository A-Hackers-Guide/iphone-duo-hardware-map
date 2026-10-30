# `_ANESharedWaitEvent`

- Image: [`/System/Library/PrivateFrameworks/AppleNeuralEngine.framework/AppleNeuralEngine`](../userland/System__Library__PrivateFrameworks__AppleNeuralEngine.framework__AppleNeuralEngine.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 7 instance methods, 3 class methods

## Instance variables

```
Q _value;
Q _eventType;
@"IOSurfaceSharedEvent" _sharedEvent;
```

## Properties

```
@property (T@"IOSurfaceSharedEvent",R,N,V_sharedEvent) sharedEvent;
@property (TQ,N,V_value) value;
@property (TQ,R,N,V_eventType) eventType;
```

## Class methods

```
+[_ANESharedWaitEvent new];
+[_ANESharedWaitEvent waitEventWithValue:sharedEvent:];
+[_ANESharedWaitEvent waitEventWithValue:sharedEvent:eventType:];
```

## Instance methods

```
-[_ANESharedWaitEvent eventType];
-[_ANESharedWaitEvent sharedEvent];
-[_ANESharedWaitEvent init];
-[_ANESharedWaitEvent value];
-[_ANESharedWaitEvent setValue:];
-[_ANESharedWaitEvent description];
-[_ANESharedWaitEvent initWithValue:sharedEvent:eventType:];
```
