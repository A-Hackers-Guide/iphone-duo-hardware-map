# `UISwipeActionButton`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIButton`
- 6 instance variables, 8 properties, 32 instance methods, 0 class methods

## Instance variables

```
B _autosizes;
@"UIColor" _defaultBackgroundColor;
@"UIColor" _highlightedBackgroundColor;
@"<UISwipeActionVisualStyle>" _visualStyle;
@"<_UISwipeActionButtonDelegate>" _swipeActionButtonDelegate;
@"UIView" _backgroundView;
```

## Properties

```
@property (T@"<_UISwipeActionButtonDelegate>",W,N,V_swipeActionButtonDelegate) swipeActionButtonDelegate;
@property (T@"UIView",&,N,V_backgroundView) backgroundView;
@property (T@"<UISwipeActionVisualStyle>",&,N,V_visualStyle) visualStyle;
@property (T@"UIColor",&,N,V_defaultBackgroundColor) defaultBackgroundColor;
@property (T@"UIColor",&,N,V_highlightedBackgroundColor) highlightedBackgroundColor;
@property (Td,R,N) buttonWidth;
@property (TB,N,V_autosizes) autosizes;
@property (T@"UIView",R,N) sourceView;
```

## Instance methods

```
-[UISwipeActionButton contextMenuInteraction:willEndForConfiguration:animator:];
-[UISwipeActionButton setVisualStyle:];
-[UISwipeActionButton visualStyle];
-[UISwipeActionButton setDefaultBackgroundColor:];
-[UISwipeActionButton defaultBackgroundColor];
-[UISwipeActionButton contextMenuInteraction:willDisplayMenuForConfiguration:animator:];
-[UISwipeActionButton setBackgroundColor:];
-[UISwipeActionButton setHighlighted:];
-[UISwipeActionButton setTitle:forState:];
-[UISwipeActionButton backgroundView];
-[UISwipeActionButton titleFont];
-[UISwipeActionButton defaultButtonWidth];
-[UISwipeActionButton initWithFrame:];
-[UISwipeActionButton setBackgroundView:];
-[UISwipeActionButton sourceView];
-[UISwipeActionButton _titleFontWeightForCurrentIdiom];
-[UISwipeActionButton _allowableContentRectForContentRect:];
-[UISwipeActionButton _defaultLayoutForHeight:];
-[UISwipeActionButton _heightDemandsCompactLayout];
-[UISwipeActionButton _horizontalPaddingForCurrentIdiom];
-[UISwipeActionButton _maxFontSizeForCurrentIdiom];
-[UISwipeActionButton _minFontSizeForCurrentIdiom];
-[UISwipeActionButton _minScaleFactorForFont:];
-[UISwipeActionButton _numberOfLinesForTitle:];
-[UISwipeActionButton autosizes];
-[UISwipeActionButton buttonWidth];
-[UISwipeActionButton highlightedBackgroundColor];
-[UISwipeActionButton setAutosizes:];
-[UISwipeActionButton setHighlightedBackgroundColor:];
-[UISwipeActionButton setSwipeActionButtonDelegate:];
-[UISwipeActionButton swipeActionButtonDelegate];
-[UISwipeActionButton titleFontOfSize:];
```
