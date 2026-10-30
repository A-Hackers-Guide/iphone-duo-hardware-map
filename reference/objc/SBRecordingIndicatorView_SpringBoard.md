# `SBRecordingIndicatorView`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `PTSettingsKeyObserver`, `SBRecordingIndicatorConfiguring`, `SAUIElementViewCustomBlurAccepting`
- 2 instance variables, 7 properties, 16 instance methods, 0 class methods

## Instance variables

```
@"CALayer<SBRecordingIndicatorLayering>" _indicatorLayer;
B _highLevel;
```

## Properties

```
@property (TB,N,GisHighLevel,V_highLevel) highLevel;
@property (TQ,N) indicatorType;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (Td,N) blurRadius;
```

## Instance methods

```
-[SBRecordingIndicatorView secureIndicatorLayer];
-[SBRecordingIndicatorView init];
-[SBRecordingIndicatorView boundingBoxes];
-[SBRecordingIndicatorView setIndicatorType:];
-[SBRecordingIndicatorView dealloc];
-[SBRecordingIndicatorView setHighLevel:];
-[SBRecordingIndicatorView layoutSubviews];
-[SBRecordingIndicatorView settings:changedValueForKey:];
-[SBRecordingIndicatorView setBackgroundColor:];
-[SBRecordingIndicatorView isHighLevel];
-[SBRecordingIndicatorView blurRadius];
-[SBRecordingIndicatorView initWithCoder:];
-[SBRecordingIndicatorView setBlurRadius:];
-[SBRecordingIndicatorView _shouldAnimatePropertyWithKey:];
-[SBRecordingIndicatorView indicatorType];
-[SBRecordingIndicatorView initWithFrame:];
```
