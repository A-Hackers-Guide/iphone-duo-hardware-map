# `PKPencilTextInputElementInteraction`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `PKScribbleInteractionWrapperProvider`, `UIInteraction`
- 3 instance variables, 6 properties, 7 instance methods, 1 class methods

## Instance variables

```
@"<PKScribbleInteractionWrapper>" _cachedWrapper;
@"<PKPencilTextInputElementInteractionDelegate>" _delegate;
@"UIView" _view;
```

## Properties

```
@property (T@"UIView",W,N,V_view) view;
@property (T@"<PKPencilTextInputElementInteractionDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[PKPencilTextInputElementInteraction _pencilTextInputElementInteractionInView:];
```

## Instance methods

```
-[PKPencilTextInputElementInteraction scribbleInteractionWrapper];
-[PKPencilTextInputElementInteraction setView:];
-[PKPencilTextInputElementInteraction view];
-[PKPencilTextInputElementInteraction setDelegate:];
-[PKPencilTextInputElementInteraction willMoveToView:];
-[PKPencilTextInputElementInteraction delegate];
-[PKPencilTextInputElementInteraction didMoveToView:];
```
