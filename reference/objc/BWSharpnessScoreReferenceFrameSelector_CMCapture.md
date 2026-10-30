# `BWSharpnessScoreReferenceFrameSelector`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 0 properties, 3 instance methods, 1 class methods

## Instance variables

```
@"CMISharpnessScore" _sharpnessScoreCalculator;
i _candidateFrameCount;
i _receivedCandidateFrameCount;
^{opaqueCMSampleBuffer=} _currentCandidateFrame;
f _currentCandidateSharpnessScore;
B _faceScoresEnabled;
i _maxNumberOfFaceScores;
```

## Class methods

```
+[BWSharpnessScoreReferenceFrameSelector externalMemoryDescriptorWithMaxInputDimensions:];
```

## Instance methods

```
-[BWSharpnessScoreReferenceFrameSelector dealloc];
-[BWSharpnessScoreReferenceFrameSelector addReferenceFrameCandidate:referenceFrameOut:];
-[BWSharpnessScoreReferenceFrameSelector initWithCommandQueue:externalMemoryResource:candidateCount:];
```
