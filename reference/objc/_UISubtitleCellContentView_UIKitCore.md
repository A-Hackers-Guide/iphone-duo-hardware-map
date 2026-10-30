# `_UISubtitleCellContentView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `_UIContentViewComponentDescribing`, `_UIContentView`
- 9 instance variables, 12 properties, 27 instance methods, 0 class methods

## Instance variables

```
@"_UISubtitleCellContentViewConfiguration" _animatingFromConfiguration;
@"_UISubtitleCellContentViewConfiguration" _animatingToConfiguration;
d _preferredMaxLayoutWidth;
@"_UIContentViewEditingController" _editingController;
@"_UISubtitleCellContentViewConfiguration" _configuration;
@"UIImageView" _imageView;
@"UILabel" _textLabel;
@"UILabel" _subtitleLabel;
@? _primaryTextFrameDidChangeHandler;
```

## Properties

```
@property (T@"_UISubtitleCellContentViewConfiguration",C,N,V_configuration) configuration;
@property (T@"UIImageView",R,N,V_imageView) imageView;
@property (T@"UILabel",R,N,V_textLabel) textLabel;
@property (T@"UILabel",R,N,V_subtitleLabel) subtitleLabel;
@property (T@"NSLayoutRect",R,N) _primaryTextLayoutRect;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) _primaryTextLayoutFrame;
@property (T@?,C,N,S_setPrimaryTextFrameDidChangeHandler:,V_primaryTextFrameDidChangeHandler) _primaryTextFrameDidChangeHandler;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TB,?,R,N) _preventFocus;
```

## Instance methods

```
-[_UISubtitleCellContentView subtitleLabel];
-[_UISubtitleCellContentView _preferredMaxLayoutWidth];
-[_UISubtitleCellContentView _layoutMarginsDidChangeFromOldMargins:];
-[_UISubtitleCellContentView _multilineContextWidth];
-[_UISubtitleCellContentView _intrinsicSizeWithinSize:];
-[_UISubtitleCellContentView _primaryTextLayoutRect];
-[_UISubtitleCellContentView _primaryTextFrameDidChangeHandler];
-[_UISubtitleCellContentView textLabel];
-[_UISubtitleCellContentView becomeFirstResponder];
-[_UISubtitleCellContentView setConfiguration:];
-[_UISubtitleCellContentView _prepareForSecondIntrinsicContentSizeCalculationWithLayoutEngineBounds:];
-[_UISubtitleCellContentView layoutSubviews];
-[_UISubtitleCellContentView _setPrimaryTextFrameDidChangeHandler:];
-[_UISubtitleCellContentView initWithConfiguration:];
-[_UISubtitleCellContentView _setMultilineContextWidth:];
-[_UISubtitleCellContentView _encodableSubviews];
-[_UISubtitleCellContentView _prepareForFirstIntrinsicContentSizeCalculation];
-[_UISubtitleCellContentView sizeThatFits:];
-[_UISubtitleCellContentView _needsDoubleUpdateConstraintsPass];
-[_UISubtitleCellContentView configuration];
-[_UISubtitleCellContentView encodeWithCoder:];
-[_UISubtitleCellContentView description];
-[_UISubtitleCellContentView initWithCoder:];
-[_UISubtitleCellContentView _primaryTextLayoutFrame];
-[_UISubtitleCellContentView imageView];
-[_UISubtitleCellContentView systemLayoutSizeFittingSize:withHorizontalFittingPriority:verticalFittingPriority:];
-[_UISubtitleCellContentView _preventFocus];
```
