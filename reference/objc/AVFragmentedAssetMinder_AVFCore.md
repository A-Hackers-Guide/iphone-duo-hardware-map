# `AVFragmentedAssetMinder`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 2 properties, 10 instance methods, 1 class methods

## Instance variables

```
@"AVFragmentedAssetMinderInternal" _fragmentedAssetMinder;
```

## Properties

```
@property (Td,N) mindingInterval;
@property (T@"NSArray",R,N) assets;
```

## Class methods

```
+[AVFragmentedAssetMinder fragmentedAssetMinderWithAsset:mindingInterval:];
```

## Instance methods

```
-[AVFragmentedAssetMinder init];
-[AVFragmentedAssetMinder dealloc];
-[AVFragmentedAssetMinder assets];
-[AVFragmentedAssetMinder mindingInterval];
-[AVFragmentedAssetMinder _setMindingInterval:removeAllAssets:];
-[AVFragmentedAssetMinder _throwsWhenAlreadyMindedAssetIsAdded];
-[AVFragmentedAssetMinder addFragmentedAsset:];
-[AVFragmentedAssetMinder initWithAsset:mindingInterval:];
-[AVFragmentedAssetMinder removeFragmentedAsset:];
-[AVFragmentedAssetMinder setMindingInterval:];
```
