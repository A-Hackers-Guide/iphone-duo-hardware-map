# `BWHVSEmbeddingAnalysisResult`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 6 properties, 10 instance methods, 0 class methods

## Instance variables

```
f _similarityScore;
f _frameScore;
@"NSString" _detectedContext;
@"NSDictionary" _contextProbabilities;
@"NSDictionary" _imageEmbedding;
```

## Properties

```
@property (Tf,N,V_similarityScore) similarityScore;
@property (Tf,R,N,V_frameScore) frameScore;
@property (T@"NSString",R,N,V_detectedContext) detectedContext;
@property (T@"NSDictionary",R,N,V_contextProbabilities) contextProbabilities;
@property (T@"NSDictionary",R,N,V_imageEmbedding) imageEmbedding;
@property (T@"NSDictionary",R,N) metadataRepresentation;
```

## Instance methods

```
-[BWHVSEmbeddingAnalysisResult dealloc];
-[BWHVSEmbeddingAnalysisResult similarityScore];
-[BWHVSEmbeddingAnalysisResult initWithMetadataDictionary:];
-[BWHVSEmbeddingAnalysisResult imageEmbedding];
-[BWHVSEmbeddingAnalysisResult detectedContext];
-[BWHVSEmbeddingAnalysisResult frameScore];
-[BWHVSEmbeddingAnalysisResult contextProbabilities];
-[BWHVSEmbeddingAnalysisResult initWithImageEmbedding:contextProbabilities:detectedContext:similarityScore:frameScore:];
-[BWHVSEmbeddingAnalysisResult metadataRepresentation];
-[BWHVSEmbeddingAnalysisResult setSimilarityScore:];
```
