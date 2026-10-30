# `UIKBKeyplaneLayout` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 3 properties, 48 instance methods, 0 class methods

## Properties

```
@property (T@"UIKBRenderingContext",&,N) renderingContext;
@property (T@"UIKBRenderConfig",&,N) renderConfig;
@property (TB,N) suppressDrawing;
```

## Instance methods

```
-[UIKBKeyplaneLayout isSplit];
-[UIKBKeyplaneLayout keyplaneMaskView];
-[UIKBKeyplaneLayout changingSelectedVariantForKey:atPoint:isDragging:];
-[UIKBKeyplaneLayout updateToSize:];
-[UIKBKeyplaneLayout rightSplitSize];
-[UIKBKeyplaneLayout setOverrideScreenTraits:];
-[UIKBKeyplaneLayout setKeyplane:];
-[UIKBKeyplaneLayout setDockHidesItemsOverlappingEmoji:];
-[UIKBKeyplaneLayout deactivateAdaptiveKey:];
-[UIKBKeyplaneLayout transitionWillFinishWithProgress:completion:];
-[UIKBKeyplaneLayout purgeFactory];
-[UIKBKeyplaneLayout existingVariantsKeyViewForKey:];
-[UIKBKeyplaneLayout deactivateKeys];
-[UIKBKeyplaneLayout activeKeyViews];
-[UIKBKeyplaneLayout showSplitKeyplane:animated:];
-[UIKBKeyplaneLayout currentHandBias];
-[UIKBKeyplaneLayout suppressDrawing];
-[UIKBKeyplaneLayout validForKeyplane:withVisualStyle:];
-[UIKBKeyplaneLayout leftSplitSize];
-[UIKBKeyplaneLayout updateVariantSelectorFramesForKey:];
-[UIKBKeyplaneLayout setKeyboardBias:];
-[UIKBKeyplaneLayout stateForKey:];
-[UIKBKeyplaneLayout fullHeightForDockedKeyboard];
-[UIKBKeyplaneLayout setRemoteKeyViewProvider:];
-[UIKBKeyplaneLayout supportsSplit];
-[UIKBKeyplaneLayout setOverrideScreenTraits:currentKeyboardMode:];
-[UIKBKeyplaneLayout hitTestVariantKeyAtPoint:];
-[UIKBKeyplaneLayout supportsStateAnimations];
-[UIKBKeyplaneLayout renderingContext];
-[UIKBKeyplaneLayout purgeLayerContents];
-[UIKBKeyplaneLayout setRenderingContext:];
-[UIKBKeyplaneLayout updateFrameForKey:];
-[UIKBKeyplaneLayout setSuppressDrawing:];
-[UIKBKeyplaneLayout isDynamicLayout];
-[UIKBKeyplaneLayout finishedSelectingVariantForKey:atPoint:];
-[UIKBKeyplaneLayout purgeKeyViews];
-[UIKBKeyplaneLayout purgeActiveKeyViews];
-[UIKBKeyplaneLayout retestSelectedVariantIndexForKey:atPoint:phase:];
-[UIKBKeyplaneLayout addKeyToDelayedDeactivationSet:];
-[UIKBKeyplaneLayout keyplaneInsets];
-[UIKBKeyplaneLayout purgeSubviews];
-[UIKBKeyplaneLayout renderConfig];
-[UIKBKeyplaneLayout factory];
-[UIKBKeyplaneLayout dimKeys:];
-[UIKBKeyplaneLayout prepareForDisplay];
-[UIKBKeyplaneLayout setRenderConfig:];
-[UIKBKeyplaneLayout setState:forKey:];
-[UIKBKeyplaneLayout viewForKey:];
```
