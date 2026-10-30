# `BWInferenceVideoRequirement`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWInferenceMediaRequirement`
- Protocols: `NSCopying`
- 2 instance variables, 3 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"BWInferenceVideoFormat" _videoFormat;
i _videoStorageType;
```

## Properties

```
@property (T@"BWInferenceVideoFormat",R,N,V_videoFormat) videoFormat;
@property (Ti,R,N,V_videoStorageType) videoStorageType;
@property (T@"NSString",R,N) shortDescription;
```

## Instance methods

```
-[BWInferenceVideoRequirement videoFormat];
-[BWInferenceVideoRequirement initWithAttachedMediaKey:count:];
-[BWInferenceVideoRequirement dealloc];
-[BWInferenceVideoRequirement initWithVideoRequirement:];
-[BWInferenceVideoRequirement shortDescription];
-[BWInferenceVideoRequirement videoStorageType];
-[BWInferenceVideoRequirement initWithAttachedMediaKey:videoFormat:videoStorageType:];
-[BWInferenceVideoRequirement description];
-[BWInferenceVideoRequirement isSatisfiedByRequirement:];
-[BWInferenceVideoRequirement initWithAttachedMediaKey:videoFormat:count:];
-[BWInferenceVideoRequirement copyWithZone:];
-[BWInferenceVideoRequirement satisfactionHash];
-[BWInferenceVideoRequirement initWithAttachedMediaKey:videoFormat:];
```
