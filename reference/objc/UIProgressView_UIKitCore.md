# `UIProgressView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `NSCoding`
- 10 instance variables, 9 properties, 36 instance methods, 3 class methods

## Instance variables

```
q _progressViewStyle;
f _progress;
q _barStyle;
@"UIColor" _progressTintColor;
@"UIColor" _trackTintColor;
@"NSProgress" _observedProgress;
@"NSObservation" _progressObservation;
@"UIView<UIProgressViewVisualElement>" _visualElement;
@"UIImage" _trackImage;
@"UIImage" _progressImage;
```

## Properties

```
@property (Tq,N) barStyle;
@property (T@"UIColor",&,N,G_progressColor,S_setProgressColor:) progressColor;
@property (Tq,N,V_progressViewStyle) progressViewStyle;
@property (Tf,N,V_progress) progress;
@property (T@"UIColor",&,N,V_progressTintColor) progressTintColor;
@property (T@"UIColor",&,N,V_trackTintColor) trackTintColor;
@property (T@"UIImage",&,N,V_progressImage) progressImage;
@property (T@"UIImage",&,N,V_trackImage) trackImage;
@property (T@"NSProgress",&,N,V_observedProgress) observedProgress;
```

## Class methods

```
+[UIProgressView visualElementForTraitCollection:];
+[UIProgressView defaultSize];
+[UIProgressView visualElementClassForTraitCollection:];
```

## Instance methods

```
-[UIProgressView setTrackImage:];
-[UIProgressView setProgress:];
-[UIProgressView _intrinsicSizeWithinSize:];
-[UIProgressView alignmentRectInsets];
-[UIProgressView setProgressTintColor:];
-[UIProgressView trackTintColor];
-[UIProgressView setProgressImage:];
-[UIProgressView barStyle];
-[UIProgressView layoutSubviews];
-[UIProgressView setBounds:];
-[UIProgressView progress];
-[UIProgressView sizeThatFits:];
-[UIProgressView _contentHuggingDefault_isUsuallyFixedHeight];
-[UIProgressView setProgressViewStyle:];
-[UIProgressView setBarStyle:];
-[UIProgressView encodeWithCoder:];
-[UIProgressView setFrame:];
-[UIProgressView isElementAccessibilityExposedToInterfaceBuilder];
-[UIProgressView initWithCoder:];
-[UIProgressView _populateArchivedSubviews:];
-[UIProgressView progressTintColor];
-[UIProgressView initWithFrame:];
-[UIProgressView setTrackTintColor:];
-[UIProgressView setProgress:animated:];
-[UIProgressView _progressColor];
-[UIProgressView _refreshVisualElement];
-[UIProgressView _refreshVisualElementForTraitCollection:populatingAPIProperties:];
-[UIProgressView _setProgress:];
-[UIProgressView _setProgressAnimated:duration:delay:options:];
-[UIProgressView _setProgressColor:];
-[UIProgressView initWithProgressViewStyle:];
-[UIProgressView observedProgress];
-[UIProgressView progressImage];
-[UIProgressView progressViewStyle];
-[UIProgressView setObservedProgress:];
-[UIProgressView trackImage];
```
