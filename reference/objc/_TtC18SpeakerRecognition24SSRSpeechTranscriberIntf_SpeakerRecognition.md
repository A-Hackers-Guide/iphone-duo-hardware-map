# `_TtC18SpeakerRecognition24SSRSpeechTranscriberIntf`

- Image: [`/System/Library/PrivateFrameworks/SpeakerRecognition.framework/SpeakerRecognition`](../userland/System__Library__PrivateFrameworks__SpeakerRecognition.framework__SpeakerRecognition.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 14 instance variables, 3 properties, 13 instance methods, 1 class methods

## Instance variables

```
(objc_protocol 0x2054f03d8) ? delegate;
Foundation.Locale locale;
Swift.Bool isTranscribing;
os.Logger logger;
DispatchQueue cleanupQueue;
Speech.DictationTranscriber ? dictationTranscriber;
Speech.SpeechAnalyzer ? speechAnalyzer;
Swift.AsyncStream.Continuation Speech.AnalyzerInput _$s_GSg -> audioEnqueuer;
_$sScTyyt Swift.Never ? resultHandlerTask;
_$sScTyyt Swift.Never ? teardownTask;
_$sSo13AVAudioFormatC audioFormat;
Swift.Bool isCleaningUp;
SpeakerRecognition.SSREnrollmentSNRCalculator snrCalculator;
_$sSaySfG floatConversionBuffer;
```

## Properties

```
@property (T@"<_TtP18SpeakerRecognition32SSRSpeechTranscriberIntfDelegate_>",N,W,Vdelegate) delegate;
@property (T@"NSLocale",N,R) locale;
@property (TB,N,VisTranscribing) isTranscribing;
```

## Class methods

```
+[_TtC18SpeakerRecognition24SSRSpeechTranscriberIntf validateAssetAvailabilityForLocale:completion:];
```

## Instance methods

```
-[_TtC18SpeakerRecognition24SSRSpeechTranscriberIntf initWithLocale:];
-[_TtC18SpeakerRecognition24SSRSpeechTranscriberIntf init];
-[_TtC18SpeakerRecognition24SSRSpeechTranscriberIntf dealloc];
-[_TtC18SpeakerRecognition24SSRSpeechTranscriberIntf isTranscribing];
-[_TtC18SpeakerRecognition24SSRSpeechTranscriberIntf setDelegate:];
-[_TtC18SpeakerRecognition24SSRSpeechTranscriberIntf locale];
-[_TtC18SpeakerRecognition24SSRSpeechTranscriberIntf delegate];
-[_TtC18SpeakerRecognition24SSRSpeechTranscriberIntf setIsTranscribing:];
-[_TtC18SpeakerRecognition24SSRSpeechTranscriberIntf addAudio:];
-[_TtC18SpeakerRecognition24SSRSpeechTranscriberIntf finishAudio];
-[_TtC18SpeakerRecognition24SSRSpeechTranscriberIntf initWithLocaleString:];
-[_TtC18SpeakerRecognition24SSRSpeechTranscriberIntf startTranscriptionWithCompletion:];
-[_TtC18SpeakerRecognition24SSRSpeechTranscriberIntf stopTranscription];
```
