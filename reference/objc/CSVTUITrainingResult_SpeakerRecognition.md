# `CSVTUITrainingResult`

- Image: [`/System/Library/PrivateFrameworks/SpeakerRecognition.framework/SpeakerRecognition`](../userland/System__Library__PrivateFrameworks__SpeakerRecognition.framework__SpeakerRecognition.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 3 instance variables, 3 properties, 6 instance methods, 1 class methods

## Instance variables

```
i _sessionStatus;
i _audioStatus;
q _sessionId;
```

## Properties

```
@property (Tq,R,N,V_sessionId) sessionId;
@property (Ti,R,N,V_sessionStatus) sessionStatus;
@property (Ti,R,N,V_audioStatus) audioStatus;
```

## Class methods

```
+[CSVTUITrainingResult supportsSecureCoding];
```

## Instance methods

```
-[CSVTUITrainingResult audioStatus];
-[CSVTUITrainingResult sessionId];
-[CSVTUITrainingResult encodeWithCoder:];
-[CSVTUITrainingResult initWithCoder:];
-[CSVTUITrainingResult sessionStatus];
-[CSVTUITrainingResult initWithSessionId:sessionStatus:audioStatus:];
```
