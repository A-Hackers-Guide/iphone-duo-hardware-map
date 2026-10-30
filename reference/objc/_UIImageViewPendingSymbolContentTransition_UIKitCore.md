# `_UIImageViewPendingSymbolContentTransition`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 7 properties, 10 instance methods, 1 class methods

## Instance variables

```
B _pendingLayoutPass;
@"NSSymbolContentTransition" _symbolContentTransition;
@"NSSymbolEffectOptions" _options;
@? _completionHandler;
@"UIImage" _sourceSymbolImage;
@"UIImage" _targetSymbolImage;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _initialSymbolAbsoluteRect;
```

## Properties

```
@property (T@"NSSymbolContentTransition",R,N,V_symbolContentTransition) symbolContentTransition;
@property (T@"NSSymbolEffectOptions",R,N,V_options) options;
@property (T@?,R,N,V_completionHandler) completionHandler;
@property (T@"UIImage",R,N,V_sourceSymbolImage) sourceSymbolImage;
@property (T@"UIImage",R,N,V_targetSymbolImage) targetSymbolImage;
@property (TB,N,GisPendingLayoutPass,V_pendingLayoutPass) pendingLayoutPass;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_initialSymbolAbsoluteRect) initialSymbolAbsoluteRect;
```

## Class methods

```
+[_UIImageViewPendingSymbolContentTransition transitionWithTransition:sourceSymbolImage:targetSymbolImage:options:completion:];
```

## Instance methods

```
-[_UIImageViewPendingSymbolContentTransition completionHandler];
-[_UIImageViewPendingSymbolContentTransition init];
-[_UIImageViewPendingSymbolContentTransition options];
-[_UIImageViewPendingSymbolContentTransition initialSymbolAbsoluteRect];
-[_UIImageViewPendingSymbolContentTransition isPendingLayoutPass];
-[_UIImageViewPendingSymbolContentTransition setInitialSymbolAbsoluteRect:];
-[_UIImageViewPendingSymbolContentTransition setPendingLayoutPass:];
-[_UIImageViewPendingSymbolContentTransition sourceSymbolImage];
-[_UIImageViewPendingSymbolContentTransition symbolContentTransition];
-[_UIImageViewPendingSymbolContentTransition targetSymbolImage];
```
