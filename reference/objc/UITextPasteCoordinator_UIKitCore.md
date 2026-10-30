# `UITextPasteCoordinator`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 1 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"NSMutableArray" _items;
@"NSObject<OS_dispatch_group>" _wait;
@"<UITextPasteCoordinatorDelegate>" _delegate;
```

## Properties

```
@property (T@"<UITextPasteCoordinatorDelegate>",R,W,N,V_delegate) delegate;
```

## Instance methods

```
-[UITextPasteCoordinator initWithDelegate:];
-[UITextPasteCoordinator _finish];
-[UITextPasteCoordinator addItem:];
-[UITextPasteCoordinator delegate];
-[UITextPasteCoordinator _determineFinished];
-[UITextPasteCoordinator performBlockingWait:];
-[UITextPasteCoordinator setResult:forItem:];
```
