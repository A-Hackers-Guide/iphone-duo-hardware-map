# `UIActivityIndicatorView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `_UIVisualStyleStylable`, `UIActivityIndicatorProvider`, `NSCoding`
- 26 instance variables, 26 properties, 108 instance methods, 4 class methods

## Instance variables

```
B _wasAnimatingWhenAnimationsRemoved;
@"_UIActivityIndicatorViewStyleView" _styleView;
Q _preferredBehavioralStyle;
B _animating;
B _hidesWhenStopped;
B _restartAnimationOnNextLayout;
B _disableUpdateColorOnTraitCollectionChange;
B _hasShadow;
B _spinning;
q _activityIndicatorViewStyle;
d _duration;
d _customWidth;
@"UIColor" _color;
@"UIImageView" _animatingImageView;
@"_UIActivityIndicatorMessageLabel" _messageLabel;
@"NSString" _message;
q _actualActivityIndicatorViewStyle;
@"NSArray" _spokeImages;
@"NSArray" _spokeHighlightImages;
q _spokeCount;
q _spokeFrameRatio;
@"_UIActivityIndicatorViewArtworkCacheKey" _lastArtCacheKey;
@"_UIActivityIndicatorViewArtworkCacheKey" _lastHighlightArtCacheKey;
@"UIColor" _shadowColor;
d _width;
{CGSize="width"d"height"d} _shadowOffset;
```

## Properties

```
@property (TQ,R,N) behavioralStyle;
@property (TQ,N) preferredBehavioralStyle;
@property (T@"UIImageView",R,N,G_animatingImageView,V_animatingImageView) animatingImageView;
@property (T@"_UIActivityIndicatorMessageLabel",R,N,G_messageLabel,V_messageLabel) messageLabel;
@property (T@"NSString",&,N,G_message,S_setMessage:,V_message) message;
@property (Td,N,V_duration) animationDuration;
@property (TB,N,GisAnimating,V_animating) animating;
@property (Tq,R,N,G_actualActivityIndicatorViewStyle,V_actualActivityIndicatorViewStyle) actualActivityIndicatorViewStyle;
@property (TB,R,N,G_restartAnimationOnNextLayout,V_restartAnimationOnNextLayout) restartAnimationOnNextLayout;
@property (T@"NSArray",R,N,G_spokeImages,V_spokeImages) spokeImages;
@property (T@"NSArray",R,N,G_spokeHighlightImages,V_spokeHighlightImages) spokeHighlightImages;
@property (Tq,R,N,G_spokeCount,V_spokeCount) spokeCount;
@property (Tq,R,N,G_spokeFrameRatio,V_spokeFrameRatio) spokeFrameRatio;
@property (TB,R,N,G_disableUpdateColorOnTraitCollectionChange,V_disableUpdateColorOnTraitCollectionChange) disableUpdateColorOnTraitCollectionChange;
@property (T@"_UIActivityIndicatorViewArtworkCacheKey",R,N,G_lastArtCacheKey,V_lastArtCacheKey) lastArtCacheKey;
@property (T@"_UIActivityIndicatorViewArtworkCacheKey",R,N,G_lastHighlightArtCacheKey,V_lastHighlightArtCacheKey) lastHighlightArtCacheKey;
@property (Td,N,S_setCustomWidth:,V_customWidth) _customWidth;
@property (T{CGSize=dd},N,V_shadowOffset) shadowOffset;
@property (T@"UIColor",&,N,V_shadowColor) shadowColor;
@property (Td,N,V_width) width;
@property (TB,N,V_hasShadow) hasShadow;
@property (TB,V_spinning) spinning;
@property (Tq,N,V_activityIndicatorViewStyle) activityIndicatorViewStyle;
@property (TB,N,V_hidesWhenStopped) hidesWhenStopped;
@property (T@"UIColor",&,N,V_color) color;
@property (TB,D,N,GisHidden) hidden;
```

## Class methods

```
+[UIActivityIndicatorView defaultSizeForStyle:];
+[UIActivityIndicatorView _imageSetNameForArtworkBasedStyle:outImageCount:];
+[UIActivityIndicatorView visualStyleRegistryIdentity];
+[UIActivityIndicatorView _loadResourcesForArtworkBasedStyle:];
```

## Instance methods

