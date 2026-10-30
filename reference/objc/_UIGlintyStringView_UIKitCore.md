# `_UIGlintyStringView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 36 instance variables, 37 properties, 113 instance methods, 0 class methods

## Instance variables

```
B _animationRepeats;
B _adjustsFontSizeToFitWidth;
B _hasCustomBackgroundColor;
B _highlight;
B _allowsLuminanceAdjustments;
B _usesBackgroundDimming;
B _needsTextUpdate;
B _animating;
B _fading;
B _showing;
i _textIndex;
@"<_UIGlintyStringViewDelegate>" _delegate;
@"NSString" _text;
@"UIFont" _font;
@"NSString" _textLanguage;
@"_UILegibilitySettings" _legibilitySettings;
@"_UIVibrantSettings" _vibrantSettings;
@"UIView" _backgroundView;
@"UIColor" _backgroundColor;
@"UIColor" _chevronBackgroundColor;
@"UIColor" _textColor;
@"UIColor" _shimmerColor;
q _chevronStyle;
d _horizontalPadding;
@"UILabel" _label;
@"UIView" _spotlightView;
@"UIImage" _chevron;
@"UIView" _highlightView;
@"UIView" _effectView;
@"UIView" _blurView;
@"UIView" _shimmerImageView;
@"UIView" _reflectionImageView;
d _blurAlpha;
@"NSMutableSet" _blurHiddenRequesters;
{CGSize="width"d"height"d} _labelSize;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _chevronFrame;
```

## Properties

```
@property (TB,N,V_needsTextUpdate) needsTextUpdate;
@property (T@"UILabel",&,N,V_label) label;
@property (T{CGSize=dd},N,V_labelSize) labelSize;
@property (T@"UIView",&,N,V_spotlightView) spotlightView;
@property (Ti,N,V_textIndex) textIndex;
@property (T@"UIImage",&,N,V_chevron) chevron;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_chevronFrame) chevronFrame;
@property (T@"UIView",&,N,V_highlightView) highlightView;
@property (TB,N,V_animating) animating;
@property (TB,N,V_fading) fading;
@property (TB,N,V_showing) showing;
@property (T@"UIView",&,N,V_effectView) effectView;
@property (T@"UIView",&,N,V_blurView) blurView;
@property (T@"UIView",&,N,V_shimmerImageView) shimmerImageView;
@property (T@"UIView",&,N,V_reflectionImageView) reflectionImageView;
@property (Td,N,V_blurAlpha) blurAlpha;
@property (T@"NSMutableSet",&,N,V_blurHiddenRequesters) blurHiddenRequesters;
@property (T@"<_UIGlintyStringViewDelegate>",N,V_delegate) delegate;
@property (T@"NSString",C,N,V_text) text;
@property (T@"UIFont",&,N,V_font) font;
@property (T@"NSString",C,N,V_textLanguage) textLanguage;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) labelFrame;
@property (T@"_UILegibilitySettings",&,N,V_legibilitySettings) legibilitySettings;
@property (T@"_UIVibrantSettings",&,N,V_vibrantSettings) vibrantSettings;
@property (T@"UIView",&,N,V_backgroundView) backgroundView;
@property (T@"UIColor",&,N,V_backgroundColor) backgroundColor;
@property (T@"UIColor",&,N,V_chevronBackgroundColor) chevronBackgroundColor;
@property (T@"UIColor",&,N,V_textColor) textColor;
@property (T@"UIColor",&,N,V_shimmerColor) shimmerColor;
@property (TB,N,V_animationRepeats) animationRepeats;
@property (TB,N,V_adjustsFontSizeToFitWidth) adjustsFontSizeToFitWidth;
@property (TB,N,V_hasCustomBackgroundColor) hasCustomBackgroundColor;
@property (Tq,N,V_chevronStyle) chevronStyle;
@property (Td,N,V_horizontalPadding) horizontalPadding;
@property (TB,N,V_highlight) highlight;
@property (TB,N,V_allowsLuminanceAdjustments) allowsLuminanceAdjustments;
@property (TB,N,V_usesBackgroundDimming) usesBackgroundDimming;
```

## Instance methods

