# `UITextRange`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 7 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"<NSObject>" _attachmentRange;
```

## Properties

```
@property (TB,R,N,G_isCaret) isCaret;
@property (TB,R,N,G_isRanged) isRanged;
@property (T@"UITextRangeImpl",R,N,G_isImpl) isImpl;
@property (T@"<NSObject>",&,N,G_attachmentRange,S_setAttachmentRange:,V_attachmentRange) _attachmentRange;
@property (TB,R,N,GisEmpty) empty;
@property (T@"UITextPosition",R,N) start;
@property (T@"UITextPosition",R,N) end;
```

## Instance methods

```
-[UITextRange start];
-[UITextRange end];
-[UITextRange isEmpty];
-[UITextRange _isImpl];
-[UITextRange _NSTextRanges];
-[UITextRange _asNSRangeRelativeToDocument:];
-[UITextRange _asNSRangeRelativeToDocument:relativeToCurrentLine:];
-[UITextRange _attachmentRange];
-[UITextRange _isCaret];
-[UITextRange _isRanged];
-[UITextRange _setAttachmentRange:];
-[UITextRange _unionNSTextRange];
```
