# `UIStatusBarServiceItemView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIStatusBarItemView`
- 11 instance variables, 0 properties, 20 instance methods, 0 class methods

## Instance variables

```
@"NSString" _serviceString;
@"NSString" _crossfadeString;
Q _crossfadeStep;
d _maxWidth;
d _serviceWidth;
d _crossfadeWidth;
i _contentType;
B _loopingNecessaryForString;
B _loopNowIfNecessary;
B _loopingNow;
d _letterSpacing;
```

## Instance methods

```
-[UIStatusBarServiceItemView accessibilityHUDRepresentation];
-[UIStatusBarServiceItemView contentsImage];
-[UIStatusBarServiceItemView legibilityStyle];
-[UIStatusBarServiceItemView standardPadding];
-[UIStatusBarServiceItemView _contentsImageFromString:withWidth:letterSpacing:];
-[UIStatusBarServiceItemView _crossfadeContentsImage];
-[UIStatusBarServiceItemView _crossfadeStepAnimation];
-[UIStatusBarServiceItemView _crossfaded];
-[UIStatusBarServiceItemView _loopAnimationDidStopInDirection:];
-[UIStatusBarServiceItemView _loopingNecessary];
-[UIStatusBarServiceItemView _serviceContentsImage];
-[UIStatusBarServiceItemView addContentOverlap:];
-[UIStatusBarServiceItemView animatesDataChange];
-[UIStatusBarServiceItemView extraRightPadding];
-[UIStatusBarServiceItemView performPendedActions];
-[UIStatusBarServiceItemView resetContentOverlap];
-[UIStatusBarServiceItemView setVisible:frame:duration:];
-[UIStatusBarServiceItemView updateContentsAndWidth];
-[UIStatusBarServiceItemView updateForContentType:serviceString:serviceCrossfadeString:maxWidth:actions:];
-[UIStatusBarServiceItemView updateForNewData:actions:];
```
