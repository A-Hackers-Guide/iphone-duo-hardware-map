# `_ANESharedEvents`

- Image: [`/System/Library/PrivateFrameworks/AppleNeuralEngine.framework/AppleNeuralEngine`](../userland/System__Library__PrivateFrameworks__AppleNeuralEngine.framework__AppleNeuralEngine.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 7 instance methods, 2 class methods

## Instance variables

```
@"NSArray" _signalEvents;
@"NSArray" _waitEvents;
```

## Properties

```
@property (T@"NSArray",&,N,V_signalEvents) signalEvents;
@property (T@"NSArray",&,N,V_waitEvents) waitEvents;
```

## Class methods

```
+[_ANESharedEvents new];
+[_ANESharedEvents sharedEventsWithSignalEvents:waitEvents:];
```

## Instance methods

```
-[_ANESharedEvents init];
-[_ANESharedEvents description];
-[_ANESharedEvents initWithSignalEvents:waitEvents:];
-[_ANESharedEvents setSignalEvents:];
-[_ANESharedEvents setWaitEvents:];
-[_ANESharedEvents signalEvents];
-[_ANESharedEvents waitEvents];
```
