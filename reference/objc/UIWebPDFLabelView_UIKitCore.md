# `UIWebPDFLabelView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 4 instance variables, 2 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"UILabel" _label;
@"_UIBackdropView" _backdropView;
@"NSTimer" _timer;
Q currentPageIndex;
```

## Properties

```
@property (TB,R,N,GisTimerInstalled) timerInstalled;
@property (TQ,N,VcurrentPageIndex) currentPageIndex;
```

## Instance methods

```
-[UIWebPDFLabelView clearTimer];
-[UIWebPDFLabelView sizeToFit];
-[UIWebPDFLabelView dealloc];
-[UIWebPDFLabelView currentPageIndex];
-[UIWebPDFLabelView fadeOut];
-[UIWebPDFLabelView setText:];
-[UIWebPDFLabelView setCurrentPageIndex:];
-[UIWebPDFLabelView initWithFrame:];
-[UIWebPDFLabelView _fadeOutAnimationDidStop];
-[UIWebPDFLabelView _fadeOutDelay];
-[UIWebPDFLabelView _fadeOutDuration];
-[UIWebPDFLabelView _makeRoundedCorners];
-[UIWebPDFLabelView isTimerInstalled];
-[UIWebPDFLabelView showNowInSuperView:atOrigin:withText:animated:];
```
