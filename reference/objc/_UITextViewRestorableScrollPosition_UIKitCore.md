# `_UITextViewRestorableScrollPosition`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCoding`
- 2 instance variables, 0 properties, 8 instance methods, 4 class methods

## Instance variables

```
{_NSRange="location"Q"length"Q} _range;
d _offsetInLine;
```

## Class methods

```
+[_UITextViewRestorableScrollPosition restorableScrollPositionForStateRestoration:];
+[_UITextViewRestorableScrollPosition restorableScrollPositionForTextView:];
+[_UITextViewRestorableScrollPosition restorableScrollPositionWithDictionary:];
+[_UITextViewRestorableScrollPosition restorableScrollPositionWithRange:];
```

## Instance methods

```
-[_UITextViewRestorableScrollPosition range];
-[_UITextViewRestorableScrollPosition debugDescription];
-[_UITextViewRestorableScrollPosition initWithTextView:];
-[_UITextViewRestorableScrollPosition initWithTextViewForStateRestoration:];
-[_UITextViewRestorableScrollPosition encodeWithCoder:];
-[_UITextViewRestorableScrollPosition initWithCoder:];
-[_UITextViewRestorableScrollPosition offsetWithinLine];
-[_UITextViewRestorableScrollPosition dictionaryRepresentation];
```
