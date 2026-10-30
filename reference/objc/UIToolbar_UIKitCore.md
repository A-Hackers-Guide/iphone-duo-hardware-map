# `UIToolbar`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `UIAccessibilityHUDGestureDelegate`, `_UIBarPositioningInternal`, `UIGestureRecognizerDelegatePrivate`, `UIBarPositioning`
- 21 instance variables, 36 properties, 122 instance methods, 6 class methods

## Instance variables

```
@"<_UIToolbarDelegateInternal>" _delegate;
@"NSArray" _items;
@"UIColor" _barTintColor;
{?="barStyle"b3"barTranslucence"b3"isLocked"b1"linkedBeforeWhitetailAndInitializedFromCoder"b1"disableBlurTinting"b1"delegateRespondsToInterfaceOrientationWindowSelector"b1"appearanceHint"b2} _toolbarFlags;
@ __appearanceStorage;
@"_UIToolbarVisualProvider" _visualProvider;
@"UIAccessibilityHUDGestureManager" _axHUDGestureManager;
Q _disableAutolayoutWarnings;
B _autoHidesToolbarInFullscreen;
B _centerTextButtons;
@"UIView" _shadowView;
q _barPosition;
@"UIToolbarAppearance" _standardAppearance;
@"UIToolbarAppearance" _scrollEdgeAppearance;
@"UIToolbarAppearance" _compactScrollEdgeAppearance;
@"UIToolbarAppearance" _compactAppearance;
@? __itemsDidChangeBlock;
Q __edgesRequiringContentMargin;
Q __adjacentBarEdges;
@"UIBarButtonItem" _centerItem;
@"NSArray" _backgroundEffects;
```

## Properties

```
@property (T@?,C,N,S_setItemsDidChangeBlock:,V__itemsDidChangeBlock) _itemsDidChangeBlock;
@property (TQ,N,S_setEdgesRequiringContentMargin:,V__edgesRequiringContentMargin) _edgesRequiringContentMargin;
@property (TQ,N,S_setAdjacentBarEdges:,V__adjacentBarEdges) _adjacentBarEdges;
@property (T@"UIView",R,N) currentBackgroundView;
@property (TB,N,G_isLocked,S_setLocked:) _locked;
@property (T@"UIView",&,N,S_setShadowView:,V_shadowView) _shadowView;
@property (Tq,R,N) _barTranslucence;
@property (Td,N,S_setBackgroundTransitionProgress:) _backgroundTransitionProgress;
@property (T@"UIBarButtonItem",&,N,V_centerItem) centerItem;
@property (TB,N,V_autoHidesToolbarInFullscreen) autoHidesToolbarInFullscreen;
@property (Tq,R,N) _hintFromCurrentAppearance;
@property (Tq,N,S_setAppearanceHint:) _appearanceHint;
@property (T@"UIView",&,N,S_setBackgroundView:) _backgroundView;
@property (TB,N,S_setHidesShadow:) _hidesShadow;
@property (TB,N,S_setDisableBlurTinting:) _disableBlurTinting;
@property (T@"NSArray",C,N,V_backgroundEffects) backgroundEffects;
@property (TB,R,N) _shouldStretchDuringCrossfadeTransition;
@property (Tq,N,S_setItemDistribution:) _itemDistribution;
@property (TB,N,V_centerTextButtons) centerTextButtons;
@property (TB,R,N,GisMinibar) minibar;
@property (T@"NSString",C,N,G_backdropViewLayerGroupName,S_setBackdropViewLayerGroupName:) _backdropViewLayerGroupName;
@property (Tq,N) barStyle;
@property (T@"NSArray",C,N,V_items) items;
@property (TB,N,GisTranslucent) translucent;
@property (T@"UIColor",&,D,N) tintColor;
@property (T@"UIColor",&,N,V_barTintColor) barTintColor;
@property (T@"UIToolbarAppearance",C,N,V_standardAppearance) standardAppearance;
@property (T@"UIToolbarAppearance",C,N,V_compactAppearance) compactAppearance;
@property (T@"UIToolbarAppearance",C,N,V_scrollEdgeAppearance) scrollEdgeAppearance;
@property (T@"UIToolbarAppearance",C,N,V_compactScrollEdgeAppearance) compactScrollEdgeAppearance;
@property (T@"<UIToolbarDelegate>",W,N) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (Tq,R,N,V_barPosition) barPosition;
```

## Class methods

```
+[UIToolbar defaultHeight];
+[UIToolbar _visualProviderClassForToolbar:];
+[UIToolbar _forceLegacyVisualProvider];
+[UIToolbar _visualProviderForToolbar:];
+[UIToolbar defaultButtonFont];
+[UIToolbar defaultHeightForBarSize:];
```

## Instance methods