```
-[UIActivityIndicatorView _setMessage:];
-[UIActivityIndicatorView _commonInit];
-[UIActivityIndicatorView hasShadow];
-[UIActivityIndicatorView _applicationWillEnterForeground:];
-[UIActivityIndicatorView _applicationDidEnterBackground:];
-[UIActivityIndicatorView stopAnimating];
-[UIActivityIndicatorView startAnimating];
-[UIActivityIndicatorView _message];
-[UIActivityIndicatorView startAnimation];
-[UIActivityIndicatorView setColor:];
-[UIActivityIndicatorView setAnimationDuration:];
-[UIActivityIndicatorView _intrinsicContentSizeInvalidatedForChildView:];
-[UIActivityIndicatorView setSpinning:];
-[UIActivityIndicatorView _refreshStyle];
-[UIActivityIndicatorView animationDuration];
-[UIActivityIndicatorView setShadowOffset:];
-[UIActivityIndicatorView _intrinsicSizeWithinSize:];
-[UIActivityIndicatorView isHighlighted];
-[UIActivityIndicatorView dealloc];
-[UIActivityIndicatorView layoutSubviews];
-[UIActivityIndicatorView _didMoveFromWindow:toWindow:];
-[UIActivityIndicatorView setBounds:];
-[UIActivityIndicatorView shadowColor];
-[UIActivityIndicatorView setStyle:];
-[UIActivityIndicatorView color];
-[UIActivityIndicatorView sizeThatFits:];
-[UIActivityIndicatorView _contentHuggingDefault_isUsuallyFixedHeight];
-[UIActivityIndicatorView tintColorDidChange];
-[UIActivityIndicatorView setHighlighted:];
-[UIActivityIndicatorView _setUpAnimation];
-[UIActivityIndicatorView _removeAllAnimations:];
-[UIActivityIndicatorView encodeWithCoder:];
-[UIActivityIndicatorView setFrame:];
-[UIActivityIndicatorView isElementAccessibilityExposedToInterfaceBuilder];
-[UIActivityIndicatorView initWithCoder:];
-[UIActivityIndicatorView traitCollectionDidChange:];
-[UIActivityIndicatorView _populateArchivedSubviews:];
-[UIActivityIndicatorView setShadowColor:];
-[UIActivityIndicatorView _supportsMacIdiom];
-[UIActivityIndicatorView setWidth:];
-[UIActivityIndicatorView width];
-[UIActivityIndicatorView isAnimating];
-[UIActivityIndicatorView setAnimating:];
-[UIActivityIndicatorView initWithFrame:];
-[UIActivityIndicatorView shadowOffset];
-[UIActivityIndicatorView setHasShadow:];
-[UIActivityIndicatorView _contentHuggingDefault_isUsuallyFixedWidth];
-[UIActivityIndicatorView _updateSubviewFramesWithBounds:];
-[UIActivityIndicatorView behavioralStyle];
-[UIActivityIndicatorView initWithActivityIndicatorStyle:];
-[UIActivityIndicatorView _actualActivityIndicatorViewStyle];
-[UIActivityIndicatorView _actualStyleByResolvingAutoUpdatingStyle:];
-[UIActivityIndicatorView _alphaValueForStep:];
-[UIActivityIndicatorView _animatingImageView];
-[UIActivityIndicatorView _animatingImageViewFrameForBounds:];
-[UIActivityIndicatorView _artCacheKeyWithStyle:color:];
-[UIActivityIndicatorView _colorRequiresDynamicTinting];
-[UIActivityIndicatorView _customStyleForStyle:];
-[UIActivityIndicatorView _customWidth];
-[UIActivityIndicatorView _defaultColorForStyle:];
-[UIActivityIndicatorView _defaultSizeConsultingCustomWidthIfApplicable];
-[UIActivityIndicatorView _defaultStyle];
-[UIActivityIndicatorView _disableUpdateColorOnTraitCollectionChange];
-[UIActivityIndicatorView _effectiveCustomWidth];
-[UIActivityIndicatorView _externalStyleForStyle:];
-[UIActivityIndicatorView _generateImagesForColor:highlight:];
-[UIActivityIndicatorView _generateModernImagesForImages:color:];
-[UIActivityIndicatorView _hasClientSetColor];
-[UIActivityIndicatorView _hasShadow];
-[UIActivityIndicatorView _highlightColorForStyle:];
-[UIActivityIndicatorView _imageForStep:withColor:];
-[UIActivityIndicatorView _imagesForStyle:color:highlight:];
-[UIActivityIndicatorView _indexOfFirstImageForStartingAnimation];
-[UIActivityIndicatorView _internalStyleForStyle:];
-[UIActivityIndicatorView _isArtworkBasedStyle];
-[UIActivityIndicatorView _isShowingMessage];
-[UIActivityIndicatorView _isStatusBarStyle];
-[UIActivityIndicatorView _lastArtCacheKey];
-[UIActivityIndicatorView _lastHighlightArtCacheKey];
-[UIActivityIndicatorView _messageLabel];
-[UIActivityIndicatorView _messageLabelFrameForBounds:];
-[UIActivityIndicatorView _restartAnimationOnNextLayout];
-[UIActivityIndicatorView _restoreRemovedAnimationsIncludingSubviews];
-[UIActivityIndicatorView _setCustomWidth:];
-[UIActivityIndicatorView _shouldGoBackToBaseStyle];
-[UIActivityIndicatorView _shouldGoToCustomStyle];
-[UIActivityIndicatorView _sizeForStyle:];
-[UIActivityIndicatorView _spokeCount];
-[UIActivityIndicatorView _spokeFrameRatio];
-[UIActivityIndicatorView _spokeHighlightImages];
-[UIActivityIndicatorView _spokeImages];
-[UIActivityIndicatorView _spokeLengthForGearWidth:];
-[UIActivityIndicatorView _spokeWidthForGearWidth:];
-[UIActivityIndicatorView _tearDownAnimation];
-[UIActivityIndicatorView _updateLayoutInfo];
-[UIActivityIndicatorView _updateMessageForStyle:];
-[UIActivityIndicatorView _updateVisualStyleProperties];
-[UIActivityIndicatorView _useCustomStyleForLegacyStyles];
-[UIActivityIndicatorView _wantsAnimationRestoration];
-[UIActivityIndicatorView _widthForGearWidth:];
-[UIActivityIndicatorView activityIndicatorViewStyle];
-[UIActivityIndicatorView hidesWhenStopped];
-[UIActivityIndicatorView preferredBehavioralStyle];
-[UIActivityIndicatorView setActivityIndicatorViewStyle:];
-[UIActivityIndicatorView setHidesWhenStopped:];
-[UIActivityIndicatorView setPreferredBehavioralStyle:];
-[UIActivityIndicatorView spinning];
-[UIActivityIndicatorView stopAnimation];
```
