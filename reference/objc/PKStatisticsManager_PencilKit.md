# `PKStatisticsManager`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 0 properties, 1 instance methods, 0 class methods

## Instance variables

```
@"NSString" _recentShapeCreated;
d _latestShapeCreatedTimestamp;
@"NSDictionary" _recentTextLinesStraightened;
d _latestTextLinesStraightenedTimestamp;
@"PKInk" _recentRollStrokeInk;
d _recentStrokeRollAngleDelta;
B _recentRollStrokeDidUndo;
@"<PKDrawingPaletteStatistics>" _drawingPaletteStatistics;
```

## Instance methods

```
-[PKStatisticsManager submitRecentRollStroke];
```
