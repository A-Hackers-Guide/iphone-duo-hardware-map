# `_UITabMorphing` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 6 properties, 9 instance methods, 0 class methods

## Properties

```
@property (T@"NSString",R,C,N) componentKey;
@property (T@"UIView",R,N) contentView;
@property (T@"UIView",R,N) backgroundView;
@property (T{CACornerRadii={CGSize=dd}{CGSize=dd}{CGSize=dd}{CGSize=dd}},R,N) contentCornerRadii;
@property (T@"_UIShadowProperties",R,N) shadowProperties;
@property (T@"UIViewSpringAnimationBehavior",R,N) morphTargetSpringBehavior;
```

## Instance methods

```
-[_UITabMorphing contentCornerRadii];
-[_UITabMorphing shadowProperties];
-[_UITabMorphing transitionDidEnd];
-[_UITabMorphing performAlongsideTransitionToVisibility:];
-[_UITabMorphing morphTargetSpringBehavior];
-[_UITabMorphing componentKey];
-[_UITabMorphing contentView];
-[_UITabMorphing prepareForTransitionToVisibility:];
-[_UITabMorphing backgroundView];
```