```
-[_UIGlintyStringView blurView];
-[_UIGlintyStringView labelSize];
-[_UIGlintyStringView setBlurView:];
-[_UIGlintyStringView stopAnimating];
-[_UIGlintyStringView startAnimating];
-[_UIGlintyStringView hide];
-[_UIGlintyStringView spotlightView];
-[_UIGlintyStringView allowsLuminanceAdjustments];
-[_UIGlintyStringView animating];
-[_UIGlintyStringView didMoveToWindow];
-[_UIGlintyStringView _chevronVerticalOffset];
-[_UIGlintyStringView _highlightCompositingFilter];
-[_UIGlintyStringView setHighlightView:];
-[_UIGlintyStringView fading];
-[_UIGlintyStringView setAllowsLuminanceAdjustments:];
-[_UIGlintyStringView _chevronImageForStyle:];
-[_UIGlintyStringView setChevronStyle:];
-[_UIGlintyStringView text];
-[_UIGlintyStringView updateTextWithBounds:];
-[_UIGlintyStringView _chevronPadding];
-[_UIGlintyStringView horizontalPadding];
-[_UIGlintyStringView setChevronFrame:];
-[_UIGlintyStringView chevron];
-[_UIGlintyStringView textColor];
-[_UIGlintyStringView _chevronWidthWithPaddingCompression:];
-[_UIGlintyStringView label];
-[_UIGlintyStringView setShimmerColor:];
-[_UIGlintyStringView _updateHighlight];
-[_UIGlintyStringView setLabel:];
-[_UIGlintyStringView textLanguage];
-[_UIGlintyStringView setUsesBackgroundDimming:];
-[_UIGlintyStringView setEffectView:];
-[_UIGlintyStringView setHorizontalPadding:];
-[_UIGlintyStringView dealloc];
-[_UIGlintyStringView showEffects];
-[_UIGlintyStringView setTextColor:];
-[_UIGlintyStringView shimmerColor];
-[_UIGlintyStringView blurAlpha];
-[_UIGlintyStringView needsTextUpdate];
-[_UIGlintyStringView setAdjustsFontSizeToFitWidth:];
-[_UIGlintyStringView layoutSubviews];
-[_UIGlintyStringView hideBlur];
-[_UIGlintyStringView fadeIn];
-[_UIGlintyStringView setBlurHiddenRequesters:];
-[_UIGlintyStringView setSpotlightView:];
-[_UIGlintyStringView usesBackgroundDimming];
-[_UIGlintyStringView setBackgroundColor:];
-[_UIGlintyStringView setChevronBackgroundColor:];
-[_UIGlintyStringView _updateLabelWithFrame:];
-[_UIGlintyStringView addShimmerAnimationToLayer:];
-[_UIGlintyStringView sizeThatFits:];
-[_UIGlintyStringView setDelegate:];
-[_UIGlintyStringView setFading:];
-[_UIGlintyStringView setShimmerImageView:];
-[_UIGlintyStringView setBlurAlpha:];
-[_UIGlintyStringView effectView];
-[_UIGlintyStringView setShowing:];
-[_UIGlintyStringView fadeOut];
-[_UIGlintyStringView setHighlight:];
-[_UIGlintyStringView showBlur];
-[_UIGlintyStringView setTextLanguage:];
-[_UIGlintyStringView _highlightColor];
-[_UIGlintyStringView setBlurHidden:forRequester:];
-[_UIGlintyStringView adjustsFontSizeToFitWidth];
-[_UIGlintyStringView _labelSizeThatFits:];
-[_UIGlintyStringView textIndex];
-[_UIGlintyStringView vibrantSettings];
-[_UIGlintyStringView reflectionImageView];
-[_UIGlintyStringView addGlintyAnimations];
-[_UIGlintyStringView setHasCustomBackgroundColor:];
-[_UIGlintyStringView animationRepeats];
-[_UIGlintyStringView updateText];
-[_UIGlintyStringView removeGlintyAnimations];
-[_UIGlintyStringView delegate];
-[_UIGlintyStringView _chevronWidthWithPadding];
-[_UIGlintyStringView show];
-[_UIGlintyStringView backgroundColor];
-[_UIGlintyStringView backgroundView];
-[_UIGlintyStringView setReflectionImageView:];
-[_UIGlintyStringView updateBlurForHiddenRequesters];
-[_UIGlintyStringView shapeViewForCharactersInString:withFont:centeredInFrame:];
-[_UIGlintyStringView legibilitySettings];
-[_UIGlintyStringView setChevron:];
-[_UIGlintyStringView setAnimationRepeats:];
-[_UIGlintyStringView fadeInWithDuration:];
-[_UIGlintyStringView setText:];
-[_UIGlintyStringView blurHiddenRequesters];
-[_UIGlintyStringView hideEffects];
-[_UIGlintyStringView showing];
-[_UIGlintyStringView setNeedsTextUpdate:];
-[_UIGlintyStringView chevronBackgroundColor];
-[_UIGlintyStringView setLabelSize:];
-[_UIGlintyStringView font];
-[_UIGlintyStringView chevronFrame];
-[_UIGlintyStringView _chevronHeightWithMaxOffset];
-[_UIGlintyStringView highlight];
-[_UIGlintyStringView chevronStyle];
-[_UIGlintyStringView hasCustomBackgroundColor];
-[_UIGlintyStringView setLegibilitySettings:];
-[_UIGlintyStringView initWithText:andFont:];
-[_UIGlintyStringView isAnimating];
-[_UIGlintyStringView setAnimating:];
-[_UIGlintyStringView baselineOffsetFromBottomWithSize:];
-[_UIGlintyStringView labelFrame];
-[_UIGlintyStringView setVibrantSettings:];
-[_UIGlintyStringView addReflectionAnimationToLayer:];
-[_UIGlintyStringView setBackgroundView:];
-[_UIGlintyStringView highlightView];
-[_UIGlintyStringView shimmerImageView];
-[_UIGlintyStringView setTextIndex:];
-[_UIGlintyStringView fadeOutWithDuration:];
-[_UIGlintyStringView baselineOffsetFromBottom];
-[_UIGlintyStringView setFont:];
```
