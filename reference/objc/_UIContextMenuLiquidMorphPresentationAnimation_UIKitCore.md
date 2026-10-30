# `_UIContextMenuLiquidMorphPresentationAnimation`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIContextMenuPresentationAnimation`
- 7 instance variables, 18 properties, 40 instance methods, 0 class methods

## Instance variables

```
@"_TtC5UIKit23_UILiquidMorphAnimation" morphAnimation;
@"UITargetedPreview" outgoingAnimationPreview;
@"_UIContextMenuLayoutArbiterOutput" presentedLayout;
$__lazy_storage_$_animationProgress;
? accessoryAnimationBlock;
@"UITargetedPreview" stashedDismissalPreview;
@"UITargetedPreview" stashedDismissalPivot;
```

## Properties

```
@property (T@"UITargetedPreview",N,&) sourcePreview;
@property (T@"_TtC5UIKit23_UILiquidMorphAnimation",N,&,VmorphAnimation) morphAnimation;
@property (T@"UITargetedPreview",N,&,VoutgoingAnimationPreview) outgoingAnimationPreview;
@property (T@"_UIContextMenuLayoutArbiterOutput",N,&,VpresentedLayout) presentedLayout;
@property (T@"UIViewFloatAnimatableProperty",N,&) animationProgress;
@property (T@?,N,C) accessoryAnimationBlock;
@property (T@"UITargetedPreview",N,&,VstashedDismissalPreview) stashedDismissalPreview;
@property (T@"UITargetedPreview",N,&,VstashedDismissalPivot) stashedDismissalPivot;
@property (T@"_UIContentPlatterView",N,R) contentPlatterView;
@property (T@"UITargetedPreview",N,R) resolvedSourcePreview;
@property (TB,N,R) isCompactMenu;
@property (TB,N,R) sourcePreviewMorphsToMenu;
@property (T@"UITargetedPreview",N,R) morphPreviewFromAttachmentPoint;
@property (T@"_UIContextMenuPlatformMetrics",N,R) _currentPlatformMetrics;
@property (TB,N,R) _hasVisibleBackground;
@property (TB,N,R) _isDismissingToDrag;
@property (T@"UITargetedPreview",N,R) _targetedPreviewForDismissalAnimation;
@property (T@"NSArray",N,R) _accessoryViews;
```

## Instance methods

```
-[_UIContextMenuLiquidMorphPresentationAnimation addCompletion:];
-[_UIContextMenuLiquidMorphPresentationAnimation _dismissedMenuLayout];
-[_UIContextMenuLiquidMorphPresentationAnimation setPresentedLayout:];
-[_UIContextMenuLiquidMorphPresentationAnimation prepareTransitionToView:];
-[_UIContextMenuLiquidMorphPresentationAnimation _currentPlatformMetrics];
-[_UIContextMenuLiquidMorphPresentationAnimation accessoryAnimationBlock];
-[_UIContextMenuLiquidMorphPresentationAnimation initWithUIController:];
-[_UIContextMenuLiquidMorphPresentationAnimation transitionDidEnd:];
-[_UIContextMenuLiquidMorphPresentationAnimation retargetDismissingMenuToPreview:];
-[_UIContextMenuLiquidMorphPresentationAnimation setStashedDismissalPreview:];
-[_UIContextMenuLiquidMorphPresentationAnimation _installAccessories];
-[_UIContextMenuLiquidMorphPresentationAnimation stashedDismissalPivot];
-[_UIContextMenuLiquidMorphPresentationAnimation _targetedPreviewForDismissalAnimation];
-[_UIContextMenuLiquidMorphPresentationAnimation init];
-[_UIContextMenuLiquidMorphPresentationAnimation morphAnimation];
-[_UIContextMenuLiquidMorphPresentationAnimation _updateAccessoryAttachment:];
-[_UIContextMenuLiquidMorphPresentationAnimation sourcePreview];
-[_UIContextMenuLiquidMorphPresentationAnimation animationProgress];
-[_UIContextMenuLiquidMorphPresentationAnimation setAccessoryAnimationBlock:];
-[_UIContextMenuLiquidMorphPresentationAnimation _accessoryViews];
-[_UIContextMenuLiquidMorphPresentationAnimation presentedLayout];
-[_UIContextMenuLiquidMorphPresentationAnimation _isDismissingToDrag];
-[_UIContextMenuLiquidMorphPresentationAnimation stashedDismissalPreview];
-[_UIContextMenuLiquidMorphPresentationAnimation contentPlatterView];
-[_UIContextMenuLiquidMorphPresentationAnimation sourcePreviewMorphsToMenu];
-[_UIContextMenuLiquidMorphPresentationAnimation setOutgoingAnimationPreview:];
-[_UIContextMenuLiquidMorphPresentationAnimation _secondaryDismissalPreviewFor:];
-[_UIContextMenuLiquidMorphPresentationAnimation setMorphAnimation:];
-[_UIContextMenuLiquidMorphPresentationAnimation _prepareAnimatablePropertyBasedAnimations];
-[_UIContextMenuLiquidMorphPresentationAnimation resolvedSourcePreview];
-[_UIContextMenuLiquidMorphPresentationAnimation setAnimationProgress:];
-[_UIContextMenuLiquidMorphPresentationAnimation initWithUIController:previousAnimation:];
-[_UIContextMenuLiquidMorphPresentationAnimation setSourcePreview:];
-[_UIContextMenuLiquidMorphPresentationAnimation _hasVisibleBackground];
-[_UIContextMenuLiquidMorphPresentationAnimation performTransition];
-[_UIContextMenuLiquidMorphPresentationAnimation outgoingAnimationPreview];
-[_UIContextMenuLiquidMorphPresentationAnimation morphPreviewFromAttachmentPoint];
-[_UIContextMenuLiquidMorphPresentationAnimation setStashedDismissalPivot:];
-[_UIContextMenuLiquidMorphPresentationAnimation isCompactMenu];
-[_UIContextMenuLiquidMorphPresentationAnimation _setBackgroundVisible:];
```
