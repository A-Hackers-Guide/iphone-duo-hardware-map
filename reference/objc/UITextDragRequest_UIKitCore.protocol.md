# `UITextDragRequest` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 5 properties, 5 instance methods, 0 class methods

## Properties

```
@property (T@"UITextRange",R,N) dragRange;
@property (T@"NSArray",R,N) suggestedItems;
@property (T@"NSArray",R,N) existingItems;
@property (TB,R,N,GisSelected) selected;
@property (T@"<UIDragSession>",R,N) dragSession;
```

## Instance methods

```
-[UITextDragRequest dragSession];
-[UITextDragRequest isSelected];
-[UITextDragRequest dragRange];
-[UITextDragRequest existingItems];
-[UITextDragRequest suggestedItems];
```
