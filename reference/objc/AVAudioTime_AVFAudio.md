# `AVAudioTime`

- Image: [`/System/Library/Frameworks/AVFAudio.framework/AVFAudio`](../userland/System__Library__Frameworks__AVFAudio.framework__AVFAudio.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 6 properties, 13 instance methods, 6 class methods

## Instance variables

```
{AudioTimeStamp="mSampleTime"d"mHostTime"Q"mRateScalar"d"mWordClockTime"Q"mSMPTETime"{SMPTETime="mSubframes"s"mSubframeDivisor"s"mCounter"I"mType"I"mFlags"I"mHours"s"mMinutes"s"mSeconds"s"mFrames"s}"mFlags"I"mReserved"I} _ats;
d _sampleRate;
^v _reserved;
```

## Properties

```
@property (TB,R,N,GisHostTimeValid) hostTimeValid;
@property (TQ,R,N) hostTime;
@property (TB,R,N,GisSampleTimeValid) sampleTimeValid;
@property (Tq,R,N) sampleTime;
@property (Td,R,N) sampleRate;
@property (T{AudioTimeStamp=dQdQ{SMPTETime=ssIIIssss}II},R,N) audioTimeStamp;
```

## Class methods

```
+[AVAudioTime hostTimeForSeconds:];
+[AVAudioTime secondsForHostTime:];
+[AVAudioTime timeWithAudioTimeStamp:sampleRate:];
+[AVAudioTime timeWithHostTime:];
+[AVAudioTime timeWithHostTime:sampleTime:atRate:];
+[AVAudioTime timeWithSampleTime:atRate:];
```

## Instance methods

```
-[AVAudioTime sampleRate];
-[AVAudioTime init];
-[AVAudioTime description];
-[AVAudioTime hostTime];
-[AVAudioTime sampleTime];
-[AVAudioTime initWithSampleTime:atRate:];
-[AVAudioTime isHostTimeValid];
-[AVAudioTime audioTimeStamp];
-[AVAudioTime extrapolateTimeFromAnchor:];
-[AVAudioTime initWithAudioTimeStamp:sampleRate:];
-[AVAudioTime initWithHostTime:];
-[AVAudioTime initWithHostTime:sampleTime:atRate:];
-[AVAudioTime isSampleTimeValid];
```
