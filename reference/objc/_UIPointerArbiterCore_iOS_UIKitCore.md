# `_UIPointerArbiterCore_iOS`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `PSPointerClientControllerDelegate`, `_UILumaTrackingBackdropViewDelegate`, `_UIAssertionControllerSubject`, `_UIPointerArbitrating`
- 17 instance variables, 22 properties, 58 instance methods, 0 class methods

## Instance variables

```
B _hasRunningTransaction;
B _updatesPausedViaAssertion;
@"_UIPointerLensView" _lensView;
@"NSMutableArray" _pendingTransactionBlocks;
@"UIPointerStyle" _activePointerStyle;
@"UIPointerRegion" _activePointerRegion;
@"PSPointerHoverRegion" _lastSentHoverRegion;
Q _lastMaterialLuminance;
@"NSMapTable" _pointerRegionToMatchMoveSourceMap;
@"PSPointerClientController" _pointerClientController;
@"PSPointerPortalSourceCollection" _pointerPortalSourceCollection;
@"_UIPortalView" _pointerPortalView;
@"_UIPortalView" _overlayEffectPortalView;
@"_UILumaTrackingBackdropView" _samplingBackdropView;
Q _transactionRevisionID;
@"UIPointerRegion" _scrollingRegion;
@"_UIAssertionController" _pauseAssertionController;
```

## Properties

```
@property (TB,N,V_hasRunningTransaction) hasRunningTransaction;
@property (T@"NSMutableArray",&,N,V_pendingTransactionBlocks) pendingTransactionBlocks;
@property (T@"UIPointerStyle",&,N,V_activePointerStyle) activePointerStyle;
@property (T@"UIPointerRegion",&,N,V_activePointerRegion) activePointerRegion;
@property (T@"PSPointerHoverRegion",&,N,V_lastSentHoverRegion) lastSentHoverRegion;
@property (TQ,N,V_lastMaterialLuminance) lastMaterialLuminance;
@property (T@"NSMapTable",&,N,V_pointerRegionToMatchMoveSourceMap) pointerRegionToMatchMoveSourceMap;
@property (T@"PSPointerClientController",&,N,V_pointerClientController) pointerClientController;
@property (T@"PSPointerPortalSourceCollection",C,N,V_pointerPortalSourceCollection) pointerPortalSourceCollection;
@property (T@"_UIPortalView",&,N,V_pointerPortalView) pointerPortalView;
@property (T@"_UIPortalView",&,N,V_overlayEffectPortalView) overlayEffectPortalView;
@property (T@"_UILumaTrackingBackdropView",&,N,V_samplingBackdropView) samplingBackdropView;
@property (TQ,N,V_transactionRevisionID) transactionRevisionID;
@property (T@"UIPointerRegion",&,N,V_scrollingRegion) scrollingRegion;
@property (T@"_UIAssertionController",&,N,V_pauseAssertionController) pauseAssertionController;
@property (TB,N,V_updatesPausedViaAssertion) updatesPausedViaAssertion;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (Tq,R,N) pointerState;
@property (T@"_UIPointerLensView",R,N,V_lensView) lensView;
```

## Instance methods

