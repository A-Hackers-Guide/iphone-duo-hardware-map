# `TCTextCompositionSmartResponsesGate`

- Image: [`/System/Library/PrivateFrameworks/TextComposer.framework/TextComposer`](../userland/System__Library__PrivateFrameworks__TextComposer.framework__TextComposer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 1 properties, 6 instance methods, 1 class methods

## Instance variables

```
@"NSMutableDictionary" _inflightEntries;
@"NSObject<OS_dispatch_queue>" _gateQueue;
d _inflightTimeout;
```

## Properties

```
@property (Td,N,V_inflightTimeout) inflightTimeout;
```

## Class methods

```
+[TCTextCompositionSmartResponsesGate sharedGate];
```

## Instance methods

```
-[TCTextCompositionSmartResponsesGate init];
-[TCTextCompositionSmartResponsesGate inflightTimeout];
-[TCTextCompositionSmartResponsesGate coalescingKeyForContextHistory:responseTypes:contextBeforeCursor:];
-[TCTextCompositionSmartResponsesGate enqueueOrMarkInflight:token:callback:onEviction:];
-[TCTextCompositionSmartResponsesGate fulfillCallbacksForKey:token:result:options:error:];
-[TCTextCompositionSmartResponsesGate setInflightTimeout:];
```
