# `UIKBKeyView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `UIKBCacheableView`
- 24 instance variables, 32 properties, 82 instance methods, 1 class methods

## Instance variables

```
@"UIKBTree" m_keyplane;
@"UIKBTree" m_key;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} m_drawFrame;
^{__CFBoolean=} m_allowsCaching;
@"UIKBRenderConfig" m_renderConfig;
@"UIKBRenderFactory" m_factory;
@"NSMutableDictionary" _keyLayers;
i _renderedKeyState;
@"NSString" _cachedTraitsHashString;
^{CGColor=} _activeBackgroundColor;
@ _activeCompositingFilter;
B _singleRerender;
d _cachedBackgroundOpacity;
@"CAShapeLayer" _debugHitTargetLayer;
B _cachedControlKeyRenderingPreference;
B _renderAsMask;
B _containedInDynamicKey;
Q _cachedAnchorCorner;
Q _cachedShiftState;
q _cachedSelector;
@"UIKeyboardMenuView" _popupMenu;
d _endingTransitionDuration;
@"UIKBScreenTraits" _screenTraits;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _debugDisplayRect;
```

## Properties

```
@property (TB,N,V_renderAsMask) renderAsMask;
@property (Tq,R) cachedRenderFlags;
@property (T{UIEdgeInsets=dddd},R,N) displayInsets;
@property (T@"NSString",&,N,V_cachedTraitsHashString) cachedTraitsHashString;
@property (TQ,N,V_cachedAnchorCorner) cachedAnchorCorner;
@property (TQ,N,V_cachedShiftState) cachedShiftState;
@property (Tq,N,V_cachedSelector) cachedSelector;
@property (TB,N,V_cachedControlKeyRenderingPreference) cachedControlKeyRenderingPreference;
@property (TB,N,V_containedInDynamicKey) containedInDynamicKey;
@property (T@"UIKBTree",R,N,Vm_keyplane) keyplane;
@property (T@"UIKBTree",R,N,Vm_key) key;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,Vm_drawFrame) drawFrame;
@property (T@"UIKBRenderConfig",&,N,Vm_renderConfig) renderConfig;
@property (T@"UIKBRenderFactory",&,N,Vm_factory) factory;
@property (T@"UIKeyboardMenuView",W,N,V_popupMenu) popupMenu;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) variantFrame;
@property (T@"UIKBKeyView",R,N) contentsKeyView;
@property (Td,N,V_endingTransitionDuration) endingTransitionDuration;
@property (T@"UIKBScreenTraits",&,N,V_screenTraits) screenTraits;
@property (TB,R,N) isDynamicKey;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_debugDisplayRect) debugDisplayRect;
@property (T@"NSString",R,N) cacheKey;
@property (TB,R,N) cacheDeferable;
@property (Td,R,N) cachedWidth;
@property (TB,R,N) keepNonPersistent;
@property (TB,R,N) displaysColorImage;
@property (Tq,R,N) assetIdiom;
@property (Tq,?,R,N) cacheDeferPriority;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UIKBKeyView wantsScreenTraits];
```

## Instance methods

```
-[UIKBKeyView keyplane];
-[UIKBKeyView drawFrame];
-[UIKBKeyView imageOrientationForLayer:];
-[UIKBKeyView assetIdiom];
-[UIKBKeyView setDrawFrame:];
-[UIKBKeyView touchesEnded:withEvent:];
-[UIKBKeyView updateKeycapLayerOrientation];
-[UIKBKeyView renderConfig];
-[UIKBKeyView contentsKeyView];
-[UIKBKeyView _canDrawContent];
-[UIKBKeyView requiresSublayers];
-[UIKBKeyView cachedWidth];
-[UIKBKeyView layerForRenderFlags:];
-[UIKBKeyView factory];
-[UIKBKeyView changeBackgroundToEnabled];
-[UIKBKeyView dimKeys:];
-[UIKBKeyView prepareForDisplay];
-[UIKBKeyView hasRendered];
-[UIKBKeyView displayInsets];
-[UIKBKeyView initWithFrame:keyplane:key:];
-[UIKBKeyView setRenderConfig:];
-[UIKBKeyView displayLayer:];
-[UIKBKeyView setFactory:];
-[UIKBKeyView drawContentsOfRenderers:];
-[UIKBKeyView changeBackgroundToActiveIfNecessary];
-[UIKBKeyView cacheKey];
-[UIKBKeyView updateForKeyplane:key:];
-[UIKBKeyView setScreenTraits:];
-[UIKBKeyView keepNonPersistent];
-[UIKBKeyView displaysColorImage];
-[UIKBKeyView screenTraits];
-[UIKBKeyView dealloc];
-[UIKBKeyView cacheKeysForRenderFlags:];
-[UIKBKeyView cacheDeferable];
-[UIKBKeyView layoutSubviews];
-[UIKBKeyView _setupDictationSlotView];
-[UIKBKeyView removeFromSuperview];
-[UIKBKeyView isDynamicKey];
-[UIKBKeyView textEffectsVisibilityLevel];
-[UIKBKeyView key];
-[UIKBKeyView subTreeHitTest:];
-[UIKBKeyView _applyAppearanceInvocations];
-[UIKBKeyView _generateBackdropAndBorderMaskImage];
-[UIKBKeyView _isActivePopupKey];
-[UIKBKeyView _populateLayer:withContents:];
-[UIKBKeyView _shouldUpdateLayers];
-[UIKBKeyView _updateDebugHitTargetLayer];
-[UIKBKeyView _viewShouldBeOpaque];
-[UIKBKeyView allowBackgroundCachingForRenderFlags:];
-[UIKBKeyView cachedAnchorCorner];
-[UIKBKeyView cachedControlKeyRenderingPreference];
-[UIKBKeyView cachedRenderFlags];
-[UIKBKeyView cachedSelector];
-[UIKBKeyView cachedShiftState];
-[UIKBKeyView cachedTraitsHashString];
-[UIKBKeyView configureBackdropView:forRenderConfig:];
-[UIKBKeyView containedInDynamicKey];
-[UIKBKeyView debugDisplayRect];
-[UIKBKeyView didInputSubTree:];
-[UIKBKeyView endingTransitionDuration];
-[UIKBKeyView focusableVariantCount];
-[UIKBKeyView hideKeyCap:];
-[UIKBKeyView initWithFrame:keyplane:key:screenTraits:];
-[UIKBKeyView orientKeyCap:];
-[UIKBKeyView popupMenu];
-[UIKBKeyView renderAsMask];
-[UIKBKeyView renderFlagsForTraits:];
-[UIKBKeyView resetRenderedKeyState];
-[UIKBKeyView setCachedAnchorCorner:];
-[UIKBKeyView setCachedControlKeyRenderingPreference:];
-[UIKBKeyView setCachedSelector:];
-[UIKBKeyView setCachedShiftState:];
-[UIKBKeyView setCachedTraitsHashString:];
-[UIKBKeyView setContainedInDynamicKey:];
-[UIKBKeyView setDebugDisplayRect:];
-[UIKBKeyView setEndingTransitionDuration:];
-[UIKBKeyView setPopupMenu:];
-[UIKBKeyView setRenderAsMask:];
-[UIKBKeyView updateKeySelectedVariantIndex:];
-[UIKBKeyView updateKeySubtrees:];
-[UIKBKeyView variantFrame];
-[UIKBKeyView willDisplayModalActionView:withSubTreeKeyView:completion:];
```
