# `UITextDragRequest`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UITextDragRequest`
- 5 instance variables, 9 properties, 8 instance methods, 0 class methods

## Instance variables

```
B _selected;
@"UITextRange" _dragRange;
@"NSArray" _existingItems;
@"<UIDragSession>" _dragSession;
@"NSArray" _suggestedItems;
```

## Properties

```
@property (T@"NSArray",&,N,V_suggestedItems) suggestedItems;
@property (TB,N,GisSelected,V_selected) selected;
@property (T@"UITextRange",R,N,V_dragRange) dragRange;
@property (T@"NSArray",R,N,V_existingItems) existingItems;
@property (T@"<UIDragSession>",R,N,V_dragSession) dragSession;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UITextDragRequest setSelected:];
-[UITextDragRequest dragSession];
-[UITextDragRequest isSelected];
-[UITextDragRequest dragRange];
-[UITextDragRequest existingItems];
-[UITextDragRequest initWithRange:inSession:];
-[UITextDragRequest setSuggestedItems:];
-[UITextDragRequest suggestedItems];
```
