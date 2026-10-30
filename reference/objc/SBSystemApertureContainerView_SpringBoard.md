# `SBSystemApertureContainerView`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `_UILumaTrackingBackdropViewDelegate`, `PTSettingsKeyObserver`, `SBSAInterfaceElementIdentifying`, `SBSystemApertureElementViewControllingContaining`, `SBSystemApertureGainMapBackedRendering`
- 36 instance variables, 27 properties, 70 instance methods, 0 class methods

## Instance variables

```
@"SBSystemApertureSettings" _settings;
@"UIView" _contentClippingView;
@"_UILumaTrackingBackdropView" _backgroundLumaSamplingBackdrop;
@"UIView" _darkBkgKeyLineView;
@"_SBAdaptiveKeyLineBackdropView" _lightBkgKeyLineView;
@"UIView" _shadowView;
@"UIView" _blobEnablingBlackFillView;
@"_SBSystemApertureGainMapView" _gainMapView;
@"UIView" _backgroundGroupingView;
@"UIView" _subBackgroundGroupingView;
@"UIView" _elevatedSubBackgroundGroupingView;
@"_SBSystemApertureGainMapView" _elevatedGainMapView;
@"UIView" _hitTestView;
{?="rect"{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}}"cornerRadius"d"roundedCorners"Q} _hitRegion;
@"UIView" _scalingContentView;
@"UIView" _rotatingContentView;
@"_SBSystemApertureContentBorderView" _contentBorderView;
d _contentBorderWidth;
q _keyLineMode;
q _shadowStyle;
q _renderingBackgroundLuminanceLevel;
@"UIColor" _keyLineTintColor;
@"UIColor" _cachedValidatedKeyLineTintColor;
@"NSMutableDictionary" _transitionIDsToReasons;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _gainMapLayerInsets;
Q _rank;
@"NSHashTable" _geometryObservers;
q _elevationStyle;
B _needsShadowStyleUpdate;
d _blurRadius;
@"UIView" _matchMoveSourceView;
@"NSUUID" _interfaceElementIdentifier;
@"UIViewController<SAUIElementViewControlling>" _elementViewController;
@"UIViewController<SAUIElementViewControlling>" _outgoingElementViewController;
@"<SBSystemApertureContainerViewDelegate>" _delegate;
q _sampledBackgroundLuminanceLevel;
```

## Properties

```
@property (T@"UIView",R,N) scalingContentView;
@property (T@"UIView",R,N) rotatingContentView;
@property (T@"UIView",R,N) backgroundGroupingView;
@property (T@"UIView",R,N) subBackgroundGroupingView;
@property (T@"UIView",R,N) elevatedSubBackgroundGroupingView;
@property (TQ,N) rank;
@property (T@"<SBSystemApertureContainerViewDelegate>",W,N,V_delegate) delegate;
@property (TB,N,GisContentClippingEnabled) contentClippingEnabled;
@property (TB,N,GisHitTestingEnabled) hitTestingEnabled;
@property (T@"SBSAContainerViewDescription",R,C,N) containerViewDescription;
@property (Td,N,V_blurRadius) blurRadius;
@property (Tq,N) shadowStyle;
@property (Tq,N) elevationStyle;
@property (T@"UIView",W,N,V_matchMoveSourceView) matchMoveSourceView;
@property (Tq,N) keyLineMode;
@property (T@"UIColor",C,N) keyLineTintColor;
@property (Tq,R,N,V_sampledBackgroundLuminanceLevel) sampledBackgroundLuminanceLevel;
@property (Td,N) contentBorderWidth;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSUUID",R,C,N,V_interfaceElementIdentifier) interfaceElementIdentifier;
@property (T@"UIViewController<SAUIElementViewControlling>",W,N,V_elementViewController) elementViewController;
@property (T@"UIViewController<SAUIElementViewControlling>",R,W,N,V_outgoingElementViewController) outgoingElementViewController;
@property (T{SBSystemApertureContainerRenderingConfiguration=qqB},N) renderingConfiguration;
@property (Td,N) resolutionTransitionStrength;
```

## Instance methods

