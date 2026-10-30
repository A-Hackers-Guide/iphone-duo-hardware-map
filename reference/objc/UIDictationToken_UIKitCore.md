# `UIDictationToken`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 3 instance variables, 3 properties, 11 instance methods, 1 class methods

## Instance variables

```
B _removeSpaceBefore;
B _removeSpaceAfter;
@"NSString" _text;
```

## Properties

```
@property (T@"NSString",C,N,V_text) text;
@property (TB,N,V_removeSpaceBefore) removeSpaceBefore;
@property (TB,R,N,V_removeSpaceAfter) removeSpaceAfter;
```

## Class methods

```
+[UIDictationToken supportsSecureCoding];
```

## Instance methods

```
-[UIDictationToken text];
-[UIDictationToken encodeWithCoder:];
-[UIDictationToken description];
-[UIDictationToken initWithCoder:];
-[UIDictationToken setText:];
-[UIDictationToken isEqual:];
-[UIDictationToken _descriptionExtra];
-[UIDictationToken initWithText:removeSpaceBefore:removeSpaceAfter:];
-[UIDictationToken removeSpaceAfter];
-[UIDictationToken removeSpaceBefore];
-[UIDictationToken setRemoveSpaceBefore:];
```
