# `UIAutocorrectTextView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 6 instance variables, 2 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"NSString" m_string;
i m_type;
i m_edgeType;
@"UIFont" m_textFont;
B m_animating;
B m_isLongString;
```

## Properties

```
@property (TB,N,Vm_animating) animating;
@property (TB,N,Vm_isLongString) isLongString;
```

## Instance methods

```
-[UIAutocorrectTextView animating];
-[UIAutocorrectTextView pointInside:forEvent:];
-[UIAutocorrectTextView drawRect:];
-[UIAutocorrectTextView pointInside:withEvent:];
-[UIAutocorrectTextView setAnimating:];
-[UIAutocorrectTextView _calculateRectForExpandedHitRegion];
-[UIAutocorrectTextView initWithFrame:string:type:edgeType:];
-[UIAutocorrectTextView isLongString];
-[UIAutocorrectTextView setEdgeType:];
-[UIAutocorrectTextView setIsLongString:];
```
