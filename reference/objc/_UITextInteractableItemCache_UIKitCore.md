# `_UITextInteractableItemCache`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"NSMutableSet" _attachmentItems;
@"NSMutableSet" _linkItems;
@"NSMutableSet" _tagItems;
```

## Properties

```
@property (T@"NSMutableSet",&,N,V_attachmentItems) attachmentItems;
@property (T@"NSMutableSet",&,N,V_linkItems) linkItems;
@property (T@"NSMutableSet",&,N,V_tagItems) tagItems;
```

## Instance methods

```
-[_UITextInteractableItemCache setAttachmentItems:];
-[_UITextInteractableItemCache init];
-[_UITextInteractableItemCache removeItem:];
-[_UITextInteractableItemCache itemForAttachment:range:];
-[_UITextInteractableItemCache invalidate];
-[_UITextInteractableItemCache setTagItems:];
-[_UITextInteractableItemCache itemForTag:range:];
-[_UITextInteractableItemCache addItem:];
-[_UITextInteractableItemCache _cachedItemInSet:predicate:];
-[_UITextInteractableItemCache attachmentItems];
-[_UITextInteractableItemCache setLinkItems:];
-[_UITextInteractableItemCache itemForLink:range:];
-[_UITextInteractableItemCache linkItems];
-[_UITextInteractableItemCache tagItems];
```
