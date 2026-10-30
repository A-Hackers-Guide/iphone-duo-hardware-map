# `UIDynamicCatalogColor`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIDynamicColor`
- 6 instance variables, 0 properties, 10 instance methods, 1 class methods

## Instance variables

```
@"NSString" _name;
@"_UIAssetManager" _assetManager;
@"UIColor" _genericColor;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _cachedColorLock;
@"UIColor" _cachedColor;
Q _cachedThemeKey;
```

## Class methods

```
+[UIDynamicCatalogColor supportsSecureCoding];
```

## Instance methods

```
-[UIDynamicCatalogColor _debugName];
-[UIDynamicCatalogColor encodeWithCoder:];
-[UIDynamicCatalogColor hash];
-[UIDynamicCatalogColor description];
-[UIDynamicCatalogColor _resolvedColorWithTraitCollection:];
-[UIDynamicCatalogColor copyWithZone:];
-[UIDynamicCatalogColor _debugCatalogBundleIdentifier];
-[UIDynamicCatalogColor _setDebugCatalogBundleIdentifier:];
-[UIDynamicCatalogColor isEqual:];
-[UIDynamicCatalogColor _setDebugName:];
```
