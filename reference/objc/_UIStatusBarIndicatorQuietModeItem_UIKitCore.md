# `_UIStatusBarIndicatorQuietModeItem`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIStatusBarIndicatorItem`
- 2 instance variables, 2 properties, 11 instance methods, 1 class methods

## Instance variables

```
@"NSString" _focusName;
@"_UIStatusBarImageView" _emphasizedImageView;
```

## Properties

```
@property (T@"_UIStatusBarImageView",&,N,V_emphasizedImageView) emphasizedImageView;
@property (T@"NSString",&,N,V_focusName) focusName;
```

## Class methods

```
+[_UIStatusBarIndicatorQuietModeItem emphasizedQuietModeIdentifier];
```

## Instance methods

```
-[_UIStatusBarIndicatorQuietModeItem viewForIdentifier:];
-[_UIStatusBarIndicatorQuietModeItem shouldUpdateIndicatorForIdentifier:];
-[_UIStatusBarIndicatorQuietModeItem imageViewForIdentifier:];
-[_UIStatusBarIndicatorQuietModeItem setEmphasizedImageView:];
-[_UIStatusBarIndicatorQuietModeItem focusName];
-[_UIStatusBarIndicatorQuietModeItem indicatorEntryKey];
-[_UIStatusBarIndicatorQuietModeItem setFocusName:];
-[_UIStatusBarIndicatorQuietModeItem applyUpdate:toDisplayItem:];
-[_UIStatusBarIndicatorQuietModeItem _create_emphasizedImageView];
-[_UIStatusBarIndicatorQuietModeItem systemImageNameForUpdate:];
-[_UIStatusBarIndicatorQuietModeItem emphasizedImageView];
```
