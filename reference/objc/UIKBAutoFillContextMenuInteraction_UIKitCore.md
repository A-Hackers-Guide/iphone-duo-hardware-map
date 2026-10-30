# `UIKBAutoFillContextMenuInteraction`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `AFUICompletionDelegate_Staging`, `AFUIContactsUIDelegate_Staging`, `UIInteraction`
- 2 instance variables, 6 properties, 9 instance methods, 3 class methods

## Instance variables

```
@"UIView" _view;
@"UIViewController<AFUIContextMenuViewController_Staging>" _contextMenuViewController;
```

## Properties

```
@property (T@"UIViewController<AFUIContextMenuViewController_Staging>",&,N,V_contextMenuViewController) contextMenuViewController;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"UIView",R,W,N,V_view) view;
```

## Class methods

```
+[UIKBAutoFillContextMenuInteraction _setupXPCConnection];
+[UIKBAutoFillContextMenuInteraction checkHasSuggestionsForConnection:completion:];
+[UIKBAutoFillContextMenuInteraction shouldShowOnResponder:completion:];
```

## Instance methods

```
-[UIKBAutoFillContextMenuInteraction view];
-[UIKBAutoFillContextMenuInteraction willMoveToView:];
-[UIKBAutoFillContextMenuInteraction performTextOperations:];
-[UIKBAutoFillContextMenuInteraction selectionScrolling:];
-[UIKBAutoFillContextMenuInteraction didMoveToView:];
-[UIKBAutoFillContextMenuInteraction didEnd];
-[UIKBAutoFillContextMenuInteraction contextMenuViewController];
-[UIKBAutoFillContextMenuInteraction presentContactPicker];
-[UIKBAutoFillContextMenuInteraction setContextMenuViewController:];
```
