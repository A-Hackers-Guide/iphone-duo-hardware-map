# `SSRSpeakerProfileEmbedding`

- Image: [`/System/Library/PrivateFrameworks/SpeakerRecognition.framework/SpeakerRecognition`](../userland/System__Library__PrivateFrameworks__SpeakerRecognition.framework__SpeakerRecognition.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 6 instance variables, 6 properties, 11 instance methods, 1 class methods

## Instance variables

```
I _numEmbedding;
I _dimension;
@"NSString" _siriSharedUserId;
@"NSString" _voiceProfileId;
@"NSData" _embeddings;
Q _speakerRecognizerType;
```

## Properties

```
@property (T@"NSString",R,N,V_siriSharedUserId) siriSharedUserId;
@property (T@"NSString",R,N,V_voiceProfileId) voiceProfileId;
@property (T@"NSData",R,N,V_embeddings) embeddings;
@property (TI,R,N,V_numEmbedding) numEmbedding;
@property (TI,R,N,V_dimension) dimension;
@property (TQ,R,N,V_speakerRecognizerType) speakerRecognizerType;
```

## Class methods

```
+[SSRSpeakerProfileEmbedding supportsSecureCoding];
```

## Instance methods

```
-[SSRSpeakerProfileEmbedding dimension];
-[SSRSpeakerProfileEmbedding encodeWithCoder:];
-[SSRSpeakerProfileEmbedding description];
-[SSRSpeakerProfileEmbedding initWithCoder:];
-[SSRSpeakerProfileEmbedding embeddings];
-[SSRSpeakerProfileEmbedding speakerRecognizerType];
-[SSRSpeakerProfileEmbedding initWithSiriSharedUserId:embeddings:numEmbedding:dimension:speakerRecognizerType:];
-[SSRSpeakerProfileEmbedding initWithVoiceProfileId:embeddings:numEmbedding:dimension:speakerRecognizerType:];
-[SSRSpeakerProfileEmbedding numEmbedding];
-[SSRSpeakerProfileEmbedding siriSharedUserId];
-[SSRSpeakerProfileEmbedding voiceProfileId];
```
