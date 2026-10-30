# `_UIContextMenuPresentationAnimation`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIClickPresentationTransition`
- 6 instance variables, 11 properties, 18 instance methods, 0 class methods

## Instance variables

```
B _isDismissTransition;
@"UITargetedPreview" _sourcePreview;
@"_UIContextMenuUIController" _uiController;
@"_UIContextMenuAnimator" _presentationAlongsideAnimator;
@"_UIContextMenuAnimator" _dismissalAlongsideAnimator;
Q _dismissalStyle;
```

## Properties

```
@property (T@"UITargetedPreview",C,N,V_sourcePreview) sourcePreview;
@property (T@"_UIContextMenuUIController",R,N,V_uiController) uiController;
@property (T@"_UIContextMenuAnimator",&,N,V_presentationAlongsideAnimator) presentationAlongsideAnimator;
@property (T@"_UIContextMenuAnimator",&,N,V_dismissalAlongsideAnimator) dismissalAlongsideAnimator;
@property (TB,N,V_isDismissTransition) isDismissTransition;
@property (TQ,N,V_dismissalStyle) dismissalStyle;
@property (T@"UIViewPropertyAnimator",?,R,N) customAnimator;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIContextMenuPresentationAnimation addCompletion:];
-[_UIContextMenuPresentationAnimation uiController];
-[_UIContextMenuPresentationAnimation prepareTransitionToView:];
-[_UIContextMenuPresentationAnimation initWithUIController:];
-[_UIContextMenuPresentationAnimation transitionDidEnd:];
-[_UIContextMenuPresentationAnimation retargetDismissingMenuToPreview:];
-[_UIContextMenuPresentationAnimation sourcePreview];
-[_UIContextMenuPresentationAnimation setSourcePreview:];
-[_UIContextMenuPresentationAnimation performTransition];
-[_UIContextMenuPresentationAnimation dismissalAlongsideAnimator];
-[_UIContextMenuPresentationAnimation dismissalStyle];
-[_UIContextMenuPresentationAnimation isDismissTransition];
-[_UIContextMenuPresentationAnimation performTransitionFromView:toView:containerView:];
-[_UIContextMenuPresentationAnimation presentationAlongsideAnimator];
-[_UIContextMenuPresentationAnimation setDismissalAlongsideAnimator:];
-[_UIContextMenuPresentationAnimation setDismissalStyle:];
-[_UIContextMenuPresentationAnimation setIsDismissTransition:];
-[_UIContextMenuPresentationAnimation setPresentationAlongsideAnimator:];
```
