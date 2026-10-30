# `UIContentUnavailableView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `UIScrollViewDelegate`, `UIContentView`
- 13 instance variables, 15 properties, 52 instance methods, 0 class methods

## Instance variables

```
d _preferredMaxLayoutWidth;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _keyboardFrame;
{?="isEmbeddedInWrapperView"b1"trackingKeyboardFrame"b1"adjustsLayoutForKeyboard"b1"imageViewFrameInvalid"b1"activityIndicatorFrameInvalid"b1"textLabelFrameInvalid"b1"secondaryTextLabelFrameInvalid"b1"buttonFrameInvalid"b1"secondaryButtonFrameInvalid"b1} _contentViewFlags;
B _scrollEnabled;
@"UIContentUnavailableConfiguration" _configuration;
@"UIImageView" _imageView;
@"UILabel" _textLabel;
@"UILabel" _secondaryTextLabel;
@"UIButton" _button;
@"UIButton" _secondaryButton;
@"UIActivityIndicatorView" _activityIndicator;
@"_UIContentUnavailableScrollView" _scrollView;
@"_UISystemBackgroundView" _backgroundView;
```

## Properties

```
@property (T@"UIImageView",R,N,G_imageView,V_imageView) imageView;
@property (T@"UILabel",R,N,G_textLabel,V_textLabel) textLabel;
@property (T@"UILabel",R,N,G_secondaryTextLabel,V_secondaryTextLabel) secondaryTextLabel;
@property (T@"UIButton",R,N,G_button,V_button) button;
@property (T@"UIButton",R,N,G_secondaryButton,V_secondaryButton) secondaryButton;
@property (T@"UIActivityIndicatorView",R,N,G_activityIndicator,V_activityIndicator) activityIndicator;
@property (T@"_UIContentUnavailableScrollView",R,N,G_scrollView,V_scrollView) scrollView;
@property (T@"_UISystemBackgroundView",R,N,G_backgroundView,V_backgroundView) backgroundView;
@property (TB,R,N) shouldReparentScrollViewPanGestureRecognizer;
@property (T@"UIContentUnavailableConfiguration",C,N,V_configuration) configuration;
@property (TB,N,GisScrollEnabled,V_scrollEnabled) scrollEnabled;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UIContentUnavailableView _reconfigureKeyboardLayoutAdjustment];
-[UIContentUnavailableView _scrollView];
-[UIContentUnavailableView _applyBackgroundConfiguration:];
-[UIContentUnavailableView _keyboardAboutToChangeFrame:];
-[UIContentUnavailableView _activityIndicator];
-[UIContentUnavailableView _checkWhetherEmbeddedInWrapperView];
-[UIContentUnavailableView didMoveToWindow];
-[UIContentUnavailableView _imageView];
-[UIContentUnavailableView _preferredMaxLayoutWidth];
-[UIContentUnavailableView _layoutMarginsDidChangeFromOldMargins:];
-[UIContentUnavailableView _registerForTextLegibilityTraitChangesOnView:];
-[UIContentUnavailableView _multilineContextWidth];
-[UIContentUnavailableView _keyboardInset];
-[UIContentUnavailableView supportsConfiguration:];
-[UIContentUnavailableView _secondaryButton];
-[UIContentUnavailableView _intrinsicSizeWithinSize:];
-[UIContentUnavailableView _clearInvalidFrameFlags];
-[UIContentUnavailableView _alignmentInsetsForView:];
-[UIContentUnavailableView _computeButtonLayoutInfo:];
-[UIContentUnavailableView isScrollEnabled];
-[UIContentUnavailableView _button];
-[UIContentUnavailableView _computeLayoutInfoForView:info:layoutInfo:];
-[UIContentUnavailableView _keyboardAboutToShow:];
-[UIContentUnavailableView _computeLayoutInfoRestrictedToSize:];
-[UIContentUnavailableView setConfiguration:];
-[UIContentUnavailableView _textLegibilityOrContentSizeTraitsChanged];
-[UIContentUnavailableView _prepareForSecondIntrinsicContentSizeCalculationWithLayoutEngineBounds:];
-[UIContentUnavailableView _textLabel];
-[UIContentUnavailableView layoutSubviews];
-[UIContentUnavailableView scrollViewDidChangeAdjustedContentInset:];
-[UIContentUnavailableView hitTest:withEvent:];
-[UIContentUnavailableView initWithConfiguration:];
-[UIContentUnavailableView _scrollViewInsets];
-[UIContentUnavailableView _backgroundView];
-[UIContentUnavailableView _secondaryTextLabel];
-[UIContentUnavailableView _setMultilineContextWidth:];
-[UIContentUnavailableView _encodableSubviews];
-[UIContentUnavailableView _prepareForFirstIntrinsicContentSizeCalculation];
-[UIContentUnavailableView _applyConfiguration:];
-[UIContentUnavailableView _handleKeyboardNotification:aboutToHide:];
-[UIContentUnavailableView shouldReparentScrollViewPanGestureRecognizer];
-[UIContentUnavailableView _prefersEqualButtonAndSecondaryButtonWidths];
-[UIContentUnavailableView sizeThatFits:];
-[UIContentUnavailableView _needsDoubleUpdateConstraintsPass];
-[UIContentUnavailableView setScrollEnabled:];
-[UIContentUnavailableView _keyboardAboutToHide:];
-[UIContentUnavailableView configuration];
-[UIContentUnavailableView encodeWithCoder:];
-[UIContentUnavailableView initWithCoder:];
-[UIContentUnavailableView traitCollectionDidChange:];
-[UIContentUnavailableView didMoveToSuperview];
-[UIContentUnavailableView systemLayoutSizeFittingSize:withHorizontalFittingPriority:verticalFittingPriority:];
```
