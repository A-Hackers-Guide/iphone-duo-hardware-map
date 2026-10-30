# `MLOutputBackingsVerifier`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 1 properties, 6 instance methods, 0 class methods

## Instance variables

```
@"NSDictionary" _outputDescriptions;
```

## Properties

```
@property (T@"NSDictionary",R,N,V_outputDescriptions) outputDescriptions;
```

## Instance methods

```
-[MLOutputBackingsVerifier _verifyOutputBacking:forFeature:error:];
-[MLOutputBackingsVerifier outputDescriptions];
-[MLOutputBackingsVerifier _verifyMultiArrayOutputBacking:forFeature:error:];
-[MLOutputBackingsVerifier initWithOutputDescriptions:];
-[MLOutputBackingsVerifier verifyOutputBackings:predictionUsesBatch:error:];
-[MLOutputBackingsVerifier _verifyPixelBufferOutputBacking:forFeature:error:];
```
