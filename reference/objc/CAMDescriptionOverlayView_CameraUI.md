# `CAMDescriptionOverlayView`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 21 instance variables, 24 properties, 72 instance methods, 0 class methods

## Instance variables

```
B _blackoutFrameVisible;
B __isDisplayZoomed;
@"<CAMDescriptionOverlayViewDelegate>" _delegate;
q _orientation;
d _contentBottomInset;
d _maxContentWidth;
@"UIVisualEffectView" __blurEffectView;
@"UIView" __blackoutView;
@"CAShapeLayer" __blackoutMask;
@"CAMPortraitModeDescriptionOverlayPrimaryVibrancyEffectView" __primaryVibrancyEffectView;
@"UILabel" __titleLabel;
@"UILabel" __descriptionTitleLabel;
@"UILabel" __descriptionLabel;
@"UILabel" __infoTitleLabel;
@"UILabel" __infoLabel;
@"UIButton" __detailButton;
@"UIButton" __acknowledgmentButton;
d __descriptionFontSizeMultiplier;
d __infoFontSizeMultiplier;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _viewportFrame;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _textViewFrame;
```

## Properties

```
@property (T@"UIVisualEffectView",R,N,V__blurEffectView) _blurEffectView;
@property (T@"UIView",R,N,V__blackoutView) _blackoutView;
@property (T@"CAShapeLayer",R,N,V__blackoutMask) _blackoutMask;
@property (T@"CAMPortraitModeDescriptionOverlayPrimaryVibrancyEffectView",R,N,V__primaryVibrancyEffectView) _primaryVibrancyEffectView;
@property (T@"UILabel",R,N,V__titleLabel) _titleLabel;
@property (T@"UILabel",R,N,V__descriptionTitleLabel) _descriptionTitleLabel;
@property (T@"UILabel",R,N,V__descriptionLabel) _descriptionLabel;
@property (T@"UILabel",R,N,V__infoTitleLabel) _infoTitleLabel;
@property (T@"UILabel",R,N,V__infoLabel) _infoLabel;
@property (T@"UIButton",R,N,V__detailButton) _detailButton;
@property (T@"UIButton",R,N,V__acknowledgmentButton) _acknowledgmentButton;
@property (Td,N,S_setDescriptionFontSizeMultiplier:,V__descriptionFontSizeMultiplier) _descriptionFontSizeMultiplier;
@property (Td,N,S_setInfoFontSizeMultiplier:,V__infoFontSizeMultiplier) _infoFontSizeMultiplier;
@property (TB,N,S_setIsDisplayZoomed:,V__isDisplayZoomed) _isDisplayZoomed;
@property (T@"<CAMDescriptionOverlayViewDelegate>",W,N,V_delegate) delegate;
@property (TB,N,GisDetailButtonHighlighted) detailButtonHighlighted;
@property (TB,N,GisAcknowledgmentButtonHighlighted) acknowledgmentButtonHighlighted;
@property (Tq,N,V_orientation) orientation;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_viewportFrame) viewportFrame;
@property (Td,N,V_contentBottomInset) contentBottomInset;
@property (Td,N,V_maxContentWidth) maxContentWidth;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_textViewFrame) textViewFrame;
@property (TB,N,GisBlackoutFrameVisible,V_blackoutFrameVisible) blackoutFrameVisible;
@property (TB,R,N,GisVisible) visible;
```

## Instance methods

