# `UIDraggingBeginningSessionConfiguration`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIDraggingSessionConfiguration`
- 3 instance variables, 3 properties, 4 instance methods, 4 class methods

## Instance variables

```
q _dataOwner;
@"UIView" _sourceView;
@"NSArray" _items;
```

## Properties

```
@property (Tq,R,N,V_dataOwner) dataOwner;
@property (T@"UIView",R,N,V_sourceView) sourceView;
@property (T@"NSArray",R,N,V_items) items;
```

## Class methods

```
+[UIDraggingBeginningSessionConfiguration configurationWithItems:dataOwner:initialCentroidInSourceWindow:requiredContextIds:sourceView:accessibilityEndpoint:];
+[UIDraggingBeginningSessionConfiguration configurationWithItems:dataOwner:pointerTouch:requiredContextIds:sourceView:];
+[UIDraggingBeginningSessionConfiguration configurationWithItems:dataOwner:touches:requiredContextIds:sourceView:];
+[UIDraggingBeginningSessionConfiguration configurationWithItems:initialCentroidInSourceWindow:sourceView:];
```

## Instance methods

```
-[UIDraggingBeginningSessionConfiguration items];
-[UIDraggingBeginningSessionConfiguration sourceView];
-[UIDraggingBeginningSessionConfiguration dataOwner];
-[UIDraggingBeginningSessionConfiguration initWithItems:dataOwner:requiredContextIds:sourceView:];
```
