# `PKDrawingPaletteStatisticsEventLogger`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `PKDrawingPaletteStatistics`
- 2 instance variables, 6 properties, 7 instance methods, 0 class methods

## Instance variables

```
d _lastHandwritingToolUsedOverDrawingAttachmentTimestamp;
d _lastInkingToolUsedOverNonDrawingAttachmentTimestamp;
```

## Properties

```
@property (Td,N,V_lastHandwritingToolUsedOverDrawingAttachmentTimestamp) lastHandwritingToolUsedOverDrawingAttachmentTimestamp;
@property (Td,N,V_lastInkingToolUsedOverNonDrawingAttachmentTimestamp) lastInkingToolUsedOverNonDrawingAttachmentTimestamp;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[PKDrawingPaletteStatisticsEventLogger lastHandwritingToolUsedOverDrawingAttachmentTimestamp];
-[PKDrawingPaletteStatisticsEventLogger lastInkingToolUsedOverNonDrawingAttachmentTimestamp];
-[PKDrawingPaletteStatisticsEventLogger recordHandwritingToolSelected];
-[PKDrawingPaletteStatisticsEventLogger recordHandwritingToolUsedOverDrawingAttachmentWithTimestamp:];
-[PKDrawingPaletteStatisticsEventLogger recordInkingToolUsedOverNonDrawingAttachmentWithTimestamp:];
-[PKDrawingPaletteStatisticsEventLogger setLastHandwritingToolUsedOverDrawingAttachmentTimestamp:];
-[PKDrawingPaletteStatisticsEventLogger setLastInkingToolUsedOverNonDrawingAttachmentTimestamp:];
```
