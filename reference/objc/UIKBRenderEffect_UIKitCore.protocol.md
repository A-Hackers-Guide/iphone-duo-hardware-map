# `UIKBRenderEffect` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`, `NSCopying`
- 0 instance variables, 5 properties, 8 instance methods, 0 class methods

## Properties

```
@property (TB,R,N) isValid;
@property (TB,R,N) renderUnder;
@property (Td,N) weight;
@property (TB,R,N) usesRGBColors;
@property (T@"UIKBGradient",R,N) gradient;
```

## Instance methods

```
-[UIKBRenderEffect gradient];
-[UIKBRenderEffect CGColor];
-[UIKBRenderEffect weight];
-[UIKBRenderEffect usesRGBColors];
-[UIKBRenderEffect setWeight:];
-[UIKBRenderEffect isValid];
-[UIKBRenderEffect renderEffectWithRenderer:traits:];
-[UIKBRenderEffect renderUnder];
```
