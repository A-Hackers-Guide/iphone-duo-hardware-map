# `SBAppPlatterDragPreview`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `SBIconDragPreview`, `BSDescriptionProviding`
- 42 instance variables, 28 properties, 94 instance methods, 0 class methods

## Instance variables

```
B _isBlurredPlatterReady;
B _hasAnimatedToBlurredPlatter;
Q _platterViewAlphaAnimationCount;
@"NSHashTable" _cleanupDelayAssertions;
B _flocked;
B _iconCanShowResizeHandle;
B _iconAllowsLabelArea;
B _iconAllowsAccessory;
B _iconCanShowCloseBox;
B _iconIsHighlighted;
B _iconInitiallyShowingCloseBox;
B _iconInitiallyShowingResizeHandle;
B _delayingCleanup;
Q _dragState;
d _iconContentScale;
@? _cleanUpHandler;
Q _mode;
@"UIView" _sourceView;
d _sourceViewScale;
@"SBApplicationBlurContentView" _platterView;
@? _platterViewAlphaAnimationCompletionBlock;
@"NSArray" _diffuseShadowFilters;
@"NSArray" _rimShadowFilters;
@"BSCornerRadiusConfiguration" _cornerRadiusConfiguration;
d _rotation;
@"SBIconView" _referenceIconView;
@"SBIconView" _iconView;
@"UIView" _captureOnlyBackgroundView;
@"UIViewController<SBIconViewCustomImageViewControlling>" _customIconImageViewController;
@"<SBIconListLayoutProvider>" _pendingIconViewListLayoutProvider;
@"UIView" _anchorPointAdjustmentContainerView;
@"UIView" _iconContainerView;
@"UIView" _cornerMaskingView;
@"SBPortalView" _sourcePortalView;
@"UIView" _unclippedSourceContainerView;
@"SBFView" _diffuseShadowView;
@"SBFView" _rimShadowView;
@"SBSlideOverTongueView" _slideOverTongueView;
{CGSize="width"d"height"d} _platterSize;
{CGPoint="x"d"y"d} _anchorPoint;
{SBDragPreviewShadowParameters="shadowOpacity"d"shadowRadius"d"shadowOffset"{CGSize="width"d"height"d}} _diffuseShadowParameters;
{SBDragPreviewShadowParameters="shadowOpacity"d"shadowRadius"d"shadowOffset"{CGSize="width"d"height"d}} _rimShadowParameters;
```

## Properties