```
-[SBSystemApertureContainerView setNeedsLayout];
-[SBSystemApertureContainerView shadowStyle];
-[SBSystemApertureContainerView contentBorderWidth];
-[SBSystemApertureContainerView setShadowStyle:];
-[SBSystemApertureContainerView resolutionTransitionStrength];
-[SBSystemApertureContainerView setContentBorderWidth:];
-[SBSystemApertureContainerView _setCornerRadius:];
-[SBSystemApertureContainerView keyLineTintColor];
-[SBSystemApertureContainerView rank];
-[SBSystemApertureContainerView isContentClippingEnabled];
-[SBSystemApertureContainerView backgroundLumaView:didTransitionToLevel:];
-[SBSystemApertureContainerView willMoveToSuperview:];
-[SBSystemApertureContainerView sampledBackgroundLuminanceLevel];
-[SBSystemApertureContainerView keyLineMode];
-[SBSystemApertureContainerView setRenderingConfiguration:];
-[SBSystemApertureContainerView setCenter:];
-[SBSystemApertureContainerView layoutSubviews];
-[SBSystemApertureContainerView setTransform:];
-[SBSystemApertureContainerView elevationStyle];
-[SBSystemApertureContainerView setBounds:];
-[SBSystemApertureContainerView settings:changedValueForKey:];
-[SBSystemApertureContainerView setResolutionTransitionStrength:];
-[SBSystemApertureContainerView setDelegate:];
-[SBSystemApertureContainerView setAlpha:];
-[SBSystemApertureContainerView setKeyLineTintColor:];
-[SBSystemApertureContainerView blurRadius];
-[SBSystemApertureContainerView _setContinuousCornerRadius:];
-[SBSystemApertureContainerView setRank:];
-[SBSystemApertureContainerView delegate];
-[SBSystemApertureContainerView renderingConfiguration];
-[SBSystemApertureContainerView setFrame:];
-[SBSystemApertureContainerView interfaceElementIdentifier];
-[SBSystemApertureContainerView setElevationStyle:];
-[SBSystemApertureContainerView setElementViewController:];
-[SBSystemApertureContainerView alpha];
-[SBSystemApertureContainerView setBlurRadius:];
-[SBSystemApertureContainerView elementViewController];
-[SBSystemApertureContainerView pointInside:withEvent:];
-[SBSystemApertureContainerView setKeyLineMode:];
-[SBSystemApertureContainerView setContentClippingEnabled:];
-[SBSystemApertureContainerView _applySettingsValues];
-[SBSystemApertureContainerView _generateAccessibilityIdentifier];
-[SBSystemApertureContainerView _invertColorsChanged:];
-[SBSystemApertureContainerView _layoutHitTestViewWithBounds:];
-[SBSystemApertureContainerView _notifyGeometryObserversBoundsDidChange:];
-[SBSystemApertureContainerView _notifyGeometryObserversCenterDidChange:];
-[SBSystemApertureContainerView _notifyGeometryObserversFrameDidChange:];
-[SBSystemApertureContainerView _notifyGeometryObserversResolutionTransitionStrengthDidChange:];
-[SBSystemApertureContainerView _setupLayerFilters];
-[SBSystemApertureContainerView _updateContentBorderAppearance];
-[SBSystemApertureContainerView _updateElevatedGainMapRenderingConfiguration];
-[SBSystemApertureContainerView _updateKeyLineFilters];
-[SBSystemApertureContainerView _updateShadowStyleIfNeeded];
-[SBSystemApertureContainerView _validatedKeyLineTintColor];
-[SBSystemApertureContainerView addContainerViewGeometryObserver:];
-[SBSystemApertureContainerView addContentSubview:];
-[SBSystemApertureContainerView backgroundGroupingView];
-[SBSystemApertureContainerView containerViewDescription];
-[SBSystemApertureContainerView elevatedSubBackgroundGroupingView];
-[SBSystemApertureContainerView initWithInterfaceElementIdentifier:];
-[SBSystemApertureContainerView isHitTestingEnabled];
-[SBSystemApertureContainerView matchMoveSourceView];
-[SBSystemApertureContainerView outgoingElementViewController];
-[SBSystemApertureContainerView removeContainerViewGeometryObserver:];
-[SBSystemApertureContainerView rotatingContentView];
-[SBSystemApertureContainerView scalingContentView];
-[SBSystemApertureContainerView setHitTestingEnabled:];
-[SBSystemApertureContainerView setIDCornerRadius:];
-[SBSystemApertureContainerView setMatchMoveSourceView:];
-[SBSystemApertureContainerView subBackgroundGroupingView];
```
