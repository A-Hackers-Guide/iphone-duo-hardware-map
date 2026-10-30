# `UIVisualEffectView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `_UIAssertionControllerSubject`, `NSSecureCoding`
- 16 instance variables, 27 properties, 113 instance methods, 2 class methods

## Instance variables

```
@"UIView" _maskView;
@"UIImage" _maskImage;
@"_UIVisualEffectViewBackdropCaptureGroup" _captureGroup;
@"NSMutableArray" _captureDependents;
@"_UIVisualEffectHost" _backgroundHost;
@"_UIVisualEffectHost" _contentHost;
@"_UIVisualEffectEnvironment" _environment;
@"_UIAssertionController" _assertionController;
{?="backgroundHostNeedsUpdate"b1"contentHostNeedsUpdate"b1"allowsDithering"b1"allowsGroupFiltering"b1"useReducedTransparencyForContentHost"b1"isUpdatingSubviews"b1"hasBackdropBackgroundColorAlpha"b1"isContentStatic"b1"blurClippingMode"I} _effectViewFlags;
B _useLiveMasking;
@"UIVisualEffect" _effect;
@"UIVisualEffectView" _captureSource;
@"_UIVisualEffectViewCornerMask" __cornerMask;
@"NSArray" _backgroundEffects;
@"NSArray" _contentEffects;
q _blurQuality;
```

## Properties

```
@property (Td,N,S_setCornerRadius:) _cornerRadius;
@property (T@"_UIVisualEffectViewCornerMask",&,N,S_setCornerMask:,V__cornerMask) _cornerMask;
@property (TB,R,N) _applyCornerMaskToSelf;
@property (Td,N,S_setBackdropViewBackgroundColorAlpha:) _backdropViewBackgroundColorAlpha;
@property (T@"NSArray",C,N,V_backgroundEffects) backgroundEffects;
@property (T@"NSArray",C,N,V_contentEffects) contentEffects;
@property (TB,N,G_useLiveMasking,S_setUseLiveMasking:,V_useLiveMasking) useLiveMasking;
@property (TB,N,G_isContentViewStatic,S_setIsContentViewStatic:) _isContentViewStatic;
@property (TB,N,G_isNoiseEnabled,S_setNoiseEnabled:) _noiseEnabled;
@property (T@"NSString",C,N,S_setGroupName:) _groupName;
@property (T@"_UIVisualEffectBackdropView",W,N,S_setCaptureView:) _captureView;
@property (TB,N) allowsDithering;
@property (TB,N) allowsBlurring;
@property (Tq,N,V_blurQuality) blurQuality;
@property (T@"_UIVisualEffectViewBackdropCaptureGroup",R,N) _captureGroup;
@property (T@"NSArray",C,N,S_setCaptureDependents:) _captureDependents;
@property (T@"UIVisualEffectView",R,W,N,V_captureSource) _captureSource;
@property (Tq,N,S_setRenderMode:) _renderMode;
@property (T@"UIImage",&,N,S_setMaskImage:) _maskImage;
@property (TB,N,S_setAllowsGroupFiltering:) _allowsGroupFiltering;
@property (TB,N,G_useReducedTransparencyForContentEffects,S_setUseReducedTransparencyForContentEffects:) useReducedTransparencyForContentEffects;
@property (T@"UIView",R,N) contentView;
@property (T@"UIVisualEffect",C,N,V_effect) effect;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UIVisualEffectView supportsSecureCoding];
+[UIVisualEffectView _contentViewClass];
```

## Instance methods

