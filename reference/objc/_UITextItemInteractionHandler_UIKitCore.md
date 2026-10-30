# `_UITextItemInteractionHandler`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"_UITextInteractableItem" _item;
@"UIView<_UITextContent>" _textContentView;
{_NSRange="location"Q"length"Q} _range;
```

## Properties

```
@property (T{_NSRange=QQ},R,N,V_range) range;
@property (T@"_UITextInteractableItem",R,W,N,V_item) item;
@property (T@"UIView<_UITextContent>",R,W,N,V_textContentView) textContentView;
```

## Instance methods

```
-[_UITextItemInteractionHandler primaryAction];
-[_UITextItemInteractionHandler range];
-[_UITextItemInteractionHandler item];
-[_UITextItemInteractionHandler _defaultMenuForInteractableItem];
-[_UITextItemInteractionHandler textContentView];
-[_UITextItemInteractionHandler _canPresentMenuWithoutPrimaryAction];
-[_UITextItemInteractionHandler _defaultContextMenuConfiguration];
-[_UITextItemInteractionHandler _defaultPrimaryActionForInteractableItem];
-[_UITextItemInteractionHandler _editMenuConfiguration];
-[_UITextItemInteractionHandler _menuForInteractableItem];
-[_UITextItemInteractionHandler _preparedMenuConfigurationWithDefaultMenu:];
-[_UITextItemInteractionHandler contextMenuConfiguration];
-[_UITextItemInteractionHandler initWithItem:textContentView:];
```
