# `_UISearchParticipantInteraction`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIInteraction_Private`, `UIInteraction`
- 3 instance variables, 8 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"<BSInvalidatable>" __searchParticipantToken;
@"UIView" _view;
@"UIWindowScene" __windowScene;
```

## Properties

```
@property (T@"<BSInvalidatable>",&,N,V__searchParticipantToken) _searchParticipantToken;
@property (T@"UIView",W,N,V_view) view;
@property (T@"UIWindowScene",W,N,V__windowScene) _windowScene;
@property (T@"<UIInteractionEffect>",?,&,N) interactionEffect;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UISearchParticipantInteraction _windowScene];
-[_UISearchParticipantInteraction dealloc];
-[_UISearchParticipantInteraction setView:];
-[_UISearchParticipantInteraction _didMoveFromWindow:toWindow:];
-[_UISearchParticipantInteraction view];
-[_UISearchParticipantInteraction willMoveToView:];
-[_UISearchParticipantInteraction didMoveToView:];
-[_UISearchParticipantInteraction _teardown];
-[_UISearchParticipantInteraction _searchParticipantToken];
-[_UISearchParticipantInteraction _updateActiveSearchParticipationIfNeeded];
-[_UISearchParticipantInteraction set_searchParticipantToken:];
-[_UISearchParticipantInteraction set_windowScene:];
```
