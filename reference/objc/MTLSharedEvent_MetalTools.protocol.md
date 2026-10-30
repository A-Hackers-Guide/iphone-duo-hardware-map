# `MTLSharedEvent` (protocol)

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `MTLEvent`
- 0 instance variables, 1 properties, 5 instance methods, 0 class methods

## Properties

```
@property (TQ) signaledValue;
```

## Instance methods

```
-[MTLSharedEvent newSharedEventHandle];
-[MTLSharedEvent notifyListener:atValue:block:];
-[MTLSharedEvent setSignaledValue:];
-[MTLSharedEvent signaledValue];
-[MTLSharedEvent waitUntilSignaledValue:timeoutMS:];
```
