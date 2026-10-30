# `UIImageAsset`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 11 instance variables, 8 properties, 53 instance methods, 3 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
@"NSBundle" _containingBundle;
@"UITraitCollection" _defaultTraitCollection;
{?="hasRegisteredImages"b1"supportsBlockGeneration"b1"isUncached"b1"isIconAsset"b1} _assetFlags;
@"_UIAssetManager" _strongAssetManager;
@"_UIAssetManager" _assetManager;
@"CUINamedLayerStack" _layerStack;
@ _unpinObserver;
@? _rebuildStackImage;
@? _creationBlock;
@"NSString" _assetName;
```

## Properties

```
@property (T@?,C,N,V_creationBlock) creationBlock;
@property (T@,W,N,S_setUnpinObserver:,V_unpinObserver) _unpinObserver;
@property (T@"NSString",C,N,V_assetName) assetName;
@property (T@"_UIAssetManager",W,V_assetManager) _assetManager;
@property (T@"UITraitCollection",R,N,V_defaultTraitCollection) _defaultTraitCollection;
@property (TB,N,S_setStronglyRetainsAssetManager:) _stronglyRetainsAssetManager;
@property (T@?,C,N,S_setRebuildStackImage:,V_rebuildStackImage) _rebuildStackImage;
@property (T@"CUINamedLayerStack",&,N,S_setLayerStack:,V_layerStack) _layerStack;
```

## Class methods

```
+[UIImageAsset supportsSecureCoding];
+[UIImageAsset _dynamicAssetNamed:generator:];
+[UIImageAsset _uncachedDynamicIconAssetNamed:generator:];
```

## Instance methods

```
-[UIImageAsset _unregisterImageWithDescription:];
-[UIImageAsset setAssetName:];
-[UIImageAsset _withLock_unregisterImageWithDescription:];
-[UIImageAsset _cacheRendition:forKey:];
-[UIImageAsset _symbolConfiguration];
-[UIImageAsset _rebuildStackImage];
-[UIImageAsset _containsImagesInPath:];
-[UIImageAsset _clearResolvedImageResources];
-[UIImageAsset _disconnectFromAssetManager];
-[UIImageAsset _withLock_mutableCatalog];
-[UIImageAsset setCreationBlock:];
-[UIImageAsset _initWithAssetName:forManager:];
-[UIImageAsset _canProvideCatalogData];
-[UIImageAsset _layerStack];
-[UIImageAsset _unpinObserver];
-[UIImageAsset _renditionCache:];
-[UIImageAsset registerImage:withTraitCollection:];
-[UIImageAsset unregisterImageWithTraitCollection:];
-[UIImageAsset _stronglyRetainsAssetManager];
-[UIImageAsset _withLock_imageWithConfiguration:];
-[UIImageAsset _setUnpinObserver:];
-[UIImageAsset _registerImage:withConfiguration:];
-[UIImageAsset set_assetManager:];
-[UIImageAsset _cachedRenditionForKey:];
-[UIImageAsset creationBlock];
-[UIImageAsset _withLock_catalogData];
-[UIImageAsset registerImage:withConfiguration:];
-[UIImageAsset imageWithTraitCollection:];
-[UIImageAsset _catalogData];
-[UIImageAsset _withLock_registerImage:withConfiguration:];
-[UIImageAsset _performLookUpRegisteredObjectForTraitCollection:withAccessorWithAppearanceName:];
-[UIImageAsset assetName];
-[UIImageAsset unregisterImageWithConfiguration:];
-[UIImageAsset init];
-[UIImageAsset _setRebuildStackImage:];
-[UIImageAsset dealloc];
-[UIImageAsset _withLock_lookUpRegisteredObjectForTraitCollection:withAccessorWithAppearanceName:];
-[UIImageAsset _unsafe_mutableCatalog];
-[UIImageAsset _initWithAssetName:forFilesInBundle:];
-[UIImageAsset _nameForStoringRuntimeRegisteredImagesInMutableCatalog];
-[UIImageAsset _unsafe_registerImage:withConfiguration:];
-[UIImageAsset encodeWithCoder:];
-[UIImageAsset _setLayerStack:];
-[UIImageAsset hash];
-[UIImageAsset _withLock_updateAssetFromBlockGenerationWithConfiguration:resolvedCatalogImage:];
-[UIImageAsset initWithCoder:];
-[UIImageAsset _defaultTraitCollection];
-[UIImageAsset isEqual:];
-[UIImageAsset imageWithConfiguration:];
-[UIImageAsset _withLock_registeredAppearanceNames];
-[UIImageAsset _assetManager];
-[UIImageAsset _setStronglyRetainsAssetManager:];
-[UIImageAsset _isIconAsset];
```
