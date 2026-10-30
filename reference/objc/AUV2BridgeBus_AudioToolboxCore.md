# `AUV2BridgeBus`

- Image: [`/System/Library/PrivateFrameworks/AudioToolboxCore.framework/AudioToolboxCore`](../userland/System__Library__PrivateFrameworks__AudioToolboxCore.framework__AudioToolboxCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AUAudioUnitBus`
- 4 instance variables, 0 properties, 4 instance methods, 0 class methods

## Instance variables

```
@"AUAudioUnitV2Bridge" _owner;
I _scope;
I _element;
{recursive_mutex="__m_"{_opaque_pthread_mutex_t="__sig"q"__opaque"[56c]}} _mutex;
```

## Instance methods

```
-[AUV2BridgeBus setEnabled:];
-[AUV2BridgeBus format];
-[AUV2BridgeBus initWithOwner:au:scope:element:];
-[AUV2BridgeBus setFormat:error:];
```
