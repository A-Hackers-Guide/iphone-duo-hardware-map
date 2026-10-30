# `UIWKDocumentContext`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 10 instance variables, 15 properties, 37 instance methods, 0 class methods

## Instance variables

```
B _rectsAreInCharacterOrder;
{_NSRange="location"Q"length"Q} _lastRectRange;
@"NSMutableData" _selectionRects;
@"NSObject" _contextBefore;
@"NSObject" _selectedText;
@"NSObject" _contextAfter;
@"NSObject" _markedText;
@"NSArray" _autocorrectedRanges;
@"NSAttributedString" _annotatedText;
{_NSRange="location"Q"length"Q} _selectedRangeInMarkedText;
```

## Properties

```
@property (T@"NSMutableData",&,N,V_selectionRects) _selectionRects;
@property (T@"NSString",R,N) _contextBeforeString;
@property (T@"NSString",R,N) _selectedTextString;
@property (T@"NSString",R,N) _contextAfterString;
@property (T@"NSString",R,N) _markedTextString;
@property (T@"NSObject",C,N,V_contextBefore) contextBefore;
@property (T@"NSObject",C,N,V_selectedText) selectedText;
@property (T@"NSObject",C,N,V_contextAfter) contextAfter;
@property (T@"NSObject",C,N,V_markedText) markedText;
@property (T{_NSRange=QQ},N,V_selectedRangeInMarkedText) selectedRangeInMarkedText;
@property (T{_NSRange=QQ},R,N) selectedTextRange;
@property (T{_NSRange=QQ},R,N) markedTextRange;
@property (T@"NSArray",C,N,V_autocorrectedRanges) autocorrectedRanges;
@property (T@"NSString",R,N) fullText;
@property (T@"NSAttributedString",C,N,V_annotatedText) annotatedText;
```

## Instance methods

```
-[UIWKDocumentContext selectedTextRange];
-[UIWKDocumentContext markedTextRange];
-[UIWKDocumentContext contextBefore];
-[UIWKDocumentContext fullText];
-[UIWKDocumentContext enumerateLayoutRects:];
-[UIWKDocumentContext setMarkedText:];
-[UIWKDocumentContext characterRectsForCharacterRange:];
-[UIWKDocumentContext deltaForSelectionRange:];
-[UIWKDocumentContext setSelectedText:];
-[UIWKDocumentContext init];
-[UIWKDocumentContext directionalRangeForSelectionRange:];
-[UIWKDocumentContext _markedTextString];
-[UIWKDocumentContext annotatedText];
-[UIWKDocumentContext dealloc];
-[UIWKDocumentContext setAnnotatedText:];
-[UIWKDocumentContext setContextBefore:];
-[UIWKDocumentContext selectedText];
-[UIWKDocumentContext setSelectedRangeInMarkedText:];
-[UIWKDocumentContext resetTextRects];
-[UIWKDocumentContext _contextAfterString];
-[UIWKDocumentContext contextAfter];
-[UIWKDocumentContext _selectedTextString];
-[UIWKDocumentContext setContextAfter:];
-[UIWKDocumentContext rangeContainedWithinRect:];
-[UIWKDocumentContext _selectionRects];
-[UIWKDocumentContext addTextRect:forCharacterRange:];
-[UIWKDocumentContext _textFromDirectionalRange:];
-[UIWKDocumentContext set_selectionRects:];
-[UIWKDocumentContext markedText];
-[UIWKDocumentContext _contextBeforeString];
-[UIWKDocumentContext stringContainedWithinRect:];
-[UIWKDocumentContext closestCharacterIndexForPoint:];
-[UIWKDocumentContext enumerateLayoutRectsWithOptions:characterRange:block:];
-[UIWKDocumentContext autocorrectedRanges];
-[UIWKDocumentContext setAutocorrectedRanges:];
-[UIWKDocumentContext selectedRangeInMarkedText];
-[UIWKDocumentContext sortTextRectsByCharacterRange];
```
