# `UIKeyboardMediaServiceRemoteViewController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIRemoteViewController`
- Protocols: `UIKeyboardMediaHostProtocol`, `_UIStickerPickerHostProtocol`
- 2 instance variables, 6 properties, 18 instance methods, 5 class methods

## Instance variables

```
B _shownInline;
@"<UIKeyboardMediaServiceRemoteViewControllerDelegate>" _delegate;
```

## Properties

```
@property (TB,N,G_isShownInline,S_setShownInline:,V_shownInline) _shownInline;
@property (T@"<UIKeyboardMediaServiceRemoteViewControllerDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UIKeyboardMediaServiceRemoteViewController exportedInterface];
+[UIKeyboardMediaServiceRemoteViewController __shouldHostRemoteTextEffectsWindow];
+[UIKeyboardMediaServiceRemoteViewController requestCardViewControllerWithConnectionHandler:];
+[UIKeyboardMediaServiceRemoteViewController requestInlineViewControllerWithConnectionHandler:];
+[UIKeyboardMediaServiceRemoteViewController serviceViewControllerInterface];
```

## Instance methods

```
-[UIKeyboardMediaServiceRemoteViewController presentCard];
-[UIKeyboardMediaServiceRemoteViewController viewServiceDidTerminateWithError:];
-[UIKeyboardMediaServiceRemoteViewController dismissCard];
-[UIKeyboardMediaServiceRemoteViewController draggedStickerToPoint:];
-[UIKeyboardMediaServiceRemoteViewController stageStickerWithIdentifier:representations:name:externalURI:accessibilityLabel:];
-[UIKeyboardMediaServiceRemoteViewController _canShowWhileLocked];
-[UIKeyboardMediaServiceRemoteViewController setDelegate:];
-[UIKeyboardMediaServiceRemoteViewController remoteHandlesRecentsStickerDonationWithCompletionHandler:];
-[UIKeyboardMediaServiceRemoteViewController stickerPickerCardDidLoad];
-[UIKeyboardMediaServiceRemoteViewController requestInsertionPointCompletion:];
-[UIKeyboardMediaServiceRemoteViewController delegate];
-[UIKeyboardMediaServiceRemoteViewController stageSticker:];
-[UIKeyboardMediaServiceRemoteViewController pasteImageAtFileHandle:];
-[UIKeyboardMediaServiceRemoteViewController stageStickerWithFileHandle:url:accessibilityLabel:];
-[UIKeyboardMediaServiceRemoteViewController __shouldRemoteViewControllerFenceGeometryChange:forAncestor:];
-[UIKeyboardMediaServiceRemoteViewController _isShownInline];
-[UIKeyboardMediaServiceRemoteViewController _setShownInline:];
-[UIKeyboardMediaServiceRemoteViewController setHostBundleID:];
```
