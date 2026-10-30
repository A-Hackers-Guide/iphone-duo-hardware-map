# `BWMetadataTimeMachine`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 2 properties, 11 instance methods, 1 class methods

## Instance variables

```
@"NSString" _name;
i _capacity;
@? _addHandler;
@"NSObject<OS_dispatch_queue>" _metadataHandlingQueue;
@"NSMutableArray" _metadata;
@"NSMutableArray" _requests;
{?="value"q"timescale"i"flags"I"epoch"q} _earliestAllowedPTS;
i _numberOfConsecutiveFlushes;
```

## Properties

```
@property (T@"NSString",R,N,V_name) name;
@property (T{?=qiIq}) earliestAllowedPTS;
```

## Class methods

```
+[BWMetadataTimeMachine initialize];
```

## Instance methods

```
-[BWMetadataTimeMachine dealloc];
-[BWMetadataTimeMachine reset];
-[BWMetadataTimeMachine metadata];
-[BWMetadataTimeMachine name];
-[BWMetadataTimeMachine addMetadata:];
-[BWMetadataTimeMachine addDroppedFrameForPortType:pts:];
-[BWMetadataTimeMachine earliestAllowedPTS];
-[BWMetadataTimeMachine initWithName:capacity:metadataHandlingPriority:addHandler:];
-[BWMetadataTimeMachine metadataForPTSRange:timeout:];
-[BWMetadataTimeMachine setEarliestAllowedPTS:];
-[BWMetadataTimeMachine waitUntilCapacity:timeout:];
```
