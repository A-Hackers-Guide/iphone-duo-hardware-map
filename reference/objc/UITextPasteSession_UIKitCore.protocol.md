# `UITextPasteSession` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 4 properties, 9 instance methods, 0 class methods

## Properties

```
@property (T@"UITextRange",R,N) range;
@property (T@"NSAttributedString",R,N) pasteResult;
@property (T@"<UITextPasteSessionDelegate>",W,N) delegate;
@property (T@"NSArray",C,N) originalItems;
```

## Instance methods

```
-[UITextPasteSession range];
-[UITextPasteSession setDelegate:];
-[UITextPasteSession delegate];
-[UITextPasteSession animationCompleted];
-[UITextPasteSession animationStarted];
-[UITextPasteSession originalItems];
-[UITextPasteSession pasteResult];
-[UITextPasteSession positionedPasteResult];
-[UITextPasteSession setOriginalItems:];
```
