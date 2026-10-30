# `UIKBKeyplaneView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIKBSplitImageView`
- Protocols: `UIKBCacheableView`, `UIKBKeyplaneLayout`
- 22 instance variables, 24 properties, 108 instance methods, 0 class methods

## Instance variables

```
@"UIKBTree" _keyplane;
@"UIKBTree" _defaultKeyplane;
@"UIKBCacheToken" _cacheToken;
@"UIKBCacheToken" _defaultKeyplaneCacheToken;
@"UIKBKeyViewAnimator" _keyViewAnimator;
@"UIKeyboardEmojiKeyDisplayController" _emojiKeyManager;
@"UIKBKeyView" _candidateGapView;
@"NSMutableDictionary" _subviewIndex;
@"NSMutableDictionary" _activeViewIndex;
@"NSMutableDictionary" _renderedKeyViews;
@"NSMutableDictionary" _delayedDeactivationKeys;
B _shouldDrawRect;
@"UIKBSplitImageView" _keyBorders;
@"UIKBSplitImageView" _keyBackgrounds;
@"UIKBSplitImageView" _keyCaps;
@"UIView" _keyplaneMaskView;
@"UIKBRenderConfig" _renderConfig;
@"UIKBRenderingContext" _renderingContext;
@"UIKBRenderFactory" _factory;
B suppressDrawing;
@"UIKBScreenTraits" _overrideScreenTraits;
@"<UIKBKeyplaneViewDelegate>" _delegate;
```

## Properties

```
@property (T@"UIKBScreenTraits",&,N,V_overrideScreenTraits) overrideScreenTraits;
@property (T@"UIKBRenderFactory",&,N,V_factory) factory;
@property (T@"UIView",&,N,V_keyplaneMaskView) keyplaneMaskView;
@property (T@"<UIKBKeyplaneViewDelegate>",W,N,V_delegate) delegate;
@property (T@"UIKBTree",&,N,V_keyplane) keyplane;
@property (T@"UIKBTree",&,N,V_defaultKeyplane) defaultKeyplane;
@property (T@"UIKBCacheToken",&,N,V_cacheToken) cacheToken;
@property (T@"UIKBCacheToken",&,N,V_defaultKeyplaneCacheToken) defaultKeyplaneCacheToken;
@property (T@"UIKBKeyViewAnimator",&,N,V_keyViewAnimator) keyViewAnimator;
@property (T@"UIKeyboardEmojiKeyDisplayController",&,N,V_emojiKeyManager) emojiKeyManager;
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
@property (T@"UIKBRenderingContext",&,N,V_renderingContext) renderingContext;
@property (T@"UIKBRenderConfig",&,N,V_renderConfig) renderConfig;
@property (TB,N,VsuppressDrawing) suppressDrawing;
```

## Instance methods

