# `UIListContentView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `_UIContentViewComponentDescribing`, `_UIContentViewDefaultStylingObtaining`, `UIContentView`
- 13 instance variables, 14 properties, 31 instance methods, 0 class methods

## Instance variables

```
@"UIListContentConfiguration" _animatingFromConfiguration;
@"UIListContentConfiguration" _animatingToConfiguration;
d _preferredMaxLayoutWidth;
@"_UIContentViewEditingController" _editingController;
{?="imageViewFrameInvalid"b1"textLabelFrameInvalid"b1"secondaryTextLabelFrameInvalid"b1} _contentViewFlags;
@"UIListContentConfiguration" _configuration;
@"_UIListContentImageView" _imageView;
@"UILabel" _textLabel;
@"UILabel" _secondaryTextLabel;
@? _primaryTextFrameDidChangeHandler;
@"UILayoutGuide" _textLayoutGuide;
@"UILayoutGuide" _secondaryTextLayoutGuide;
@"UILayoutGuide" _imageLayoutGuide;
```

## Properties

```
@property (T@"UIListContentConfiguration",C,N,V_configuration) configuration;
@property (T@"UILayoutGuide",R,N,V_textLayoutGuide) textLayoutGuide;
@property (T@"UILayoutGuide",R,N,V_secondaryTextLayoutGuide) secondaryTextLayoutGuide;
@property (T@"UILayoutGuide",R,N,V_imageLayoutGuide) imageLayoutGuide;
@property (T@"NSLayoutRect",R,N) _primaryTextLayoutRect;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) _primaryTextLayoutFrame;
@property (T@?,C,N,S_setPrimaryTextFrameDidChangeHandler:,V_primaryTextFrameDidChangeHandler) _primaryTextFrameDidChangeHandler;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@?,?,C,N,S_setDefaultListContentConfigurationProvider:) _defaultListContentConfigurationProvider;
@property (Tq,?,R,N) _listCellStyle;
@property (Tq,?,R,N) _listCellProminence;
```

## Instance methods

```
-[UIListContentView imageLayoutGuide];
-[UIListContentView _preferredMaxLayoutWidth];
-[UIListContentView _layoutMarginsDidChangeFromOldMargins:];
-[UIListContentView _multilineContextWidth];
-[UIListContentView supportsConfiguration:];
-[UIListContentView _intrinsicSizeWithinSize:];
-[UIListContentView _primaryTextLayoutRect];
-[UIListContentView _primaryTextFrameDidChangeHandler];
-[UIListContentView _listCellProminence];
-[UIListContentView becomeFirstResponder];
-[UIListContentView setConfiguration:];
-[UIListContentView _textLegibilityOrContentSizeTraitsChanged];
-[UIListContentView _prepareForSecondIntrinsicContentSizeCalculationWithLayoutEngineBounds:];
-[UIListContentView layoutSubviews];
-[UIListContentView _setPrimaryTextFrameDidChangeHandler:];
-[UIListContentView textLayoutGuide];
-[UIListContentView initWithConfiguration:];
-[UIListContentView _setMultilineContextWidth:];
-[UIListContentView _encodableSubviews];
-[UIListContentView _prepareForFirstIntrinsicContentSizeCalculation];
-[UIListContentView sizeThatFits:];
-[UIListContentView _needsDoubleUpdateConstraintsPass];
-[UIListContentView configuration];
-[UIListContentView encodeWithCoder:];
-[UIListContentView description];
-[UIListContentView _listCellStyle];
-[UIListContentView initWithCoder:];
-[UIListContentView _primaryTextLayoutFrame];
-[UIListContentView secondaryTextLayoutGuide];
-[UIListContentView _shouldAnimatePropertyWithKey:];
-[UIListContentView systemLayoutSizeFittingSize:withHorizontalFittingPriority:verticalFittingPriority:];
```
