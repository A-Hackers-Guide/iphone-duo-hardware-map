# `PKPaletteButton`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIControl`
- Protocols: `PKPaletteViewSizeScaling`, `UIPointerInteractionDelegate`
- 7 instance variables, 14 properties, 37 instance methods, 12 class methods

## Instance variables

```
B _useCompactLayout;
d _scalingFactor;
@"<PKPaletteButtonDelegate>" _delegate;
@"UIMenu" _menu;
@"UIPointerInteraction" _pointerInteraction;
@"NSHashTable" _observers;
@"UIButton" _button;
```

## Properties

```
@property (T@"NSHashTable",&,N,V_observers) observers;
@property (T@"UIButton",R,N,V_button) button;
@property (T@"UIColor",R,N) _tintColorForCurrentState;
@property (T@"UIColor",R,N) _backgroundColor;
@property (T@"<PKPaletteButtonDelegate>",W,N,V_delegate) delegate;
@property (T@"UIMenu",&,N,V_menu) menu;
@property (TB,N,V_useCompactLayout) useCompactLayout;
@property (T@"UIPointerInteraction",&,N,V_pointerInteraction) pointerInteraction;
@property (TB,R,N) hasContextMenuVisible;
@property (Td,N,V_scalingFactor) scalingFactor;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[PKPaletteButton closeButton];
+[PKPaletteButton redoButton];
+[PKPaletteButton textButton];
+[PKPaletteButton undoButton];
+[PKPaletteButton _preventsAppearanceProxyCustomization];
+[PKPaletteButton keyboardButton];
+[PKPaletteButton plusButton];
+[PKPaletteButton returnKeyButton];
+[PKPaletteButton UCBButton];
+[PKPaletteButton ellipsisButton];
+[PKPaletteButton emojiKeyboardButton];
+[PKPaletteButton shapeButton];
```

## Instance methods

```
-[PKPaletteButton menu];
-[PKPaletteButton setPointerInteraction:];
-[PKPaletteButton initWithImage:];
-[PKPaletteButton setSelected:];
-[PKPaletteButton intrinsicContentSize];
-[PKPaletteButton _backgroundColor];
-[PKPaletteButton pointerInteraction:styleForRegion:];
-[PKPaletteButton setHidden:];
-[PKPaletteButton contextMenuInteraction:configurationForMenuAtLocation:];
-[PKPaletteButton scalingFactor];
-[PKPaletteButton button];
-[PKPaletteButton layoutSubviews];
-[PKPaletteButton setDelegate:];
-[PKPaletteButton setHighlighted:];
-[PKPaletteButton pointerInteraction];
-[PKPaletteButton setEnabled:];
-[PKPaletteButton pointerInteraction:regionForRequest:defaultRegion:];
-[PKPaletteButton delegate];
-[PKPaletteButton setScalingFactor:];
-[PKPaletteButton setObservers:];
-[PKPaletteButton traitCollectionDidChange:];
-[PKPaletteButton observers];
-[PKPaletteButton _updateUI];
-[PKPaletteButton initWithFrame:];
-[PKPaletteButton setMenu:];
-[PKPaletteButton dismissContextMenu];
-[PKPaletteButton useCompactLayout];
-[PKPaletteButton setUseCompactLayout:];
-[PKPaletteButton _buttonTransform];
-[PKPaletteButton _notifyIntrinsicContentSizeDidChange];
-[PKPaletteButton _tintColorForCurrentState];
-[PKPaletteButton _uiButtonInstance];
-[PKPaletteButton _wantsCustomBackgroundColor];
-[PKPaletteButton _wantsCustomTintColor];
-[PKPaletteButton addIntrinsicContentSizeObserver:];
-[PKPaletteButton hasContextMenuVisible];
-[PKPaletteButton removeIntrinsicContentSizeObserver:];
```
