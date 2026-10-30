# `UITextLinkInteraction`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UITextItemInteractionInteraction`
- 2 instance variables, 4 properties, 7 instance methods, 1 class methods

## Instance variables

```
@"UIContextMenuInteraction" _contextMenuInteraction;
@"_UITextInteractableItemCache" _textInteractableItemCache;
```

## Properties

```
@property (T@"<UIContextMenuInteractionDelegate>",R,W,N) contextMenuDelegateProxy;
@property (T@"UIEditMenuInteraction",R,N) editMenuInteraction;
@property (T@"UIContextMenuInteraction",R,N,V_contextMenuInteraction) contextMenuInteraction;
@property (T@"_UITextInteractableItemCache",&,N,V_textInteractableItemCache) _textInteractableItemCache;
```

## Class methods

```
+[UITextLinkInteraction interactionWithShouldProxyContextMenuDelegate:];
```

## Instance methods

```
-[UITextLinkInteraction _textInteractableItemAtPoint:precision:itemInteractableView:cache:];
-[UITextLinkInteraction editMenuInteraction];
-[UITextLinkInteraction contextMenuInteraction];
-[UITextLinkInteraction contextMenuDelegateProxy];
-[UITextLinkInteraction _textInteractableItemCache];
-[UITextLinkInteraction set_textInteractableItemCache:];
-[UITextLinkInteraction dismissEditMenuOnSelectionChangeIfNecessary];
```
