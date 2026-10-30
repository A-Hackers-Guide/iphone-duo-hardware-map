# `UIWritingToolsCoordinatorContext`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 6 properties, 10 instance methods, 0 class methods

## Instance variables

```
{_NSRange="location"Q"length"Q} _proposedRange;
@"WTContext" _wtContext;
{_NSRange="location"Q"length"Q} _resolvedRange;
```

## Properties

```
@property (T{_NSRange=QQ},N,S_setEvaluatedRange:) evaluatedRange;
@property (T@"WTContext",&,N,S_setWTContext:,V_wtContext) _wtContext;
@property (T@"NSAttributedString",R,C,N) attributedString;
@property (T{_NSRange=QQ},R,N) range;
@property (T@"NSUUID",R,N) identifier;
@property (T{_NSRange=QQ},R,N,V_resolvedRange) resolvedRange;
```

## Instance methods

```
-[UIWritingToolsCoordinatorContext range];
-[UIWritingToolsCoordinatorContext identifier];
-[UIWritingToolsCoordinatorContext attributedString];
-[UIWritingToolsCoordinatorContext description];
-[UIWritingToolsCoordinatorContext initWithAttributedString:range:];
-[UIWritingToolsCoordinatorContext _setEvaluatedRange:];
-[UIWritingToolsCoordinatorContext _setWTContext:];
-[UIWritingToolsCoordinatorContext _wtContext];
-[UIWritingToolsCoordinatorContext evaluatedRange];
-[UIWritingToolsCoordinatorContext resolvedRange];
```
