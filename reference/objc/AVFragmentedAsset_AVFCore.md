# `AVFragmentedAsset`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVURLAsset`
- Protocols: `AVFragmentMinding`
- 1 instance variables, 2 properties, 9 instance methods, 2 class methods

## Instance variables

```
@"AVFragmentedAssetInternal" _fragmentedAsset;
```

## Properties

```
@property (T@"NSArray",R,N) tracks;
@property (TB,R,N,GisAssociatedWithFragmentMinder) associatedWithFragmentMinder;
```

## Class methods

```
+[AVFragmentedAsset fragmentedAssetWithURL:options:];
+[AVFragmentedAsset expectsPropertyRevisedNotifications];
```

## Instance methods

```
-[AVFragmentedAsset isAssociatedWithFragmentMinder];
-[AVFragmentedAsset tracksWithMediaCharacteristic:];
-[AVFragmentedAsset tracksWithMediaType:];
-[AVFragmentedAsset initWithURL:options:];
-[AVFragmentedAsset trackWithTrackID:];
-[AVFragmentedAsset _setIsAssociatedWithFragmentMinder:];
-[AVFragmentedAsset tracks];
-[AVFragmentedAsset _mindsFragments];
-[AVFragmentedAsset _classForAssetTracks];
```
