# `SBPIPContentViewLayoutMetrics`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 8 properties, 10 instance methods, 18 class methods

## Instance variables

```
B _prefersDefaultPosition;
@"NSString" _contentTypeIdentifier;
d _padding;
d _paddingWhileStashed;
d _defaultCornerRadius;
@"SBPIPContentViewLayoutMetricsSizePolicy" _sizePolicy;
Q _defaultPosition;
{CGSize="width"d"height"d} _minimumStashedTabSize;
```

## Properties

```
@property (T@"NSString",R,C,N,V_contentTypeIdentifier) contentTypeIdentifier;
@property (Td,R,N,V_padding) padding;
@property (Td,R,N,V_paddingWhileStashed) paddingWhileStashed;
@property (T{CGSize=dd},R,N,V_minimumStashedTabSize) minimumStashedTabSize;
@property (Td,R,N,V_defaultCornerRadius) defaultCornerRadius;
@property (T@"SBPIPContentViewLayoutMetricsSizePolicy",R,N,V_sizePolicy) sizePolicy;
@property (TQ,R,N,V_defaultPosition) defaultPosition;
@property (TB,R,N,V_prefersDefaultPosition) prefersDefaultPosition;
```

## Class methods

```
+[SBPIPContentViewLayoutMetrics minimumEdgeInsetForSurfaceType:];
+[SBPIPContentViewLayoutMetrics coverSurfaceMinimumEdgeInset];
+[SBPIPContentViewLayoutMetrics foldableSurfaceMinimumBottomEdgeInset];
+[SBPIPContentViewLayoutMetrics innerSurfaceMinimumEdgeInset];
+[SBPIPContentViewLayoutMetrics microPIPLandscapeSizePreferences:portraitSizePreferences:squareSizePreferences:];
+[SBPIPContentViewLayoutMetrics minimumLandscapePadding];
+[SBPIPContentViewLayoutMetrics minimumStashedTabWidth];
+[SBPIPContentViewLayoutMetrics pegasusDefaultMetrics];
+[SBPIPContentViewLayoutMetrics pegasusDefaultMicroPIPMetrics];
+[SBPIPContentViewLayoutMetrics pegasusMetricsForContentType:];
+[SBPIPContentViewLayoutMetrics pegasusQNBacklinkMetrics];
+[SBPIPContentViewLayoutMetrics pegasusScreenSharingMetrics];
+[SBPIPContentViewLayoutMetrics pegasusVideoCallMetrics];
+[SBPIPContentViewLayoutMetrics screenSharingLandscapeSizePreferences:portraitSizePreferences:squareSizePreferences:];
+[SBPIPContentViewLayoutMetrics systemNotesMetricsForPresentationMode:];
+[SBPIPContentViewLayoutMetrics unstashedPeripheryPadding];
+[SBPIPContentViewLayoutMetrics videoCallLandscapeSizePreferences:portraitSizePreferences:squareSizePreferences:];
+[SBPIPContentViewLayoutMetrics videoContentLandscapeSizePreferences:portraitSizePreferences:squareSizePreferences:];
```

## Instance methods

```
-[SBPIPContentViewLayoutMetrics padding];
-[SBPIPContentViewLayoutMetrics defaultCornerRadius];
-[SBPIPContentViewLayoutMetrics contentTypeIdentifier];
-[SBPIPContentViewLayoutMetrics defaultPosition];
-[SBPIPContentViewLayoutMetrics initWithContentTypeIdentifier:padding:paddingWhileStashed:minimumStashedTabSize:defaultCornerRadius:sizePolicy:defaultPosition:];
-[SBPIPContentViewLayoutMetrics initWithContentTypeIdentifier:padding:paddingWhileStashed:minimumStashedTabSize:defaultCornerRadius:sizePolicy:defaultPosition:prefersDefaultPosition:];
-[SBPIPContentViewLayoutMetrics minimumStashedTabSize];
-[SBPIPContentViewLayoutMetrics paddingWhileStashed];
-[SBPIPContentViewLayoutMetrics prefersDefaultPosition];
-[SBPIPContentViewLayoutMetrics sizePolicy];
```
