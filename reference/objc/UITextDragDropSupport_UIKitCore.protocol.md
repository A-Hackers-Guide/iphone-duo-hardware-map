# `UITextDragDropSupport` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 4 properties, 7 instance methods, 0 class methods

## Properties

```
@property (T@"UIDragInteraction",R,N) dragInteraction;
@property (T@"UIDropInteraction",R,N) dropInteraction;
@property (TB,R,N,GisDragActive) dragActive;
@property (TB,R,N,GisDropActive) dropActive;
```

## Instance methods

```
-[UITextDragDropSupport isDragActive];
-[UITextDragDropSupport notifyTextInteraction];
-[UITextDragDropSupport dropInteraction];
-[UITextDragDropSupport dragInteraction];
-[UITextDragDropSupport isDropActive];
-[UITextDragDropSupport invalidateDropCaret];
-[UITextDragDropSupport accessibilityCanDrag];
```
