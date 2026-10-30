# `UIInputViewSetPlacementOwner` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 11 properties, 14 instance methods, 0 class methods

## Properties

```
@property (TB,R) keyboardController;
@property (T@"UIInputViewSetPlacement",R) placement;
@property (T@"<UIInputViewSetPlacementApplicator>",R,N) applicator;
@property (T@"UIInputViewSet",R) inputViewSet;
@property (T{UIEdgeInsets=dddd},R) inputViewPadding;
@property (T@"UIView",R) hostView;
@property (T@"UIView",R) containerView;
@property (TB) hideInputViewBackdrops;
@property (Tq,R) inputViewBackdropStyle;
@property (TB) hideInputView;
@property (T@"TUIInputAssistantHostView",R) inputAssistantHostView;
```

## Instance methods

```
-[UIInputViewSetPlacementOwner hostView];
-[UIInputViewSetPlacementOwner inputViewSet];
-[UIInputViewSetPlacementOwner hideInputView];
-[UIInputViewSetPlacementOwner placement];
-[UIInputViewSetPlacementOwner updateCombinedBackdropView];
-[UIInputViewSetPlacementOwner inputViewPadding];
-[UIInputViewSetPlacementOwner applicator];
-[UIInputViewSetPlacementOwner containerView];
-[UIInputViewSetPlacementOwner setHideInputViewBackdrops:];
-[UIInputViewSetPlacementOwner inputViewBackdropStyle];
-[UIInputViewSetPlacementOwner hideInputViewBackdrops];
-[UIInputViewSetPlacementOwner inputAssistantHostView];
-[UIInputViewSetPlacementOwner keyboardController];
-[UIInputViewSetPlacementOwner setHideInputView:];
```
