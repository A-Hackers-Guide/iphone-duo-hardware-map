# `BWAdaptiveBracketingFrameParameters`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 4 instance variables, 5 properties, 7 instance methods, 3 class methods

## Instance variables

```
d _evZeroRatio;
i _integrationTimeInMicroseconds;
f _gain;
i _maxAGC;
```

## Properties

```
@property (Td,R,N) evZeroRatio;
@property (Ti,R,N) integrationTimeInMicroseconds;
@property (Td,R,N) integrationTimeInSeconds;
@property (Tf,R,N) gain;
@property (Ti,R,N) maxAGC;
```

## Class methods

```
+[BWAdaptiveBracketingFrameParameters supportsSecureCoding];
+[BWAdaptiveBracketingFrameParameters frameParametersWithEVZeroRatio:integrationTimeInMicroseconds:gain:maxAGC:];
+[BWAdaptiveBracketingFrameParameters frameParametersWithEVZeroRatio:integrationTimeInSeconds:gain:maxAGC:];
```

## Instance methods

```
-[BWAdaptiveBracketingFrameParameters gain];
-[BWAdaptiveBracketingFrameParameters encodeWithCoder:];
-[BWAdaptiveBracketingFrameParameters initWithCoder:];
-[BWAdaptiveBracketingFrameParameters evZeroRatio];
-[BWAdaptiveBracketingFrameParameters integrationTimeInMicroseconds];
-[BWAdaptiveBracketingFrameParameters integrationTimeInSeconds];
-[BWAdaptiveBracketingFrameParameters maxAGC];
```