```
-[_UIPointerArbiterCore_iOS pointerState];
-[_UIPointerArbiterCore_iOS _pointerShapeForStyle:region:];
-[_UIPointerArbiterCore_iOS assertionActivationStateForType:];
-[_UIPointerArbiterCore_iOS pointerClientControllerClientInteractionStateDidChange:];
-[_UIPointerArbiterCore_iOS _clearMatchMoveSourceForRegion:immediately:];
-[_UIPointerArbiterCore_iOS pauseAssertionController];
-[_UIPointerArbiterCore_iOS backgroundLumaView:didTransitionToLevel:];
-[_UIPointerArbiterCore_iOS lastMaterialLuminance];
-[_UIPointerArbiterCore_iOS init];
-[_UIPointerArbiterCore_iOS setLastMaterialLuminance:];
-[_UIPointerArbiterCore_iOS endScrollingWithRegion:];
-[_UIPointerArbiterCore_iOS pointerClientController];
-[_UIPointerArbiterCore_iOS setUpdatesPausedViaAssertion:];
-[_UIPointerArbiterCore_iOS setLastSentHoverRegion:];
-[_UIPointerArbiterCore_iOS transactionRevisionID];
-[_UIPointerArbiterCore_iOS _notifyPointerStateDidChange];
-[_UIPointerArbiterCore_iOS obtainPointerUpdatePauseAssertion];
-[_UIPointerArbiterCore_iOS activePointerRegion];
-[_UIPointerArbiterCore_iOS _performNextTransaction];
-[_UIPointerArbiterCore_iOS _coordinateSpaceSourceViewForRegion:withStyle:];
-[_UIPointerArbiterCore_iOS pointerPortalView];
-[_UIPointerArbiterCore_iOS setPointerRegionToMatchMoveSourceMap:];
-[_UIPointerArbiterCore_iOS hasRunningTransaction];
-[_UIPointerArbiterCore_iOS updatesPausedViaAssertion];
-[_UIPointerArbiterCore_iOS setOverlayEffectPortalView:];
-[_UIPointerArbiterCore_iOS lastSentHoverRegion];
-[_UIPointerArbiterCore_iOS pointerClientControllerWillDecelerate:targetPointerPosition:velocity:inContextID:cursorRegionLookupRadius:cursorRegionLookupResolution:lookupConeAngle:];
-[_UIPointerArbiterCore_iOS overlayEffectPortalView];
-[_UIPointerArbiterCore_iOS applyStyle:forRegion:effectSourceHandler:completion:];
-[_UIPointerArbiterCore_iOS setSamplingBackdropView:];
-[_UIPointerArbiterCore_iOS beginScrollingWithRegion:];
-[_UIPointerArbiterCore_iOS pointerPortalSourceCollection];
-[_UIPointerArbiterCore_iOS _hoverRegionWithStyle:forRegion:];
-[_UIPointerArbiterCore_iOS _prepareContentMatchMoveSourceForPointerRegion:completion:];
-[_UIPointerArbiterCore_iOS setScrollingRegion:];
-[_UIPointerArbiterCore_iOS _setActiveHoverRegion:style:forPointerRegion:transactionID:completion:];
-[_UIPointerArbiterCore_iOS activePointerStyle];
-[_UIPointerArbiterCore_iOS setPendingTransactionBlocks:];
-[_UIPointerArbiterCore_iOS _preparePointerPortalSourceCollectionWithCompletion:];
-[_UIPointerArbiterCore_iOS setPointerClientController:];
-[_UIPointerArbiterCore_iOS setActivePointerStyle:];
-[_UIPointerArbiterCore_iOS setHasRunningTransaction:];
-[_UIPointerArbiterCore_iOS setActivePointerRegion:];
-[_UIPointerArbiterCore_iOS _psPointerShapeFromUIPointerShape:atScale:];
-[_UIPointerArbiterCore_iOS assertionActivationStateChangedToState:forType:];
-[_UIPointerArbiterCore_iOS setPointerPortalView:];
-[_UIPointerArbiterCore_iOS pointerClientController:didInvalidatePortalSourceCollections:matchMoveSources:];
-[_UIPointerArbiterCore_iOS exitRegion:removeStyle:completion:];
-[_UIPointerArbiterCore_iOS samplingBackdropView];
-[_UIPointerArbiterCore_iOS _getPointerRegion:andStyle:atLocation:inWindow:];
-[_UIPointerArbiterCore_iOS setPauseAssertionController:];
-[_UIPointerArbiterCore_iOS _performTransactionUsingBlock:];
-[_UIPointerArbiterCore_iOS setPointerPortalSourceCollection:];
-[_UIPointerArbiterCore_iOS scrollingRegion];
-[_UIPointerArbiterCore_iOS pointerRegionToMatchMoveSourceMap];
-[_UIPointerArbiterCore_iOS pendingTransactionBlocks];
-[_UIPointerArbiterCore_iOS setTransactionRevisionID:];
-[_UIPointerArbiterCore_iOS lensView];
```
