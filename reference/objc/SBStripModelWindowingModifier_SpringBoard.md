# `SBStripModelWindowingModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBWindowingModifier`
- 9 instance variables, 0 properties, 10 instance methods, 0 class methods

## Instance variables

```
Q _appLayoutsCount;
@"SBAppLayout" _appLayout;
@"SBWindowingStrip" _nextStrip;
@"NSDictionary" _cycleOrderForIdentifier;
Q _cycleResetGenerationCount;
B _needsUpdate;
@"SBAppLayout" _peekingAppLayout;
@"SBAppLayout" _previousPeekingAppLayout;
@"SBAppLayout" _upcomingAppLayoutForExitingAppExpose;
```

## Instance methods

```
-[SBStripModelWindowingModifier stateModel];
-[SBStripModelWindowingModifier willUpdate];
-[SBStripModelWindowingModifier transitionDidUpdate:];
-[SBStripModelWindowingModifier didUpdate];
-[SBStripModelWindowingModifier transitionWillBegin:];
-[SBStripModelWindowingModifier timerFired:];
-[SBStripModelWindowingModifier willBegin];
-[SBStripModelWindowingModifier _currentCycleResetGenerationCount];
-[SBStripModelWindowingModifier _stageStripIdentifiersFromStrip:];
-[SBStripModelWindowingModifier gestureDidUpdate:];
```
