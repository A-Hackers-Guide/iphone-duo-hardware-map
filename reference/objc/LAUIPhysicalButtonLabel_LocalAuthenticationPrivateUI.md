# `LAUIPhysicalButtonLabel`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationPrivateUI.framework/LocalAuthenticationPrivateUI`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationPrivateUI.framework__LocalAuthenticationPrivateUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 10 instance variables, 11 properties, 44 instance methods, 0 class methods

## Instance variables

```
@"UITextView" _textView;
@"CALayer" _backdropContainer;
@"CALayer" _backdropSourceLayer;
{vector<CGRect, std::allocator<CGRect>>="__begin_"^{CGRect}"__end_"^{CGRect}""{?="__cap_"^{CGRect}}} _lastBackdropLineRects;
@"UIColor" _backdropColor;
@"UIFont" _configuredFont;
B _showsBackdrop;
B _adjustsFontSizeToFitWidth;
d _minimumScaleFactor;
{?="boundsSize"{CGSize="width"d"height"d}"chosenSize"d"valid"B} _shrinkFitCache;
```

## Properties

```
@property (T@"NSString",C,N) text;
@property (T@"UIFont",&,N) font;
@property (T@"UIColor",&,N) textColor;
@property (Tq,N) textAlignment;
@property (Tq,N) numberOfLines;
@property (Tq,N) lineBreakMode;
@property (TB,N) adjustsFontSizeToFitWidth;
@property (Td,N) minimumScaleFactor;
@property (TB,R,N,V_showsBackdrop) showsBackdrop;
@property (T@"UIColor",&,N) backdropColor;
@property (T@"CALayer",R,N) textLayer;
```

## Instance methods

```
-[LAUIPhysicalButtonLabel setTextAlignment:];
-[LAUIPhysicalButtonLabel intrinsicContentSize];
-[LAUIPhysicalButtonLabel textAlignment];
-[LAUIPhysicalButtonLabel text];
-[LAUIPhysicalButtonLabel textColor];
-[LAUIPhysicalButtonLabel accessibilityTraits];
-[LAUIPhysicalButtonLabel numberOfLines];
-[LAUIPhysicalButtonLabel setTextColor:];
-[LAUIPhysicalButtonLabel setAdjustsFontSizeToFitWidth:];
-[LAUIPhysicalButtonLabel layoutSubviews];
-[LAUIPhysicalButtonLabel sizeThatFits:];
-[LAUIPhysicalButtonLabel _blurFilterWithRadius:];
-[LAUIPhysicalButtonLabel minimumScaleFactor];
-[LAUIPhysicalButtonLabel adjustsFontSizeToFitWidth];
-[LAUIPhysicalButtonLabel accessibilityLabel];
-[LAUIPhysicalButtonLabel setNumberOfLines:];
-[LAUIPhysicalButtonLabel isAccessibilityElement];
-[LAUIPhysicalButtonLabel setText:];
-[LAUIPhysicalButtonLabel font];
-[LAUIPhysicalButtonLabel setMinimumScaleFactor:];
-[LAUIPhysicalButtonLabel initWithFrame:];
-[LAUIPhysicalButtonLabel setLineBreakMode:];
-[LAUIPhysicalButtonLabel lineBreakMode];
-[LAUIPhysicalButtonLabel setFont:];
-[LAUIPhysicalButtonLabel backdropColor];
-[LAUIPhysicalButtonLabel _buildBackdropContainerIfNeeded];
-[LAUIPhysicalButtonLabel _animateBackdropOpacity:animated:];
-[LAUIPhysicalButtonLabel _applyShrinkFitForBounds:];
-[LAUIPhysicalButtonLabel _applyShrinkFitFromCacheForBounds:];
-[LAUIPhysicalButtonLabel _invalidateShrinkFitCache];
-[LAUIPhysicalButtonLabel _lineBoundingRectsForCurrentTextView];
-[LAUIPhysicalButtonLabel _reapplyBackdropPillAppearance];
-[LAUIPhysicalButtonLabel _refreshBackdropIfNeeded];
-[LAUIPhysicalButtonLabel _springLayer:toBounds:];
-[LAUIPhysicalButtonLabel _springLayer:toCornerRadius:];
-[LAUIPhysicalButtonLabel _springLayer:toOpacity:];
-[LAUIPhysicalButtonLabel _springLayer:toPosition:];
-[LAUIPhysicalButtonLabel _storeShrinkFitCacheForBounds:chosenSize:];
-[LAUIPhysicalButtonLabel _textFitsInBounds:];
-[LAUIPhysicalButtonLabel _updateBackdropLayersWithLineRects:];
-[LAUIPhysicalButtonLabel setBackdropColor:];
-[LAUIPhysicalButtonLabel setShowsBackdrop:animated:];
-[LAUIPhysicalButtonLabel showsBackdrop];
-[LAUIPhysicalButtonLabel textLayer];
```
