# `_UIStatusBarIndicatorItem`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIStatusBarItem`
- 2 instance variables, 5 properties, 18 instance methods, 0 class methods

## Instance variables

```
@"NSArray" _currentImageNamePrefixes;
@"_UIStatusBarImageView" _imageView;
```

## Properties

```
@property (T@"NSArray",C,N,V_currentImageNamePrefixes) currentImageNamePrefixes;
@property (T@"_UIStatusBarImageView",&,N,V_imageView) imageView;
@property (T@"NSString",R,N) indicatorEntryKey;
@property (TB,R,N) isTemplateImage;
@property (TB,R,N) flipsForRightToLeftLayoutDirection;
```

## Instance methods

```
-[_UIStatusBarIndicatorItem viewForIdentifier:];
-[_UIStatusBarIndicatorItem setImageView:];
-[_UIStatusBarIndicatorItem shouldUpdateIndicatorForIdentifier:];
-[_UIStatusBarIndicatorItem imageForUpdate:];
-[_UIStatusBarIndicatorItem imageViewForIdentifier:];
-[_UIStatusBarIndicatorItem indicatorEntryKey];
-[_UIStatusBarIndicatorItem dependentEntryKeys];
-[_UIStatusBarIndicatorItem applyUpdate:toDisplayItem:];
-[_UIStatusBarIndicatorItem imageView];
-[_UIStatusBarIndicatorItem imageNameForUpdate:];
-[_UIStatusBarIndicatorItem useMultiColorSystemImageForUpdate:];
-[_UIStatusBarIndicatorItem systemImageNameForUpdate:];
-[_UIStatusBarIndicatorItem flipsForRightToLeftLayoutDirection];
-[_UIStatusBarIndicatorItem isTemplateImage];
-[_UIStatusBarIndicatorItem _create_imageView];
-[_UIStatusBarIndicatorItem crossfadeForUpdate:];
-[_UIStatusBarIndicatorItem currentImageNamePrefixes];
-[_UIStatusBarIndicatorItem setCurrentImageNamePrefixes:];
```
