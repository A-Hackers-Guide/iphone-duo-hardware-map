# `_UISceneLayerHostContainerView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `FBSceneLayerManagerObserver`, `BSInvalidatable`
- 14 instance variables, 8 properties, 55 instance methods, 0 class methods

## Instance variables

```
@"FBScene" _scene;
@"<_UISceneLayerHostContainerViewDataSource>" _dataSource;
@"NSMutableOrderedSet" _hostViews;
@"NSMutableOrderedSet" _hostedLayers;
@"NSMutableSet" _hiddenLayers;
@"FBSSceneSettings" _effectiveSceneSettings;
@"UIScenePresentationContext" _presentationContext;
@"UIView" _innerLayerContainer;
@"UIView" _backgroundView;
@"CAContext" _asyncRenderGroupingContext;
@"_UISceneLayerHostContainerView" _asyncRenderGroupingContainerView;
@"_UIContextLayerHostView" _asyncRenderGroupingHostView;
@"NSString" _debugDescription;
B _invalidated;
```

## Properties

```
@property (T@"FBScene",R,W,N,V_scene) scene;
@property (T@"<_UISceneLayerHostContainerViewDataSource>",R,W,N,V_dataSource) dataSource;
@property (T@"NSSet",R,N) hostedLayers;
@property (T@"NSSet",R,N) nonHostedLayers;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UISceneLayerHostContainerView _toggleResizesHostedContextWithNewContext:];
-[_UISceneLayerHostContainerView _presentationContextChangedFrom:toContext:force:];
-[_UISceneLayerHostContainerView debugDescription];
-[_UISceneLayerHostContainerView succinctDescriptionBuilder];
-[_UISceneLayerHostContainerView _toggleStopsSecureSuperlayersValidationWithNewContext:];
-[_UISceneLayerHostContainerView init];
-[_UISceneLayerHostContainerView dealloc];
-[_UISceneLayerHostContainerView _focusedSound];
-[_UISceneLayerHostContainerView _invalidateAndRemoveAsyncViewsFromHierarchy];
-[_UISceneLayerHostContainerView _filteredLayersToPresent];
-[_UISceneLayerHostContainerView _updateAsyncDrawingOptionsInAsyncPresentation];
-[_UISceneLayerHostContainerView _asyncRenderingHostView];
-[_UISceneLayerHostContainerView _asyncRenderingContainerView];
-[_UISceneLayerHostContainerView window];
-[_UISceneLayerHostContainerView _toggleClippingDisabledWithNewContext:];
-[_UISceneLayerHostContainerView _applyBackgroundViewToHierarchy];
-[_UISceneLayerHostContainerView descriptionWithMultilinePrefix:];
-[_UISceneLayerHostContainerView _updateRenderingModeForLayersInNormalPresentation];
-[_UISceneLayerHostContainerView _backgroundView];
-[_UISceneLayerHostContainerView _setBackgroundView:];
-[_UISceneLayerHostContainerView _rebuildLayersForReason:withFence:];
-[_UISceneLayerHostContainerView _refreshDataSource];
-[_UISceneLayerHostContainerView succinctDescription];
-[_UISceneLayerHostContainerView _realHostedLayers];
-[_UISceneLayerHostContainerView nonHostedLayers];
-[_UISceneLayerHostContainerView invalidate];
-[_UISceneLayerHostContainerView _toggleZombifiesHostedContextWithNewContext:];
-[_UISceneLayerHostContainerView updateForGeometrySettingsChanges:];
-[_UISceneLayerHostContainerView hostedLayers];
-[_UISceneLayerHostContainerView _toggleInheritsSecurityWithNewContext:];
-[_UISceneLayerHostContainerView dataSource];
-[_UISceneLayerHostContainerView scene];
-[_UISceneLayerHostContainerView initWithScene:debugDescription:];
-[_UISceneLayerHostContainerView refreshDataSource:];
-[_UISceneLayerHostContainerView _toggleStopsHitTestTransformAccumulationWithNewContext:];
-[_UISceneLayerHostContainerView _presentationContextForLayer:];
-[_UISceneLayerHostContainerView _setDataSource:];
-[_UISceneLayerHostContainerView _rebuildLayersForAsyncPresentationWithReason:withFence:];
-[_UISceneLayerHostContainerView description];
-[_UISceneLayerHostContainerView _rebuildLayersForNormalPresentationWithReason:withFence:];
-[_UISceneLayerHostContainerView popDataSource:];
-[_UISceneLayerHostContainerView _hostViews];
-[_UISceneLayerHostContainerView initWithCoder:];
-[_UISceneLayerHostContainerView _hitTest:withEvent:windowServerHitTestWindow:];
-[_UISceneLayerHostContainerView _createHostViewForLayer:];
-[_UISceneLayerHostContainerView sceneLayerManagerDidUpdateLayers:];
-[_UISceneLayerHostContainerView _shouldAnimatePropertyWithKey:];
-[_UISceneLayerHostContainerView _asyncContext];
-[_UISceneLayerHostContainerView initWithFrame:];
-[_UISceneLayerHostContainerView _canShowKeyboardLayer];
-[_UISceneLayerHostContainerView _presentationContext];
-[_UISceneLayerHostContainerView pushDataSource:];
-[_UISceneLayerHostContainerView descriptionBuilderWithMultilinePrefix:];
-[_UISceneLayerHostContainerView _adjustHostViewFrameAlignment:];
-[_UISceneLayerHostContainerView _setPresentationContext:];
```
