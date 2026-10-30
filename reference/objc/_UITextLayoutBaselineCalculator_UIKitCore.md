# `_UITextLayoutBaselineCalculator`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UITextLayoutBaselineCalculator`
- 6 instance variables, 6 properties, 5 instance methods, 0 class methods

## Instance variables

```
@"_UITextLayoutControllerBase<_UITextLayoutController>" _textLayoutController;
@"NSDictionary" _typingAttributes;
@"<UICoordinateSpace>" _coordinateSpace;
d _scale;
B _usesLineFragmentOrigin;
{CGPoint="x"d"y"d} _fallbackTextContainerOrigin;
```

## Properties

```
@property (Td,R,N) firstBaselineOffsetFromTop;
@property (Td,R,N) lastBaselineOffsetFromBottom;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UITextLayoutBaselineCalculator lastBaselineOffsetFromBottom];
-[_UITextLayoutBaselineCalculator initWithTextLayoutController:typingAttributes:usesLineFragmentOrigin:coordinateSpace:scale:fallbackTextContainerOrigin:];
-[_UITextLayoutBaselineCalculator firstBaselineOffsetFromTop];
-[_UITextLayoutBaselineCalculator _baselineOffsetAtPosition:];
-[_UITextLayoutBaselineCalculator _convertOffset:];
```