```
-[UIKBKeyplaneView isSplit];
-[UIKBKeyplaneView keyplaneMaskView];
-[UIKBKeyplaneView _shouldAllowKey:];
-[UIKBKeyplaneView changingSelectedVariantForKey:atPoint:isDragging:];
-[UIKBKeyplaneView updateToSize:];
-[UIKBKeyplaneView rightSplitSize];
-[UIKBKeyplaneView setOverrideScreenTraits:];
-[UIKBKeyplaneView setKeyplane:];
-[UIKBKeyplaneView keyplane];
-[UIKBKeyplaneView setDockHidesItemsOverlappingEmoji:];
-[UIKBKeyplaneView cacheIdentifierForKey:withState:];
-[UIKBKeyplaneView deactivateAdaptiveKey:];
-[UIKBKeyplaneView transitionWillFinishWithProgress:completion:];
-[UIKBKeyplaneView purgeFactory];
-[UIKBKeyplaneView existingVariantsKeyViewForKey:];
-[UIKBKeyplaneView deactivateKeys];
-[UIKBKeyplaneView activeKeyViews];
-[UIKBKeyplaneView showSplitKeyplane:animated:];
-[UIKBKeyplaneView currentHandBias];
-[UIKBKeyplaneView suppressDrawing];
-[UIKBKeyplaneView validForKeyplane:withVisualStyle:];
-[UIKBKeyplaneView leftSplitSize];
-[UIKBKeyplaneView updateVariantSelectorFramesForKey:];
-[UIKBKeyplaneView setKeyboardBias:];
-[UIKBKeyplaneView stateForKey:];
-[UIKBKeyplaneView fullHeightForDockedKeyboard];
-[UIKBKeyplaneView setRemoteKeyViewProvider:];
-[UIKBKeyplaneView supportsSplit];
-[UIKBKeyplaneView setOverrideScreenTraits:currentKeyboardMode:];
-[UIKBKeyplaneView _generateFactoryIfNeeded];
-[UIKBKeyplaneView assetIdiom];
-[UIKBKeyplaneView hitTestVariantKeyAtPoint:];
-[UIKBKeyplaneView supportsStateAnimations];
-[UIKBKeyplaneView setContentScaleFactor:];
-[UIKBKeyplaneView renderingContext];
-[UIKBKeyplaneView purgeLayerContents];
-[UIKBKeyplaneView initWithFrame:keyplane:];
-[UIKBKeyplaneView deactivateKey:previousState:];
-[UIKBKeyplaneView setRenderingContext:];
-[UIKBKeyplaneView updateFrameForKey:];
-[UIKBKeyplaneView setSuppressDrawing:];
-[UIKBKeyplaneView isDynamicLayout];
-[UIKBKeyplaneView finishedSelectingVariantForKey:atPoint:];
-[UIKBKeyplaneView purgeKeyViews];
-[UIKBKeyplaneView purgeActiveKeyViews];
-[UIKBKeyplaneView retestSelectedVariantIndexForKey:atPoint:phase:];
-[UIKBKeyplaneView addKeyToDelayedDeactivationSet:];
-[UIKBKeyplaneView keyplaneInsets];
-[UIKBKeyplaneView purgeSubviews];
-[UIKBKeyplaneView _generateRenderingContextIfNeeded];
-[UIKBKeyplaneView renderConfig];
-[UIKBKeyplaneView cancelDelayedDeactivation];
-[UIKBKeyplaneView _canDrawContent];
-[UIKBKeyplaneView cachedWidth];
-[UIKBKeyplaneView factory];
-[UIKBKeyplaneView dimKeys:];
-[UIKBKeyplaneView prepareForDisplay];
-[UIKBKeyplaneView setRenderConfig:];
-[UIKBKeyplaneView displayLayer:];
-[UIKBKeyplaneView setFactory:];
-[UIKBKeyplaneView drawContentsOfRenderers:];
-[UIKBKeyplaneView setState:forKey:];
-[UIKBKeyplaneView keyViewAnimator];
-[UIKBKeyplaneView cacheKey];
-[UIKBKeyplaneView viewForKey:];
-[UIKBKeyplaneView shouldAnimateOutKeyView:];
-[UIKBKeyplaneView useDefaultKeyplaneCacheTokenForRenderFlags:];
-[UIKBKeyplaneView viewForKey:state:];
-[UIKBKeyplaneView setKeyplaneMaskView:];
-[UIKBKeyplaneView keepNonPersistent];
-[UIKBKeyplaneView _shouldInheritScreenScaleAsContentScaleFactor];
-[UIKBKeyplaneView displaysColorImage];
-[UIKBKeyplaneView overrideScreenTraits];
-[UIKBKeyplaneView dealloc];
-[UIKBKeyplaneView cacheKeysForRenderFlags:];
-[UIKBKeyplaneView containingViewForKey:withState:wantsActiveOut:];
-[UIKBKeyplaneView cacheDeferable];
-[UIKBKeyplaneView _safeFrameForKeyViewFrame:inContainer:forKey:];
-[UIKBKeyplaneView layoutSubviews];
-[UIKBKeyplaneView hitTest:withEvent:];
-[UIKBKeyplaneView cornerMaskForKey:recursive:];
-[UIKBKeyplaneView _updateKeyplaneMaskView];
-[UIKBKeyplaneView cacheIdentifierForKey:];
-[UIKBKeyplaneView orientKeyCapForKey:orientation:];
-[UIKBKeyplaneView cacheToken];
-[UIKBKeyplaneView setDelegate:];
-[UIKBKeyplaneView cacheDeferPriority];
-[UIKBKeyplaneView setCacheToken:];
-[UIKBKeyplaneView willMoveToWindow:];
-[UIKBKeyplaneView removeFromSuperview];
-[UIKBKeyplaneView removeKeyFromDelayedDeactivationSet:];
-[UIKBKeyplaneView shouldAnimateInKeyView:];
-[UIKBKeyplaneView delegate];
-[UIKBKeyplaneView deactivateKeysWithReason:force:];
-[UIKBKeyplaneView hideKeyCaps:andControlKeysWithInteractionTypes:];
-[UIKBKeyplaneView setDefaultKeyplaneCacheToken:];
-[UIKBKeyplaneView defaultKeyplaneCacheToken];
-[UIKBKeyplaneView isPasscodeStyle];
-[UIKBKeyplaneView emojiKeyManager];
-[UIKBKeyplaneView deactivateKey:previousState:keyView:];
-[UIKBKeyplaneView setKeyViewAnimator:];
-[UIKBKeyplaneView defaultKeyplane];
-[UIKBKeyplaneView setDefaultKeyplane:];
-[UIKBKeyplaneView setEmojiKeyManager:];
-[UIKBKeyplaneView _shouldUseUnifiedKeyView:forState:];
-[UIKBKeyplaneView activateKeys];
-[UIKBKeyplaneView setState:forKey:withReason:force:];
-[UIKBKeyplaneView hideKeyCaps:];
```
