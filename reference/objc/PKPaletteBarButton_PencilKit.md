# `PKPaletteBarButton`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PKPaletteButton`
- Protocols: `_UIBarButtonItemViewOwner`
- 3 instance variables, 7 properties, 22 instance methods, 1 class methods

## Instance variables

```
@"UIBarButtonItem" _barButtonItem;
@"UIView" _customView;
@? _menuProvider;
```

## Properties

```
@property (T@"UIView",&,N,V_customView) customView;
@property (T@?,C,N,V_menuProvider) menuProvider;
@property (T@"UIBarButtonItem",R,N,V_barButtonItem) barButtonItem;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[PKPaletteBarButton _imageByApplyingDefaultImageSymbolConfigurationWithImage:];
```

## Instance methods

```
-[PKPaletteBarButton _itemDidChangeWidth:];
-[PKPaletteBarButton customView];
-[PKPaletteBarButton _itemDidChangeSelectionState:];
-[PKPaletteBarButton _itemStandardViewNeedsUpdate:];
-[PKPaletteBarButton _itemDidChangeEnabledState:];
-[PKPaletteBarButton _itemCustomViewDidChange:fromView:];
-[PKPaletteBarButton _itemDidChangeHiddenState:];
-[PKPaletteBarButton contextMenuInteraction:configurationForMenuAtLocation:];
-[PKPaletteBarButton barButtonItem];
-[PKPaletteBarButton layoutSubviews];
-[PKPaletteBarButton setMenuProvider:];
-[PKPaletteBarButton setTintColor:];
-[PKPaletteBarButton setCustomView:];
-[PKPaletteBarButton setScalingFactor:];
-[PKPaletteBarButton initWithBarButtonItem:];
-[PKPaletteBarButton _contextMenuInteraction:styleForMenuWithConfiguration:];
-[PKPaletteBarButton dismissContextMenu];
-[PKPaletteBarButton menuProvider];
-[PKPaletteBarButton _checkCurrentBarButtonItemState];
-[PKPaletteBarButton _handleTouchUpInside:event:];
-[PKPaletteBarButton _updateForButtonItemChange];
-[PKPaletteBarButton _updateMenu];
```
