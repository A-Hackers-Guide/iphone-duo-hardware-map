# `_UIBasicCellContentView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `_UIContentViewComponentDescribing`, `_UIContentView`
- 8 instance variables, 11 properties, 26 instance methods, 0 class methods

## Instance variables

```
@"_UIBasicCellContentViewConfiguration" _animatingFromConfiguration;
@"_UIBasicCellContentViewConfiguration" _animatingToConfiguration;
d _preferredMaxLayoutWidth;
@"_UIContentViewEditingController" _editingController;
@"_UIBasicCellContentViewConfiguration" _configuration;
@"UIImageView" _imageView;
@"UILabel" _textLabel;
@? _primaryTextFrameDidChangeHandler;
```

## Properties

```
@property (T@"_UIBasicCellContentViewConfiguration",C,N,V_configuration) configuration;
@property (T@"UIImageView",R,N,V_imageView) imageView;
@property (T@"UILabel",R,N,V_textLabel) textLabel;
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
-[_UIBasicCellContentView _preferredMaxLayoutWidth];
-[_UIBasicCellContentView _layoutMarginsDidChangeFromOldMargins:];
-[_UIBasicCellContentView _multilineContextWidth];
-[_UIBasicCellContentView _intrinsicSizeWithinSize:];
-[_UIBasicCellContentView _primaryTextLayoutRect];
-[_UIBasicCellContentView _primaryTextFrameDidChangeHandler];
-[_UIBasicCellContentView textLabel];
-[_UIBasicCellContentView becomeFirstResponder];
-[_UIBasicCellContentView setConfiguration:];
-[_UIBasicCellContentView _prepareForSecondIntrinsicContentSizeCalculationWithLayoutEngineBounds:];
-[_UIBasicCellContentView layoutSubviews];
-[_UIBasicCellContentView _setPrimaryTextFrameDidChangeHandler:];
-[_UIBasicCellContentView initWithConfiguration:];
-[_UIBasicCellContentView _setMultilineContextWidth:];
-[_UIBasicCellContentView _encodableSubviews];
-[_UIBasicCellContentView _prepareForFirstIntrinsicContentSizeCalculation];
-[_UIBasicCellContentView sizeThatFits:];
-[_UIBasicCellContentView _needsDoubleUpdateConstraintsPass];
-[_UIBasicCellContentView configuration];
-[_UIBasicCellContentView encodeWithCoder:];
-[_UIBasicCellContentView description];
-[_UIBasicCellContentView initWithCoder:];
-[_UIBasicCellContentView _primaryTextLayoutFrame];
-[_UIBasicCellContentView imageView];
-[_UIBasicCellContentView systemLayoutSizeFittingSize:withHorizontalFittingPriority:verticalFittingPriority:];
-[_UIBasicCellContentView _preventFocus];
```
