# `BWSensitiveContentAnalyzerSinkNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWSinkNode`
- 2 instance variables, 1 properties, 9 instance methods, 1 class methods

## Instance variables

```
@"SCVideoStreamAnalyzer" _sensitiveContentAnalyzer;
B _sensitiveContentAnalyzerEnabled;
```

## Properties

```
@property (TB,N,V_sensitiveContentAnalyzerEnabled) sensitiveContentAnalyzerEnabled;
```

## Class methods

```
+[BWSensitiveContentAnalyzerSinkNode initialize];
```

## Instance methods

```
-[BWSensitiveContentAnalyzerSinkNode sensitiveContentAnalyzerEnabled];
-[BWSensitiveContentAnalyzerSinkNode renderSampleBuffer:forInput:];
-[BWSensitiveContentAnalyzerSinkNode dealloc];
-[BWSensitiveContentAnalyzerSinkNode handleDroppedSample:forInput:];
-[BWSensitiveContentAnalyzerSinkNode nodeSubType];
-[BWSensitiveContentAnalyzerSinkNode setSensitiveContentAnalyzerEnabled:];
-[BWSensitiveContentAnalyzerSinkNode didSelectFormat:forInput:];
-[BWSensitiveContentAnalyzerSinkNode nodeType];
-[BWSensitiveContentAnalyzerSinkNode initWithAnalyzer:sinkID:interruptionDelegate:];
```
