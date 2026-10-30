# `DCPlacardView`

- Image: [`/System/Library/PrivateFrameworks/DocumentCamera.framework/DocumentCamera`](../userland/System__Library__PrivateFrameworks__DocumentCamera.framework__DocumentCamera.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 8 instance variables, 8 properties, 20 instance methods, 1 class methods

## Instance variables

```
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 label;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 labelTopConstraint;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 labelBottomConstraint;
@"UIColor" backgroundTintColor;
B usesLabelStyleBackground;
d verticalLabelInset;
B isFaded;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 isPlayingFadeAnimation;
```

## Properties

```
@property (T@"NSString",N,C) text;
@property (T@"UIFont",N,&) font;
@property (T@"UIColor",N,&,VbackgroundTintColor) backgroundTintColor;
@property (TB,N,VusesLabelStyleBackground) usesLabelStyleBackground;
@property (Td,N,VverticalLabelInset) verticalLabelInset;
@property (TB,N) isLabelAccessibilityElement;
@property (TB,N,R) hasAnimations;
@property (TB,N,VisFaded) isFaded;
```

## Class methods

```
+[DCPlacardView isGlassStyleEnabled];
```

## Instance methods

```
-[DCPlacardView text];
-[DCPlacardView removeAllAnimations];
-[DCPlacardView initWithCoder:];
-[DCPlacardView setText:];
-[DCPlacardView backgroundTintColor];
-[DCPlacardView font];
-[DCPlacardView initWithFrame:];
-[DCPlacardView setFont:];
-[DCPlacardView setBackgroundTintColor:];
-[DCPlacardView setIsLabelAccessibilityElement:];
-[DCPlacardView isFaded];
-[DCPlacardView hasAnimations];
-[DCPlacardView isLabelAccessibilityElement];
-[DCPlacardView playFadeAnimation];
-[DCPlacardView setIsFaded:];
-[DCPlacardView setUsesLabelStyleBackground:];
-[DCPlacardView setVerticalLabelInset:];
-[DCPlacardView speakIfVisibleAfterDelay:];
-[DCPlacardView usesLabelStyleBackground];
-[DCPlacardView verticalLabelInset];
```
