# `UITextRangeImpl`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UITextRange`
- 2 instance variables, 2 properties, 10 instance methods, 2 class methods

## Instance variables

```
@"DOMRange" _domRange;
q _affinityIfCollapsed;
```

## Properties

```
@property (T@"DOMRange",&,N,V_domRange) domRange;
@property (Tq,N,V_affinityIfCollapsed) affinity;
```

## Class methods

```
+[UITextRangeImpl wrapDOMRange:];
+[UITextRangeImpl wrapDOMRange:withAffinity:];
```

## Instance methods

```
-[UITextRangeImpl affinity];
-[UITextRangeImpl start];
-[UITextRangeImpl end];
-[UITextRangeImpl isEmpty];
-[UITextRangeImpl description];
-[UITextRangeImpl isEqual:];
-[UITextRangeImpl adjustAffinityOfPosition:isStart:];
-[UITextRangeImpl domRange];
-[UITextRangeImpl setAffinity:];
-[UITextRangeImpl setDomRange:];
```
