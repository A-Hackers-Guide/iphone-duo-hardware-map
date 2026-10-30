# `_UISceneBarSizeClassResolver`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSXPCSecureCoding`
- 1 instance variables, 1 properties, 10 instance methods, 1 class methods

## Instance variables

```
sizeClassType;
```

## Properties

```
@property (Tq,N,R) hash;
```

## Class methods

```
+[_UISceneBarSizeClassResolver supportsBSXPCSecureCoding];
```

## Instance methods

```
-[_UISceneBarSizeClassResolver initWithBarSizeClassForTop:leading:bottom:trailing:layoutDirection:];
-[_UISceneBarSizeClassResolver init];
-[_UISceneBarSizeClassResolver barSizeClassForEdge:orientation:];
-[_UISceneBarSizeClassResolver hash];
-[_UISceneBarSizeClassResolver initWithBarSizeClassForTop:left:bottom:right:];
-[_UISceneBarSizeClassResolver encodeWithBSXPCCoder:];
-[_UISceneBarSizeClassResolver initWithBSXPCCoder:];
-[_UISceneBarSizeClassResolver initWithConstantBarSizeClass:];
-[_UISceneBarSizeClassResolver initWithBarSizeClassForPortraitTop:portraitLeft:portraitBottom:portraitRight:landscapeTop:landscapeLeft:landscapeBottom:landscapeRight:];
-[_UISceneBarSizeClassResolver isEqual:];
```
