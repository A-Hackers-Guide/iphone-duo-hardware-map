# `MTLGPUDebugSynchronizedBiMap`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 2 properties, 8 instance methods, 0 class methods

## Instance variables

```
{shared_mutex="__base_"{__shared_mutex_base="__mut_"{mutex="__m_"{_opaque_pthread_mutex_t="__sig"q"__opaque"[56c]}}"__gate1_"{condition_variable="__cv_"{_opaque_pthread_cond_t="__sig"q"__opaque"[40c]}}"__gate2_"{condition_variable="__cv_"{_opaque_pthread_cond_t="__sig"q"__opaque"[40c]}}"__state_"I}} _mutex;
@"NSMutableArray" _indexToString;
@"NSMutableDictionary" _stringToIndex;
```

## Properties

```
@property (T@"NSMutableArray",N,V_indexToString) indexToString;
@property (T@"NSMutableDictionary",N,V_stringToIndex) stringToIndex;
```

## Instance methods

```
-[MTLGPUDebugSynchronizedBiMap init];
-[MTLGPUDebugSynchronizedBiMap dealloc];
-[MTLGPUDebugSynchronizedBiMap getCommandInfo:];
-[MTLGPUDebugSynchronizedBiMap getKeyForCommand:];
-[MTLGPUDebugSynchronizedBiMap indexToString];
-[MTLGPUDebugSynchronizedBiMap setIndexToString:];
-[MTLGPUDebugSynchronizedBiMap setStringToIndex:];
-[MTLGPUDebugSynchronizedBiMap stringToIndex];
```
