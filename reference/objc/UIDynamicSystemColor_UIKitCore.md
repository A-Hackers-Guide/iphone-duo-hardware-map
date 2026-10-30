# `UIDynamicSystemColor`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIDynamicColor`
- 4 instance variables, 0 properties, 5 instance methods, 0 class methods

## Instance variables

```
@"NSDictionary" _colorsByThemeKey;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _cachedColorLock;
@"UIColor" _cachedColor;
Q _cachedThemeKey;
```

## Instance methods

```
-[UIDynamicSystemColor hash];
-[UIDynamicSystemColor description];
-[UIDynamicSystemColor _resolvedColorWithTraitCollection:];
-[UIDynamicSystemColor copyWithZone:];
-[UIDynamicSystemColor isEqual:];
```
