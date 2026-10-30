# `UIKBAutoFillModalPickerInteraction`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `AFUICompletionDelegate_Staging`, `UIInteraction`
- 4 instance variables, 8 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"UIView" _view;
q _autoFillMode;
@"NSObject<AFUIExplicitAutoFillController_Staging>" _explicitAutoFillController;
@"RTITextOperations" _pendingTextOperations;
```

## Properties

```
@property (T@"NSObject<AFUIExplicitAutoFillController_Staging>",&,N,V_explicitAutoFillController) explicitAutoFillController;
@property (Tq,V_autoFillMode) autoFillMode;
@property (T@"RTITextOperations",&,N,V_pendingTextOperations) pendingTextOperations;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"UIView",R,W,N,V_view) view;
```

## Instance methods

```
-[UIKBAutoFillModalPickerInteraction view];
-[UIKBAutoFillModalPickerInteraction willMoveToView:];
-[UIKBAutoFillModalPickerInteraction performTextOperations:];
-[UIKBAutoFillModalPickerInteraction didMoveToView:];
-[UIKBAutoFillModalPickerInteraction didEnd];
-[UIKBAutoFillModalPickerInteraction _performPendingTextOperations];
-[UIKBAutoFillModalPickerInteraction _textInputResponderDidChange:];
-[UIKBAutoFillModalPickerInteraction autoFillMode];
-[UIKBAutoFillModalPickerInteraction explicitAutoFillController];
-[UIKBAutoFillModalPickerInteraction initWithAutoFillMode:];
-[UIKBAutoFillModalPickerInteraction pendingTextOperations];
-[UIKBAutoFillModalPickerInteraction setAutoFillMode:];
-[UIKBAutoFillModalPickerInteraction setExplicitAutoFillController:];
-[UIKBAutoFillModalPickerInteraction setPendingTextOperations:];
```
