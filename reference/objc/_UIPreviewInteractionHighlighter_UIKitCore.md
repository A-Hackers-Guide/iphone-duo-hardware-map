# `_UIPreviewInteractionHighlighter`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIInteractionEffect`
- 26 instance variables, 18 properties, 41 instance methods, 0 class methods

## Instance variables

```
@"UIView" _view;
@"<_UIInteractiveHighlighting>" _interactiveHighlightView;
@"UIControl" _compatibilityHighlightView;
@"_UIInteractiveHighlightEffect" _interactiveHighlightEffect;
@"NSArray" _accessoryHighlightEffects;
@"_UIInteractiveHighlightEffect" _presentationControllerHighlightEffect;
@"<UIInteraction>" _interaction;
B _active;
B _animatesContentEffects;
@"NSUUID" _contentAnimationIdentifier;
B _animatesBackgroundEffects;
q _preferredAnimationStyle;
d _preferredMinimumScale;
d _preferredMaximumScale;
B _shouldApplyEffectsOnProxyView;
B _shouldApplyContentEffects;
B _shouldApplyBackgroundEffects;
B _shouldEndWithCancelAnimation;
B _shouldTransferViewOwnership;
B _cancelsInteractionWhenScrolling;
@? _completionBlock;
Q _clickEffectPhase;
@? _privateCompletionBlock;
@"UIView" _customContainerView;
@"UIView" _customBackgroundEffectView;
@? _backgroundEffectApplyBlock;
```

## Properties

```
@property (TB,N,V_shouldApplyEffectsOnProxyView) shouldApplyEffectsOnProxyView;
@property (TB,N,V_shouldEndWithCancelAnimation) shouldEndWithCancelAnimation;
@property (TQ,N,V_clickEffectPhase) clickEffectPhase;
@property (T@"_UIInteractiveHighlightEffect",R,N) interactiveHighlightEffect;
@property (T@?,C,N,V_privateCompletionBlock) privateCompletionBlock;
@property (T@"UIView",W,N,V_customContainerView) customContainerView;
@property (T@"UIView",&,N,V_customBackgroundEffectView) customBackgroundEffectView;
@property (TB,N,V_shouldTransferViewOwnership) shouldTransferViewOwnership;
@property (TB,N,V_shouldApplyContentEffects) shouldApplyContentEffects;
@property (TB,N,V_shouldApplyBackgroundEffects) shouldApplyBackgroundEffects;
@property (TB,N,V_cancelsInteractionWhenScrolling) cancelsInteractionWhenScrolling;
@property (T@?,C,N,V_backgroundEffectApplyBlock) backgroundEffectApplyBlock;
@property (T@"UIView",R,W,N,V_view) view;
@property (T@?,C,N,V_completionBlock) completionBlock;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIPreviewInteractionHighlighter setCompletionBlock:];
-[_UIPreviewInteractionHighlighter completionBlock];
-[_UIPreviewInteractionHighlighter initWithView:];
-[_UIPreviewInteractionHighlighter interaction:didChangeWithContext:];
-[_UIPreviewInteractionHighlighter view];
-[_UIPreviewInteractionHighlighter cancelsInteractionWhenScrolling];
-[_UIPreviewInteractionHighlighter setShouldTransferViewOwnership:];
-[_UIPreviewInteractionHighlighter _animateAlongsideViewControllerPresentationDismiss];
-[_UIPreviewInteractionHighlighter _animateForDelayedViewControllerPresentation];
-[_UIPreviewInteractionHighlighter _applyHighlightEffectsToViewControllerDuringCancellation:];
-[_UIPreviewInteractionHighlighter _delayedViewControllerPresentationDidCancel];
-[_UIPreviewInteractionHighlighter _finalizeAfterInteraction];
-[_UIPreviewInteractionHighlighter _finalizeAfterInteractionIfNeeded];
-[_UIPreviewInteractionHighlighter _prepareAccessoryViewsForScrollView:environment:];
-[_UIPreviewInteractionHighlighter _prepareContentEffectsForInteraction:];
-[_UIPreviewInteractionHighlighter _prepareForInteraction:];
-[_UIPreviewInteractionHighlighter _prepareForViewControllerPresentation:];
-[_UIPreviewInteractionHighlighter _setHighlighted:forViewIfNeeded:];
-[_UIPreviewInteractionHighlighter _updateFromInteraction:fractionComplete:ended:];
-[_UIPreviewInteractionHighlighter _viewControllerPresentationDidEnd];
-[_UIPreviewInteractionHighlighter backgroundEffectApplyBlock];
-[_UIPreviewInteractionHighlighter clickEffectPhase];
-[_UIPreviewInteractionHighlighter customBackgroundEffectView];
-[_UIPreviewInteractionHighlighter customContainerView];
-[_UIPreviewInteractionHighlighter interactiveHighlightEffect];
-[_UIPreviewInteractionHighlighter privateCompletionBlock];
-[_UIPreviewInteractionHighlighter setBackgroundEffectApplyBlock:];
-[_UIPreviewInteractionHighlighter setCancelsInteractionWhenScrolling:];
-[_UIPreviewInteractionHighlighter setClickEffectPhase:];
-[_UIPreviewInteractionHighlighter setCustomBackgroundEffectView:];
-[_UIPreviewInteractionHighlighter setCustomContainerView:];
-[_UIPreviewInteractionHighlighter setPrivateCompletionBlock:];
-[_UIPreviewInteractionHighlighter setShouldApplyBackgroundEffects:];
-[_UIPreviewInteractionHighlighter setShouldApplyContentEffects:];
-[_UIPreviewInteractionHighlighter setShouldApplyEffectsOnProxyView:];
-[_UIPreviewInteractionHighlighter setShouldEndWithCancelAnimation:];
-[_UIPreviewInteractionHighlighter shouldApplyBackgroundEffects];
-[_UIPreviewInteractionHighlighter shouldApplyContentEffects];
-[_UIPreviewInteractionHighlighter shouldApplyEffectsOnProxyView];
-[_UIPreviewInteractionHighlighter shouldEndWithCancelAnimation];
-[_UIPreviewInteractionHighlighter shouldTransferViewOwnership];
```
