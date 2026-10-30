# `BWInferenceSharedE5ANEMemoryProvider`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWInferenceSharedResourceManager`
- 2 instance variables, 0 properties, 6 instance methods, 2 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _networkListLock;
@"NSMutableDictionary" _networksUsingE5ANEMemoryProviderByExecutionPriority;
```

## Class methods

```
+[BWInferenceSharedE5ANEMemoryProvider initialize];
+[BWInferenceSharedE5ANEMemoryProvider resourceCategory];
```

## Instance methods

```
-[BWInferenceSharedE5ANEMemoryProvider init];
-[BWInferenceSharedE5ANEMemoryProvider dealloc];
-[BWInferenceSharedE5ANEMemoryProvider description];
-[BWInferenceSharedE5ANEMemoryProvider completeANEMemoryProviderCreationForNetwork:executionPriority:wasSuccessful:];
-[BWInferenceSharedE5ANEMemoryProvider fetchANEMemoryProviderForNetwork:executionPriority:];
-[BWInferenceSharedE5ANEMemoryProvider registerANEMemoryProvider:forNetwork:executionPriority:];
```
