# `MTLResourceListPool`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 0 properties, 4 instance methods, 0 class methods

## Instance variables

```
{_MTLResourceListPoolPrivate="queue"{resourceListQueue="tqh_first"@"MTLResourceList""tqh_last"^@}"lock"{os_unfair_lock_s="_os_unfair_lock_opaque"I}"count"i} _priv;
i _resourceListCapacity;
```

## Instance methods

```
-[MTLResourceListPool availableCount];
-[MTLResourceListPool dealloc];
-[MTLResourceListPool purge];
-[MTLResourceListPool initWithResourceListCapacity:];
```
