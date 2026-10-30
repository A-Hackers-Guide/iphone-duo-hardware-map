# `_UITextKitTextRange`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UITextRange`
- Protocols: `NSCopying`
- 5 instance variables, 5 properties, 15 instance methods, 5 class methods

## Instance variables

```
@"_UITextKitTextPosition" _start;
@"_UITextKitTextPosition" _end;
@"NSArray" _textKit2Ranges;
@"NSTextRange" _unionTextRange;
@"NSArray" _ranges;
```

## Properties

```
@property (T@"_UITextKitTextPosition",&,N,V_start) start;
@property (T@"_UITextKitTextPosition",&,N,V_end) end;
@property (T@"NSArray",&,N,V_textKit2Ranges) textKit2Ranges;
@property (T@"NSTextRange",R,N,V_unionTextRange) unionTextRange;
@property (T@"NSArray",R,N,V_ranges) ranges;
```

## Class methods

```
+[_UITextKitTextRange rangeWithTextContentManager:textRanges:affinity:];
+[_UITextKitTextRange rangeWithRange:];
+[_UITextKitTextRange rangeWithStart:end:];
+[_UITextKitTextRange rangeWithRange:affinity:];
+[_UITextKitTextRange rangeWithTextContentManager:textRanges:startAffinity:endAffinity:];
```

## Instance methods

```
-[_UITextKitTextRange ranges];
-[_UITextKitTextRange init];
-[_UITextKitTextRange textKit2Ranges];
-[_UITextKitTextRange start];
-[_UITextKitTextRange end];
-[_UITextKitTextRange unionTextRange];
-[_UITextKitTextRange asRange];
-[_UITextKitTextRange setEnd:];
-[_UITextKitTextRange setStart:];
-[_UITextKitTextRange isEmpty];
-[_UITextKitTextRange hash];
-[_UITextKitTextRange setTextKit2Ranges:];
-[_UITextKitTextRange description];
-[_UITextKitTextRange copyWithZone:];
-[_UITextKitTextRange isEqual:];
```
