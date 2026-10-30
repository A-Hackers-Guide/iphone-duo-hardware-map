# `_UIStickerPickerKeyboardSession`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIStickerPickerViewControllerDelegate`
- 4 instance variables, 5 properties, 6 instance methods, 0 class methods

## Instance variables

```
@"UIResponder<UITextInput>" _textInput;
@"UIView" _view;
@"_UIStickerPickerViewController" _stickerPicker;
@"<_UIStickerPickerKeyboardSessionDelegate>" _delegate;
```

## Properties

```
@property (T@"<_UIStickerPickerKeyboardSessionDelegate>",W,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIStickerPickerKeyboardSession remoteHandlesRecentsStickerDonation];
-[_UIStickerPickerKeyboardSession setDelegate:];
-[_UIStickerPickerKeyboardSession delegate];
-[_UIStickerPickerKeyboardSession insertStickerFromItemProvider:completionHandler:];
-[_UIStickerPickerKeyboardSession presentWithTextInput:view:];
-[_UIStickerPickerKeyboardSession stickerPickerViewControllerDidDismiss];
```
