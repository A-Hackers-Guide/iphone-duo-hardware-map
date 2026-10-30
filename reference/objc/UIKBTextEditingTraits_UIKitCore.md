# `UIKBTextEditingTraits`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 13 instance variables, 13 properties, 15 instance methods, 2 class methods

## Instance variables

```
B _canToggleBoldface;
B _canToggleItalics;
B _canToggleUnderline;
B _supportStyling;
B _canCut;
B _canCopy;
B _canPaste;
B _canMoveCursorLeft;
B _canMoveCursorRight;
B _isBold;
B _isItalicized;
B _isUnderlined;
@"UIResponder" _firstResponder;
```

## Properties

```
@property (TB,R,N,V_isBold) isBold;
@property (TB,R,N,V_isItalicized) isItalicized;
@property (TB,R,N,V_isUnderlined) isUnderlined;
@property (TB,R,N,V_canToggleBoldface) canToggleBoldface;
@property (TB,R,N,V_canToggleItalics) canToggleItalics;
@property (TB,R,N,V_canToggleUnderline) canToggleUnderline;
@property (TB,R,N,V_supportStyling) supportStyling;
@property (TB,N,V_canCut) canCut;
@property (TB,R,N,V_canCopy) canCopy;
@property (TB,R,N,V_canPaste) canPaste;
@property (TB,R,N,V_canMoveCursorLeft) canMoveCursorLeft;
@property (TB,R,N,V_canMoveCursorRight) canMoveCursorRight;
@property (T@"UIResponder",R,W,N,V_firstResponder) firstResponder;
```

## Class methods

```
+[UIKBTextEditingTraits traitsForEditingInteractionWithFirstResponder:canRespondBlock:keyMaskFlags:];
+[UIKBTextEditingTraits traitsWithResponder:keyMaskFlags:];
```

## Instance methods

```
-[UIKBTextEditingTraits canCopy];
-[UIKBTextEditingTraits canPaste];
-[UIKBTextEditingTraits canCut];
-[UIKBTextEditingTraits canMoveCursorLeft];
-[UIKBTextEditingTraits canMoveCursorRight];
-[UIKBTextEditingTraits canToggleBoldface];
-[UIKBTextEditingTraits canToggleItalics];
-[UIKBTextEditingTraits canToggleUnderline];
-[UIKBTextEditingTraits firstResponder];
-[UIKBTextEditingTraits initWithResponder:canRespondBlock:keyMaskFlags:sender:];
-[UIKBTextEditingTraits isBold];
-[UIKBTextEditingTraits isItalicized];
-[UIKBTextEditingTraits isUnderlined];
-[UIKBTextEditingTraits setCanCut:];
-[UIKBTextEditingTraits supportStyling];
```
