# `CAMElapsedTimeView`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 10 instance variables, 12 properties, 40 instance methods, 1 class methods

## Instance variables

```
B _wantsLargerText;
q _layoutStyle;
q _backgroundStyle;
@"<CAMElapsedTimeViewDelegate>" _delegate;
@"NSDate" _startTime;
@"NSDate" _pausedTime;
@"NSString" _contentSizeCategory;
@"UILabel" __timeLabel;
@"UIView" __backgroundView;
@"NSTimer" __updateTimer;
```

## Properties

```
@property (T@"UILabel",R,N,V__timeLabel) _timeLabel;
@property (T@"UIView",R,N,V__backgroundView) _backgroundView;
@property (T@"NSTimer",R,N,V__updateTimer) _updateTimer;
@property (Tq,N,V_layoutStyle) layoutStyle;
@property (TB,N,S_setWantsLargerText:,V_wantsLargerText) wantsLargerText;
@property (TB,N,GisShowingBackground) showingBackground;
@property (Tq,N,V_backgroundStyle) backgroundStyle;
@property (T@"<CAMElapsedTimeViewDelegate>",W,N,V_delegate) delegate;
@property (T@"NSDate",R,N,V_startTime) startTime;
@property (T@"NSDate",R,N,V_pausedTime) pausedTime;
@property (TB,N,GisTimerPaused) timerPaused;
@property (T@"NSString",C,N,V_contentSizeCategory) contentSizeCategory;
```

## Class methods

```
+[CAMElapsedTimeView elapsedTimeFormatter];
```

## Instance methods

```
-[CAMElapsedTimeView setLayoutStyle:];
-[CAMElapsedTimeView startTimer];
-[CAMElapsedTimeView layoutStyle];
-[CAMElapsedTimeView intrinsicContentSize];
-[CAMElapsedTimeView _timeLabel];
-[CAMElapsedTimeView _updateFont];
-[CAMElapsedTimeView startTime];
-[CAMElapsedTimeView initWithLayoutStyle:];
-[CAMElapsedTimeView dealloc];
-[CAMElapsedTimeView layoutSubviews];
-[CAMElapsedTimeView _backgroundView];
-[CAMElapsedTimeView _preferredContentSizeCategoryDidChange];
-[CAMElapsedTimeView _updateText];
-[CAMElapsedTimeView backgroundStyle];
-[CAMElapsedTimeView sizeThatFits:];
-[CAMElapsedTimeView setDelegate:];
-[CAMElapsedTimeView _setStartTime:];
-[CAMElapsedTimeView delegate];
-[CAMElapsedTimeView resetTimer];
-[CAMElapsedTimeView setContentSizeCategory:];
-[CAMElapsedTimeView endTimer];
-[CAMElapsedTimeView initWithFrame:];
-[CAMElapsedTimeView setBackgroundStyle:animated:];
-[CAMElapsedTimeView setBackgroundStyle:];
-[CAMElapsedTimeView contentSizeCategory];
-[CAMElapsedTimeView _updateTimer];
-[CAMElapsedTimeView setTimerPaused:];
-[CAMElapsedTimeView wantsLargerText];
-[CAMElapsedTimeView _commonCAMElapsedTimeViewInitializationWithLayoutStyle:];
-[CAMElapsedTimeView _setWantsLargerText:];
-[CAMElapsedTimeView _startPausedAnimation];
-[CAMElapsedTimeView _stopPausedAnimation];
-[CAMElapsedTimeView _updateBackgroundViewAnimated:];
-[CAMElapsedTimeView _updateForTimer:];
-[CAMElapsedTimeView initWithBadgeAppearance];
-[CAMElapsedTimeView isShowingBackground];
-[CAMElapsedTimeView isTimerPaused];
-[CAMElapsedTimeView pausedTime];
-[CAMElapsedTimeView setShowingBackground:];
-[CAMElapsedTimeView setShowingBackground:animated:];
```
