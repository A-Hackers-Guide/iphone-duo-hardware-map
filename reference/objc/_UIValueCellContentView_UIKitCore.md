# `_UIValueCellContentView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `_UIContentViewComponentDescribing`, `_UIContentView`
- 8 instance variables, 12 properties, 25 instance methods, 0 class methods

## Instance variables

```
@"_UIValueCellContentViewConfiguration" _animatingFromConfiguration;
@"_UIValueCellContentViewConfiguration" _animatingToConfiguration;
d _preferredMaxLayoutWidth;
@"_UIValueCellContentViewConfiguration" _configuration;
@"UIImageView" _imageView;
@"UILabel" _textLabel;
@"UILabel" _valueLabel;
@? _primaryTextFrameDidChangeHandler;
```

## Properties

```
@property (T@"_UIValueCellContentViewConfiguration",C,N,V_configuration) configuration;
@property (T@"UIImageView",R,N,V_imageView) imageView;
@property (T@"UILabel",R,N,V_textLabel) textLabel;
@property (T@"UILabel",R,N,V_valueLabel) valueLabel;
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
-[_UIValueCellContentView valueLabel];
-[_UIValueCellContentView _preferredMaxLayoutWidth];
-[_UIValueCellContentView _layoutMarginsDidChangeFromOldMargins:];
-[_UIValueCellContentView _multilineContextWidth];
-[_UIValueCellContentView _intrinsicSizeWithinSize:];
-[_UIValueCellContentView _primaryTextLayoutRect];
-[_UIValueCellContentView _primaryTextFrameDidChangeHandler];
-[_UIValueCellContentView textLabel];
-[_UIValueCellContentView setConfiguration:];
-[_UIValueCellContentView _prepareForSecondIntrinsicContentSizeCalculationWithLayoutEngineBounds:];
-[_UIValueCellContentView layoutSubviews];
-[_UIValueCellContentView _setPrimaryTextFrameDidChangeHandler:];
-[_UIValueCellContentView initWithConfiguration:];
-[_UIValueCellContentView _setMultilineContextWidth:];
-[_UIValueCellContentView _encodableSubviews];
-[_UIValueCellContentView _prepareForFirstIntrinsicContentSizeCalculation];
-[_UIValueCellContentView sizeThatFits:];
-[_UIValueCellContentView _needsDoubleUpdateConstraintsPass];
-[_UIValueCellContentView configuration];
-[_UIValueCellContentView encodeWithCoder:];
-[_UIValueCellContentView description];
-[_UIValueCellContentView initWithCoder:];
-[_UIValueCellContentView _primaryTextLayoutFrame];
-[_UIValueCellContentView imageView];
-[_UIValueCellContentView systemLayoutSizeFittingSize:withHorizontalFittingPriority:verticalFittingPriority:];
```
