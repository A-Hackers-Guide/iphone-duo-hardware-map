# `_UIStatusBarIndicatorLocationItem`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIStatusBarIndicatorItem`
- 2 instance variables, 2 properties, 13 instance methods, 2 class methods

## Instance variables

```
@"_UIStatusBarImageView" _prominentImageView;
q _previousType;
```

## Properties

```
@property (T@"_UIStatusBarImageView",&,N,V_prominentImageView) prominentImageView;
@property (Tq,N,V_previousType) previousType;
```

## Class methods

```
+[_UIStatusBarIndicatorLocationItem groupWithPriority:];
+[_UIStatusBarIndicatorLocationItem prominentDisplayIdentifier];
```

## Instance methods

```
-[_UIStatusBarIndicatorLocationItem previousType];
-[_UIStatusBarIndicatorLocationItem initWithIdentifier:statusBar:];
-[_UIStatusBarIndicatorLocationItem viewForIdentifier:];
-[_UIStatusBarIndicatorLocationItem prominentImageView];
-[_UIStatusBarIndicatorLocationItem createDisplayItemForIdentifier:];
-[_UIStatusBarIndicatorLocationItem canEnableDisplayItem:fromData:];
-[_UIStatusBarIndicatorLocationItem setPreviousType:];
-[_UIStatusBarIndicatorLocationItem indicatorEntryKey];
-[_UIStatusBarIndicatorLocationItem applyUpdate:toDisplayItem:];
-[_UIStatusBarIndicatorLocationItem setProminentImageView:];
-[_UIStatusBarIndicatorLocationItem _create_prominentImageView];
-[_UIStatusBarIndicatorLocationItem systemImageNameForUpdate:];
-[_UIStatusBarIndicatorLocationItem overriddenStyleAttributesForData:identifier:];
```
