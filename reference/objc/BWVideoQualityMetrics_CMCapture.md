# `BWVideoQualityMetrics`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 1 properties, 5 instance methods, 4 class methods

## Instance variables

```
q _totalLux;
i _frames;
```

## Properties

```
@property (TI,R,N) qualityScoringVersion;
```

## Class methods

```
+[BWVideoQualityMetrics initialize];
+[BWVideoQualityMetrics filterMetadata:];
+[BWVideoQualityMetrics _luxThreshold];
+[BWVideoQualityMetrics _luxTransition];
```

## Instance methods

```
-[BWVideoQualityMetrics reset];
-[BWVideoQualityMetrics _computeLuxScore];
-[BWVideoQualityMetrics computeQualityScore];
-[BWVideoQualityMetrics processMetadata:];
-[BWVideoQualityMetrics qualityScoringVersion];
```
