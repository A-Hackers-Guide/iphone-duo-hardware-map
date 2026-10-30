# `BWInferenceCompressedVideoRequirement`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWInferenceVideoRequirement`
- 1 instance variables, 1 properties, 5 instance methods, 1 class methods

## Instance variables

```
@"BWInferenceVideoRequirement" _uncompressedRequirement;
```

## Properties

```
@property (T@"BWInferenceVideoRequirement",R,N,V_uncompressedRequirement) uncompressedRequirement;
```

## Class methods

```
+[BWInferenceCompressedVideoRequirement newRequirementWithUncompressedRequirement:supportedCompressionType:supportedLossyCompressionLevel:];
```

## Instance methods

```
-[BWInferenceCompressedVideoRequirement dealloc];
-[BWInferenceCompressedVideoRequirement uncompressedRequirement];
-[BWInferenceCompressedVideoRequirement isSatisfiedByRequirement:];
-[BWInferenceCompressedVideoRequirement copyWithZone:];
-[BWInferenceCompressedVideoRequirement satisfactionHash];
```
