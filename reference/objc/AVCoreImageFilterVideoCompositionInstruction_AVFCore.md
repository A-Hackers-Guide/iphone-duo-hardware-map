# `AVCoreImageFilterVideoCompositionInstruction`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `AVVideoCompositionInstruction`
- 4 instance variables, 12 properties, 11 instance methods, 0 class methods

## Instance variables

```
{?="start"{?="value"q"timescale"i"flags"I"epoch"q}"duration"{?="value"q"timescale"i"flags"I"epoch"q}} _timeRange;
@"NSArray" _requiredSourceTrackIDs;
@? _handler;
{CGAffineTransform="a"d"b"d"c"d"d"d"tx"d"ty"d} _sourceTrackPreferredTransform;
```

## Properties

```
@property (T@?,R,N,V_handler) handler;
@property (T{CGAffineTransform=dddddd},N,V_sourceTrackPreferredTransform) sourceTrackPreferredTransform;
@property (T{?={?=qiIq}{?=qiIq}},R,N,V_timeRange) timeRange;
@property (TB,R,D,N) enablePostProcessing;
@property (TB,R,D,N) containsTweening;
@property (T@"NSArray",R,N,V_requiredSourceTrackIDs) requiredSourceTrackIDs;
@property (Ti,R,D,N) passthroughTrackID;
@property (T@"NSArray",?,R,N) requiredSourceSampleDataTrackIDs;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[AVCoreImageFilterVideoCompositionInstruction timeRange];
-[AVCoreImageFilterVideoCompositionInstruction init];
-[AVCoreImageFilterVideoCompositionInstruction dealloc];
-[AVCoreImageFilterVideoCompositionInstruction handler];
-[AVCoreImageFilterVideoCompositionInstruction containsTweening];
-[AVCoreImageFilterVideoCompositionInstruction enablePostProcessing];
-[AVCoreImageFilterVideoCompositionInstruction initWithTimeRange:sourceTrackIDs:handler:];
-[AVCoreImageFilterVideoCompositionInstruction passthroughTrackID];
-[AVCoreImageFilterVideoCompositionInstruction requiredSourceTrackIDs];
-[AVCoreImageFilterVideoCompositionInstruction setSourceTrackPreferredTransform:];
-[AVCoreImageFilterVideoCompositionInstruction sourceTrackPreferredTransform];
```
