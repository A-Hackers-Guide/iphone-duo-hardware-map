# `UITextDraggableObject`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 8 instance methods, 1 class methods

## Instance variables

```
@"NSItemProvider" _itemProvider;
@"UITextRange" _range;
@? _targetedPreviewProvider;
@? _previewProvider;
```

## Properties

```
@property (T@"NSItemProvider",&,N,V_itemProvider) itemProvider;
@property (T@"UITextRange",&,N,V_range) range;
@property (T@?,C,N,V_targetedPreviewProvider) targetedPreviewProvider;
@property (T@?,C,N,V_previewProvider) previewProvider;
```

## Class methods

```
+[UITextDraggableObject draggableObjectWithItemProvider:fromRange:];
```

## Instance methods

```
-[UITextDraggableObject range];
-[UITextDraggableObject setPreviewProvider:];
-[UITextDraggableObject setRange:];
-[UITextDraggableObject itemProvider];
-[UITextDraggableObject previewProvider];
-[UITextDraggableObject setItemProvider:];
-[UITextDraggableObject setTargetedPreviewProvider:];
-[UITextDraggableObject targetedPreviewProvider];
```
