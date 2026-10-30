# `_UITextInteractableItem`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 14 instance variables, 16 properties, 41 instance methods, 1 class methods

## Instance variables

```
{?="primaryAction"b1"menu"b1} _requested;
@"UIAction" _primaryAction;
@"<_UIInvalidatable>" _selectionHiddenAssertion;
@"UITextItem" _representedTextItem;
@"_UITextItemInteractionHandler" _itemHandler;
@"UIView<_UITextItemInteracting>" _textItemInteractingView;
@"UITextItemMenuConfiguration" _preparedMenuConfiguration;
@"UIContextMenuInteraction" _contextMenuInteraction;
@"UIEditMenuInteraction" _editMenuInteraction;
@"<_UITextContent>" _textContent;
@"_UITextItemHighlightView" _highlightView;
@"UIAction" _defaultAction;
@"UINotificationFeedbackGenerator" _feedbackGenerator;
{CGPoint="x"d"y"d} _location;
```

## Properties

```
@property (T@"<_UITextContent>",W,N,V_textContent) textContent;
@property (T@"_UITextItemInteractionHandler",&,N,V_itemHandler) itemHandler;
@property (T@"_UITextItemHighlightView",R,N,V_highlightView) highlightView;
@property (T@"UIAction",R,N,V_defaultAction) defaultAction;
@property (T@"UINotificationFeedbackGenerator",R,N,V_feedbackGenerator) feedbackGenerator;
@property (T{_NSRange=QQ},R,N) range;
@property (T{CGPoint=dd},R,N,V_location) location;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) bounds;
@property (T@"NSArray",R,N) rects;
@property (T@"UITextItem",R,N,V_representedTextItem) representedTextItem;
@property (T@"UIView<_UITextItemInteracting>",R,W,N,V_textItemInteractingView) textItemInteractingView;
@property (T@"UITextItemMenuConfiguration",R,N,V_preparedMenuConfiguration) preparedMenuConfiguration;
@property (Tq,R,N) preferredMenuExpression;
@property (TQ,R,N) preferredElementDisplayMode;
@property (T@"UIContextMenuInteraction",W,N,V_contextMenuInteraction) contextMenuInteraction;
@property (T@"UIEditMenuInteraction",W,N,V_editMenuInteraction) editMenuInteraction;
```

## Class methods

```
+[_UITextInteractableItem itemForTextItem:view:location:];
```

## Instance methods

```
-[_UITextInteractableItem textContent];
-[_UITextInteractableItem feedbackGenerator];
-[_UITextInteractableItem range];
-[_UITextInteractableItem location];
-[_UITextInteractableItem defaultAction];
-[_UITextInteractableItem dealloc];
-[_UITextInteractableItem preferredElementDisplayMode];
-[_UITextInteractableItem setContextMenuInteraction:];
-[_UITextInteractableItem setTextContent:];
-[_UITextInteractableItem editMenuInteraction];
-[_UITextInteractableItem contextMenuInteraction];
-[_UITextInteractableItem bounds];
-[_UITextInteractableItem highlight];
-[_UITextInteractableItem isEqual:];
-[_UITextInteractableItem highlightView];
-[_UITextInteractableItem _allowHighlight];
-[_UITextInteractableItem setItemHandler:];
-[_UITextInteractableItem _actionPresentsMenu:];
-[_UITextInteractableItem _allowInteraction:];
-[_UITextInteractableItem _initWithTextItem:view:location:];
-[_UITextInteractableItem _showsPreviewByDefault];
-[_UITextInteractableItem _warnForInvalidAction];
-[_UITextInteractableItem canInvokeDefaultAction];
-[_UITextInteractableItem contextMenuConfiguration];
-[_UITextInteractableItem defaultActionPresentsMenu];
-[_UITextInteractableItem hasPrimaryAction];
-[_UITextInteractableItem invokeDefaultAction];
-[_UITextInteractableItem isAttachmentItem];
-[_UITextInteractableItem isLinkItem];
-[_UITextInteractableItem isTagItem];
-[_UITextInteractableItem itemHandler];
-[_UITextInteractableItem preferredMenuExpression];
-[_UITextInteractableItem prepareMenuConfigurationWithDefaultMenu:];
-[_UITextInteractableItem preparedMenuConfiguration];
-[_UITextInteractableItem preparedPrimaryActionWithDefaultAction:];
-[_UITextInteractableItem rects];
-[_UITextInteractableItem representedTextItem];
-[_UITextInteractableItem setEditMenuInteraction:];
-[_UITextInteractableItem showsMenuPreview];
-[_UITextInteractableItem textItemInteractingView];
-[_UITextInteractableItem unhighlight];
```
