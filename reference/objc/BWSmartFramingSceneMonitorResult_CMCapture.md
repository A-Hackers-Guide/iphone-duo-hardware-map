# `BWSmartFramingSceneMonitorResult`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 10 instance variables, 0 properties, 11 instance methods, 0 class methods

## Instance variables

```
i _suggestedFieldOfView;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _suggestedFieldOfViewRect;
@"NSDictionary" _subjectDistanceRange;
f _subjectMotionPerSecond;
B _atLeastOneSubjectGazingForShutterSoundRelaxation;
i _significantSubjectCount;
@"NSArray" _significantSubjectGroupIDs;
i _persistentlySignificantSubjectCount;
@"NSArray" _persistentlySignificantSubjectGroupIDs;
I _smartFramingSceneMonitorMode;
```

## Instance methods

```
-[BWSmartFramingSceneMonitorResult dealloc];
-[BWSmartFramingSceneMonitorResult apertureControlDistanceRangeWithError:];
-[BWSmartFramingSceneMonitorResult atLeastOneSubjectGazingForShutterSoundRelaxationWithError:];
-[BWSmartFramingSceneMonitorResult initWithSmartFramingSceneMonitorMode:suggestedFieldOfView:suggestedFieldOfViewRect:subjectDistanceRange:subjectMotionPerSecond:atLeastOneSubjectGazingForShutterSoundRelaxation:significantSubjectCount:significantSubjectGroupIDs:persistentlySignificantSubjectCount:persistentlySignificantSubjectGroupIDs:];
-[BWSmartFramingSceneMonitorResult persistentlySignificantSubjectCountWithError:];
-[BWSmartFramingSceneMonitorResult persistentlySignificantSubjectGroupIDsWithError:];
-[BWSmartFramingSceneMonitorResult significantSubjectCountWithError:];
-[BWSmartFramingSceneMonitorResult significantSubjectGroupIDsWithError:];
-[BWSmartFramingSceneMonitorResult subjectMotionPerSecondWithError:];
-[BWSmartFramingSceneMonitorResult suggestedFieldOfViewRectWithError:];
-[BWSmartFramingSceneMonitorResult suggestedFieldOfViewWithError:];
```
