# `BWInferenceSharedResourceManager`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 0 properties, 6 instance methods, 2 class methods

## Instance variables

```
{_opaque_pthread_rwlock_t="__sig"q"__opaque"[192c]} _sharedResourceDirectoryRWLock;
@"NSMutableDictionary" _sharedResourceDirectoryByCategory;
{_opaque_pthread_mutex_t="__sig"q"__opaque"[56c]} _resourceCreationMutex;
@"NSMutableSet" _resourcesBeingCreated;
@"NSMutableDictionary" _conditionVariablesTrackedByResourceCategory;
```

## Class methods

```
+[BWInferenceSharedResourceManager initialize];
+[BWInferenceSharedResourceManager resourceCategory];
```

## Instance methods

```
-[BWInferenceSharedResourceManager init];
-[BWInferenceSharedResourceManager dealloc];
-[BWInferenceSharedResourceManager description];
-[BWInferenceSharedResourceManager retrieveSharedResourceForResourceCategoryAndLockIfNotAvailable:];
-[BWInferenceSharedResourceManager finalizeResourceCreationAttemptForCategory:];
-[BWInferenceSharedResourceManager stashSharedResource:forResourceCategory:];
```
