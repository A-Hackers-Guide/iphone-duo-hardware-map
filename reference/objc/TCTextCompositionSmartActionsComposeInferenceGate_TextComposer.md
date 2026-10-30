# `TCTextCompositionSmartActionsComposeInferenceGate`

- Image: [`/System/Library/PrivateFrameworks/TextComposer.framework/TextComposer`](../userland/System__Library__PrivateFrameworks__TextComposer.framework__TextComposer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 1 properties, 5 instance methods, 1 class methods

## Instance variables

```
@"NSString" _lastInput;
@"TCSmartActionsResponse" _cachedResponse;
@"NSObject<OS_dispatch_queue>" _queue;
```

## Properties

```
@property (T@"TCSmartActionsResponse",R,N) cachedResponse;
```

## Class methods

```
+[TCTextCompositionSmartActionsComposeInferenceGate sharedGate];
```

## Instance methods

```
-[TCTextCompositionSmartActionsComposeInferenceGate init];
-[TCTextCompositionSmartActionsComposeInferenceGate reset];
-[TCTextCompositionSmartActionsComposeInferenceGate cachedResponse];
-[TCTextCompositionSmartActionsComposeInferenceGate gateInput:];
-[TCTextCompositionSmartActionsComposeInferenceGate updateWithInput:result:];
```
