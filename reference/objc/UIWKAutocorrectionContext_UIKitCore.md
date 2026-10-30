# `UIWKAutocorrectionContext`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"NSString" _contextBeforeSelection;
@"NSString" _selectedText;
@"NSString" _contextAfterSelection;
@"NSString" _markedText;
{_NSRange="location"Q"length"Q} _rangeInMarkedText;
```

## Properties

```
@property (T@"NSString",C,N,V_contextBeforeSelection) contextBeforeSelection;
@property (T@"NSString",C,N,V_selectedText) selectedText;
@property (T@"NSString",C,N,V_contextAfterSelection) contextAfterSelection;
@property (T@"NSString",C,N,V_markedText) markedText;
@property (T{_NSRange=QQ},N,V_rangeInMarkedText) rangeInMarkedText;
```

## Instance methods

```
-[UIWKAutocorrectionContext setMarkedText:];
-[UIWKAutocorrectionContext setSelectedText:];
-[UIWKAutocorrectionContext selectedText];
-[UIWKAutocorrectionContext markedText];
-[UIWKAutocorrectionContext contextAfterSelection];
-[UIWKAutocorrectionContext contextBeforeSelection];
-[UIWKAutocorrectionContext rangeInMarkedText];
-[UIWKAutocorrectionContext setContextAfterSelection:];
-[UIWKAutocorrectionContext setContextBeforeSelection:];
-[UIWKAutocorrectionContext setRangeInMarkedText:];
```