```
-[UIVisualEffectView _commonInit];
-[UIVisualEffectView _traitCollectionForChildEnvironment:];
-[UIVisualEffectView assertionActivationStateForType:];
-[UIVisualEffectView _setCornerRadius:];
-[UIVisualEffectView setContentView:];
-[UIVisualEffectView didMoveToWindow];
-[UIVisualEffectView backgroundEffects];
-[UIVisualEffectView _generateDeferredAnimations:];
-[UIVisualEffectView _cornerRadius];
-[UIVisualEffectView blurQuality];
-[UIVisualEffectView setContentEffects:];
-[UIVisualEffectView dealloc];
-[UIVisualEffectView _updateEffectForAccessibilityChanges:];
-[UIVisualEffectView layoutSubviews];
-[UIVisualEffectView effect];
-[UIVisualEffectView setAllowsBlurring:];
-[UIVisualEffectView initWithEffect:];
-[UIVisualEffectView _continuousCornerRadius];
-[UIVisualEffectView _updateSubviews];
-[UIVisualEffectView contentEffects];
-[UIVisualEffectView _generateBackgroundEffects:contentEffects:];
-[UIVisualEffectView _ensureBackgroundHost];
-[UIVisualEffectView _setContinuousCornerRadius:];
-[UIVisualEffectView _addSubview:positioned:relativeTo:];
-[UIVisualEffectView _applyCornerMaskToSelf];
-[UIVisualEffectView encodeWithCoder:];
-[UIVisualEffectView setBackgroundEffects:];
-[UIVisualEffectView _configureEffects];
-[UIVisualEffectView _unregisterNotifications];
-[UIVisualEffectView contentView];
-[UIVisualEffectView _applyCornerRadiusToSubviews];
-[UIVisualEffectView setEffect:];
-[UIVisualEffectView _updateEnvironmentAndFlagUpdatesIfNecessary:];
-[UIVisualEffectView description];
-[UIVisualEffectView assertionActivationStateChangedToState:forType:];
-[UIVisualEffectView initWithCoder:];
-[UIVisualEffectView traitCollectionDidChange:];
-[UIVisualEffectView allowsDithering];
-[UIVisualEffectView _populateArchivedSubviews:];
-[UIVisualEffectView setBlurQuality:];
-[UIVisualEffectView _effectDescriptorForEffects:usage:];
-[UIVisualEffectView setAllowsDithering:];
-[UIVisualEffectView _registerNotifications];
-[UIVisualEffectView didMoveToSuperview];
-[UIVisualEffectView _initialValueForKey:];
-[UIVisualEffectView initWithFrame:];
-[UIVisualEffectView allowsBlurring];
-[UIVisualEffectView _backgroundHost];
-[UIVisualEffectView _setCornerMask:];
-[UIVisualEffectView _isNoiseEnabled];
-[UIVisualEffectView _setRenderMode:];
-[UIVisualEffectView _updateEffectForSnapshotDidEnd:];
-[UIVisualEffectView _useLiveMasking];
-[UIVisualEffectView __isLandmarkView];
-[UIVisualEffectView __markerLayerColorForSubclass:otherModule:];
-[UIVisualEffectView __shouldShowVisualizationForSubclass:isOtherModule:];
-[UIVisualEffectView __titleForBackgroundBlurEffect];
-[UIVisualEffectView __titleForBlurEffect:];
-[UIVisualEffectView __titleForContentBlurEffect];
-[UIVisualEffectView __titleForMainBlurEffect];
-[UIVisualEffectView __vis_layoutSubviews];
-[UIVisualEffectView _addCaptureDependent:];
-[UIVisualEffectView _allowsGroupFiltering];
-[UIVisualEffectView _backdropViewBackgroundColorAlpha];
-[UIVisualEffectView _captureDependents];
-[UIVisualEffectView _captureGroup];
-[UIVisualEffectView _captureSource];
-[UIVisualEffectView _captureView];
-[UIVisualEffectView _colorViewBoundsOverlayCreateIfNecessary:];
-[UIVisualEffectView _contentHost];
-[UIVisualEffectView _cornerCurve];
-[UIVisualEffectView _cornerMask];
-[UIVisualEffectView _debug];
-[UIVisualEffectView _didUpdateContentView];
-[UIVisualEffectView _ensureContentHostWithView:];
-[UIVisualEffectView _environment];
-[UIVisualEffectView _generateEffectAnimations:];
-[UIVisualEffectView _groupName];
-[UIVisualEffectView _interceptGlassEffect:];
-[UIVisualEffectView _isContentViewStatic];
-[UIVisualEffectView _maskImage];
-[UIVisualEffectView _maskImageForMaskView:];
-[UIVisualEffectView _maskView];
-[UIVisualEffectView _obtainDynamicContentAssertionForReason:];
-[UIVisualEffectView _removeCaptureDependent:];
-[UIVisualEffectView _renderMode];
-[UIVisualEffectView _resetEffect];
-[UIVisualEffectView _setAllowsGroupFiltering:];
-[UIVisualEffectView _setBackdropViewBackgroundColorAlpha:];
-[UIVisualEffectView _setCaptureDependents:];
-[UIVisualEffectView _setCaptureView:];
-[UIVisualEffectView _setCornerRadius:continuous:maskedCorners:];
-[UIVisualEffectView _setEffect:];
-[UIVisualEffectView _setGroupName:];
-[UIVisualEffectView _setIsContentViewStatic:];
-[UIVisualEffectView _setMaskImage:];
-[UIVisualEffectView _setMaskView:];
-[UIVisualEffectView _setNoiseEnabled:];
-[UIVisualEffectView _setTintOpacity:];
-[UIVisualEffectView _setUseLiveMasking:];
-[UIVisualEffectView _setUseReducedTransparencyForContentEffects:];
-[UIVisualEffectView _updateCaptureDependents];
-[UIVisualEffectView _updateCornerTraits];
-[UIVisualEffectView _updateEffectBackgroundColor];
-[UIVisualEffectView _updateEffectForAlphaTransitionDidEnd:];
-[UIVisualEffectView _updateEffectForAlphaTransitionWillBegin:];
-[UIVisualEffectView _updateEffectForReducedTransparency];
-[UIVisualEffectView _updateEffectForSnapshotWillBegin:];
-[UIVisualEffectView _updateEffectsFromLegacyEffect];
-[UIVisualEffectView _updateSubView:frame:];
-[UIVisualEffectView _useReducedTransparencyForContentEffects];
-[UIVisualEffectView _whatsWrongWithThisEffect];
-[UIVisualEffectView respondToSettingsUpdate];
```
