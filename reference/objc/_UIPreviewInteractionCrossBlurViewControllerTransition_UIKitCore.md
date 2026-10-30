# `_UIPreviewInteractionCrossBlurViewControllerTransition`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIPreviewInteractionViewControllerTransition`
- 3 instance variables, 6 properties, 9 instance methods, 0 class methods

## Instance variables

```
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _initialPlatterRect;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _finalPlatterRect;
B _dismissTransition;
```

## Properties

```
@property (TB,N,GisDismissTransition,V_dismissTransition) dismissTransition;
@property (T@"UITargetedPreview",?,C,N) sourcePreview;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIPreviewInteractionCrossBlurViewControllerTransition transitionDidEnd:];
-[_UIPreviewInteractionCrossBlurViewControllerTransition isDismissTransition];
-[_UIPreviewInteractionCrossBlurViewControllerTransition performAppearanceTransitionFromView:toView:containerView:];
-[_UIPreviewInteractionCrossBlurViewControllerTransition performDisappearanceTransitionFromView:toView:containerView:];
-[_UIPreviewInteractionCrossBlurViewControllerTransition performTransitionFromView:toView:containerView:];
-[_UIPreviewInteractionCrossBlurViewControllerTransition prepareAppearanceTransitionFromView:toView:containerView:];
-[_UIPreviewInteractionCrossBlurViewControllerTransition prepareDisappearanceTransitionFromView:toView:containerView:];
-[_UIPreviewInteractionCrossBlurViewControllerTransition prepareTransitionFromView:toView:containerView:];
-[_UIPreviewInteractionCrossBlurViewControllerTransition setDismissTransition:];
```
