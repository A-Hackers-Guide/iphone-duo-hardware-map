# `_UIContextMenuBasicMorphPresentationAnimation`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIContextMenuPresentationAnimation`
- 10 instance variables, 9 properties, 50 instance methods, 0 class methods

## Instance variables

```
B _isSingleItemMenu;
@"UITargetedPreview" _sourcePreview;
@"_UIPortalView" _reparentingPortalView;
@"_UIContextMenuReparentingContainerView" _reparentingContainerView;
@"UIViewFloatAnimatableProperty" _animationProgress;
@? _reparentingAnimationBlock;
@? _accessoryAnimationBlock;
@"_UIContextMenuLayoutArbiterOutput" _expandedLayout;
@"_UIGroupCompletion" _groupCompletion;
@"UITargetedPreview" _stashedDismissalPreview;
```

## Properties

```
@property (TB,N,V_isSingleItemMenu) isSingleItemMenu;
@property (T@"_UIPortalView",&,N,V_reparentingPortalView) reparentingPortalView;
@property (T@"_UIContextMenuReparentingContainerView",&,N,V_reparentingContainerView) reparentingContainerView;
@property (T@"UIViewFloatAnimatableProperty",&,N,V_animationProgress) animationProgress;
@property (T@?,C,N,V_reparentingAnimationBlock) reparentingAnimationBlock;
@property (T@?,C,N,V_accessoryAnimationBlock) accessoryAnimationBlock;
@property (T@"_UIContextMenuLayoutArbiterOutput",&,N,V_expandedLayout) expandedLayout;
@property (T@"_UIGroupCompletion",&,N,V_groupCompletion) groupCompletion;
@property (T@"UITargetedPreview",&,N,V_stashedDismissalPreview) stashedDismissalPreview;
```

## Instance methods

```
-[_UIContextMenuBasicMorphPresentationAnimation addCompletion:];
-[_UIContextMenuBasicMorphPresentationAnimation prepareTransitionToView:];
-[_UIContextMenuBasicMorphPresentationAnimation accessoryAnimationBlock];
-[_UIContextMenuBasicMorphPresentationAnimation initWithUIController:];
-[_UIContextMenuBasicMorphPresentationAnimation transitionDidEnd:];
-[_UIContextMenuBasicMorphPresentationAnimation setStashedDismissalPreview:];
-[_UIContextMenuBasicMorphPresentationAnimation _installAccessories];
-[_UIContextMenuBasicMorphPresentationAnimation _targetedPreviewForDismissalAnimation];
-[_UIContextMenuBasicMorphPresentationAnimation _secondarySourcePreviews];
-[_UIContextMenuBasicMorphPresentationAnimation _updateAccessoryAttachment:];
-[_UIContextMenuBasicMorphPresentationAnimation sourcePreview];
-[_UIContextMenuBasicMorphPresentationAnimation animationProgress];
-[_UIContextMenuBasicMorphPresentationAnimation setAccessoryAnimationBlock:];
-[_UIContextMenuBasicMorphPresentationAnimation _accessoryViews];
-[_UIContextMenuBasicMorphPresentationAnimation groupCompletion];
-[_UIContextMenuBasicMorphPresentationAnimation _isDismissingToDrag];
-[_UIContextMenuBasicMorphPresentationAnimation stashedDismissalPreview];
-[_UIContextMenuBasicMorphPresentationAnimation _backgroundView];
-[_UIContextMenuBasicMorphPresentationAnimation _containerView];
-[_UIContextMenuBasicMorphPresentationAnimation _prepareAnimatablePropertyBasedAnimations];
-[_UIContextMenuBasicMorphPresentationAnimation isSingleItemMenu];
-[_UIContextMenuBasicMorphPresentationAnimation setAnimationProgress:];
-[_UIContextMenuBasicMorphPresentationAnimation setSourcePreview:];
-[_UIContextMenuBasicMorphPresentationAnimation _hasVisibleBackground];
-[_UIContextMenuBasicMorphPresentationAnimation performTransition];
-[_UIContextMenuBasicMorphPresentationAnimation _setBackgroundVisible:];
-[_UIContextMenuBasicMorphPresentationAnimation _shouldAnimateBackgroundEffects];
-[_UIContextMenuBasicMorphPresentationAnimation _actuallyPerformTransition];
-[_UIContextMenuBasicMorphPresentationAnimation _anchorTransitionViewToTargetedPreview:];
-[_UIContextMenuBasicMorphPresentationAnimation _dismissalPreviewForSecondaryItemPreview:];
-[_UIContextMenuBasicMorphPresentationAnimation _dismissedMenuLayoutForPresentedLayout:previewLayout:anchor:];
-[_UIContextMenuBasicMorphPresentationAnimation _menuView];
-[_UIContextMenuBasicMorphPresentationAnimation _performReduceMotionAppearanceTransition];
-[_UIContextMenuBasicMorphPresentationAnimation _performReduceMotionDisappearanceTransition];
-[_UIContextMenuBasicMorphPresentationAnimation _platterTransitionView];
-[_UIContextMenuBasicMorphPresentationAnimation _platterView];
-[_UIContextMenuBasicMorphPresentationAnimation _prepareOverallAnimationCompletion];
-[_UIContextMenuBasicMorphPresentationAnimation _prepareReparentingAnimationWithDismissalTarget:];
-[_UIContextMenuBasicMorphPresentationAnimation _presentation_applyBackgroundEffectWithProgress:];
-[_UIContextMenuBasicMorphPresentationAnimation expandedLayout];
-[_UIContextMenuBasicMorphPresentationAnimation initWithUIController:asDismissal:];
-[_UIContextMenuBasicMorphPresentationAnimation reparentingAnimationBlock];
-[_UIContextMenuBasicMorphPresentationAnimation reparentingContainerView];
-[_UIContextMenuBasicMorphPresentationAnimation reparentingPortalView];
-[_UIContextMenuBasicMorphPresentationAnimation setExpandedLayout:];
-[_UIContextMenuBasicMorphPresentationAnimation setGroupCompletion:];
-[_UIContextMenuBasicMorphPresentationAnimation setIsSingleItemMenu:];
-[_UIContextMenuBasicMorphPresentationAnimation setReparentingAnimationBlock:];
-[_UIContextMenuBasicMorphPresentationAnimation setReparentingContainerView:];
-[_UIContextMenuBasicMorphPresentationAnimation setReparentingPortalView:];
```
