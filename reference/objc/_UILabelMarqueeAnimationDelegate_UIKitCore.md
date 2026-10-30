# `_UILabelMarqueeAnimationDelegate`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CAAnimationDelegate`
- 4 instance variables, 6 properties, 7 instance methods, 0 class methods

## Instance variables

```
B _started;
B _updated;
B _suppressEnded;
@"UILabel" _label;
```

## Properties

```
@property (T@"UILabel",W,N,V_label) label;
@property (TB,N,V_suppressEnded) suppressEnded;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UILabelMarqueeAnimationDelegate initWithLabel:];
-[_UILabelMarqueeAnimationDelegate animationDidStart:];
-[_UILabelMarqueeAnimationDelegate animationDidStop:finished:];
-[_UILabelMarqueeAnimationDelegate label];
-[_UILabelMarqueeAnimationDelegate setLabel:];
-[_UILabelMarqueeAnimationDelegate setSuppressEnded:];
-[_UILabelMarqueeAnimationDelegate suppressEnded];
```