```
@property (TQ,N,V_mode) mode;
@property (T@"UIView",R,N) sourceView;
@property (Td,N,V_sourceViewScale) sourceViewScale;
@property (T@"SBApplicationBlurContentView",R,N) platterView;
@property (TB,R,N,GisAnimatingPlatterViewAlpha) animatingPlatterViewAlpha;
@property (T@?,C,N,V_platterViewAlphaAnimationCompletionBlock) platterViewAlphaAnimationCompletionBlock;
@property (T{CGSize=dd},N,V_platterSize) platterSize;
@property (T{SBDragPreviewShadowParameters=dd{CGSize=dd}},N,V_diffuseShadowParameters) diffuseShadowParameters;
@property (T{SBDragPreviewShadowParameters=dd{CGSize=dd}},N,V_rimShadowParameters) rimShadowParameters;
@property (T@"NSArray",C,N,V_diffuseShadowFilters) diffuseShadowFilters;
@property (T@"NSArray",C,N,V_rimShadowFilters) rimShadowFilters;
@property (T@"BSCornerRadiusConfiguration",&,N,V_cornerRadiusConfiguration) cornerRadiusConfiguration;
@property (T{CGPoint=dd},N,V_anchorPoint) anchorPoint;
@property (Td,N,V_rotation) rotation;
@property (TQ,N,V_dragState) dragState;
@property (TB,N,GisFlocked,V_flocked) flocked;
@property (TB,N,V_iconAllowsLabelArea) iconAllowsLabelArea;
@property (TB,N,V_iconAllowsAccessory) iconAllowsAccessory;
@property (TB,N,V_iconCanShowCloseBox) iconCanShowCloseBox;
@property (Td,N,V_iconContentScale) iconContentScale;
@property (TB,N) iconIsEditing;
@property (T@"SBIcon",&,N) icon;
@property (T@?,C,N,V_cleanUpHandler) cleanUpHandler;
@property (TB,?,N,V_iconCanShowResizeHandle) iconCanShowResizeHandle;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBAppPlatterDragPreview platterView];
-[SBAppPlatterDragPreview iconContentScale];
-[SBAppPlatterDragPreview cornerRadiusConfiguration];
-[SBAppPlatterDragPreview _updateSubviewVisibility];
-[SBAppPlatterDragPreview rotation];
-[SBAppPlatterDragPreview setIconContentScale:];
-[SBAppPlatterDragPreview succinctDescriptionBuilder];
-[SBAppPlatterDragPreview dragState];
-[SBAppPlatterDragPreview setCornerRadiusConfiguration:];
-[SBAppPlatterDragPreview anchorPoint];
-[SBAppPlatterDragPreview setIcon:];
-[SBAppPlatterDragPreview _updateShadowView];
-[SBAppPlatterDragPreview _isDragging];
-[SBAppPlatterDragPreview layoutSubviews];
-[SBAppPlatterDragPreview descriptionWithMultilinePrefix:];
-[SBAppPlatterDragPreview setMode:];
-[SBAppPlatterDragPreview succinctDescription];
-[SBAppPlatterDragPreview setRotation:];
-[SBAppPlatterDragPreview mode];
-[SBAppPlatterDragPreview description];
-[SBAppPlatterDragPreview _effectiveCornerRadius];
-[SBAppPlatterDragPreview setAnchorPoint:];
-[SBAppPlatterDragPreview setDragState:];
-[SBAppPlatterDragPreview descriptionBuilderWithMultilinePrefix:];
-[SBAppPlatterDragPreview icon];
-[SBAppPlatterDragPreview sourceView];
-[SBAppPlatterDragPreview isFlocked];
-[SBAppPlatterDragPreview setPlatterSize:];
-[SBAppPlatterDragPreview platterSize];
-[SBAppPlatterDragPreview updateSourceView:];
-[SBAppPlatterDragPreview _configureIconViewWithReferenceIconView:];
-[SBAppPlatterDragPreview _removeDelayCleanupAssertion:];
-[SBAppPlatterDragPreview cleanUpHandler];
-[SBAppPlatterDragPreview delayCleanUpForReason:];
-[SBAppPlatterDragPreview draggingSourceCancelAnimationCompleted];
-[SBAppPlatterDragPreview draggingSourceDroppedWithOperation:];
-[SBAppPlatterDragPreview dropDestinationAnimationCompleted];
-[SBAppPlatterDragPreview handleCleanup];
-[SBAppPlatterDragPreview iconAllowsAccessory];
-[SBAppPlatterDragPreview iconAllowsLabelArea];
-[SBAppPlatterDragPreview iconCanShowCloseBox];
-[SBAppPlatterDragPreview iconCanShowResizeHandle];
-[SBAppPlatterDragPreview iconIsEditing];
-[SBAppPlatterDragPreview setCleanUpHandler:];
-[SBAppPlatterDragPreview setFlocked:];
-[SBAppPlatterDragPreview setIconAllowsAccessory:];
-[SBAppPlatterDragPreview setIconAllowsLabelArea:];
-[SBAppPlatterDragPreview setIconCanShowCloseBox:];
-[SBAppPlatterDragPreview setIconCanShowResizeHandle:];
-[SBAppPlatterDragPreview setIconIsEditing:];
-[SBAppPlatterDragPreview setIconIsEditing:animated:];
-[SBAppPlatterDragPreview setIconViewCustomIconImageViewController:];
-[SBAppPlatterDragPreview setIconViewDelegate:];
-[SBAppPlatterDragPreview setIconViewListLayoutProvider:];
-[SBAppPlatterDragPreview updateDestinationIconLocation:allowsLabelArea:animated:];
-[SBAppPlatterDragPreview _matchMoveView:toContainerView:];
-[SBAppPlatterDragPreview sourceViewScale];
-[SBAppPlatterDragPreview _blurContentViewIconViewCenterYOffset];
-[SBAppPlatterDragPreview _effectiveCornerRadiusConfiguration];
-[SBAppPlatterDragPreview _effectiveIconAccessoryAlpha];
-[SBAppPlatterDragPreview _effectiveIconAllowsLabelArea];
-[SBAppPlatterDragPreview _effectiveIconCanShowCloseBox];
-[SBAppPlatterDragPreview _effectiveIconCanShowResizeHandle];
-[SBAppPlatterDragPreview _effectiveIconContainerCenter];
-[SBAppPlatterDragPreview _effectiveIconContentScale];
-[SBAppPlatterDragPreview _effectiveIconIsHighlighted];
-[SBAppPlatterDragPreview _effectiveIconViewFrame];
-[SBAppPlatterDragPreview _effectiveMode];
-[SBAppPlatterDragPreview _effectivePlatterFrame];
-[SBAppPlatterDragPreview _getIconAlpha:platterAlpha:];
-[SBAppPlatterDragPreview _setSourcePortalViewHidden:];
-[SBAppPlatterDragPreview _setUpShadowViewsIfNecessary];
-[SBAppPlatterDragPreview _updateContainerViewPositionForAnchorPoint];
-[SBAppPlatterDragPreview _updateIconViewComponentVisibility];
-[SBAppPlatterDragPreview _updateShowDebugIconBorderWithColor:];
-[SBAppPlatterDragPreview _updateSlideOverTongueView];
-[SBAppPlatterDragPreview configurePlatterForSceneHandle:withTargetView:completion:];
-[SBAppPlatterDragPreview diffuseShadowFilters];
-[SBAppPlatterDragPreview diffuseShadowParameters];
-[SBAppPlatterDragPreview iconDragAlpha];
-[SBAppPlatterDragPreview initWithReferenceIconView:sourceView:];
-[SBAppPlatterDragPreview initWithReferenceIconView:sourceView:sourceViewScale:];
-[SBAppPlatterDragPreview invalidateSourceView];
-[SBAppPlatterDragPreview isAnimatingPlatterViewAlpha];
-[SBAppPlatterDragPreview platterViewAlphaAnimationCompletionBlock];
-[SBAppPlatterDragPreview rimShadowFilters];
-[SBAppPlatterDragPreview rimShadowParameters];
-[SBAppPlatterDragPreview setDiffuseShadowFilters:];
-[SBAppPlatterDragPreview setDiffuseShadowParameters:];
-[SBAppPlatterDragPreview setPlatterViewAlphaAnimationCompletionBlock:];
-[SBAppPlatterDragPreview setRimShadowFilters:];
-[SBAppPlatterDragPreview setRimShadowParameters:];
-[SBAppPlatterDragPreview setSourceViewScale:];
-[SBAppPlatterDragPreview updateWantsSlideOverTongue:state:direction:cornerRadius:animated:];
```
