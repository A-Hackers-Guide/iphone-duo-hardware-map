# `_UIStickerPickerServiceRemoteViewController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIRemoteViewController`
- 1 instance variables, 1 properties, 11 instance methods, 3 class methods

## Instance variables

```
@"<_UIStickerPickerRemoteViewControllerDelegate>" _delegate;
```

## Properties

```
@property (T@"<_UIStickerPickerRemoteViewControllerDelegate>",W,N,V_delegate) delegate;
```

## Class methods

```
+[_UIStickerPickerServiceRemoteViewController exportedInterface];
+[_UIStickerPickerServiceRemoteViewController requestCardViewControllerWithConnectionHandler:];
+[_UIStickerPickerServiceRemoteViewController serviceViewControllerInterface];
```

## Instance methods

```
-[_UIStickerPickerServiceRemoteViewController presentCard];
-[_UIStickerPickerServiceRemoteViewController viewServiceDidTerminateWithError:];
-[_UIStickerPickerServiceRemoteViewController dismissCard];
-[_UIStickerPickerServiceRemoteViewController stageStickerWithIdentifier:representations:name:externalURI:accessibilityLabel:];
-[_UIStickerPickerServiceRemoteViewController _canShowWhileLocked];
-[_UIStickerPickerServiceRemoteViewController setDelegate:];
-[_UIStickerPickerServiceRemoteViewController remoteHandlesRecentsStickerDonationWithCompletionHandler:];
-[_UIStickerPickerServiceRemoteViewController stickerPickerCardDidLoad];
-[_UIStickerPickerServiceRemoteViewController delegate];
-[_UIStickerPickerServiceRemoteViewController stageSticker:];
-[_UIStickerPickerServiceRemoteViewController _allowsKeyboardFocus];
```
