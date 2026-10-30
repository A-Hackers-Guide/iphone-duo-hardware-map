# `_UITextLayoutControllerBase`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 4 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"_UITextInputControllerLayoutManagerConnection" _textInputControllerConnection;
@"NSValue" _textOriginOverride;
B _documentObscured;
# _classicCanvasViewClass;
@"UITextRange" _unobscuredRange;
```

## Properties

```
@property (T@"UITextRange",&,N,V_unobscuredRange) unobscuredRange;
@property (TB,N,GisDocumentObscured,V_documentObscured) documentObscured;
@property (T@"NSTextContainer",R,N) firstTextContainer;
@property (T@"NSValue",&,N,V_textOriginOverride) textOriginOverride;
```

## Instance methods

```
-[_UITextLayoutControllerBase setUnobscuredRange:];
-[_UITextLayoutControllerBase adoptTextInputController:];
-[_UITextLayoutControllerBase textOriginOverride];
-[_UITextLayoutControllerBase resetTextViewportLayoutControllerLayoutForPosition:];
-[_UITextLayoutControllerBase unobscuredRange];
-[_UITextLayoutControllerBase isDocumentObscured];
-[_UITextLayoutControllerBase firstTextContainer];
-[_UITextLayoutControllerBase setDocumentObscured:];
-[_UITextLayoutControllerBase detachFromTextInputController];
-[_UITextLayoutControllerBase setTextOriginOverride:];
```
