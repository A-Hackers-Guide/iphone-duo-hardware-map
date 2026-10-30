# `BWInvalidFramesChecker`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 10 instance variables, 0 properties, 2 instance methods, 1 class methods

## Instance variables

```
@"FigStateMachine" _stateMachine;
B _invalidFrameStatsCollectionEnabled;
{?="value"q"timescale"i"flags"I"epoch"q} _mostRecentPTS;
{?="value"q"timescale"i"flags"I"epoch"q} _firstFramePTS;
{?="value"q"timescale"i"flags"I"epoch"q} _mostRecentValidPTS;
{?="value"q"timescale"i"flags"I"epoch"q} _firstIndicatorCheckInvalidPTS;
{?="value"q"timescale"i"flags"I"epoch"q} _exitIndicatorCheckInvalidPTS;
i _indicatorCheckInitialInvalidFrameCount;
i _indicatorCheckSubsequentInvalidFrameCount;
B _alreadySuggestedBlackenedFrameTTR;
```

## Class methods

```
+[BWInvalidFramesChecker initialize];
```

## Instance methods

```
-[BWInvalidFramesChecker init];
-[BWInvalidFramesChecker dealloc];
```
