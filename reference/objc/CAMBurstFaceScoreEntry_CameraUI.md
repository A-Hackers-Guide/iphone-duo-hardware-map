# `CAMBurstFaceScoreEntry`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 3 properties, 10 instance methods, 0 class methods

## Instance variables

```
f maxScore;
f minScore;
f sumScores;
f sumSqScores;
i numScores;
```

## Properties

```
@property (Tf,VmaxScore) maxScore;
@property (Tf,VminScore) minScore;
@property (Ti,VnumScores) numScores;
```

## Instance methods

```
-[CAMBurstFaceScoreEntry addScore:];
-[CAMBurstFaceScoreEntry maxScore];
-[CAMBurstFaceScoreEntry minScore];
-[CAMBurstFaceScoreEntry setMaxScore:];
-[CAMBurstFaceScoreEntry setMinScore:];
-[CAMBurstFaceScoreEntry computeAverage];
-[CAMBurstFaceScoreEntry computeStandardDeviation];
-[CAMBurstFaceScoreEntry initWithScore:];
-[CAMBurstFaceScoreEntry numScores];
-[CAMBurstFaceScoreEntry setNumScores:];
```
