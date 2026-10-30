# `UIKeyboardStickerEditorViewController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `STKStickerEffectEditorViewControllerDelegate`
- 6 instance variables, 4 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"NSUUID" _stickerIdentifier;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _sourceRect;
@"STKRemoteStickerEffectEditorViewController" _editorViewController;
@"UIKBBackdropView" _backdropView;
@"UIVisualEffectView" _visualEffectView;
B _shown;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UIKeyboardStickerEditorViewController dismissAnimated:];
-[UIKeyboardStickerEditorViewController dismiss];
-[UIKeyboardStickerEditorViewController viewDidLoad];
-[UIKeyboardStickerEditorViewController traitCollectionDidChange:];
-[UIKeyboardStickerEditorViewController configureBackdropView];
-[UIKeyboardStickerEditorViewController configureEditorViewController];
-[UIKeyboardStickerEditorViewController configureVisualEffectView];
-[UIKeyboardStickerEditorViewController initWithStickerIdentifier:sourceRect:];
-[UIKeyboardStickerEditorViewController showInKeyboard];
-[UIKeyboardStickerEditorViewController stickerEffectEditorViewControllerControllerDidTapDone];
```
