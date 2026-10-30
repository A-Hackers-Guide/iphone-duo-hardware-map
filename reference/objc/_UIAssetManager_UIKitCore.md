# `_UIAssetManager`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 18 instance variables, 7 properties, 51 instance methods, 13 class methods

## Instance variables

```
@"_UICache" _imageCache;
@"CUICatalog" _catalog;
@"NSString" _assetManagerName;
q _preferredIdiom;
d _preferredScale;
Q _preferredIdiomSubtype;
q _preferredGamut;
q _preferredLayoutDirectionTrait;
@"NSBundle" _bundle;
@"NSMapTable" _assetMap;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _assetMapLock;
@"CUIMutableCatalog" _runtimeCatalog;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _runtimeCatalogCreationLock;
@"UITraitCollection" _preferredTraitCollection;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _preferredTraitCollectionLock;
@"NSData" _assetData;
Q _type;
{?="isStandaloneAssetManager"b1} _assetManagerFlags;
```

## Properties

```
@property (Td,N,V_preferredScale) preferredScale;
@property (T@"UITraitCollection",&,N,V_preferredTraitCollection) preferredTraitCollection;
@property (T@"NSString",R,N) carFileName;
@property (T@"CUIMutableCatalog",R,N) runtimeCatalog;
@property (T@"NSBundle",R,N,V_bundle) bundle;
@property (TB,R,N,G_managingUIKitAssets) managingUIKitAssets;
@property (TB,R,N,G_managingCoreGlyphs) managingCoreGlyphs;
```

## Class methods

```
+[_UIAssetManager _clearAllCachedImagesAndAssets];
+[_UIAssetManager _dropResourceReferencesForURL:];
+[_UIAssetManager _saveAssetManager:forBundle:lock:];
+[_UIAssetManager _executeUnitTestWithAssetManagerCache:];
+[_UIAssetManager _userInterfaceIdiomForDeviceClass:];
+[_UIAssetManager sharedRuntimeCatalog];
+[_UIAssetManager newAssetNamed:fromBundle:];
+[_UIAssetManager assetManagerForBundle:];
+[_UIAssetManager clearSharedRuntimeAssetMapForUnitTests];
+[_UIAssetManager sharedRuntimeAssetMap];
+[_UIAssetManager _sharedRuntimeAssetMapKeyForAssetName:inAssetManager:];
+[_UIAssetManager _assetManagerCache];
+[_UIAssetManager _sharedRuntimeAssetMapKeyForAssetName:fromFilesInBundle:];
```

## Instance methods

```
-[_UIAssetManager imageNamed:withTrait:];
-[_UIAssetManager _insertAssetIntoMap:forName:lock:];
-[_UIAssetManager _assetForName:];
-[_UIAssetManager bundle];
-[_UIAssetManager imageNamed:configuration:];
-[_UIAssetManager _performLookUpObjectForTraitCollection:outNamedLookup:objectAccessor:];
-[_UIAssetManager _managingCoreGlyphs];
-[_UIAssetManager _imageIsSystemImage:];
-[_UIAssetManager _imageBelongsToCoreGlyphs:];
-[_UIAssetManager resolvedColorNamed:withTraitCollection:];
-[_UIAssetManager _defaultAppearanceNames];
-[_UIAssetManager _isSystemAssetManager];
-[_UIAssetManager _clearCachedResources:];
-[_UIAssetManager _appearanceNames];
-[_UIAssetManager dealloc];
-[_UIAssetManager _managingUIKitAssets];
-[_UIAssetManager _allImageNames];
-[_UIAssetManager imageNamed:scale:idiom:subtype:];
-[_UIAssetManager setPreferredScale:];
-[_UIAssetManager _initWithCatalog:idiom:];
-[_UIAssetManager imageNamed:idiom:subtype:];
-[_UIAssetManager _translateAppearanceNameToNative:];
-[_UIAssetManager _initWithName:inBundle:idiom:lock:allowMissingCatalog:type:];
-[_UIAssetManager imageNamed:configuration:cachingOptions:attachCatalogImage:];
-[_UIAssetManager runtimeCatalog];
-[_UIAssetManager preferredTraitCollection];
-[_UIAssetManager preferredScale];
-[_UIAssetManager _disconnectImageAssets];
-[_UIAssetManager dataNamed:];
-[_UIAssetManager _lookUpObjectForTraitCollection:objectAccessor:];
-[_UIAssetManager colorNamed:withTraitCollection:];
-[_UIAssetManager disableCacheFlushing];
-[_UIAssetManager _insertAssetIntoMap:forName:];
-[_UIAssetManager initWithName:inBundle:idiom:];
-[_UIAssetManager _initWithName:inBundle:idiom:type:];
-[_UIAssetManager carFileName];
-[_UIAssetManager _hasMultipleAppearances];
-[_UIAssetManager _clearCachedResources];
-[_UIAssetManager description];
-[_UIAssetManager _assetFromMapForName:];
-[_UIAssetManager imageNamed:idiom:];
-[_UIAssetManager _catalogDataForSymbolImageNamed:];
-[_UIAssetManager setPreferredTraitCollection:];
-[_UIAssetManager imageNamed:];
-[_UIAssetManager _performBlockWithAssetLock:];
-[_UIAssetManager _carPlayAssetManager];
-[_UIAssetManager _assetFromMapForName:lock:];
-[_UIAssetManager initWithData:idiom:error:];
-[_UIAssetManager initManagerWithoutCatalogWithName:];
-[_UIAssetManager initWithURL:idiom:error:];
-[_UIAssetManager _imageBelongsToUIKit:];
```
