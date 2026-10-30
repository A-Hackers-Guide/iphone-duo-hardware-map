# `_UITextServiceSessionContext`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 6 instance variables, 6 properties, 13 instance methods, 6 class methods

## Instance variables

```
@"UIResponder<UITextInput>" _textInput;
@"UIView" _view;
@"NSString" _textWithContext;
@"RVItem" _rvItemWithContext;
{_NSRange="location"Q"length"Q} _selectedRange;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _presentationRect;
```

## Properties

```
@property (T@"UIResponder<UITextInput>",R,N,V_textInput) textInput;
@property (T@"UIView",&,N,V_view) view;
@property (T@"NSString",R,C,N,V_textWithContext) textWithContext;
@property (T@"RVItem",R,C,N,V_rvItemWithContext) rvItemWithContext;
@property (T{_NSRange=QQ},R,N,V_selectedRange) selectedRange;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_presentationRect) presentationRect;
```

## Class methods

```
+[_UITextServiceSessionContext supportsSecureCoding];
+[_UITextServiceSessionContext selectedTextRangeForTextInput:];
+[_UITextServiceSessionContext selectionBoundingBoxForTextInput:];
+[_UITextServiceSessionContext sessionContextForType:withTextInput:];
+[_UITextServiceSessionContext sessionContextWithText:withRect:withRange:withView:];
+[_UITextServiceSessionContext sessionContextWithText:withRect:withView:];
```

## Instance methods

```
-[_UITextServiceSessionContext selectedRange];
-[_UITextServiceSessionContext setView:];
-[_UITextServiceSessionContext view];
-[_UITextServiceSessionContext encodeWithCoder:];
-[_UITextServiceSessionContext initWithCoder:];
-[_UITextServiceSessionContext textWithContext];
-[_UITextServiceSessionContext _gatherAdditionalContext];
-[_UITextServiceSessionContext _typeRequiresContext:];
-[_UITextServiceSessionContext convertRectToView:];
-[_UITextServiceSessionContext initForType:withText:withTextInput:withView:];
-[_UITextServiceSessionContext presentationRect];
-[_UITextServiceSessionContext rvItemWithContext];
-[_UITextServiceSessionContext textInput];
```