```
-[CAMDescriptionOverlayView viewportFrame];
-[CAMDescriptionOverlayView setOrientation:animated:];
-[CAMDescriptionOverlayView setOrientation:];
-[CAMDescriptionOverlayView didMoveToWindow];
-[CAMDescriptionOverlayView traitCollection];
-[CAMDescriptionOverlayView detailText];
-[CAMDescriptionOverlayView acknowledgmentTextUsingNarrowWidth:];
-[CAMDescriptionOverlayView currentContentSize];
-[CAMDescriptionOverlayView setTextViewFrame:];
-[CAMDescriptionOverlayView textViewFrame];
-[CAMDescriptionOverlayView orientation];
-[CAMDescriptionOverlayView infoTextUsingNarrowWidth:];
-[CAMDescriptionOverlayView isVisible];
-[CAMDescriptionOverlayView layoutSubviews];
-[CAMDescriptionOverlayView titleTextUsingNarrowWidth:];
-[CAMDescriptionOverlayView acknowledgementButtonTapped];
-[CAMDescriptionOverlayView setDelegate:];
-[CAMDescriptionOverlayView setViewportFrame:];
-[CAMDescriptionOverlayView delegate];
-[CAMDescriptionOverlayView descriptionTextUsingNarrowWidth:];
-[CAMDescriptionOverlayView initWithFrame:];
-[CAMDescriptionOverlayView infoTitleTextUsingNarrowWidth:];
-[CAMDescriptionOverlayView buttonStyle];
-[CAMDescriptionOverlayView _titleLabel];
-[CAMDescriptionOverlayView _infoTitleLabel];
-[CAMDescriptionOverlayView maxContentWidth];
-[CAMDescriptionOverlayView _blurEffectView];
-[CAMDescriptionOverlayView _acknowledgmentButton];
-[CAMDescriptionOverlayView _additionalSpacingForContentSize:];
-[CAMDescriptionOverlayView _blackoutMask];
-[CAMDescriptionOverlayView _blackoutView];
-[CAMDescriptionOverlayView _buttonTitleTransformerForTextStyle:];
-[CAMDescriptionOverlayView _contentSizeCategory:exceedsMaximum:];
-[CAMDescriptionOverlayView _descriptionFontSizeMultiplier];
-[CAMDescriptionOverlayView _descriptionLabel];
-[CAMDescriptionOverlayView _descriptionTitleLabel];
-[CAMDescriptionOverlayView _detailButton];
-[CAMDescriptionOverlayView _determineIfDisplayZoomed:];
-[CAMDescriptionOverlayView _handleAcknowledgmentButtonTapped:];
-[CAMDescriptionOverlayView _handleDetailButtonTapped:];
-[CAMDescriptionOverlayView _infoFontSizeMultiplier];
-[CAMDescriptionOverlayView _infoLabel];
-[CAMDescriptionOverlayView _isDisplayZoomed];
-[CAMDescriptionOverlayView _layoutBlackoutMaskForFrame:inFrame:];
-[CAMDescriptionOverlayView _primaryVibrancyEffectView];
-[CAMDescriptionOverlayView _setDescriptionFontSizeMultiplier:];
-[CAMDescriptionOverlayView _setInfoFontSizeMultiplier:];
-[CAMDescriptionOverlayView _setIsDisplayZoomed:];
-[CAMDescriptionOverlayView _setTextViewFrame:];
-[CAMDescriptionOverlayView _updateFontsUsingNarrowWidth:];
-[CAMDescriptionOverlayView _updateTextUsingNarrowWidth:];
-[CAMDescriptionOverlayView additionalSpacing];
-[CAMDescriptionOverlayView adjustedContentWidthForWidth:containerSize:isLandscape:];
-[CAMDescriptionOverlayView attributedDescriptionTextUsingNarrowWidth:];
-[CAMDescriptionOverlayView contentBottomInset];
-[CAMDescriptionOverlayView contentLeadingOriginForWidth:containerSize:isLandscape:];
-[CAMDescriptionOverlayView contentTopFraction];
-[CAMDescriptionOverlayView detailButtonTapped];
-[CAMDescriptionOverlayView detailTextShouldHaveVibrancyEffect];
-[CAMDescriptionOverlayView handleDescriptionLabelTapped:];
-[CAMDescriptionOverlayView isAcknowledgmentButtonHighlighted];
-[CAMDescriptionOverlayView isBlackoutFrameVisible];
-[CAMDescriptionOverlayView isDetailButtonHighlighted];
-[CAMDescriptionOverlayView isTitleMultiline];
-[CAMDescriptionOverlayView setAcknowledgmentButtonHighlighted:];
-[CAMDescriptionOverlayView setBlackoutFrameVisible:];
-[CAMDescriptionOverlayView setContentBottomInset:];
-[CAMDescriptionOverlayView setCustomSubviewsVisible:];
-[CAMDescriptionOverlayView setDetailButtonHighlighted:];
-[CAMDescriptionOverlayView setMaxContentWidth:];
-[CAMDescriptionOverlayView setVisible:animationDuration:completion:];
-[CAMDescriptionOverlayView usesTopAlignedContentPlacement];
```
