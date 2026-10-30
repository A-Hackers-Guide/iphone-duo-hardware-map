# `MTLToolsObjectCache`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 0 properties, 5 instance methods, 0 class methods

## Instance variables

```
@"NSMapTable" _map;
{recursive_mutex="__m_"{_opaque_pthread_mutex_t="__sig"q"__opaque"[56c]}} _lock;
{vector<id, std::allocator<id>>="__begin_"^@"__end_"^@""{?="__cap_"^@}} _keyRemoveList;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _listLock;
```

## Instance methods

```
-[MTLToolsObjectCache init];
-[MTLToolsObjectCache dealloc];
-[MTLToolsObjectCache removeKey:];
-[MTLToolsObjectCache getCachedObjectForKey:];
-[MTLToolsObjectCache getCachedObjectForKey:onMiss:];
```