```
-[UIToolbar setScrollEdgeAppearance:];
-[UIToolbar _shadowView];
-[UIToolbar _traitCollectionForChildEnvironment:];
-[UIToolbar scrollEdgeAppearance];
-[UIToolbar setStandardAppearance:];
-[UIToolbar standardAppearance];
-[UIToolbar _accessibilityHUDGestureManager:shouldRecognizeSimultaneouslyWithGestureRecognizer:];
-[UIToolbar _expectedInterfaceOrientation];
-[UIToolbar intrinsicContentSize];
-[UIToolbar _accessibilityHUDGestureManager:HUDItemForPoint:];
-[UIToolbar _accessibilityHUDGestureManager:gestureLiftedAtPoint:];
-[UIToolbar backgroundEffects];
-[UIToolbar _setHidesShadow:];
-[UIToolbar _setLocked:];
-[UIToolbar invalidateIntrinsicContentSize];
-[UIToolbar _edgesPropagatingSafeAreaInsetsToSubviews];
-[UIToolbar setItems:];
-[UIToolbar _hidesShadow];
-[UIToolbar setBarTintColor:];
-[UIToolbar _installDefaultAppearance];
-[UIToolbar dealloc];
-[UIToolbar drawRect:];
-[UIToolbar _updateBackgroundView];
-[UIToolbar setCenterTextButtons:];
-[UIToolbar setTranslucent:];
-[UIToolbar barStyle];
-[UIToolbar _shouldDecodeSubviews];
-[UIToolbar layoutSubviews];
-[UIToolbar _didMoveFromWindow:toWindow:];
-[UIToolbar _setDisableBlurTinting:];
-[UIToolbar items];
-[UIToolbar _effectiveBarTintColor];
-[UIToolbar _sendAction:withEvent:];
-[UIToolbar setTranslatesAutoresizingMaskIntoConstraints:];
-[UIToolbar initInView:withFrame:withItemList:];
-[UIToolbar _backgroundView];
-[UIToolbar _autolayoutSpacingAtEdge:forAttribute:inContainer:isGuide:];
-[UIToolbar setBounds:];
-[UIToolbar _setBackgroundView:];
-[UIToolbar _disableBlurTinting];
-[UIToolbar _isLocked];
-[UIToolbar sizeThatFits:];
-[UIToolbar defaultSizeForOrientation:];
-[UIToolbar _contentHuggingDefault_isUsuallyFixedHeight];
-[UIToolbar setDelegate:];
-[UIToolbar currentBackgroundView];
-[UIToolbar setTintColor:];
-[UIToolbar _itemAtPoint:];
-[UIToolbar _subclassImplementsDrawRect];
-[UIToolbar _backgroundTransitionProgress];
-[UIToolbar setBarStyle:];
-[UIToolbar encodeWithCoder:];
-[UIToolbar barPosition];
-[UIToolbar setBackgroundEffects:];
-[UIToolbar centerTextButtons];
-[UIToolbar _hasCustomAutolayoutNeighborSpacingForAttribute:];
-[UIToolbar isTranslucent];
-[UIToolbar delegate];
-[UIToolbar setFrame:];
-[UIToolbar isElementAccessibilityExposedToInterfaceBuilder];
-[UIToolbar description];
-[UIToolbar _shouldStretchDuringCrossfadeTransition];
-[UIToolbar initWithCoder:];
-[UIToolbar _setBackdropViewLayerGroupName:];
-[UIToolbar _populateArchivedSubviews:];
-[UIToolbar barTintColor];
-[UIToolbar centerItem];
-[UIToolbar pointInside:withEvent:];
-[UIToolbar _startInteractiveTransition];
-[UIToolbar _setBarPosition:];
-[UIToolbar _defaultAutolayoutSpacing];
-[UIToolbar _setBackgroundTransitionProgress:];
-[UIToolbar initWithFrame:];
-[UIToolbar setItems:animated:];
-[UIToolbar _backdropViewLayerGroupName];
-[UIToolbar _barPosition];
-[UIToolbar _appearanceHint];
-[UIToolbar _setShadowView:];
-[UIToolbar setCompactScrollEdgeAppearance:];
-[UIToolbar _46877859];
-[UIToolbar __appearanceStorage];
-[UIToolbar _adjacentBarEdges];
-[UIToolbar _barTranslucence];
-[UIToolbar _customViewChangedForButtonItem:];
-[UIToolbar _doCommonToolbarInit];
-[UIToolbar _edgesRequiringContentMargin];
-[UIToolbar _effectiveBarTintColorDidChangeWithPreviousColor:];
-[UIToolbar _finishInteractiveTransition];
-[UIToolbar _frameOfBarButtonItem:];
-[UIToolbar _frameOrBoundsChangedWithVisibleSizeChange:wasMinibar:];
-[UIToolbar _hintFromCurrentAppearance];
-[UIToolbar _hostsLayoutEngineAllowsTAMIC_NO];
-[UIToolbar _itemDistribution];
-[UIToolbar _itemsDidChangeBlock];
-[UIToolbar _largeContentViewerEnabledStatusDidChange:];
-[UIToolbar _linkedBeforeWhitetailAndInitializedFromCoder];
-[UIToolbar _positionToolbarButtonsAndResetFontScaleAdjustment:];
-[UIToolbar _setAdjacentBarEdges:];
-[UIToolbar _setAppearanceHint:];
-[UIToolbar _setButtonBackgroundImage:mini:forStates:];
-[UIToolbar _setEdgesRequiringContentMargin:];
-[UIToolbar _setForceTopBarAppearance:];
-[UIToolbar _setItemDistribution:];
-[UIToolbar _setItemsDidChangeBlock:];
-[UIToolbar _setNeedsBackgroundViewUpdate];
-[UIToolbar _setVisualAltitude:];
-[UIToolbar _setVisualAltitudeBias:];
-[UIToolbar _setupAXHUDGestureIfNecessary];
-[UIToolbar _updateBarForStyle];
-[UIToolbar _updateInteractiveTransitionWithProgress:];
-[UIToolbar autoHidesToolbarInFullscreen];
-[UIToolbar backdropView:didChangeToGraphicsQuality:];
-[UIToolbar backgroundImageForToolbarPosition:barMetrics:];
-[UIToolbar compactAppearance];
-[UIToolbar compactScrollEdgeAppearance];
-[UIToolbar isMinibar];
-[UIToolbar setAutoHidesToolbarInFullscreen:];
-[UIToolbar setBackgroundImage:forToolbarPosition:barMetrics:];
-[UIToolbar setCenterItem:];
-[UIToolbar setCompactAppearance:];
-[UIToolbar setShadowImage:forToolbarPosition:];
-[UIToolbar shadowImageForToolbarPosition:];
```
