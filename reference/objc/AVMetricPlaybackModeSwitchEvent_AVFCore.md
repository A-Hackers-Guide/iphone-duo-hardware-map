# `AVMetricPlaybackModeSwitchEvent`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVMetricEvent`
- 1 instance variables, 1 properties, 5 instance methods, 1 class methods

## Instance variables

```
q _mode;
```

## Properties

```
@property (Tq,R) mode;
```

## Class methods

```
+[AVMetricPlaybackModeSwitchEvent supportsSecureCoding];
```

## Instance methods

```
-[AVMetricPlaybackModeSwitchEvent debugDescription];
-[AVMetricPlaybackModeSwitchEvent encodeWithCoder:];
-[AVMetricPlaybackModeSwitchEvent mode];
-[AVMetricPlaybackModeSwitchEvent initWithCoder:];
-[AVMetricPlaybackModeSwitchEvent initWithDate:mediaTime:sessionID:figMetricEvent:mode:];
```
