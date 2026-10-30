# `_UIStickerPickerViewController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `_UIStickerPickerRemoteViewControllerDelegate`, `UIAdaptivePresentationControllerDelegate`, `UIViewControllerTransitioningDelegate`
- 6 instance variables, 12 properties, 41 instance methods, 1 class methods

## Instance variables

```
B _isLaunchedFromKeyboard;
B _keyWindowChangedDuringInsert;
@"<_UIStickerPickerViewControllerDelegate>" _delegate;
@"UIView" _sourceView;
@"_UIStickerPickerServiceRemoteViewController" _card;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _sourceRect;
```

## Properties

```
@property (T@?,C,N) dismissCompletionHandler;
@property (TB,N,V_isLaunchedFromKeyboard) isLaunchedFromKeyboard;
@property (T@"_UIStickerPickerServiceRemoteViewController",&,N,V_card) card;
@property (TB,R,N) supportsReturningStickerIdentifiersDuringAddition;
@property (TB,N,V_keyWindowChangedDuringInsert) keyWindowChangedDuringInsert;
@property (T@"<_UIStickerPickerViewControllerDelegate>",W,N,V_delegate) delegate;
@property (T@"UIView",&,V_sourceView) sourceView;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_sourceRect) sourceRect;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UIStickerPickerViewController requestCardViewControllerWithConnectionHandler:];
```

## Instance methods

```
-[_UIStickerPickerViewController setSourceRect:];
-[_UIStickerPickerViewController sourceRect];
-[_UIStickerPickerViewController presentationControllerDidDismiss:];
-[_UIStickerPickerViewController presentCard];
-[_UIStickerPickerViewController applicationDidEnterBackground:];
-[_UIStickerPickerViewController presentationControllerForPresentedViewController:presentingViewController:sourceViewController:];
-[_UIStickerPickerViewController init];
-[_UIStickerPickerViewController viewServiceDidTerminateWithError:];
-[_UIStickerPickerViewController dealloc];
-[_UIStickerPickerViewController dismissCard];
-[_UIStickerPickerViewController viewDidLoad];
-[_UIStickerPickerViewController setDelegate:];
-[_UIStickerPickerViewController remoteHandlesRecentsStickerDonationWithCompletionHandler:];
-[_UIStickerPickerViewController stickerPickerCardDidLoad];
-[_UIStickerPickerViewController loadView];
-[_UIStickerPickerViewController setSourceView:];
-[_UIStickerPickerViewController delegate];
-[_UIStickerPickerViewController stageSticker:];
-[_UIStickerPickerViewController setCard:];
-[_UIStickerPickerViewController card];
-[_UIStickerPickerViewController sourceView];
-[_UIStickerPickerViewController dismissCardAnimated:completion:];
-[_UIStickerPickerViewController _insertStickerFromItemProvider:];
-[_UIStickerPickerViewController _addStickerWithRepresentations:previewView:animatingTo:];
-[_UIStickerPickerViewController _remoteViewDidLoad:];
-[_UIStickerPickerViewController _sourceRectInWindowCoordinates];
-[_UIStickerPickerViewController _updatePopoverWindowLocation];
-[_UIStickerPickerViewController _viewServiceProxy];
-[_UIStickerPickerViewController addStickerWithRepresentations:previewView:originatingView:];
-[_UIStickerPickerViewController addStickerWithRepresentations:previewView:originatingView:completion:];
-[_UIStickerPickerViewController animatedStickerCreationProgressChanged:progress:];
-[_UIStickerPickerViewController dismissCardAnimated:];
-[_UIStickerPickerViewController dismissCompletionHandler];
-[_UIStickerPickerViewController isLaunchedFromKeyboard];
-[_UIStickerPickerViewController keyWindowChangedDuringInsert];
-[_UIStickerPickerViewController setDismissCompletionHandler:];
-[_UIStickerPickerViewController setIsLaunchedFromKeyboard:];
-[_UIStickerPickerViewController setKeyWindowChangedDuringInsert:];
-[_UIStickerPickerViewController stageStickerWithIdentifier:representations:name:externalURI:accessibilityLabel:metadata:];
-[_UIStickerPickerViewController supportsReturningStickerIdentifiersDuringAddition];
-[_UIStickerPickerViewController supportsReturningStickerIdentifiersDuringAdditionV2];
```
