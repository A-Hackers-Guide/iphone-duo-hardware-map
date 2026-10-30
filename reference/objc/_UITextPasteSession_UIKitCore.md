# `_UITextPasteSession`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UITextDropPasteSession`
- 9 instance variables, 13 properties, 20 instance methods, 0 class methods

## Instance variables

```
B _animating;
@"<UITextPasteSessionDelegate>" _delegate;
@"UITextPasteController" _controller;
@"UITextPasteCoordinator" _coordinator;
@"UITextRange" _range;
@"<_UITextPasteProgressSupport>" _progressSupport;
@"NSAttributedString" _pasteResult;
@"NSArray" _originalItems;
@"UITextRange" _hiddenRange;
```

## Properties

```
@property (T@"UITextPasteController",W,N,V_controller) controller;
@property (T@"UITextPasteCoordinator",&,N,V_coordinator) coordinator;
@property (T@"UITextRange",&,N,V_range) range;
@property (T@"<_UITextPasteProgressSupport>",&,N,V_progressSupport) progressSupport;
@property (T@"NSAttributedString",&,N,V_pasteResult) pasteResult;
@property (T@"NSArray",C,N,V_originalItems) originalItems;
@property (T@"UITextRange",&,N,V_hiddenRange) hiddenRange;
@property (TB,R,N,GisAnimating,V_animating) animating;
@property (T@"<UITextPasteSessionDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UITextPasteSession range];
-[_UITextPasteSession controller];
-[_UITextPasteSession setCoordinator:];
-[_UITextPasteSession setController:];
-[_UITextPasteSession setRange:];
-[_UITextPasteSession setDelegate:];
-[_UITextPasteSession delegate];
-[_UITextPasteSession coordinator];
-[_UITextPasteSession isAnimating];
-[_UITextPasteSession setPasteResult:];
-[_UITextPasteSession progressSupport];
-[_UITextPasteSession setHiddenRange:];
-[_UITextPasteSession animationCompleted];
-[_UITextPasteSession animationStarted];
-[_UITextPasteSession hiddenRange];
-[_UITextPasteSession originalItems];
-[_UITextPasteSession pasteResult];
-[_UITextPasteSession positionedPasteResult];
-[_UITextPasteSession setOriginalItems:];
-[_UITextPasteSession setProgressSupport:];
```
