# `_UIContentViewEditingState`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 3 instance variables, 3 properties, 6 instance methods, 0 class methods

## Instance variables

```
@"NSString" _text;
@"NSString" _proposedReplacementText;
{_NSRange="location"Q"length"Q} _proposedReplacementRange;
```

## Properties

```
@property (T@"NSString",R,N,V_text) text;
@property (T@"NSString",R,N,V_proposedReplacementText) proposedReplacementText;
@property (T{_NSRange=QQ},R,N,V_proposedReplacementRange) proposedReplacementRange;
```

## Instance methods

```
-[_UIContentViewEditingState text];
-[_UIContentViewEditingState initWithText:];
-[_UIContentViewEditingState copyWithZone:];
-[_UIContentViewEditingState initWithText:proposedReplacementText:proposedReplacementRange:];
-[_UIContentViewEditingState proposedReplacementRange];
-[_UIContentViewEditingState proposedReplacementText];
```
