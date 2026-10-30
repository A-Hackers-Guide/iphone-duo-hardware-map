# `_UITextDragCaretView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 3 instance variables, 1 properties, 25 instance methods, 0 class methods

## Instance variables

```
@"UIView<UITextInput>" _view;
@"CAShapeLayer" _mask;
B _rangesExcludeSelection;
```

## Properties

```
@property (TB,N,V_rangesExcludeSelection) rangesExcludeSelection;
```

## Instance methods

```
-[_UITextDragCaretView remove];
-[_UITextDragCaretView _rectsForRange:];
-[_UITextDragCaretView _performUpdate:];
-[_UITextDragCaretView _caretColor];
-[_UITextDragCaretView _configureMask:withPath:];
-[_UITextDragCaretView _insertAtRangeOrPosition:animations:completion:animated:];
-[_UITextDragCaretView _isRemoveAnimatesBackToCaret];
-[_UITextDragCaretView _maskForRects:];
-[_UITextDragCaretView _rangeColor];
-[_UITextDragCaretView _updateToRangeOrPosition:animations:completion:animated:];
-[_UITextDragCaretView initWithTextInputView:];
-[_UITextDragCaretView insertAtPosition:];
-[_UITextDragCaretView insertAtPosition:animations:completion:];
-[_UITextDragCaretView insertAtRange:];
-[_UITextDragCaretView insertAtRange:animations:completion:];
-[_UITextDragCaretView insertAtRange:animations:completion:animated:];
-[_UITextDragCaretView rangesExcludeSelection];
-[_UITextDragCaretView removeWithAnimations:completion:];
-[_UITextDragCaretView removeWithAnimations:completion:animated:];
-[_UITextDragCaretView setRangesExcludeSelection:];
-[_UITextDragCaretView updateToPosition:];
-[_UITextDragCaretView updateToPosition:animations:completion:];
-[_UITextDragCaretView updateToRange:];
-[_UITextDragCaretView updateToRange:animations:completion:];
-[_UITextDragCaretView updateToRange:animations:completion:animated:];
```
